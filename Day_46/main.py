# https://www.officialcharts.com/charts/singles-chart/20010805/
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

URL = "https://www.officialcharts.com/charts/singles-chart/"
user_input = input("Which year do you want to travel to? Type date in this format YYY-MM-DD: ")

res = requests.get(f"{URL}/{user_input}", headers=header)

res.raise_for_status()

contents = res.text
soup = BeautifulSoup(contents, "html.parser")

list_of_titles = [title.text for title in soup.select(".description.block p a.chart-name span:last-child")]

print(list_of_titles)
# 867051867517-pdl6ntjd9cmf7hjo2aum90o1s28i9gb0.apps.googleusercontent.com
YTMusic.setup_oauth()
ytmusic = YTMusic()