import cloudscraper
import openai
import tenacity
from bs4 import BeautifulSoup
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

"""
scraper = cloudscraper.create_scraper()
html_doc = scraper.get(input("Post an indeed job detail page link: ")).text

soup = BeautifulSoup(html_doc, "html.parser")

job_title = soup.h1.get_text()
job_description = soup.find("div", id="jobDescriptionText").get_text()
company_name = soup.find("div", {"data-company-name": "true"}).get_text()
"""

education = [os.getenv("EDU1"), os.getenv("EDU2"), os.getenv("EDU3")]
experience = [os.getenv("EXP1")]
coding_skills = {
    "Python": "very good",
    "Bash": "good",
    "SQL": "good",
    "HTML": "good",
    "CSS": "okay",
    "Julia": "okay",
}
soft_skills = ["am a hard worker", "perform well under stress", "love learning new things"]
tools = {
    "Data Science": [
        "pandas",
        "sklearn",
        "TensorFlow",
        "matplotlib",
        "seaborn",
        "plotly",
        "numpy",
        "polars",
    ],
    "DevOps": ["Docker", "Ansible", "Terraform", "Apache Airflow"],
    "Web Development": ["Django", "Flask", "Quart", "TailwindCSS", "HTMX"],
    "General": ["git", "Linux", "No SQL", "asyncio"],
    "Databases": ["PostgreSQL", "MongoDB", "SQLite"],
}
about_me = [os.getenv("ABM1"), os.getenv("ABM2"), os.getenv("ABM3"), os.getenv("ABM4")]
portfolio = [
    "A script that scrapes job offers from different sources, cleans them and then calls the OpenAI API to generate a personalized cover letter text using information about me and the job description. The response from Chat-GPT is then used to create a cover letter PDF.",
    "An entry into the Spaceship Titanic Kaggle competition, where i finished in the top 10% with a classification model based on the catboost algorithm.",
    "My personal homepage, where i explored async await in Python and used the Quart async framework as the backend, MongoDB as database and TailwindCSS and HTMX for the frontend.",
    "A deployment script that can be used for DevOps or MLOps and deploys a Django project to Linode using Terraform and Ansible with a PostgreSQL database. Complete with all the scripts to configure Linux Cloudnodes, Docker, Firewalls, Monitoring and Logging via GitHub Actions. Runs as a high availability cluster with a loadbalancer in front of several Django nodes with Redis as Cache and Celery for asynchronous tasks connecting to a managed PostgreSQL database."
]

language = input("Output language: ")
characters = input("Maximum number of characters: ")
job_title = input("Name of the job: ")
with open("job_input.txt") as f:
    job_description = f.read()
company_name = input("Name of the company you are applying to: ")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": f"You are a helpful assistant. Your task is to write cover letters for job applications in {language} with a maximum of {characters} characters. The user will give you informations about a job opening as well as about themselves - compare both and write a personalized cover letter accordingly.",
        },
        {
            "role": "user",
            "content": f"Write a cover letter for a job as a '{job_title}' at '{company_name}' with the following job description: '{job_description}'. I have the following education: {education}. My work experience is as follows: {experience}. I have a variety of programming skills ({coding_skills}) and know a lot of IT tools ({tools}). The following statements describe me: {about_me}. I {soft_skills}. This is my portfolio: {portfolio}.",
        },
    ],
)

with open(f"{datetime.datetime.now()}-{company_name}", "w") as f:
    f.write(completion.choices[0].message.content)
print(completion.choices[0].message.content)
