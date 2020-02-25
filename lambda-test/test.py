import requests


def getHTML(url):
    res = requests.get(url)
    return res.text


def handler(event, context):
    return {'event': str(event), 'context': str(context)}
