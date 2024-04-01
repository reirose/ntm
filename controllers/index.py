import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix='/test',
    tags=['home']
)


@router.get("/")
async def welcome_home():
    logger.info("1")
    return {"1": '2'}
