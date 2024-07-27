from typing import Union

from fastapi import FastAPI
import uvicorn
import sys
SERVICE_PATH = "/root/chatv2"
sys.path.append(SERVICE_PATH)
from service.message.check_url import checkURL

app = FastAPI()

@app.get("/chat", summary="企业微信的验证接口", description="用于验证服务器有效性",
          response_description= "约定的验证密钥",)
async def vertify(msg_signature: str, timestamp: str, nonce: str, echostr: str):

    return checkURL(msg_signature, timestamp, nonce, echostr)


if __name__ == '__main__':
    uvicorn.run("chatv2_server:app", host="0.0.0.0", port=16668, reload=True)