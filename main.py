from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

load_dotenv("variables.env")

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

driver_path = "/Users/gael/Desktop/100_days_code/*Tools/chromedriver"

driver = webdriver.Chrome(driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3243174449&f_AL=true&f_E=1&f_JT=I&keywords=D%C3%A9veloppeur%20Python&refresh=true&sortBy=R")

login = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
login.click()

login_email = driver.find_element(By.NAME, "session_key")
login_email.send_keys(email)

login_password = driver.find_element(By.ID, "password")
login_password.send_keys(password)

login_click = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
login_click.click()

job_listings = driver.find_elements(By.CSS_SELECTOR, 'ul li div div div div div a.job-card-list__title')
jobs = [job.get_attribute("id") for job in job_listings]
print(jobs)

for job in jobs:
    time.sleep(2)
    driver.find_element(By.ID, job).click()
    time.sleep(2)
    save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    save_button.click()

driver.quit()
