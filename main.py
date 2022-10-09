from urllib import response
import requests
import re

# from bs4 import BeautifulSoup
import urllib.request
 

numerade_link = input("Insert numerade link: ").strip("/")
soup = requests.get(numerade_link).text

# soup = BeautifulSoup(response_html, 'html.parser')
# print(soup.find('videoUrl'))
# with open('data/video_link.html', 'w') as file:
#     file.write(response_html)

video_url_code = re.search('videoUrl = "(.*)"', soup).group(1)
video_title = re.match(
    "https://www.numerade.com/ask/question/(.*)", numerade_link
).group(1)
video_url = f"https://cdn.numerade.com/encoded/{video_url_code}.mp4"

print(video_url)
# downloading video
resp = requests.get(video_url)
with open(video_title + ".mp4", "wb") as f:
    f.write(resp.content)

# "https://api.spotify-downloader.com/"
# https://api.codetabs.com/v1/proxy/?quest=https://get.mp3fromyou.tube/download/VSapCTmw31g/mp3/320/1663227321/730d1a571f566fca28f076ae3bcfb73d18be46bc9e8215bb7a03bf05cf5029b9/0
# https://spotify-downloader.com/verify.html?key=dl_key_0.2345341100735221
