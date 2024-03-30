import uvicorn

from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from bin.db import coll
from bin.init import templates, newsapi_key
from bin.functions import parse_news

app = FastAPI()


@app.get('/')
async def root() -> FileResponse:
    return FileResponse("lib/template/index.html")


@app.get("/sentry-debug")
async def trigger_error() -> float:
    division_by_zero = 1 / 0
    return division_by_zero


@app.get("/search", response_class=HTMLResponse)
async def get_search_query(request: Request, q: Union[str, None] = None) -> templates.TemplateResponse:
    data = parse_news(f"https://newsapi.org/v2/everything?apiKey={newsapi_key}"
                      f"&sortBy=publishedAt&q={q}")

    if data['status'] == "ok":
        n = 0
        for item in data["articles"]:
            coll.insert_one(item)
            n += 1
        data["totalResults"] = n

    return templates.TemplateResponse(
        request=request,
        name="search_response.html",
        context={"data": data}
    )


if __name__ == "__main__":
    uvicorn.run(app,
                host='0.0.0.0',
                port=5000)
