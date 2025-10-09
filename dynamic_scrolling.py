from selenium.webdriver.common.by import By
import time

def check_exists(driver, xpath):
    try:
        elem = driver.find_element(By.XPATH, xpath)
        elem.click()
        return True
    except:
        return False

def scroll(driver, xpath, increment):
    current_height = 0
    page_height = driver.execute_script("return document.body.scrollHeight")
    while not check_exists(driver, xpath) and current_height < page_height:
        current_height += increment
        driver.execute_script(f'window.scrollTo(0,{current_height})')
        time.sleep(0.1)