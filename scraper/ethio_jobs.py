import requests
import json
from datetime import datetime

def fetch_ethio_jobs():
    url = "https://api.ethiojobs.net/ethiojobs/api/search?entity=jobs&page=1&per_page=100"
    response = requests.get(url)
    data = json.loads(response.text)
    jobs = data["data"][0]["items"]
    
    job_list = []
    for job in jobs:
        job_info = {
            "ID": job.get("listings_id"),
            "Title": job.get("title", ""),
            "Company": job.get("company", {}).get("name", ""),
            "Phone": job.get("company", {}).get("phone", ""),
            "Email": job.get("company", {}).get("email", ""),
            "Website": job.get("company", {}).get("website", ""),
            "How to apply": job.get("how_to_apply", ""),
            "Requirement": job.get("requirement", ""),
            "City": job.get("city", ""),
            "Date Published": job.get("date_published", ""),
            "Date End": job.get("date_expiry", ""),
        }
        job_list.append(job_info)
    return job_list
