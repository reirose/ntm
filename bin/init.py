import sentry_sdk
from fastapi.templating import Jinja2Templates

sentry_sdk.init(
    dsn="https://e36c13527c6d93485c31205a1309e6da@o4506976349519872.ingest.us.sentry.io/4506976351223808",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
templates = Jinja2Templates(directory="lib/template")