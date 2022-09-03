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


# Подключаем роутеры к серверу
app.include_router(router=routes.router)


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