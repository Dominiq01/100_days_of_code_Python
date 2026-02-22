# https://www.amazon.it/Ultra-Pro-Penny-collezione-trasparenti/dp/B085DNDLC1/?_encoding=UTF8&pd_rd_w=8lv8Z&content-id=amzn1.sym.b4434d57-8aaf-4606-a7d8-4a94c430d33e%3Aamzn1.symc.b1464ab7-6d6a-4fc8-be8f-f2e9bcc64228&pf_rd_p=b4434d57-8aaf-4606-a7d8-4a94c430d33e&pf_rd_r=6BXWZBVSCW1B5ZN29FNT&pd_rd_wg=Ii3Ug&pd_rd_r=44864c17-2e63-4947-9eb3-2ac296771f48&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d&th=1
import requests
import os
import smtplib
my_email = "dominik.wedzina1245@gmail.com"
smtp = "smtp.gmail.com"
from bs4 import BeautifulSoup

header = {
    "User-Agent": os.environ.get("HEADER")
}
res = requests.get("https://www.amazon.it/Ultra-Pro-Penny-collezione-trasparenti/dp/B085DNDLC1?th=1", headers=header)
res.raise_for_status()

amazon_soup = BeautifulSoup(res.text, "html.parser")

whole_price = amazon_soup.find("span", class_="a-price-whole").text
decimal_price = amazon_soup.find("span", class_="a-price-fraction").text

curr_price = float((whole_price + decimal_price).replace(',', '.'))
print(curr_price)

# if curr_price < 8:
#     with smtplib.SMTP(smtp) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="dominik.wedzina@onet.pl",
#                             msg=f"PRICE ALERT!\n\n{curr_price}")