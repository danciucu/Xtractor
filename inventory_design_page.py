from selenium.webdriver.common.by import By
import time

def get_design_info(driver, bridge_dict, i):
    # click on INVENTORY button
    time.sleep(2)
    inventory_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[2]/div/h3[3]/table/tbody/tr/td[1]/div')
    inventory_driver.click()
    # click on ADMIN button
    time.sleep(2)
    admin_driver = driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_m_cphLeftPane_m_TaskBar_m_TaskBarMenu_divMenuItems"]/div[3]/div[2]/div/div[3]/div[1]/a')
    admin_driver.click()
    # read Facility Carried value
    time.sleep(2)
    facility_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr[9]/td/table/tbody/tr/td[2]/input')
    bridge_dict['Facility Carried'][1] = facility_driver.get_attribute('value')
    
    # click on DESIGN button
    time.sleep(2)
    design_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[2]/div/div[3]/div[2]/a')
    design_driver.click()
    # get the number of spans
    time.sleep(2)
    no_of_spans_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
    bridge_dict['No of Spans'][1] = no_of_spans_driver.get_attribute('value')
    # get the type of structure
    structure_type_driver = driver.find_element(By.XPATH,'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[4]/td/table/tbody/tr/td[2]/select')
    if 'Culvert' in structure_type_driver.get_attribute('value'):
        bridge_dict['Bridge/Culvert'][1] = 'Culvert'
    else:
        bridge_dict['Bridge/Culvert'][1] = 'Bridge'
    
    # click on ROADS button
    time.sleep(2)
    roads_driver = driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_m_cphLeftPane_m_TaskBar_m_TaskBarMenu_divMenuItems"]/div[3]/div[2]/div/div[3]/div[3]/a')
    roads_driver.click()
    # read Road/Route name value
    time.sleep(2)
    road_name_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
    bridge_dict['Road Name'][1] = '(' + str(road_name_driver.get_attribute('value')).title() + ')'