from sanic.response import json
from sanic import Blueprint

api = Blueprint("api", url_prefix="/api")

@api.route("/")
async def bp_root(request):
    return json({"message": "Hello from API"})
