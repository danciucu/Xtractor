from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import globalvars, dynamic_scrolling

def get_condition(driver, bridge_dict, i):
    # define empty variables
    elem_count = 0
    elem_tab_count = 0
    child_count = 0
    child_tab_count = 0
    elem_repeated = 0
    # only for the first element 
    if i == 0:
        # click on KYTC tab
        time.sleep(5)
        inspection_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/h3[2]/table/tbody/tr/td[1]')
        inspection_driver.click()
        # click on WEIGHTS tab
        time.sleep(5)
        condition_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/div[3]/div[2]/div/h3[1]')
        condition_driver.click()
    # insert bridges IDs in the bridge box
    time.sleep(2)
    bridgebox_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/div/input[2]')
    bridgebox_driver.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    bridgebox_driver.send_keys(globalvars.bridgeID[i])
    time.sleep(5)
    bridgebox_driver.send_keys(Keys.ENTER)
    time.sleep(2)
    # get deck rating
    deck_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.C.01 (Deck) (Item 58)'][1] =  deck_rating_driver.get_attribute('value')
    # get superstructure rating
    superstructure_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.C.02 (Superstructure) (Item 59)'][1] =  superstructure_rating_driver.get_attribute('value')
    # get substructure rating
    substructure_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.C.03 (Substructure) (Item 60)'][1] =  substructure_rating_driver.get_attribute('value')
    # get substructure rating
    channel_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.C.09 (Channel) (Item 61)'][1] =  channel_rating_driver.get_attribute('value')
    # get culvert rating
    culvert_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.C.04 (Culverts) (Item 62)'][1] =  culvert_rating_driver.get_attribute('value')
    # get waterway rating
    waterway_rating_driver = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/select')
    bridge_dict['B.AP.02 (Overtopping Likelihood) (Item 71 - Waterway Adequacy)'][1] =  waterway_rating_driver.get_attribute('value')
    # scroll down
    #zoom_out = driver.execute_script("document.body.style.zoom='50%'")
    #page_height = driver.execute_script("return document.body.scrollHeight")
    #scroll_driver = driver.execute_script(f'window.scrollTo(0,{page_height * 0.4})')
    # get elements and properties
    while True:
        try:
            # xpath element number
            elem_no_xpath = f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[2]'
            # scroll to the element
            dynamic_scrolling.scroll(driver, elem_no_xpath, 200)
            # add element number to the dictionary
            elem_no_driver = driver.find_element(By.XPATH, elem_no_xpath)
            # add element total quantity to the dictionary
            elem_totalq_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[8]/input')
            # add element CS1 to the dictionary
            elem_cs1_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[10]/b')
            # add element CS2 to the dictionary
            elem_cs2_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[11]/input')
            # add element CS3 to the dictionary
            elem_cs3_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[12]/input')
            # add element CS4 to the dictionary
            elem_cs4_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[13]/input')
            # add the description to the dictionary
            elem_no_driver.click()
            elem_description_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[3]/table/tbody/tr[3]/td/span[1]/a')
            elem_description_driver.click()
            elem_description_text_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[3]/table/tbody/tr[4]/td/textarea')
            # update element dictionary
            add_element(bridge_dict = bridge_dict,
                        elem_no_driver = elem_no_driver,
                        elem_totalq_driver = elem_totalq_driver,
                        elem_cs1_driver = elem_cs1_driver,
                        elem_cs2_driver = elem_cs2_driver,
                        elem_cs3_driver = elem_cs3_driver,
                        elem_cs4_driver = elem_cs4_driver,
                        elem_description_text_driver = elem_description_text_driver,
                        elem_count = elem_count,
                        elem_repeated = elem_repeated)
            # update the element count
            elem_count += 1
            # click on the element arrow if exists otherwise move to the next element
            elem_arrow_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[2]/table/tbody/tr/td[1]/input')
            try:
                elem_arrow_driver.click()
            except:
                elem_tab_count += 1
                continue

            # add secondary elements
            while True:
                try:
                    # add child number to the dictionary
                    child_no_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[2]')

                    # check if is a true child
                    if child_no_driver.text not in ['811', '812', '813', '814', '815', '816', '510', '515', '520', '521']:
                        child_tab_count += 1
                        continue

                    # check if the child is repeated
                    #if child_no_driver.text in bridge_dict['Elements'][1]:
                    #    elem_repeated += 1
                    
                    # add child total quantity to the dictionary
                    child_totalq_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[6]/input')
                    # add child CS1 to the dictionary
                    child_cs1_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[8]/b')
                    # add child CS2 to the dictionary
                    child_cs2_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[9]/input')
                    # add child CS3 to the dictionary
                    child_cs3_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[10]/input')
                    # add child CS4 to the dictionary
                    child_cs4_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/table/tbody/tr/td[11]/input')
                    # add the description to the dictionary
                    child_no_driver.click()
                    child_description_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/div/table/tbody/tr[2]/td/span[1]/a')
                    child_description_driver.click()
                    child_description_text_driver = driver.find_element(By.XPATH, f'/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[1]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/fieldset/table/tbody/tr/td/div/div[1]/div[1]/div[8]/div[{elem_tab_count + 1}]/div[4]/div[{child_tab_count + 1}]/div[1]/div/table/tbody/tr[3]/td/textarea')
                    # update element dictionary
                    add_element(bridge_dict = bridge_dict,
                                elem_no_driver = child_no_driver,
                                elem_totalq_driver = child_totalq_driver,
                                elem_cs1_driver = child_cs1_driver,
                                elem_cs2_driver = child_cs2_driver,
                                elem_cs3_driver = child_cs3_driver,
                                elem_cs4_driver = child_cs4_driver,
                                elem_description_text_driver = child_description_text_driver,
                                elem_count = elem_count,
                                elem_repeated = elem_repeated)

                    # update element and child count
                    child_count += 1
                    elem_count += 1
                    child_tab_count += 1

                except:
                    # click on the arrow again to collapse
                    elem_arrow_driver.click()
                    child_tab_count = 0
                    break
            # update element tab count
            elem_tab_count += 1
        except:
            # scroll up
            #zoom_out = driver.execute_script("document.body.style.zoom='100%'")
            #scroll_driver = driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
            driver.execute_script(f'window.scrollTo(0,0)')
            break

    #print(bridge_dict)

    
