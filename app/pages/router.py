from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix=['pages/'],
    tags=['Фронт']
)

templates = Jinja2Templates(directory='app/templates')

@router.get("/salon")
async def get_salone_page(
        request: Request,
):
    return templates.TemplateResponse(name='salon', context={'request': request})