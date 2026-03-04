# 150Mbps download, 10Mbps upload.
from internet_speed_twitter_bot import InternetSpeedTweeterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

bot = InternetSpeedTweeterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()