from urllib import response
import requests
import re
# from bs4 import BeautifulSoup
import urllib.request


numerade_link = input("Insert numerade link: ").strip('/')
soup = requests.get(numerade_link).text

# soup = BeautifulSoup(response_html, 'html.parser')
# print(soup.find('videoUrl'))
# with open('data/video_link.html', 'w') as file:
#     file.write(response_html)

video_url_code = re.search('videoUrl = "(.*)"', soup).group(1)
video_title = re.match('https://www.numerade.com/ask/question/(.*)', numerade_link).group(1)
video_url = fr"https://cdn.numerade.com/ask_video/{video_url_code}.mp4"

#downloading video
resp = requests.get(video_url)
with open(video_title+'.mp4', "wb") as f:
    f.write(resp.content)

