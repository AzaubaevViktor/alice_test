#!/usr/bin/env python
from aiohttp import web
import os
import logging

from alice import AliceQuestion


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    logging.info(request)
    print(request.text())
    return web.Response(text=text)


async def alice(request):
    data = await request.json()
    q = AliceQuestion(data)
    print(data)
    answer_json = q.process()
    return web.json_response(answer_json)


async def webhook(request):
    text = """<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: e61e2475dcfaa0e7</body>
</html>"""
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.post('/', alice),
                web.get('/{name}', handle),
                web.get('/yandex_e61e2475dcfaa0e7.html', webhook)])
port = 8080
server = "127.0.0.1"
if 'PORT' in os.environ:
    port = os.environ['PORT']
    server = "0.0.0.0"

web.run_app(app, host=server, port=port)
