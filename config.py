import os

# Environment Variables
BARD_API_KEY = os.environ.get("BARD")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GMAIL_PASSWORD = os.environ.get("PASSWORD")
POE_TOKENS = {
    'p-b': os.environ.get('PB'), 
    'p-lat': os.environ.get('PLAT')
}
