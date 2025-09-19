import schedule
import time
from app import run_stock
from datetime import datetime

def basic_job():
    print("Job started at:", datetime.now())