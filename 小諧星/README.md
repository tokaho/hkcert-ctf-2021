# 小諧星 (A Joke Cipher)

![](../thumbnail/22.jpg)

| Key | Value |
| --- | ----- |
| ID | 22 |
| Tags (Categories) | #crypto #☆☆☆☆☆ |
| Challenge release timestamp | 2021-11-12T10:00:00.000Z |
| Score | 50 |
| Total solves (Final) | 88 |

# YouTube

| Key | Value |
| --- | ----- |
| Avatar | ![](../avatar/mystiz.jpg)
| Singer (Challenge Author) | mystiz |
| Link | https://youtu.be/LoHKilN1-Ug |

# Description

> 早知不可獲勝
> 擠出喜感做諧星
> 無力當 你們崇尚的精英
> 有幸獻醜的 小丑 都不失敬

In the beginning of 2020, Khaled A. Nagaty invented a cryptosystem based on key exchange. The cipher is faster than ever... It is impossible to break, right?

To solve this challenge, you need to read the source code `chall.py`. Try to get those questions answered:

- Can `shared_key` generated from `y_A` and `y_B`?
- If so, how do we calculate `m` from `c` and `shared_key`?
- How can we convert the number `m` into a flag that is in the format `hkcert21{...}`?

_(Updated hint at 13/11 18:56)_

This is a key exchange scheme, where two entity (Alice and Bob) use the "cryptosystem" to exchange a shared key (i.e. after the process, they can generate the same key). After the key exchange, they can then use the shared key to encrypt / decrypt any message.

Thus, to decrypt the ciphertext back to plaintext (i.e. the flag), you will have to know the shared key, then use the "cryptosystem" to decrypt the ciphertext.

Can you get the shared key from the provided information? You have `p`, `y_A` and `y_B`, can you generate the shared key?

From the `exchange` function, `self.shared_key = S_AB`, and `S_AB = (y_AB * y_B) * S_A % self.p`; `y_AB = y_A * y_B`.

You have `p`, `y_A` and `y_B`, what are you missing? What is the relation between `S_A` and `y_A` and how can we use that?

_(Updated hint at 14/11 00:25)_

We are given `output.txt` that contains `y_A` and `y_B`, which are the public keys for Alice and Bob respectively. In this challenge, you need to derive the shared key `S_AB` from those public keys.

Look at the below line:

```python
y_AB = y_A * y_B
S_AB = (y_AB * y_B) * S_A % self.p
```

From above, we can compute the shared key `S_AB` from `y_A`, `y_B` and `S_A`. However, the challenge is so "secure" that we don't even need any private keys. That said we can compute `S_AB` solely from `y_A` and `y_B`. How? Look at the relationship between `S_A` and `y_A`. In short, `S_AB = (y_A * y_B * y_B) * y_A % p = (y_A * y_B)^2 % p`.

One question is, how do we convert base 16 (those strings starting with `0x`) to base 10? We can use [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base(10)To_Base(16)) to convert numbers. You can also find a product of two large numbers with Cyberchef. There is one question remain: What does `%` mean? Try to find it yourself!

Now we have the shared key `S_AB` (it is called `sk` below). If we have the ciphertext `c`, we can look the decrypt function shows how they decrypt:

```python
def decrypt(self, c):
    sk = self.shared_key
    if sk is None: raise Exception('Key exchange is not completed')

    return c // sk
```

Okay, it is now a simple division. Now it is a primary-level math (actually not). Now you have a message represented as a number, you can convert the number here with [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base(10)To_Base(16)From_Hex('Auto')) again. Now put down the number for the flag!

_(Updated hint at 14/11 02:45)_

If you are getting something like `0x686B636572743231`, that is `hkcert21` in HEX. Find a HEX decoder online to grab your flag!

### Attachments

- [the-little-comedian_58178adf8b732db76116f5bb7e0c4198.zip](./the-little-comedian_58178adf8b732db76116f5bb7e0c4198.zip)

