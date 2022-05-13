from contextlib import nullcontext
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def Hold():
    sleep(9999)

def LaunchBrowser():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.recreation.gov/camping/campgrounds/232491")
    sleep(3)
    # driver.switch_to.alert().dismiss()
    try:
        driver.switchTo().frame(driver.find_element_by_id(("overlay")))
        pop_up=driver.find_elements_by_name("button").click
        pop_up.click()
        print("Found pop-up")
    except:
        print("Can't find pop-up")
        pass
        #Hold()
    try:
        location=driver.find_element_by_id("campground-start-date-calendar").click()               # Find check in date
        location.send_keys(Keys.ESCAPE)
        sleep(3)
        available_dates=driver.find_element_by_class_name("rec-calendar-day rec-available-day").text
        print(available_dates)
        #location.send_keys(Keys.RETURN)
    except:
        Hold()
LaunchBrowser()
    
    