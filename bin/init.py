import logging

import sentry_sdk

from json import load
from fastapi.templating import Jinja2Templates

newsapi_key = ""
logfile_path = ""

try:
    with open("config.json", "rt") as f:
        cfg = load(f)
        newsapi_key = cfg["news_api_key"]
        try:
            logfile_path = cfg["log_path"]
        except KeyError:
            logfile_path = "ntm.log"
except FileNotFoundError:
    logging.error("config file not found")
    input("press [enter] to exit")
    exit(0)

logging.basicConfig(filename=logfile_path)

sentry_sdk.init(dsn="https://e36c13527c6d93485c31205a1309e6da@o4506976349519872.ingest.us.sentry.io/4506976351223808",
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,)

templates = Jinja2Templates(directory="lib/template")
