import asyncio
from datetime import datetime

import uvloop
from mode import Worker

from gravity.app import App


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


app = App(node_id='test')


@app.timer(interval=1)
async def timer():
    date_now = datetime.now()
    await app.send(date_now)


if __name__ == '__main__':
    Worker(app, loglevel="info", loop=loop).execute_from_commandline()

