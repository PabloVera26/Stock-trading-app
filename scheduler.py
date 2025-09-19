import schedule
import time
from app import run_stock
from datetime import datetime

def log_job_start():
    print("Job started at:", datetime.now())

schedule.every().minute.do(log_job_start)

schedule.every().minute.do(run_stock)

while True:
    schedule.run_pending()
    time.sleep(1)