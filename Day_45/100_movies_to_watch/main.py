import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
res.raise_for_status()
print(res.text)
contents = res.text

soup = BeautifulSoup(contents, "html.parser")

titles = [title.text for title in soup.select(".article-title-description__text h3.title")]

print(titles)
titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as new_file:
    for title in titles:
        new_file.write(f"{title}\n")

print(titles)