## 話題比例分類系統開發 啟動程式

import yaml
import asyncio
import uvicorn
from fastapi import FastAPI

from log import logger
from topic_class_system import router as tcs

# load config
with open("config.yaml", "r") as config_detail:
    config_data = yaml.load(config_detail, Loader=yaml.SafeLoader)

app = FastAPI(
    title = "Topic class system",
    description = "對文章進行話題分類,並統計每個話題出現的篇數與其佔整體資料的百分比。"
)

app.include_router(tcs)

async def main():
    ## Setting uvicorn config
    config = uvicorn.Config("main:app", host = config_data['host'], port = config_data['port'], reload = True)
    server = uvicorn.Server(config)
    await server.serve()

## start Uvicorn server
if __name__ == "__main__":
    logger.info(f"Starting the Topic class system. host: {config_data['host']}, port: {config_data['port']}")
    asyncio.run(main())