def add_element(bridge_dict, elem_no_driver, elem_totalq_driver, elem_cs1_driver, elem_cs2_driver, elem_cs3_driver, elem_cs4_driver, elem_description_text_driver, elem_count, elem_repeated):
    # check if the element number already exists
    #if elem_no_driver.text in bridge_dict['Elements'][1]:
    #    elem_no = elem_no_driver.text + '-' + str(elem_repeated + 1)
    #    bridge_dict['Elements'][1].append(elem_no)
    #    bridge_dict['Elements'][0].append([84 + elem_count, 1])
    # add element number to the dictionary
    bridge_dict['Elements'][1].append(elem_no_driver.text)
    bridge_dict['Elements'][0].append([84 + elem_count, 1])
    # add element total quantity to the dictionary
    bridge_dict['Total Quantity'][1].append(elem_totalq_driver.get_attribute('value'))
    bridge_dict['Total Quantity'][0].append([84 + elem_count, 2])
    # add element CS1 to the dictionary
    bridge_dict['CS1'][1].append(elem_cs1_driver.text)
    bridge_dict['CS1'][0].append([84 + elem_count, 3])
    # add element CS2 to the dictionary
    bridge_dict['CS2'][1].append(elem_cs2_driver.get_attribute('value'))
    bridge_dict['CS2'][0].append([84 + elem_count, 4])
    # add element CS3 to the dictionary
    bridge_dict['CS3'][1].append(elem_cs3_driver.get_attribute('value'))
    bridge_dict['CS3'][0].append([84 + elem_count, 5])
    # add element CS4 to the dictionary
    bridge_dict['CS4'][1].append(elem_cs4_driver.get_attribute('value'))
    bridge_dict['CS4'][0].append([84 + elem_count, 6])
    # add element description
    bridge_dict['Description'][1].append(elem_description_text_driver.get_attribute('value'))
    bridge_dict['Description'][0].append([84 + elem_count, 7])