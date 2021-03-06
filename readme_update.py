import feedparser, datetime

tistory_uri="https://bsssss.tistory.com/" #Your blog address here
feed = feedparser.parse(tistory_uri+"/rss")

markdown_text = """
### Hi there 👋   

### 📖   Interest   
     - BackEnd
     - DevOps   

###  🐱 github stats  

<div id="main" align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=qpyu66&count_private=true&show_icons=true&theme=radical"
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
<!--         <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=qpyu66&layout=compact"   
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>  -->
</div>

###  💁‍♀️ About Me  
<p align="center">
    <a href="https://bsssss.tistory.com/"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=Blogger&logoColor=white"/></a>
    <a href="mailto:qpyu66@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=qpyu66@gmail.com"/></a>
</p>

<br>

### 📕 Latest Blog Posts   

""" # list of blog posts will be appended here

lst = []


for i in feed['entries'][:3]:
#     dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
#     markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
#     markdown_text += f"{i['title']} {i['link']} <br>\n"
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"


    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
