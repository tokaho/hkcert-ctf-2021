# 角落生物 1 (Squirrel Community 1)

![](../thumbnail/62.jpg)

| Key | Value |
| --- | ----- |
| ID | 62 |
| Tags (Categories) | #web #☆☆☆☆☆ |
| Challenge release timestamp | 2021-11-12T10:00:00.000Z |
| Score | 50 |
| Total solves (Final) | 176 |

# YouTube

| Key | Value |
| --- | ----- |
| Avatar | ![](../avatar/apple.jpg)
| Singer (Challenge Author) | apple |
| Link | https://youtu.be/14bbnWkGHe4 |

# Description

Find out Squirrel Master's password!

http://chalf.hkcert21.pwnable.hk:28062/


---


### Walkthrough

This is a easy web challenge on **SQL injection**, which is a [common vulnerability](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection), especially in old applications. It is expected that experienced player / pentester can solve it within 5 min, but if you're new to this game, read on!



#### Understanding the application

To find out abnormalities (bugs / vulnerabilities) in a web application, you need to first understand its behavior under normal usage. Visit the homepage (http://chalf.hkcert21.pwnable.hk:28062/) and you will see a cute squirrels saying hi to you, with a big button to *Join the community*. Other links in the webpage are either out of scope (not in the same website), or not simply functioning. So lets click that button.

In the SquirrelChat application, we can see there are two function: `Login` and `Register`. After registering an account and login to the application, we can see that there are additional function `Chatroom` and `Logout`, with lengthy (but not helpful) text on the homepage.

Click into `chatroom`, you can see a textbox allowing you to send message to the channel. Try send something!

> \[🤔1\]: There are two more function in the application, can you find them out?



#### How the web works

You should already know the content in this section if you're familiar with the web.



##### Client and server model

Similar to most of the website in the world, the site you're visiting contains two parts: `client` and `server`. The `server` 'serves' you by processing your `request` and providing webpage, images, videos etc for your browser. The `client` is your web browser, which send requests to `server` and display the response on your screen.

> \[🤔2\]: What is your browser software, and what is the server software?
>
> 💡: Google "What is my browser", "How to find out website server software"



##### Input - Process - Output

When you send a message, your browser will send a request to the server `chalf.hkcert21.pwnable.hk:28062`, with your chat message and other **input** values.  The server will **process** your message and show it on every user's webpage as **output**.

> \[🤔3\]: What are the input when you send a message in SquirrelChat?



##### Path and Query string

Path and *Query string* are examples of the `input` to websites. When you do a Google search, you can notice the web browser address bar will contain an URL (web address):

```
| https://www.google.com/search?q=What+is+query+string |
|           ^             ^       ^                      |
|           Server        Path    Query string           |
```

- Server: `www.google.com`
- Path: `/search`
- Query string: `q=What+is+query+string`

> \[🤔4\]: What does `+` means in query string?
>
> 💡: Google it: `what does plus means in query string`

> \[🤔5\]: Can you change the above Google URL to search something else? Test with your web browser.

> \[🤔6\]: Send an message in the SquirrelChat chat room, then click on your own name. Can you identify the `path` and `query string` from your browser's address bar?



#### SQL in SquirrelChat

As mentioned, the **Sq**uirre**l**Chat application has a SQL injection vulnerability. The application uses SQL to store and retrieve your account details and channel messages in the server, and there are incorrect handling of user input when it construct the SQL query. Therefore it is possible to change the website behavior and leak flags from the server.

> \[🤔7\]:  In \[🤔6\], you have identified the query string of the URL. What does the numbers mean in the query string? Try changing it and see how the application behaves.



The SquirrelChat application construct the SQL query like this

```sql
SELECT * FROM users WHERE id={{Your Input}}
```

In the above SQL query, `{{Your Input}}` is replaced with the `id` provided in the query string. In plain English, this SQL query will `SELECT` (retrieve) users information, where the user `id` equals to your input in the query string.

So if you visit

```
http://chalf.hkcert21.pwnable.hk:28062/chat/user?id=123
```

The query will become:

```sql
SELECT * FROM users WHERE id=123
```

Which show the user information whose `id` equals to `123`. This code snippet looks completely innocent, but it is vulnerable to the deadly SQL injection vulnerability.



Let's lookup what is SQL injection vulnerability. Google `what is sql injection ctf` and you can find this [webpage](https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection) as the top result.

> \[🤔8\]: You got all the pieces to tackle this challenge. Can you exploit the SQL injection vulnerability without looking at the answer below?



####  Exploiting the SQL injection vulnerability

If we are able to change the SQL query to following:

```sql
SELECT * FROM users WHERE id=123 OR true
```

By visiting [profile of user 123](http://chalf.hkcert21.pwnable.hk:28062/chat/user?id=123), we know that the user does not exists (i.e. `id=123` is False). By appending `OR true` to the query, we changed the outcome to True regardless what is provided as `id`, therefore the system will return EVERY user in the system, including our target: Squirrel Master's account. Recall your Math lessons:

```
OR Truth Table
+-----+-----+--------+
|  A  |  B  | A OR B |
+-----+-----+--------+
|  T  |  T  |   T    |
|  T  |  F  |   T    |
|  F  |  T  |   T    | <--- We are here
|  F  |  F  |   F    |
+-----+-----+--------+
```


> \[🤔9\]: Can we construct the query string (input to the webpage) such that the application will run the above SQL query?



As you have answered in \[🤔4\], we have to change spaces into plus sign (`+`) in the query string. Therefore, you can send the query string as `id=123+OR+true` and get your flag.



#### Suggested Answers

##### \[🤔1\]

- Change channel
- View user details

##### \[🤔2\]

- Your browser: https://www.whatismybrowser.com/
- Server software: https://iplocation.io/website-server-software/

##### \[🤔3\]

- Your user account (cookies) such that the application can show your name along with your message
- Channel name (as in the URL)
- Message
- (There are much more...)

##### \[🤔4\]

- `+` sign has a semantic meaning in the query string. It is used to represent a space. https://stackoverflow.com/a/6855723

# Solves
| ID | Name | Solve at |
| --- | ---- | -------- |
| 82 | S0092 - Immaculate Heart of Mary College | 2021-11-12T10:06:21.326Z |
| 87 | T0095 - CUHK | 2021-11-12T10:07:29.731Z |
| 92 | O0010 - HackyClub | 2021-11-12T10:08:12.717Z |
| 106 | S0043 - CARMEL SECONDARY SCHOOL | 2021-11-12T10:11:03.463Z |
| 109 | O0027 - UND3r 20 D53 H473r5 4ND r374K3r | 2021-11-12T10:11:41.572Z |
| 117 | T0087 - CityU | 2021-11-12T10:13:48.930Z |
| 124 | S0037 - King's College | 2021-11-12T10:14:59.479Z |
| 125 | T0086 - PolyU | 2021-11-12T10:15:04.423Z |
| 126 | S0061 - Po Leung Kuk Choi Kai Yau School | 2021-11-12T10:15:26.310Z |
| 128 | O0086 - offsecFansclub | 2021-11-12T10:15:35.540Z |
| 130 | T0085 - PolyU | 2021-11-12T10:15:39.845Z |
| 134 | O0083 - c0rrupted flags | 2021-11-12T10:16:31.746Z |
| 135 | T0047 - HKUST | 2021-11-12T10:16:45.434Z |
| 138 | O0044 - O0007 – PAYCheck | 2021-11-12T10:17:42.056Z |
| 143 | T0091 - HKU | 2021-11-12T10:18:39.634Z |
| 145 | O0016 - ePotato | 2021-11-12T10:19:12.701Z |
| 146 | O0025 - SatayBeefNoodles | 2021-11-12T10:19:17.119Z |
| 147 | S0010 - The Chinese Foundation Secondary School | 2021-11-12T10:19:38.715Z |
| 148 | T0056 - THEi | 2021-11-12T10:19:54.205Z |
| 151 | T0042 - HKUST | 2021-11-12T10:20:51.618Z |
| 162 | S0112 - LOCK TAO SECONDARY SCHOOL | 2021-11-12T10:24:12.714Z |
| 165 | O0062 - P2403 | 2021-11-12T10:24:56.118Z |
| 167 | S0030 - St. Francis Xavier's College | 2021-11-12T10:25:15.777Z |
| 168 | O0050 - 7M5_N650C | 2021-11-12T10:25:22.317Z |
| 172 | T0010 - CityU,PolyU | 2021-11-12T10:27:18.711Z |
| 173 | S0107 - CHANG PUI CHUNG MEMORIAL SCHOOL | 2021-11-12T10:27:44.282Z |
| 175 | O0056 - AVADA KEDAVRA | 2021-11-12T10:28:30.368Z |
| 176 | S0101 - Youth College (Kwai Fong) | 2021-11-12T10:28:33.993Z |
| 178 | S0048 - TWGHs Wong Fut Nam College | 2021-11-12T10:29:07.849Z |
| 179 | T0054 - THEi | 2021-11-12T10:29:10.034Z |
| 188 | T0006 - CityU,PolyU | 2021-11-12T10:31:05.915Z |
| 189 | T0033 - HKMU | 2021-11-12T10:31:32.056Z |
| 190 | T0007 - CUHK | 2021-11-12T10:32:04.297Z |
| 191 | T0003 - HKUST | 2021-11-12T10:32:24.900Z |
| 192 | S0033 - CCC Ming Yin College | 2021-11-12T10:32:32.198Z |
| 196 | O0043 - The Almighty Dragon | 2021-11-12T10:33:51.019Z |
| 199 | S0023 - Tsuen Wan Public Ho Chuen Yiu Memorial College | 2021-11-12T10:34:58.001Z |
| 200 | T0021 - CUHK | 2021-11-12T10:35:45.663Z |
| 201 | O0030 - Will code for food | 2021-11-12T10:36:01.030Z |
| 204 | S0008 - The Chinese Foundation Secondary School | 2021-11-12T10:38:15.096Z |
| 210 | T0055 - THEi | 2021-11-12T10:40:47.991Z |
| 212 | T0090 - HKUST | 2021-11-12T10:41:06.221Z |
| 214 | T0016 - HKCC | 2021-11-12T10:41:42.055Z |
| 218 | T0039 - CUHK | 2021-11-12T10:44:41.089Z |
| 219 | T0053 - THEi | 2021-11-12T10:44:48.841Z |
| 220 | S0042 - CARMEL SECONDARY SCHOOL | 2021-11-12T10:45:36.992Z |
| 224 | 天枢Dubhe | 2021-11-12T10:48:44.187Z |
| 225 | T0076 - CUHK | 2021-11-12T10:49:07.680Z |
| 227 | O0071 - Noobtrytryonly | 2021-11-12T10:49:16.463Z |
| 229 | S0009 - Tsuen Wan Public Ho Chuen Yiu Memorial College | 2021-11-12T10:49:40.524Z |
| 243 | T0092 - HKCC | 2021-11-12T10:57:34.689Z |
| 244 | T0059 - HKCC | 2021-11-12T10:58:15.555Z |
| 246 | O0081 - Arbitrary | 2021-11-12T10:59:28.500Z |
| 247 | O0059 - Fragile❤ | 2021-11-12T10:59:54.482Z |
| 249 | T0025 - IVE(TM) | 2021-11-12T11:00:07.253Z |
| 251 | S0038 - Fanling Rhenish Church Secondary School | 2021-11-12T11:01:24.057Z |
| 256 | T0037 - HKBU,CityU,HKMU | 2021-11-12T11:02:54.074Z |
| 262 | S0034 - CCC Ming Yin College | 2021-11-12T11:06:30.041Z |
| 266 | S0027 - HKSYCIA Wong Tai Shan Memorial College | 2021-11-12T11:07:50.522Z |
| 267 | S0019 - St. Francis Xavier's School, Tsuen Wan | 2021-11-12T11:10:03.256Z |
| 271 | T0032 - HKCC,UOWCHK | 2021-11-12T11:12:13.090Z |
| 274 | T0004 - HKUST,HKU SPACE,CUHK | 2021-11-12T11:14:15.882Z |
| 275 | S0051 - Carmel Alison Lam Foundation Secondary School | 2021-11-12T11:14:23.779Z |
| 280 | S0095 - Buddhist Sin Tak College | 2021-11-12T11:16:09.209Z |
| 282 | S0016 - Tsuen Wan Public Ho Chuen Yiu Memorial College | 2021-11-12T11:17:07.001Z |
| 283 | S0005 - Shatin Tsung Tsin Secondary School | 2021-11-12T11:17:12.055Z |
| 286 | T0045 - HKU,HKUST,CUHK | 2021-11-12T11:19:40.269Z |
| 288 | S0059 - Fanling Kau Yan College | 2021-11-12T11:24:10.737Z |
| 289 | T0020 - HKCC | 2021-11-12T11:25:26.450Z |
| 301 | O0065 - HowDoYouTurnThisOn | 2021-11-12T11:34:47.111Z |
| 309 | T0057 - HKUST | 2021-11-12T11:40:37.313Z |
| 315 | O0028 - LU, SHAO-CHI | 2021-11-12T11:47:44.841Z |
| 317 | T0028 - CUHK,PolyU,HKCC | 2021-11-12T11:49:12.534Z |
| 323 | O0012 - HWK | 2021-11-12T11:52:37.653Z |
| 324 | O0084 - Never Gonna Let You Dump | 2021-11-12T11:53:07.394Z |
| 327 | S0031 - Ying Wa College | 2021-11-12T11:54:26.581Z |
| 328 | S0089 - Po Leung Kuk Celine Ho Yam Tong College | 2021-11-12T11:54:40.128Z |
| 329 | S0093 - De La Salle Secondary School, N.T. | 2021-11-12T11:55:00.152Z |
| 332 | S0004 - St. Paul's Secondary School | 2021-11-12T11:56:02.803Z |
| 336 | O0061 - GoGoWeaponGo | 2021-11-12T11:57:15.972Z |
| 340 | S0028 - HKSYCIA Wong Tai Shan Memorial College | 2021-11-12T11:59:39.641Z |
| 341 | O0055 - Braindump | 2021-11-12T12:00:03.250Z |
| 343 | S0097 - TWGHs Wong Fut Nam College | 2021-11-12T12:01:36.963Z |
| 347 | O0008 - RTP | 2021-11-12T12:08:12.933Z |
| 351 | T0038 - HKUST | 2021-11-12T12:11:08.648Z |
| 356 | O0018 - TechRebornation | 2021-11-12T12:21:14.424Z |
| 359 | S0040 - Fanling Rhenish Church Secondary School | 2021-11-12T12:21:55.579Z |
| 360 | S0053 - St. Francis Xavier's College | 2021-11-12T12:25:12.919Z |
| 363 | S0073 - Ying Wa College | 2021-11-12T12:27:37.594Z |
| 365 | S0090 - Immaculate Heart of Mary College | 2021-11-12T12:27:51.436Z |
| 368 | S0039 - Fanling Rhenish Church Secondary School | 2021-11-12T12:31:25.110Z |
| 371 | T0030 - HKUST,CityU | 2021-11-12T12:32:30.458Z |
| 372 | S0007 - HKCCCU Logos Academy | 2021-11-12T12:32:52.658Z |
| 374 | T0050 - HKCC | 2021-11-12T12:36:17.496Z |
| 375 | S0041 - CARMEL SECONDARY SCHOOL | 2021-11-12T12:36:33.404Z |
| 377 | O0011 - Sam01101 | 2021-11-12T12:36:54.277Z |
| 385 | S0029 - St. Francis Xavier's College | 2021-11-12T12:44:43.098Z |
| 389 | O0033 - HDMI | 2021-11-12T12:48:02.639Z |
| 394 | S0049 - TWGHs Wong Fut Nam College | 2021-11-12T12:51:00.868Z |
| 397 | MOCSCTF-A | 2021-11-12T12:58:25.962Z |
| 401 | O0074 - CLS | 2021-11-12T13:00:55.465Z |
| 403 | O0024 - SquidGamer | 2021-11-12T13:03:59.339Z |
| 404 | S0106 - Kwok Tak Seng Catholic Secondary School | 2021-11-12T13:05:16.960Z |
| 420 | S0003 - Kwun Tong Maryknoll College | 2021-11-12T13:10:41.969Z |
| 429 | T0065 - HKUST | 2021-11-12T13:20:25.529Z |
| 439 | T0062 - HKCC | 2021-11-12T13:27:10.190Z |
| 442 | T0068 - HKMU | 2021-11-12T13:29:04.748Z |
| 454 | T0035 - CUHK | 2021-11-12T13:42:56.206Z |
| 455 | T0040 - HKCC,HKUST | 2021-11-12T13:44:48.529Z |
| 457 | O0009 - faulT | 2021-11-12T13:46:39.005Z |
| 467 | S0032 - CCC Ming Yin College | 2021-11-12T13:54:22.128Z |
| 468 | S0056 - Queen's College Old Boys' Association Secondary School | 2021-11-12T13:54:24.758Z |
| 479 | O0054 - Mama Sung | 2021-11-12T14:07:31.010Z |
| 482 | T0074 - PolyU | 2021-11-12T14:12:21.539Z |
| 483 | The Duck | 2021-11-12T14:14:57.735Z |
| 486 | O0072 - Royal Sunflower Tea | Tea to enrich your day | 2021-11-12T14:19:04.320Z |
| 487 | S0047 - Munsang College (Hong Kong Island) | 2021-11-12T14:22:11.015Z |
| 493 | O0066 - QWErTY | 2021-11-12T14:29:39.442Z |
| 508 | S0109 - CHANG PUI CHUNG MEMORIAL SCHOOL | 2021-11-12T14:43:32.080Z |
| 515 | T0071 - IVE (CW) | 2021-11-12T14:51:21.323Z |
| 523 | S0062 - CARMEL SECONDARY SCHOOL | 2021-11-12T14:58:27.687Z |
| 526 | T0060 - HKU SPACE | 2021-11-12T15:00:49.665Z |
| 532 | O0073 - knownothing | 2021-11-12T15:08:06.122Z |
| 535 | T0077 - IVE (CW) | 2021-11-12T15:12:14.605Z |
| 538 | O0021 - KESR | 2021-11-12T15:16:50.336Z |
| 540 | O0004 - AUTOEXEC.BAT | 2021-11-12T15:17:42.043Z |
| 542 | O0039 - Buddiesss | 2021-11-12T15:18:12.182Z |
| 545 | S0087 - Man Kwan QualiEd College | 2021-11-12T15:22:36.299Z |
| 552 | T0088 - HKMU | 2021-11-12T15:28:59.921Z |
| 555 | O0077 - Kappa's Mouth | 2021-11-12T15:32:04.320Z |
| 561 | Super Guesser | 2021-11-12T15:38:32.637Z |
| 579 | S0018 - The Chinese Foundation Secondary School | 2021-11-12T15:56:42.319Z |
| 610 | T0049 - HKU SPACE | 2021-11-12T16:41:14.123Z |
| 616 | T0058 - CUHK | 2021-11-12T16:56:51.470Z |
| 621 | O0002 - MSPeople | 2021-11-12T16:58:35.345Z |
| 627 | O0019 - Team 388 | 2021-11-12T17:02:53.897Z |
| 646 | O0020 - SKWD | 2021-11-12T17:51:23.846Z |
| 647 | O0053 - Si Daan Kau Gei La | 2021-11-12T17:52:52.024Z |
| 655 | O0079 - NullPointer | 2021-11-12T18:04:53.897Z |
| 656 | T0061 - CUHK | 2021-11-12T18:05:22.263Z |
| 662 | MOCSCTF-B | 2021-11-12T18:20:57.806Z |
| 697 | S0086 - Man Kwan QualiEd College | 2021-11-12T20:27:09.344Z |
| 702 | DarkArmy | 2021-11-12T20:56:16.544Z |
| 722 | O0003 - ethical_Crackers | 2021-11-13T00:31:31.621Z |
| 736 | S0094 - King's College | 2021-11-13T01:43:59.408Z |
| 758 | O0034 - TeamMiracle | 2021-11-13T03:12:56.621Z |
| 761 | S0147 - De La Salle Secondary School, N.T. | 2021-11-13T03:26:35.355Z |
| 765 | T0036 - CUHK | 2021-11-13T03:27:18.885Z |
| 772 | T0043 - PolyU,CUHK,SPEED | 2021-11-13T03:40:52.126Z |
| 785 | T0075 - CUHK | 2021-11-13T04:17:53.638Z |
| 794 | O0085 - Hacker T | 2021-11-13T04:36:35.811Z |
| 804 | O0069 - Chris love Pro Fong | 2021-11-13T05:01:16.893Z |
| 813 | O0047 - FlowerTea | 2021-11-13T05:30:06.224Z |
| 820 | T0023 - CUHK | 2021-11-13T05:55:34.041Z |
| 857 | S0111 - Pui Ching Middle School | 2021-11-13T07:03:14.938Z |
| 860 | S0088 - Lock Tao Secondary School | 2021-11-13T07:06:05.727Z |
| 881 | O0063 - Jukerland | 2021-11-13T07:46:01.291Z |
| 898 | T0008 - HKMU | 2021-11-13T08:15:16.016Z |
| 901 | S0013 - St. Francis Xavier's School, Tsuen Wan | 2021-11-13T08:20:32.245Z |
| 917 | T0073 - HKBU,CUHK | 2021-11-13T08:50:31.093Z |
| 927 | S0074 - Aberdeen Technical School | 2021-11-13T09:03:21.154Z |
| 955 | T0018 - HKU | 2021-11-13T09:40:58.641Z |
| 1046 | T0027 - HKU,CUHK,PolyU | 2021-11-13T10:41:40.780Z |
| 1125 | O0067 - HC2021 | 2021-11-13T12:41:20.346Z |
| 1139 | O0046 - TeammatesNotFound | 2021-11-13T12:54:07.049Z |
| 1204 | S0057 - SKH Tang Shiu King Secondary School | 2021-11-13T14:27:44.875Z |
| 1245 | T0072 - IVE (CW) | 2021-11-13T15:25:14.859Z |
| 1281 | S0082 - SKH Kei Hau Secondary School | 2021-11-13T16:20:01.429Z |
| 1365 | S0036 - Carmel Pak U Secondary School | 2021-11-13T20:34:58.426Z |
| 1400 | O0060 - Nobody | 2021-11-14T02:29:02.510Z |
| 1412 | S0044 - The Chinese Foundation Secondary School | 2021-11-14T03:22:07.028Z |
| 1413 | O0068 - HC2021A | 2021-11-14T03:27:04.821Z |
| 1420 | O0082 - fortune | 2021-11-14T03:54:13.219Z |
| 1445 | T0064 - HKUST | 2021-11-14T04:41:12.511Z |
| 1527 | O0076 - hotelSausalito | 2021-11-14T08:18:45.101Z |
| 1539 | S0065 - SKH Kei Hau Secondary School | 2021-11-14T08:35:05.215Z |