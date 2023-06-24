from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests

from utils import create_webdriver


def email(companies, pureCompanies):
    exceptions = ['']
    for company in companies:
        url = company["site"]
        print(url)
        if url not in exceptions:
            try:
                response = requests.get(url)
                response.raise_for_status()
                try:
                    driver = create_webdriver()
                    driver.get(url)
                    element = WebDriverWait(driver, 1).until(
                        lambda x: x.find_element(By.CSS_SELECTOR, 'a[href^="mailto:"]')
                    )
                    mail = element.get_attribute("href").replace("mailto:", "")
                    company["email"] = mail.split("?")[0]
                    pureCompanies.append(company)
                except TimeoutException:
                    print("Cannot find email on site homepage")
                    contactLinks = []
                    links = driver.find_elements(By.CSS_SELECTOR, "a")
                    for link in links:
                        try:
                            if "contact" in link.get_attribute("href"):
                                contactLinks.append(link.get_attribute('href'))
                        except TypeError:
                            'Error checking link'
                    if len(contactLinks) > 0:
                        try:
                            print("Try to find email on contact page")
                            driver.get(contactLinks[0])
                            driver.switch_to.window(driver.window_handles[0])
                            try: 
                                element2 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="mailto:"]')))
                                mail = element2.get_attribute("href").replace("mailto:", "")
                                company["email"] = mail.split("?")[0]
                                pureCompanies.append(company)
                            except TimeoutException:
                                print("Cannot find email on whole site")
                                company["email"] = "N/A"
                                continue
                        except TimeoutException:
                            print("Cannot find email on whole site")
                            company["email"] = "N/A"
                            continue
                    else:
                        print("Contact page not found")
                    driver.quit()
            except requests.exceptions.RequestException as e:
                print("Site is unavailable:", e)
    print("Emails parsed successfully")