from aiohttp import web
from aiohttp import ClientSession
import json
import logging
import pathlib


# PATH CONSTANTS
CWD = pathlib.Path(__file__).resolve().parent
SERVICES_CONFIG_PATH = CWD / "modules.json"


# CONFIG
routing_config = {}

def load_route_config():
    with open(SERVICES_CONFIG_PATH) as conf_file:
        data = json.load(conf_file)
        for route in data["routes"]:
            routing_config[route["service"].lower()] = {"host": route["host"], "port": route["port"]}
    print(routing_config)

routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    return web.json_response({"msg": "It appears you are lost"})

def route_creator(service: str, host: str, port: int):
    async def route(request):
        body = await request.json() if request.can_read_body else {}
        method = request.method
        rel_url = request.url.path[len(service) + 1:]    # URL excluding host, port and service name
        rel_url = '/' if not len(rel_url) else rel_url   # URL is just '/' if the OG URL was /service_name

        if method == "GET":
            async with ClientSession() as session:
                async with session.get(f'http://{host}:{port}{rel_url}', params=request.query) as resp:
                    json_resp = await resp.json()
                    return web.json_response(json_resp)
        elif method == "POST":
            async with ClientSession() as session:
                async with session.post(f'http://{host}:{port}{rel_url}', json=body) as resp:
                    json_resp = await resp.json()
                    return web.json_response(json_resp)

        return web.json_response({"msg": f"Beep boop appears something as failed?"})


    return route



if __name__ == "__main__":
    load_route_config()

    if routing_config.keys():
        logging.basicConfig(level=logging.DEBUG)
        app = web.Application()

        app.add_routes(routes)
        for k, v in routing_config.items():
            app.add_routes([web.route('*', f'/{k}/'+ '{tail:.*}', route_creator(k, v["host"], v["port"]))])


        web.run_app(app)
    else:
        print("No routes in the table! Quitting now.")

