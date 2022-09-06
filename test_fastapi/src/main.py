'''
import uvicorn
from fastapi import FastAPI
import routes
from db import engine
from db import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
)
'''

# Подключаем роутеры к серверу
#app.include_router(router=routes.router)
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI( # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",)
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Test WebSocket</h1>
        <form action="" onsubmit="sendMessage(event)">
            <textarea id="messageText" autocomplete="off "name="post" cols="40" rows="3"></textarea>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('div')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    counter = 1
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        #data_1 = websocket.receive_json()
        await websocket.send_json({"New Message:": f"{counter}.{data}"})
        counter += 1

      
if __name__ == "__main__":
    # Приложение может запускаться командой
    # `uvicorn main:app --host 127.0.0.1 --port 8000`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
   
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
    )