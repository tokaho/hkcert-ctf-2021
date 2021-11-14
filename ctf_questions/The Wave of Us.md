# 無聲浪 (The Wave of Us)


| Key | Value |
| --- | ----- |
| ID | 11 |
| Tags (Categories) | "#forensics", "#☆☆☆☆☆" |
| Challenge release timestamp | 2021-11-12T10:00:00.000Z |

# YouTube

| Key | Value |
| --- | ----- |
| Singer (Challenge Author) | byronwai
| Link | https://youtu.be/AGU_FMudl1Y

# Description

> 像密碼 若無線索
> 只好留下困惑

_IEEE Transactions on Signal Processing, Vol.51, (no.4), pp.1020–33, 2003._

Walkthrough:

1. Google the description
2. Find the [GitHub repository](https://github.com/toots/microsoft-audio-watermarking) written by Microsoft 
3. Download the tool (repository) in zip
4. Extract the zip, for example, you extract the zip under `D:\Downloads`
5. Copy the audio file (`waterwave.wav`) to `D:\Download\microsoft-audio-watermarking-master\build\`
6. Open the command prompt and execute the following:
```
D:\Download\microsoft-audio-watermarking-master\build\detect2003.exe D:\Download\microsoft-audio-watermarking-master\build\watermark.wav
```
7. Record ass Hex decoded
7. Convert all Hex it into ASCII characters, there are many [online tools](https://www.binaryhexconverter.com/hex-to-ascii-text-converter) that can be used
8. Profit

有部分參賽者反應 Github 上的工具未能正常執行。請使用命令提示字元(cmd.exe)打開該程式。
There is some contester mentioned that the tool on Github cannot be executed normally. Please use command prompt (cmd.exe) to execute the program.

### Attachments

- [the-wave-of-us_ed82d2616c9d118d8dc8637022902330.zip](https://file.hkcert21.pwnable.hk/the-wave-of-us_ed82d2616c9d118d8dc8637022902330.zip)