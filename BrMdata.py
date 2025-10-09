from selenium.webdriver.common.by import By
from selenium import webdriver

import globalvars, dictionary_datastructure , condition_page, work_candidates, newExcel, chrome_driver, inventory_design_page, summary_miscellaneous_page, weights_page

class get_previous_data():
    def __init__(self):

        # import global variables
        globalvars.init()

        chrome_driver
        # simuate a chrome browser
        driver = webdriver.Chrome(service=globalvars.service)
        # access BrM website
        driver.get('https://brm.kytc.ky.gov/BrM6/Login.aspx?ReturnUrl=%2fBrM6%2fExpiration.aspx')
        # login into the website
        username_driver = driver.find_element(By.ID, "userid")
        username_driver.send_keys(globalvars.username)
        password_driver = driver.find_element(By.ID, "password")
        password_driver.send_keys(globalvars.password)
        login_driver = driver.find_element(By.ID, "btnSignIn")
        login_driver.click()
        # instantiate the class
        bridge_excel = newExcel.field_notes()


        for i in range(len(globalvars.bridgeID)):
            # generate an empty dictionary
            bridge_dict = dictionary_datastructure.generate_dict()
            # update the dictinary for bridgeID
            bridge_dict['Structure ID'][1] = globalvars.bridgeID[i]
            # update the dictionary based on condition page
            condition_page.get_condition(driver, bridge_dict, i)
            # update the dictionary based on inventory -> design page
            inventory_design_page.get_design_info(driver, bridge_dict, i)
            # update the dictionary based on work candidates page
            work_candidates.get_work_items(driver, bridge_dict, i)
            # update the dictionary based on summary & miscellaneous page
            summary_miscellaneous_page.get_miscellaneous(driver, bridge_dict, i)
            # update the dictionary based on weights page
            weights_page.get_posting(driver, bridge_dict, i)
            # create the Excel field note
            bridge_excel.create(bridge_dict)


        # close driver
        driver.close()