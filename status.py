import requests
from slackbot.settings import API_TOKEN

API_URL = 'https://slack.com/api/users.setPresence?token={token}&presence={status}'

def set_away():
    """
    Botのステータスを離席にする
    :return:
    """
    res = requests.get(API_URL.format(token=API_TOKEN, status='away'))
    print(res.content)
    res = requests.get(API_URL.format(token=API_TOKEN, status='away'))
    print(res.content)
    res = requests.get(API_URL.format(token=API_TOKEN, status='away'))
    print(res.content)


def set_active():
    """
    Botのステータスを在籍にする
    :return:
    """
    res = requests.get(API_URL.format(token=API_TOKEN, status='auto'))
    print(res.content)
    res = requests.get(API_URL.format(token=API_TOKEN, status='auto'))
    print(res.content)
    res = requests.get(API_URL.format(token=API_TOKEN, status='auto'))
    print(res.content)
