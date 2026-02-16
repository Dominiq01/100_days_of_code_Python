from bs4 import BeautifulSoup
# import lxml
import requests

# with open("website.html") as website_file:
#     contents = website_file.read()
#     print(contents)
#
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.prettify())

# all_a_tags = soup.find_all(name="a")
# print(all_a_tags)
#
# for tag in all_a_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

res = requests.get("https://news.ycombinator.com/newest")
res.raise_for_status()

yc_website = res.text

soup = BeautifulSoup(yc_website, "html.parser")
print(soup)

all_titles = [el.text for el in soup.select(".titleline > a:first-child")]
all_links = [el.get("href") for el in soup.select(".titleline > a:first-child")]
all_scores = [int(el.text.split(" ")[0]) for el in soup.select(".score")]

highest_score_index = all_scores.index(max(all_scores))

print(all_titles)
# print(all_links)
print(all_scores)
print(highest_score_index)
print(all_titles[highest_score_index])

print(len(all_titles))
print(len(all_scores))
print(len(all_links))
















