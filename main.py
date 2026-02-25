import os
import socket
import threading
from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "proxy working"}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"])
async def proxy(request: Request, path: str):
    url = str(request.url)
    headers = dict(request.headers)
    headers.pop("host", None)
    body = await request.body()
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=body,
            follow_redirects=True
        )
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
