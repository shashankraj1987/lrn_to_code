from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.exceptions import HTTPException


import async_for_loop_mcoding as met


async def not_implemented(request: Request):
    # raise HTTPException(status_code=500, detail="Internal Server Error")
    return PlainTextResponse("Working on this page", status_code=500)


routes = [
    Route(path="/sellers", endpoint=met.get_dist_sellers, methods=["GET"]),
    Route(path="/", endpoint=not_implemented, methods=["GET"]),
]

app = Starlette(debug=True, routes=routes)


def main():
    import uvicorn
    uvicorn.run(app, port=5000, log_level="info")


if __name__ == "__main__":
    main()
