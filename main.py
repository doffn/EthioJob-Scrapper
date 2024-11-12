from bot.telegram_bot import send_report
from bot.bard_api import bard_generate
from scraper.ethio_jobs import fetch_ethio_jobs
from scraper.database import load_data, save_data
import os

DATA_FILE = 'output.json'
CHAT_ID = os.environ.get("CHAT_ID")

def main():
    data = load_data(DATA_FILE)
    jobs = fetch_ethio_jobs()
    
    existing_ids = {job['ID'] for job in data.get('jobs', [])}
    new_jobs = [job for job in jobs if job['ID'] not in existing_ids]

    for job in new_jobs:
        summary = bard_generate(f"Summarize job: {job}")
        send_report(summary, CHAT_ID)
        data.setdefault('jobs', []).append(job)
    
    save_data(DATA_FILE, data)

if __name__ == "__main__":
    main()
