from aiohttp import web
from app import create_app


web.run_app(create_app(), port='8002')