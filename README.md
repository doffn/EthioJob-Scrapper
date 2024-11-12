Based on your provided code, here's an interactive `README.md` file with clear instructions and emojis to make it engaging and user-friendly. The README covers the core functionalities of your project, dependencies, and how to set up and run the application.

---

# 📧 Telegram Bot & Job Scraper 🚀

Welcome to the **Telegram Bot & Job Scraper** project! This application combines the power of **Telegram**, **Google Bard AI**, and **Poe API** to automate job searches and send email notifications with personalized content. 🛠️

## 📋 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## 💡 Introduction
This project includes:
1. A **Telegram bot** that notifies you about new job postings.
2. Integration with **Google Bard AI** and **Poe API** for content summarization.
3. **Job scraping** from multiple sources and automated data storage in JSON.
4. An **email sender** feature for sending CVs to companies.
5. Interactive and automated reporting using the **Telegram bot**.

## 🌟 Features
- 🤖 **Telegram Bot**: Sends notifications with job details.
- 🔍 **Job Scraping**: Retrieves job listings from various sources (like EthioJobs).
- ✉️ **Email Sender**: Sends personalized emails with attachments.
- 🧠 **AI-Powered Summarization**: Uses Google Bard AI and Poe API for job description summaries.
- 📂 **Data Storage**: Saves job listings in a local JSON file for tracking.

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/telegram-job-scraper.git
cd telegram-job-scraper
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔧 Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
PB=your_poe_api_token
PLAT=your_platform_api_token
PASSWORD=your_email_password
BARD=your_google_bard_api_key
TELEGRAM_API=your_telegram_bot_api
```

### ⚠️ Important
- Ensure you have **enabled** less secure apps for your Gmail account or generate an **App Password** for secure access.
- Obtain your **Poe API** and **Google Bard API** keys from their respective platforms.

## 🚀 How to Run

### 1. Start the Telegram Bot
```bash
python main.py
```

### 2. Sending Emails
Update the `email_sender()` function with your details, and run:
```bash
python email_sender.py
```

### 3. Running the Job Scraper
```bash
python job_scraper.py
```

## 📦 Dependencies
Here's a list of the major libraries used in this project:

- `requests`: For making HTTP requests.
- `telebot`: For interacting with Telegram's API.
- `google.generativeai`: For content summarization using Google Bard.
- `smtplib`: For sending emails.
- `beautifulsoup4`: For scraping job data.
- `markdownify`: For converting HTML content to Markdown.

Install all the dependencies using:
```bash
pip install -r requirements.txt
```

## 🔄 Usage

1. **Telegram Bot Notifications**: The bot sends you notifications with job details as new jobs are found.
2. **Email Sending**: Automatically send emails with your CV to target companies.
3. **Job Scraper**: Fetches job postings and updates a local JSON file for tracking.

## 📃 License
This project is licensed under the MIT License. Feel free to use and modify it as you see fit! 🛠️

---

Feel free to tweak the content to better fit your needs. Let me know if you need any adjustments or additional sections!
