from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_NUM = os.environ.get("PHONE_NUM")
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message_to_sent):
        self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_to_sent,
            to=f'whatsapp:{PHONE_NUM}'
        )