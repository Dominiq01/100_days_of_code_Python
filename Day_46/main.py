# https://www.officialcharts.com/charts/singles-chart/20010805/
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import os
header = {
    "User-Agent": os.environ.get("HEADER")
}

URL = "https://www.officialcharts.com/charts/singles-chart/"
user_input = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

res = requests.get(f"{URL}/{user_input}", headers=header)

res.raise_for_status()

contents = res.text
soup = BeautifulSoup(contents, "html.parser")

list_of_titles = [title.text for title in soup.select(".description.block p a.chart-name span:last-child")]

print(list_of_titles)

ytmusic = YTMusic('browser.json')

results = []
for title in list_of_titles:
    try:
        result = ytmusic.search(title, filter="songs")
        videoID = result[0]['videoId']
        results.append(videoID)
        print(result)
    except IndexError:
        print("Song doesn't exists on yt music :(")

playlist_title = f"Top 100 Songs from {user_input}"
my_new_playlist = ytmusic.create_playlist(
    title=playlist_title,
    description="My playlist with top 100 songs from the day I was born.",
    video_ids = results
)

print(f"Success! Playlist created. ID: {my_new_playlist}")