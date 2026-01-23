from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

# Теперь мы разрешаем и GET, и HEAD запросы
@app.api_route("/", methods=["GET", "HEAD"])
async def root():
    return {"status": "working", "message": "Бот скоро будет здесь!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
