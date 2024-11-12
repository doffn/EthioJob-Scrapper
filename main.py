####################### Email sender ########################
import os
import ast
import time
import html
import json
import smtplib
import telebot
import markdownify
from telebot import formatting
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from poe_api_wrapper import AsyncPoeApi, PoeApi
from collections import deque
import asyncio
tokens = {
    'p-b': os.environ['PB'], 
    'p-lat': os.environ['PLAT']
}



psd = os.environ["PASSWORD"]
bot = telebot.TeleBot("your BOT API")
genai.configure(api_key=os.environ["BARD"])
client = PoeApi(tokens=tokens)




def report(message, ID="ID number", ):

    try:
        bot.send_message(chat_id=ID, text=message, parse_mode="Markdown")
    except Exception as e:
        print(f"Failed to send message: {e}")
        bot.send_message(chat_id=ID, text=message)

def bard(text):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(text)
    return (response.text)

def poe_bot(message):
    message = "Explain quantum computing in simple terms"
    res = iter(client.send_message(bot="gpt3_5", message=message))
    dd = deque(res, maxlen=1)
    last_element = dd.pop()
    #print(last_element)
    return last_element["text"]


# Replace with the path to your file
file_path = "Dawit Neri CV.pdf"  # Adjust the path to your file

'''
def email_sender(sender_email, receiver_email, subject, name, company, file_path):

    # Create a secure connection with the server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
      server.login(sender_email, psd)

      # Create a MIMEMultipart message
      msg = MIMEMultipart()
      msg["From"] = sender_email
      msg["To"] = receiver_email
      msg["Subject"] = subject

      # Attach the message
      body = f"""Dear {name},

I am a recent 2024 graduate with a degree in Electromechanical Engineering, interested in working at {company}. My studies provided me with a strong foundation in electrical, mechanical, and control disciplines.

I am drawn to {company} because I believe I will gain valuable hands-on experience working alongside your team. Your company's focus on areas that align with my interests is particularly appealing.

I am confident that my skills and knowledge would be a valuable asset to your team. My CV is attached for your review. I would be glad to learn more about potential opportunities at {company}.

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,

Dawit Neri
+251988186840"""

      msg.attach(MIMEText(body) )

      # Attach the file
      with open(file_path, "rb") as attachment:
        file_part = MIMEBase("application", "octet-stream")
        file_part.set_payload(attachment.read())
      encoders.encode_base64(file_part)
      file_part.add_header(
          "Content-Disposition", "attachment; filename=" + os.path.basename(file_path)
      )
      msg.attach(file_part)

      # Send the email
      server.sendmail(sender_email, receiver_email, msg.as_string())

    print(f"Email sent successfully to {receiver_email} with attachment!")
    
# Replace with your details
sender_email = "dawitneri22@gmail.com"
receiver_email = "dawitneri888@gmail.com"



email_sender(sender_email, 
             "---@gmail.com", 
             "CV - [Position Title] - [Company Name]", 
             name="Yishak",
             company="doffn",
             file_path="Dawit Neri CV.pdf")


import requests


res = requests.get("https://etcareers.com/jobs/?categories[]=Engineering%20Jobs%20in%20Ethiopia&p=1")

with open("output.txt", "w") as f:
    f.write(res.text)



'''

############################### Job scrapper shit#############################

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime




def get_mongo():
    with open('output.json', 'r+') as file:
        try:
            data = json.load(file)
            return data
        except json.decoder.JSONDecodeError:
            print("There is a JSON error")
            return {}




def mongo_update(data):
      with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)
          

def markdown(text):
    # Use markdownify() function to convert HTML to Markdown
    try:
        markdown_text = markdownify.markdownify(text)
        return markdown_text
    except Exception as e:
        print(e)
        return text
    