# Solves
| ID | Name | Solve at |
| --- | ---- | -------- |
| 98 | T0047 - HKUST | 2021-11-12T10:08:55.073Z |
| 104 | 天枢Dubhe | 2021-11-12T10:10:54.865Z |
| 114 | O0027 - UND3r 20 D53 H473r5 4ND r374K3r | 2021-11-12T10:13:04.749Z |
| 154 | O0056 - AVADA KEDAVRA | 2021-11-12T10:21:37.173Z |
| 170 | T0057 - HKUST | 2021-11-12T10:26:16.420Z |
| 205 | T0042 - HKUST | 2021-11-12T10:38:27.313Z |
| 207 | O0067 - HC2021 | 2021-11-12T10:39:07.188Z |
| 221 | T0068 - HKMU | 2021-11-12T10:46:22.467Z |
| 269 | T0087 - CityU | 2021-11-12T11:10:53.774Z |
| 293 | T0095 - CUHK | 2021-11-12T11:28:50.869Z |
| 308 | T0003 - HKUST | 2021-11-12T11:39:58.036Z |
| 310 | T0036 - CUHK | 2021-11-12T11:40:51.947Z |
| 316 | O0055 - Braindump | 2021-11-12T11:48:20.440Z |
| 381 | T0039 - CUHK | 2021-11-12T12:40:29.386Z |
| 383 | T0075 - CUHK | 2021-11-12T12:40:43.660Z |
| 387 | T0028 - CUHK,PolyU,HKCC | 2021-11-12T12:45:51.463Z |
| 392 | MOCSCTF-B | 2021-11-12T12:50:03.280Z |
| 396 | The Duck | 2021-11-12T12:57:54.619Z |
| 400 | O0075 - wtfIsCTF | 2021-11-12T13:00:51.721Z |
| 408 | O0010 - HackyClub | 2021-11-12T13:05:58.146Z |
| 418 | T0086 - PolyU | 2021-11-12T13:10:15.349Z |
| 452 | O0004 - AUTOEXEC.BAT | 2021-11-12T13:41:32.245Z |
| 469 | T0065 - HKUST | 2021-11-12T13:56:44.879Z |
| 480 | T0064 - HKUST | 2021-11-12T14:07:37.819Z |
| 525 | S0043 - CARMEL SECONDARY SCHOOL | 2021-11-12T14:59:44.667Z |
| 528 | T0035 - CUHK | 2021-11-12T15:04:49.156Z |
| 558 | S0008 - The Chinese Foundation Secondary School | 2021-11-12T15:33:19.965Z |
| 570 | O0066 - QWErTY | 2021-11-12T15:45:54.354Z |
| 594 | T0038 - HKUST | 2021-11-12T16:19:41.031Z |
| 663 | O0062 - P2403 | 2021-11-12T18:26:01.721Z |
| 668 | T0059 - HKCC | 2021-11-12T18:37:17.149Z |
| 674 | O0084 - Never Gonna Let You Dump | 2021-11-12T18:55:17.566Z |
| 678 | DarkArmy | 2021-11-12T19:08:18.415Z |
| 686 | Super Guesser | 2021-11-12T19:29:52.475Z |
| 711 | T0010 - CityU,PolyU | 2021-11-12T22:29:06.927Z |
| 721 | T0032 - HKCC,UOWCHK | 2021-11-13T00:29:36.641Z |
| 737 | T0074 - PolyU | 2021-11-13T01:49:22.117Z |
| 748 | MOCSCTF-A | 2021-11-13T02:50:48.696Z |
| 773 | T0090 - HKUST | 2021-11-13T03:41:16.723Z |
| 841 | T0004 - HKUST,HKU SPACE,CUHK | 2021-11-13T06:41:27.242Z |
| 950 | O0039 - Buddiesss | 2021-11-13T09:34:59.751Z |
| 1047 | O0043 - The Almighty Dragon | 2021-11-13T10:42:13.070Z |
| 1080 | O0054 - Mama Sung | 2021-11-13T11:16:26.818Z |
| 1118 | T0025 - IVE(TM) | 2021-11-13T12:28:55.581Z |
| 1150 | O0072 - Royal Sunflower Tea | Tea to enrich your day | 2021-11-13T13:12:57.187Z |
| 1152 | O0053 - Si Daan Kau Gei La | 2021-11-13T13:15:47.649Z |
| 1187 | T0040 - HKCC,HKUST | 2021-11-13T14:02:58.208Z |
| 1233 | S0048 - TWGHs Wong Fut Nam College | 2021-11-13T15:06:55.220Z |
| 1237 | T0018 - HKU | 2021-11-13T15:10:45.233Z |
| 1254 | T0076 - CUHK | 2021-11-13T15:40:30.619Z |
| 1257 | T0030 - HKUST,CityU | 2021-11-13T15:45:18.870Z |
| 1290 | O0050 - 7M5_N650C | 2021-11-13T16:41:13.431Z |
| 1294 | T0049 - HKU SPACE | 2021-11-13T16:45:08.889Z |
| 1312 | S0057 - SKH Tang Shiu King Secondary School | 2021-11-13T17:06:31.061Z |
| 1319 | S0061 - Po Leung Kuk Choi Kai Yau School | 2021-11-13T17:25:36.877Z |
| 1323 | O0019 - Team 388 | 2021-11-13T17:32:52.419Z |
| 1331 | O0033 - HDMI | 2021-11-13T17:43:10.539Z |
| 1346 | T0037 - HKBU,CityU,HKMU | 2021-11-13T18:34:51.872Z |
| 1353 | S0042 - CARMEL SECONDARY SCHOOL | 2021-11-13T19:17:26.898Z |
| 1354 | O0073 - knownothing | 2021-11-13T19:22:24.238Z |
| 1358 | S0073 - Ying Wa College | 2021-11-13T19:46:42.984Z |
| 1367 | S0027 - HKSYCIA Wong Tai Shan Memorial College | 2021-11-13T20:50:21.208Z |
| 1368 | T0078 - HKU,CUHK | 2021-11-13T20:58:49.841Z |
| 1374 | S0033 - CCC Ming Yin College | 2021-11-13T23:22:06.367Z |
| 1381 | T0085 - PolyU | 2021-11-14T00:30:20.663Z |
| 1387 | O0046 - TeammatesNotFound | 2021-11-14T01:36:30.975Z |
| 1389 | S0112 - LOCK TAO SECONDARY SCHOOL | 2021-11-14T01:45:56.738Z |
| 1399 | S0003 - Kwun Tong Maryknoll College | 2021-11-14T02:26:54.847Z |
| 1406 | S0031 - Ying Wa College | 2021-11-14T02:42:22.802Z |
| 1424 | S0056 - Queen's College Old Boys' Association Secondary School | 2021-11-14T03:57:01.221Z |
| 1439 | T0088 - HKMU | 2021-11-14T04:28:45.358Z |
| 1441 | O0063 - Jukerland | 2021-11-14T04:36:20.002Z |
| 1470 | Beast_From_UIT | 2021-11-14T05:31:54.297Z |
| 1485 | O0016 - ePotato | 2021-11-14T06:22:28.879Z |
| 1493 | T0061 - CUHK | 2021-11-14T06:37:00.051Z |
| 1506 | O0009 - faulT | 2021-11-14T07:02:12.901Z |
| 1519 | S0018 - The Chinese Foundation Secondary School | 2021-11-14T07:57:47.612Z |
| 1546 | T0045 - HKU,HKUST,CUHK | 2021-11-14T08:47:42.112Z |
| 1548 | S0095 - Buddhist Sin Tak College | 2021-11-14T08:48:23.753Z |
| 1554 | O0086 - offsecFansclub | 2021-11-14T08:58:05.918Z |
| 1563 | S0093 - De La Salle Secondary School, N.T. | 2021-11-14T09:12:46.185Z |
| 1566 | O0061 - GoGoWeaponGo | 2021-11-14T09:13:45.139Z |
| 1567 | S0101 - Youth College (Kwai Fong) | 2021-11-14T09:15:07.573Z |
| 1568 | S0092 - Immaculate Heart of Mary College | 2021-11-14T09:16:08.865Z |
| 1575 | O0024 - SquidGamer | 2021-11-14T09:24:55.115Z |
| 1582 | S0005 - Shatin Tsung Tsin Secondary School | 2021-11-14T09:32:35.827Z |
| 1601 | O0047 - FlowerTea | 2021-11-14T09:39:54.491Z |
| 1603 | T0033 - HKMU | 2021-11-14T09:41:54.150Z |