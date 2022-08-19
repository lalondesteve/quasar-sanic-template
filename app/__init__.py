from sanic import Sanic, response
from app.api import api

QUASAR_BUILD = './dist/spa'

app = Sanic(__name__)
app.config.CORS_ORIGINS = "http://localhost"

# import api blueprint
app.blueprint(api)

# Serve Quasar Build
app.static('/static', f'{QUASAR_BUILD}/static')
app.static('/assets', f'{QUASAR_BUILD}/assets')
app.static('/icons', f'{QUASAR_BUILD}/icons')
app.static('/favicon.ico', f'{QUASAR_BUILD}/favicon.ico')


@app.get("/")
@app.get("/<path>")
async def quasar_route(_, path=''):
    return await response.file(f'{QUASAR_BUILD}/index.html')


@app.get("/ping")
async def ping(_):
    return response.json({'pong'})
