import feedparser

feed_url = "https://bsssss.tistory.com/rss"  # RSS 주소
feed = feedparser.parse(feed_url)

print(f"📡 RSS URL: {feed_url}")
print(f"📌 Status Code: {feed.get('status', 'Unknown')}")

markdown_text = """
### Hi there 👋   

### 📖   Interest   
     - BackEnd
     - DevOps   

###  🐱 github stats  

<div id="main" align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=qpyu66&count_private=true&show_icons=true&theme=radical"
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
</div>

###  💁‍♀️ About Me  
<p align="center">
    <a href="https://bsssss.tistory.com/"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=Blogger&logoColor=white"/></a>
    <a href="mailto:qpyu66@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=qpyu66@gmail.com"/></a>
</p>

<br>

### 📕 Latest Blog Posts   
"""

if not feed.entries:
    markdown_text += "⚠️ 블로그 글을 불러올 수 없습니다. RSS 설정을 확인해주세요. <br>\n"
    print("⚠️ RSS 피드를 가져오지 못했습니다. RSS 주소를 확인하세요.")
else:
    for i in feed.entries[:3]:
        title = i.get("title", "제목 없음")
        link = i.get("link", "#")
        markdown_text += f"<a href=\"{link}\"> {title} </a> <br>\n"
        print(f"✔ {title} → {link}")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
