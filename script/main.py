import os
import re
from typing import Union

import requests

file_regex = re.compile(r"\[(.+)\]\((https://file\.hkcert21\.pwnable\.hk/.+)\)")
cs = requests.Session()
cs.headers.update({
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5",
    "Cache-Control": "no-cache",
    "Cookie": f"token={open('flag.ini').read()}",
    "User-Agent": " ".join((
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "AppleWebKit/537.36 (KHTML, like Gecko)",
        "Chrome/95.0.4638.69 Safari/537.36"
    )),
    "Referer": "https://platform.ctf.hkcert.org/challenges"
})


def gen_question(challenge_id: Union[int, str]):
    api_resp = cs.get(f"https://platform.ctf.hkcert.org/api/challenges/{challenge_id}").json()
    challenge = api_resp['challenge']
    solves = api_resp['solves']
    # challenge data
    title = challenge['title']
    description = challenge['description']
    metadata = challenge['metadata']
    # metadata data
    author_thumbnail = cs.get(metadata['singerAvatarUrl']).content
    singer = "noimage" if metadata['singer'] == "?" else metadata['singer']
    with open(f"../avatar/{singer}.jpg", "wb") as f:
        f.write(author_thumbnail)
    challenge_thumbnail = cs.get(metadata['thumbnailUrl']).content
    with open(f"../thumbnail/{challenge_id}.jpg", "wb") as f:
        f.write(challenge_thumbnail)
    if file_re := file_regex.search(description):
        file_name, file_link = file_re.groups()
        file_data = cs.get(file_link).content
        description = file_regex.sub(r"[\1](./\1)", description)
        with open(f"../files/{file_name}", "wb") as f:
            f.write(file_data)
    return "\n".join((
        f"# {title['zh']} ({title['en']})",
        "",
        f"![](../thumbnail/{challenge_id}.jpg)",
        "",
        "| Key | Value |",
        "| --- | ----- |",
        f"| ID | {challenge_id} |",
        f"| Tags (Categories) | %s |" % (" ".join(f"#{tag}" for tag in challenge['categories'])),
        f"| Challenge release timestamp | {challenge['releasedAt']} |",
        f"| Score | {challenge['points']} |",
        f"| Total solves (Final) | {challenge['solves']} |",
        "",
        "# YouTube",
        "",
        "| Key | Value |",
        "| --- | ----- |",
        f"| Avatar | ![](../avatar/{metadata['singer']}.jpg)",
        f"| Singer (Challenge Author) | {metadata['singer']} |",
        f"| Link | https://youtu.be/{metadata['youtubeUrl']} |",
        "",
        "# Description",
        "",
        description,
        "",
        "# Solves",
        "| ID | Name | Solve at |",
        "| --- | ---- | -------- |",
        "\n".join(
            f"| {solve['id']} | {solve['user']['name']} | {solve['solvedAt']} |"
            for solve in solves
        ),
    ))


def main():
    main_readme = open("../README.md", "w", encoding="utf-8")
    main_readme.write("\n".join((
        "# 香港網絡保安新生代奪旗挑戰賽 2021 (HKCERT CTF 2021)",
        "This is a collection of all challenges (and writeups) in HKCERT CTF 2021",
        "",
        "# Challenges",
        "| ID | Chinese name | Name | Score | Solves | Tags (Categories) |",
        "| --- | ------------| ---- | ----- | ------ | ----------------- |",
        ""
    )))
    challenges_resp = cs.get("https://platform.ctf.hkcert.org/api/challenges")
    for challenge in challenges_resp.json()['challenges']:
        try:
            os.mkdir("../" + challenge['title']['zh'].replace("?", ""))
        except FileExistsError:
            pass
        with open("../" + challenge['title']['zh'].replace("?", "") + "/README.md", "w", encoding="utf-8") as f:
            f.write(gen_question(int(challenge['id'])))
            title = challenge['title']
            main_readme.write(f"| {challenge['id']} | {title['zh']} | {title['en']} | {challenge['points']} | {challenge['solves']} | %s |\n"
                              % (" ".join(f"#{tag}" for tag in challenge['categories'])))


if __name__ == '__main__':
    main()
