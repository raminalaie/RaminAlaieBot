# config.py

from dotenv import load_dotenv
import os

# بارگذاری فایل .env
load_dotenv()

# استفاده از متغیر توکن
TOKEN = os.getenv("TOKEN")
