# 想改寫的事 (To Modify the Past)


| Key | Value |
| --- | ----- |
| ID | 28 |
| Tags (Categories) | "#pwn", "#☆☆☆☆☆" |
| Challenge release timestamp | 2021-11-12T10:00:00.000Z |

# YouTube

| Key | Value |
| --- | ----- |
| Singer (Challenge Author) | cire_meat_pop
| Link | https://youtu.be/iK7d9__wjsQ

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

- [warmup_6eab9fa64b5dd76649f6c0372315aabe.zip](https://file.hkcert21.pwnable.hk/warmup_6eab9fa64b5dd76649f6c0372315aabe.zip)