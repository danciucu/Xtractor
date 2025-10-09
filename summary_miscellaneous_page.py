from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def get_miscellaneous(driver, bridge_dict, i):
    # click on SUMMARY & MISCELLANEOUS button
    time.sleep(2)
    summary_miscellaneous_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[3]/div/h3[1]/a/div')
    summary_miscellaneous_driver.click()
    # get scour
    time.sleep(2)
    scour_driver = driver.find_element(By.XPATH, '//html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/select')
    selected_scour = Select(scour_driver).first_selected_option.text
    bridge_dict['Scour Observed'][1] = selected_scour
    # get inspection type and frequency
    inspection_type_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr/td[2]/input')
    if '24 months' in inspection_type_driver.get_attribute('value'):
        bridge_dict['Inspection Type'][1] = 'Routine'
        bridge_dict['Inspection Frequency'][1] = '24'
    
    elif 'Special' in inspection_type_driver.get_attribute('value'):
        bridge_dict['Inspection Type'][1] = 'Special'
        bridge_dict['Inspection Frequency'][1] = 'Other'

    else:
        bridge_dict['Inspection Type'][1] = 'select one->'
        bridge_dict['Inspection Frequency'][1] = ''