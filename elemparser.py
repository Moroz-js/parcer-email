import time
from emailparser import email
from utils import create_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def elem_parse(driver, elemSelector, companies):
    elements = driver.find_elements(By.CSS_SELECTOR, elemSelector)
    for i, element in enumerate(elements):
        if(i < 50):
            link = element.find_element(By.CSS_SELECTOR, ".directory_profile")
            link.click()
            try:
                driver.switch_to.window(driver.window_handles[1])
                name = driver.find_element(By.CSS_SELECTOR, ".profile-header__title .website-link__item").text
                site = driver.find_element(By.CSS_SELECTOR, ".website-link__item").get_attribute("href").split('?')[0]
                facebook = ''
                linkedIn = ''
                if(len(driver.find_elements(By.CSS_SELECTOR, ".sg-social-media--link-linkedin")) > 0):
                    linkedIn = driver.find_element(By.CSS_SELECTOR, ".sg-social-media--link-linkedin").get_attribute("href")
                    if(len(driver.find_elements(By.CSS_SELECTOR, ".sg-social-media--link-facebook")) > 0):
                        facebook = driver.find_element(By.CSS_SELECTOR, ".sg-social-media--link-facebook").get_attribute("href")
                    
                else:
                    if(len(driver.find_elements(By.CSS_SELECTOR, ".sg-social-media--link-facebook")) > 0):
                        facebook = driver.find_element(By.CSS_SELECTOR, ".sg-social-media--link-facebook").get_attribute("href")
                companies.append({'name': name, 'site': site, 'email': '', 'facebook': facebook, 'linkedin': linkedIn})
            finally:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])