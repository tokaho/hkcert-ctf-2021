# 想改寫的事 (To Modify the Past)

![](../thumbnail/28.jpg)

| Key | Value |
| --- | ----- |
| ID | 28 |
| Tags (Categories) | #pwn #☆☆☆☆☆ |
| Challenge release timestamp | 2021-11-12T10:00:00.000Z |
| Score | 50 |
| Total solves (Final) | 54 |

# YouTube

| Key | Value |
| --- | ----- |
| Avatar | ![](../avatar/cire_meat_pop.jpg)
| Singer (Challenge Author) | cire_meat_pop |
| Link | https://youtu.be/iK7d9__wjsQ |

# Description

You may want to change something from the past, decide your future.

This challenge contains a buffer overflow vulnerability that allows attacker to write out-of-bound, overwriting the return address on the stack.

In order to get the flag, simply overwrite the return address with the address of `get_shell` function.

1. Find out the number of bytes input before reaching the return address, i.e. input 1234 'A's and next 8 bytes input will overwrite the return address.
    - How to find the offset: https://youtu.be/Ag0OcqbVggc?t=3408
2. Find out the address of `get_shell` function, e.g. 0x400123
    - How to find the address of a function: https://youtu.be/Ag0OcqbVggc?t=3651
3. Write an exploitation script to send the payload (attack input) to the server, usually this can be done by Python and a python module `pwntools`, e.g. `sendline(b'A'*1234+p64(0x400123))`
    - How to use pwntools to interact with the challenge: https://youtu.be/Ag0OcqbVggc?t=2356
4. Find the flag file in the server and then `cat` the flag!!
    - https://youtu.be/Ag0OcqbVggc?t=3824

Hints:

- Google the things that are new to you!
- https://www.youtube.com/watch?v=Ag0OcqbVggc

```bash
nc chalp.hkcert21.pwnable.hk 28028
```

### Attachments

- [warmup_6eab9fa64b5dd76649f6c0372315aabe.zip](./warmup_6eab9fa64b5dd76649f6c0372315aabe.zip)

# Solves
| ID | Name | Solve at |
| --- | ---- | -------- |
| 72 | DarkArmy | 2021-11-12T10:04:31.586Z |
| 81 | T0028 - CUHK,PolyU,HKCC | 2021-11-12T10:06:03.493Z |
| 111 | T0003 - HKUST | 2021-11-12T10:12:14.921Z |
| 121 | O0061 - GoGoWeaponGo | 2021-11-12T10:14:40.715Z |
| 131 | T0042 - HKUST | 2021-11-12T10:15:43.053Z |
| 133 | T0087 - CityU | 2021-11-12T10:15:50.897Z |
| 187 | T0047 - HKUST | 2021-11-12T10:30:53.591Z |
| 198 | T0036 - CUHK | 2021-11-12T10:34:44.630Z |
| 230 | O0027 - UND3r 20 D53 H473r5 4ND r374K3r | 2021-11-12T10:50:12.126Z |
| 238 | T0064 - HKUST | 2021-11-12T10:53:49.664Z |
| 253 | T0090 - HKUST | 2021-11-12T11:02:24.973Z |
| 273 | O0025 - SatayBeefNoodles | 2021-11-12T11:13:08.780Z |
| 322 | T0086 - PolyU | 2021-11-12T11:52:12.067Z |
| 352 | MOCSCTF-A | 2021-11-12T12:12:10.823Z |
| 354 | O0056 - AVADA KEDAVRA | 2021-11-12T12:19:32.256Z |
| 417 | O0043 - The Almighty Dragon | 2021-11-12T13:10:10.109Z |
| 427 | S0043 - CARMEL SECONDARY SCHOOL | 2021-11-12T13:18:41.924Z |
| 432 | MOCSCTF-B | 2021-11-12T13:21:30.508Z |
| 435 | T0038 - HKUST | 2021-11-12T13:23:27.027Z |
| 445 | O0059 - Fragile❤ | 2021-11-12T13:33:31.222Z |
| 446 | O0010 - HackyClub | 2021-11-12T13:34:26.838Z |
| 494 | T0030 - HKUST,CityU | 2021-11-12T14:30:25.189Z |
| 521 | O0024 - SquidGamer | 2021-11-12T14:56:30.171Z |
| 541 | Beast_From_UIT | 2021-11-12T15:17:44.680Z |
| 583 | O0066 - QWErTY | 2021-11-12T15:58:50.147Z |
| 605 | T0057 - HKUST | 2021-11-12T16:35:20.069Z |
| 617 | T0059 - HKCC | 2021-11-12T16:56:57.536Z |
| 623 | The Duck | 2021-11-12T16:59:25.634Z |
| 645 | T0039 - CUHK | 2021-11-12T17:44:04.608Z |
| 650 | O0055 - Braindump | 2021-11-12T17:55:21.418Z |
| 696 | S0086 - Man Kwan QualiEd College | 2021-11-12T20:23:51.207Z |
| 699 | T0025 - IVE(TM) | 2021-11-12T20:45:44.815Z |
| 720 | Super Guesser | 2021-11-13T00:23:40.888Z |
| 725 | T0037 - HKBU,CityU,HKMU | 2021-11-13T00:41:08.362Z |
| 774 | 天枢Dubhe | 2021-11-13T03:48:00.262Z |
| 799 | O0063 - Jukerland | 2021-11-13T04:49:47.714Z |
| 865 | O0016 - ePotato | 2021-11-13T07:15:00.365Z |
| 893 | T0085 - PolyU | 2021-11-13T08:03:45.333Z |
| 942 | S0049 - TWGHs Wong Fut Nam College | 2021-11-13T09:24:00.186Z |
| 960 | O0072 - Royal Sunflower Tea | Tea to enrich your day | 2021-11-13T09:57:25.891Z |
| 962 | O0062 - P2403 | 2021-11-13T10:01:19.775Z |
| 1020 | T0010 - CityU,PolyU | 2021-11-13T10:23:36.395Z |
| 1163 | S0048 - TWGHs Wong Fut Nam College | 2021-11-13T13:30:12.517Z |
| 1303 | O0026 - Zak0 | 2021-11-13T16:53:38.396Z |
| 1316 | O0039 - Buddiesss | 2021-11-13T17:14:00.412Z |
| 1327 | S0073 - Ying Wa College | 2021-11-13T17:36:54.801Z |
| 1403 | S0031 - Ying Wa College | 2021-11-14T02:36:06.872Z |
| 1481 | S0059 - Fanling Kau Yan College | 2021-11-14T06:19:19.267Z |
| 1504 | S0033 - CCC Ming Yin College | 2021-11-14T06:58:30.862Z |
| 1517 | O0076 - hotelSausalito | 2021-11-14T07:50:37.767Z |
| 1544 | O0004 - AUTOEXEC.BAT | 2021-11-14T08:45:00.254Z |
| 1550 | T0004 - HKUST,HKU SPACE,CUHK | 2021-11-14T08:50:23.861Z |
| 1560 | S0003 - Kwun Tong Maryknoll College | 2021-11-14T09:06:56.865Z |
| 1569 | O0054 - Mama Sung | 2021-11-14T09:16:58.072Z |