import requests
from json import loads


def parse_news(link: str) -> dict:
    res: dict = loads(requests.get(link).content)

    try:
        news: dict = {
            "totalResults": res["totalResults"],
            "status": "ok",
            "articles": []
        }
    except KeyError:
        return {"status": "error"}

    for item in res["articles"]:
        news["articles"].append({
            "source": item["source"]["name"],
            "author": item["author"],
            "title": item["title"],
            "url": item["url"],
            "content": item["content"]
        })

    return news