import json
import os
import requests


class MyLinePush:
    def __init__(self):
        with open("config.json") as conf:
            confJson = json.load(conf)

        self.URL = "https://api.line.me/v2/bot/message/push"
        Line = confJson["Line"]
        self.ACCESS_TOKEN = Line["ACCESS_TOKEN"]
        self.To = Line["To"]

    def pushline(self, content="Hello"):
        data = {
            "to": self.To,
            "messages": [
                {
                    "type": "text",
                    "text": content
                }
            ]
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.ACCESS_TOKEN
        }
        requests.post(self.URL, data=json.dumps(data), headers=headers)

# 実行方法
# from linepush import MyLinePush
# a = MyLinePush()
# a.pushline("こんにちは")

# config.json
# {
#   "Line": {
#     "To": "<LineId>",
#     "ACCESS_TOKEN": "<ACCESS_TOKEN>"
#   }
# }
