import requests

def get_questions():
    res = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    res.raise_for_status()
    question_data = res.json()["results"]
    return question_data

