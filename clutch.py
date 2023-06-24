import time
from emailparser import email
from utils import create_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elemparser import elem_parse
def parse_clutch(links, pure_companies):
    driver = create_webdriver()
    driver.maximize_window()
    driver.switch_to.window(driver.window_handles[0])

    for link in links:
        source = link
        page = 0 if "?" not in source else source.split("?")[1]
        print(f"Preparing for parse clutch\npage:{page}")
        companies = []
        driver.get(source)
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonAccept"))).click()
        except:
            print('cookie')
        elem_parse(driver, ".provider.provider-row:not(.ppc_item--element)", companies)
        elem_parse(driver, ".ppc_item--element", companies)
        print("Preparing for email parsing")
    driver.quit()
    email(companies, pure_companies)

