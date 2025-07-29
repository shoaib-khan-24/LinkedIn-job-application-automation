import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

YOUR_USERNAME = "mohd.22gcebai076@galgotiacollege.edu"
YOUR_PASSWORD = "khan2003"
YOUR_PHONE_NO = "8368316485"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search-results/?currentJobId=4272798038&eBP=NON_CHARGEABLE_CHANNEL&f_AL=true&keywords=software%20enginner%20intern&refId=xjgnx1WUzqIXmkOSCLN8tA%3D%3D&trackingId=hW%2Fprk4ho64wcrAxQSYQsw%3D%3D")
time.sleep(5)

# -------------------------***  login ***-------------------------------
user_name_entry = driver.find_element(By.ID, "username")
password_entry = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')

user_name_entry.send_keys(YOUR_USERNAME)
password_entry.send_keys(YOUR_PASSWORD)
submit_button.click()

time.sleep(3)

jobs_applied_count = 0
#storing all jobs
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-semantic-search-list li a")

#visiting all jobs
for job in all_jobs:
    job_name = job.find_element(By.TAG_NAME, "strong").text
    company_name = job.find_element(By.CSS_SELECTOR, 'div[dir="ltr"]').text
    job.click()
    time.sleep(1)
    try:
        easy_apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
        easy_apply_button.click()
        time.sleep(1)

        phone_no_entry = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4242008652-20715388188-phoneNumber-nationalNumber")
        if phone_no_entry.text == "":
            phone_no_entry.send_keys(YOUR_PHONE_NO)

        next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        next_button.click()
        time.sleep(1)

        review_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
        review_button.click()
        time.sleep(1)

        submit_application_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
        submit_application_button.click()

        done_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view mlA block")
        done_button.click()

        print(f"Application submitted in {company_name} for role of {job_name}.\n")
        jobs_applied_count += 1
        time.sleep(1)
    except NoSuchElementException:
        print(f"job for {job_name} at {company_name} has complex application.\n")
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]').click()


print(f"Total number of job application sent are: {jobs_applied_count}")
driver.quit()

