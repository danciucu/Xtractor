from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller
import time


def get_work_items(driver, bridge_dict, i):
    # set up a variable to control keyboard
    keyboard = Controller()
    # define empty variables
    work_item_count = 0
    # click on the WORK button
    work_button_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[2]/div/h3[5]')
    work_button_driver.click()
    # click on the WORK CANDIDATES button
    time.sleep(1)
    work_candidates_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[2]/div/div[5]/div[1]')
    work_candidates_driver.click()
    # get elements and properties
    time.sleep(1)
    while True:
        try:
            # action text of work item
            work_item_action_text = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[{work_item_count + 2}]/td[3]')
            action_text = work_item_action_text.text
            # xpath arrow of work item
            work_item_no_xpath = f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[{work_item_count + 1}]/td[1]'
            # click on the arrow of a work item
            work_item_arrow = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[{work_item_count + 2}]/td[1]')
            work_item_arrow.click()
            time.sleep(1)
            # find description of the work item
            work_item_description = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/textarea')
            # find action of the work item
            work_item_action = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/select')
            # find priority of the work item
            work_item_priority = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr/td[2]/select')
            # find responsibility of the work item
            work_item_responsibility = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td[1]/table/tbody/tr[11]/td/table/tbody/tr/td[2]/select')
            # update element dictionary
            add_work_item(driver = driver,
                          bridge_dict = bridge_dict,
                          work_item_description = work_item_description,
                          work_item_action = work_item_action,
                          work_item_priority = work_item_priority,
                          work_item_responsibility = work_item_responsibility,
                          work_item_count = work_item_count)
            # update the work item count
            work_item_count += 1

            # check if action text was empty
            if action_text == ' ':
                # press cancel
                work_item_save = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td')
                work_item_save.click()
                time.sleep(1)


        except:
            # click on KYTC tab
            time.sleep(2)
            kytc_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/h3[3]/table/tbody/tr/td[1]/div')
            kytc_driver.click()
            break


def add_work_item(driver, bridge_dict, work_item_description, work_item_action, work_item_priority, work_item_responsibility, work_item_count):
    # add work item description to the dictionary
    bridge_dict['Work Items Description'][1].append(work_item_description.text)
    bridge_dict['Work Items Description'][0].append([61 + work_item_count, 1])
    # add work item action to the dictionary
    select_action = Select(WebDriverWait(driver, 100).until(EC.visibility_of(work_item_action)))
    action = select_action.first_selected_option.text
    bridge_dict['Work Items Action'][1].append(action)
    bridge_dict['Work Items Action'][0].append([61 + work_item_count, 5])
    # add work item priority to the dictionary
    select_priority = Select(WebDriverWait(driver, 100).until(EC.visibility_of(work_item_priority)))
    priority = select_priority.first_selected_option.text
    bridge_dict['Work Items Priority'][1].append(priority)
    bridge_dict['Work Items Priority'][0].append([61 + work_item_count, 7])
    # add work item responsibility to the dictionary
    select_responsibility = Select(WebDriverWait(driver, 100).until(EC.visibility_of(work_item_responsibility)))
    responsibility = select_responsibility.first_selected_option.text
    bridge_dict['Work Items Responsibility'][1].append(responsibility)
    bridge_dict['Work Items Responsibility'][0].append([61 + work_item_count, 8])