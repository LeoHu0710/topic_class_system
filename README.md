# 話題比例分類系統開發

## 專案目標

本專案使用指定的 JSON 格式作為輸入，例如 `list[str, str, ...]`，其中每筆資料為一段自然語言撰寫的文章內容。系統會對這些文章進行話題分類，並統計每個話題出現的篇數及其佔整體資料的百分比。

---

## 使用方法

1. **設定 Google API 金鑰**  
   - 建立 `.env` 檔案，格式如下：  
     ```
     GOOGLE_API_KEY="你的金鑰"
     ```
   - [取得 Gemini API 金鑰](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw)

2. **登入 Hugging Face**  
   - 本專案使用 Hugging Face 的開源模型，需先註冊帳號並取得 Access Token。
3. 安裝依賴套件
    ```
    pip install -r requirements.txt
    ```
4. 執行主程式
    ```
    python main.py
    ```

## 範例輸出 :  

![範例圖片](example.png)

## 資料夾結構

    root_folder/  
    └── .env  
    └── .gitignore  
    └── config.yaml  
    └── requirements.txt  
    └── README.md  
    └── prompt.py  
    └── log.py  
    └── main.py  
