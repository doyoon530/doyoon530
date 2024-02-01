## update_blogPost.py
import feedparser

blog_url = "https://blog.rss.naver.com/kimdu002.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=doyoon530&hide=contribs,prs&show_icons=true&theme=graywhite) ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=doyoon530&layout=compact) <br>

## 스킬 Skills<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=Kotlin&logoColor=white">
<br><br>

## 논문 Dissertation<br>
[자이로 센서 데이터를 활용한 양치 위치 추정 및 비지도 학습 클러스터링을 통한 검증](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11646290)<br><br>

## 대회 Competition<br>
제 1회 ART-AWS 리빙랩글로컬 해커톤 🥈<br><br>

## 연결 Link<br>
[<img src="https://img.shields.io/badge/Blog-03C75A?style=for-the-badge&logo=Naver&logoColor=white">](https://blog.naver.com/kimdu001)
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
