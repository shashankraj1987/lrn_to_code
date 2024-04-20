# https://www.youtube.com/watch?v=dEZKySL3M9c


# imports
# ----------------------------------------
from sqlalchemy import create_engine
from sqlalchemy import Select, text
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
import json

# Global Vars
# ----------------------------------------


# DB Functions
# ----------------------------------------
async def run_sql(db_engine: create_async_engine, sql_qry: str) -> [str]:
    async with db_engine.connect() as conn:
        result = await conn.execute(text(sql_qry))
        output = result.fetchall()
        return output


async def get_dist_sellers(request: Request):
    try:
        engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/ONDC")
    except Exception as e:
        print(e.args[0])
        return
    else:
        print("Connection Established.")

    stmt = "select distinct seller_np from ondc_app.fact_order_detail"
    try:
        sellers = await run_sql(engine, stmt)
        sellers_data = json.dumps([x[0] for x in sellers])
        return JSONResponse(sellers_data)
    except Exception as e:
        return PlainTextResponse(str(e))


