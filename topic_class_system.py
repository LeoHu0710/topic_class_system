## fastapi 路由主程式

import os
import re
import json
import yaml
import emoji
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.responses import JSONResponse
from fastapi import APIRouter, UploadFile, File

from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

import prompt
from log import logger



## setting
load_dotenv()

with open("config.yaml", "r") as config_detail:
    config_data = yaml.load(config_detail, Loader=yaml.SafeLoader)

## 需自備API KEY，Gemini有免費額度，每個google帳號都可以創建 https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw
gemini_api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
llmmodel = genai.GenerativeModel(config_data['llm_model'])

## 需登入 hugging face
model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
topic_model = BERTopic(embedding_model=model)

router = APIRouter()

## test
@router.get("/root")
async def root():
    """
    測試 api 是否有通
    """

    logger.info("get root test !!")
    return {"message": "get root test !!"}

## main router
@router.post("/tcs")
async def topic_class_system_function(json_data : UploadFile = File(...)):
    """
    獲取 要分析的 json
     
    - **sentences_list** : json，格式為[str,str,....]   
    
    返回 每個主題的文章篇數與所佔總資料的百分比
    """

    try :
        logger.info("Starting topic_class_system_function")
        sentences_list_emoji2txt = []
        contents = await json_data.read()
        sentences_list = json.loads(contents)
        logger.info(f"Sentences from uploaded JSON: {sentences_list[:3]}")

        for text in sentences_list :
            text = emoji.replace_emoji(text, replace='')
            sentences_list_emoji2txt.append(text)
        logger.info(f"Processed sentences list: {sentences_list_emoji2txt[:3]}")

        topics, probs = topic_model.fit_transform(sentences_list_emoji2txt)
        logger.info(f"Model output - topics: {topics[:3]}, probs: {probs[:3]}")

        ## 顯示每個主題的代表字詞
        topic_info = topic_model.get_topic_info()
        logger.info(f"topic_info:\n{topic_info[:3]}")
        topic_representation = topic_info["Representation"]
        total_topic_representation = len(topics)
        logger.info(f"topic_representation:\n{topic_representation[:3]}")

        product_analyst_prompt = prompt.product_analyst_prompt
        topic_representation_prompt = f"""
        There are exactly {total_topic_representation} data entries, and each entry belongs to only one topic. Please analyze and calculate accordingly.
        ---
        The original input (topic_representation) is as follows:
        {topic_representation}
        ---
        """
        logger.info("Sending prompt to LLM")
        ## 由於LLM有不確定性，如果需要完全固定輸出可以將 temperature = 0
        ## Ex: generate_content_async(prompt, generation_config={"temperature": 0.3})
        response = await llmmodel.generate_content_async(product_analyst_prompt + topic_representation_prompt)
        ## 檢查返回結果是否有 text 屬性
        if hasattr(response, 'text'):
            response_strip = response.text.strip()
        logger.info(f"Success! Response :\n{response_strip}")
        print(response_strip)
        return JSONResponse(status_code = 200, content = response_strip)
    
    except Exception as e:
        logger.error(f"Error in topic_class_system_function: {e}")
        return JSONResponse(status_code = 500, content = f"Error in topic_class_system_function: {e}")
