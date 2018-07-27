#!/usr/bin/env python
from aiohttp import web
import os

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def webhook(request):
    text = """<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: e61e2475dcfaa0e7</body>
</html>"""

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/yandex_e61e2475dcfaa0e7.html', webhook)])

web.run_app(app, host="0.0.0.0", port=os.environ['PORT'] or 8080)
