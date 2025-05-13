import io
import sys
import logging

# 將控制台輸出編碼設為 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 創建一個 logger 物件
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 創建一個檔案處理器，將日誌訊息寫入檔案
file_handler = logging.FileHandler('topic_class_system.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# 創建一個格式化器，定義日誌訊息的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 將檔案處理器添加到 logger 物件
logger.addHandler(file_handler)