def Ethio_jobs():
        url = "https://api.ethiojobs.net/ethiojobs/api/search?entity=jobs&filters%5Bcatalog%5D=eyJpdiI6ImgrQ2xWcGRReWNWajVMTEhac0pDWkE9PSIsInZhbHVlIjoiZkUyUlprSDJEWUhGZWhIYlkxT25Cdz09IiwibWFjIjoiYzQwZjg3ZmJmZTQzNTEyMGIzNzlmYWM5YTI2MWMzOWM4N2FhNDQxNmY4OTgzNzUzOTVlOTU5MTk5MDYxYzkxYyIsInRhZyI6IiJ9&filters%5Bcareer_level%5D=eyJpdiI6Im1qV0RoeUhNUFVsOXpzamZISWJ4dXc9PSIsInZhbHVlIjoiV0p6SXlGVzJtYmg0L2MyMVVWbXR5dz09IiwibWFjIjoiZGUyZTc1MjMzM2YwNTNmMzliNjRhMzk3ZjVmYjNmOWRmNmQwZjMxN2UyN2Q4NTExMDdkMjQ3NDAyYWJjNzIzMCIsInRhZyI6IiJ9&filters%5Btype%5D=eyJpdiI6ImxBMXFhODZyU3dMTC9yanErZGdpaFE9PSIsInZhbHVlIjoiRk5za0IwRFE3M2NDb09pMVNQS2FTdz09IiwibWFjIjoiODE0NGI2MWI4ZjcxMzA3YjZlMjVjNTViYjFiZDMwOWMyOWU3MWQ4ODEzMDI2ZGFiMDUzNjVlYmRiNzkzM2RjMyIsInRhZyI6IiJ9&page=1&per_page=100"

        response = requests.get(url)
        
        data = json.loads(response.text)
        
        jobs = data["data"][0]["items"]
        
        datas = []
        
        for j, job in enumerate(jobs):
            id = job.get("listings_id")
            job_title = job.get("title", "")
            company = job.get("company", {}).get("name", "")
            phone = job.get("company", {}).get("phone", "")
            email = job.get("company", {}).get("email", "")
            website = job.get("company", {}).get("website", "")
            how_to_apply = job.get("how_to_apply", "")
            description = job.get("description", "")
            job_type = job.get("location_type", "")
            language = job.get("language_skills_names", [])
            date_published = job.get("date_published", "")
            date_end = job.get("date_expiry", "")
            requirement = job.get("requirement", "")
            city = job.get("city", "")
        
        
            # make a dicttionary of job
            data = {"ID":id,
                   "Title":job_title,
                   "Company":company,
                   "Phone":phone,
                   "Email":email,
                   "Website":website,
                   "Requirement":requirement,
                   "How to apply":how_to_apply,
                  # "Description":markdown(description),
                   "Job Type":job_type,
                   "Language":language,
                   "Date Published":date_published,
                   "Date End":date_end,
                   "City":city,
                   "Seen": datetime.now().isoformat()}
        
            datas.append(data)
        return datas[::-1]


data = get_mongo()

comp = [i for i in list(data["companies"]) if data["companies"][i]["Active"]][0]


try:
    ids = [id["ID"] for id in data["companies"][comp]["Data"]]
    new_data = Ethio_jobs()
    
    new_ids = [id["ID"] for id in new_data]
    diff_ids = list(set(new_ids) - set(ids))
    #print(ids[0] == new_ids[0])
    #time.sleep(34343434)
    if len(diff_ids) >=0:
        print(f"There are {len(diff_ids)} new jobs")
        for i, job in enumerate(new_data):
            if job["ID"] in diff_ids:
                
                
                try:
                    
                    result = bard(f"summarize this values of each key and send me a dict text . also remove the Markdown format. i am using teleelgram bot so if it is too long use bullet point. donot send an html parsed text. send a dictionary text: {job}")

                    
                    
                    # Find the index of the opening curly brace
                    start = result.find("{")
                    
                    # Find the index of the closing curly brace
                    end = result.find("}")
    
                    # Splice the string
                    if start != -1 and end != -1:
                        result = result[start:end+1]
                        result = ast.literal_eval(result)
                    else:
                        print("No curly braces found in the string.")
                        continue

                    
                    
                    if job["ID"] in diff_ids and job["ID"] not in ids:
                        message = f"""*🎉 New Job Found from: {comp}*\n
                        *ID:* ` {result.get('ID', '')}`
                        *Title:* {result.get('Title', '')}
                        *Company:* ``` {str(result.get('Company', ''))}```
                        *Phone:* ` {str(result.get('Phone', ''))}`
                        *Email:* ` {str(result.get('Email', ''))}`
                        *Website:* ` {str(result.get('Website', ''))}`
                        *Requirement:* ``` {result.get('Requirement', '')}```
                        *How to apply:* ``` {str(result.get('How to apply', ''))}```
                        *Job Type:* `{str(result.get('Job Type', ''))}`
                        *Language:* `{str(result.get('Language', ''))}`
                        *Date Published:* `{str(result.get('Date Published', ''))[:10]}`
                        *Date End:* `{str(result.get('Date End', ''))[:10]}`
                        *City:* `{str(result.get('City', ''))}`"""
    
                        report(message)
                        data["companies"][comp]["Data"].insert(0, job)
                        print("message added")
                        mongo_update(data)
                        
                except Exception as e:
                    print(f"Failed to send message: {e}")
                time.sleep(1)

    
    
except Exception as e:
    print(e)







