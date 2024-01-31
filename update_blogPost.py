## update_blogPost.py
import feedparser

blog_url = "https://blog.rss.naver.com/kimdu001.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=doyoon530&show_icons=true&theme=radical)<br>

## 논문 Dissertation<br>
[자이로 센서 데이터를 활용한 양치 위치 추정 및 비지도 학습 클러스터링을 통한 검증](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11646290)<br><br>

## 연결 Link<br>
[![Naver blog Badge](https://img.shields.io/badge/-Naver%20blog-brightgreen?style=flat-square&logo=Naver&logoColor=white&link=https://blog.naver.com/kimdu001)](https://blog.naver.com/kimdu001)
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
