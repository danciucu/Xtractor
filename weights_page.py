from selenium.webdriver.common.by import By
import time

def get_posting(driver, bridge_dict, i):
    # click on WEIGHTS button
    time.sleep(2)
    weights_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[3]/div/h3[4]')
    weights_driver.click()
    # scroll to the right
    page_width = driver.execute_script("return document.body.scrollWidth")
    scroll_driver = driver.execute_script(f'window.scrollTo({page_width}, 0)')
    # get posting data
    time.sleep(2)
    for i in range(8):
        xpath = f"/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/fieldset/table/tbody/tr[2]/td[2]/div/fieldset/table/tbody/tr[{i + 2}]/td/table/tbody/tr/td[2]/input"
        
        elements = driver.find_elements(By.XPATH, xpath)
        if elements:  # element exists
            value = elements[0].get_attribute("value")
            if value:   # not empty
                bridge_dict['Posting Values'][1].append(value)
                
    # scroll back to the left
    scroll_driver = driver.execute_script("window.scrollTo(0,0)")