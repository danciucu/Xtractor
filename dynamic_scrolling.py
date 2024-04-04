from selenium.common.exceptions import NoSuchElementException

def check_exists_by_xpath(element_driver):
    try:
        element_driver
    except NoSuchElementException:
        return False
    return True

def scroll(element_driver, driver):
    scroller = 0
    page_height = driver.execute_script("return document.body.scrollHeight")
    while check_exists_by_xpath(element_driver) == False:
        scroller += 1
        scroll_driver = driver.execute_script(f'window.scrollTo(0,{page_height * scroller / 10})')