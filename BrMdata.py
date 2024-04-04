from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import selenium

import globalvars, dictionary_datastructure , get_condition, newExcel

class get_previous_data():
    def __init__(self):

        # import global variables
        globalvars.init()

        # allocate a path for the chrome browser simulator
        path = Service()
        # simuate a chrome browser
        driver = selenium.webdriver.Chrome(service = path)
        # access BrM website
        driver.get('https://brm.kytc.ky.gov/BrM6/Login.aspx?ReturnUrl=%2fBrM6')
        # login into the website
        username_driver = driver.find_element(By.ID, "userid")
        username_driver.send_keys(globalvars.username)
        password_driver = driver.find_element(By.ID, "password")
        password_driver.send_keys(globalvars.password)
        login_driver = driver.find_element(By.ID, "btnSignIn")
        login_driver.click()

        for i in range(len(globalvars.bridgeID)):
            # generate an empty dictionary
            bridge_dict = dictionary_datastructure.generate_dict()
            # update the dictinary for bridgeID
            bridge_dict['Structure ID'][1] = globalvars.bridgeID[i]
            # update the dictionary based on condition page
            get_condition.main(driver, bridge_dict, i)
            # create the Excel field note
            newExcel.field_notes.create(bridge_dict)



        # close driver
        driver.close()