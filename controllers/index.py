logger = logging.getLogger(__name__)

router = APIRouter(
    prefix='home',
    tage=['home']
)


@router.get("/test")
async def welcome_home():
    logger.info("1")
    return {"1": '2'}