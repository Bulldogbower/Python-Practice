from contextlib import nullcontext
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def LaunchBrowser():
    available_days=[]
    count=0

    driver = webdriver.Firefox()
    #driver.implicitly_wait(3)
    driver.get("https://www.recreation.gov/camping/campgrounds/232491")
    #sleep(999)
    # driver.switch_to.alert().dismiss()
    pop_up=driver.find_element_by_css_selector("button.sarsa-modal-close-button").click()# sarsa-modal-close-button sarsa-button-subtle sarsa-button-md").click
    start_date=driver.find_element_by_css_selector("input.DateInput_input_1").click()
    
    # months=driver.find_elements_by_class_name("CalendarMonth_caption.CalendarMonth_caption_1")
    # for i in range(len(months)):
    #     print(months[i].text)

    dates=driver.find_elements_by_class_name("CalendarDay__default_2")
    for i in range(len(dates)):
        print(dates[i].text)
    next_page=driver.find_element_by_class_name("sarsa-day-picker-range-controller-month-navigation-button.right")
    # print(months)
    # print(dates)
    current_month=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div")
    current_month_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table")
    print("Current Month: ", current_month.text)
    #print("Currernt Month Days: ", current_month_days.text)

    for i in range(len(current_month_days.text)):
        if current_month_days.text[i] =="A":
            print(current_month_days.text[i-3], current_month_days.text[i-2])

    #next_page.click(3)
    # for i in range(len(months)):
    #     print(months[i].text)
    # for i in range(len(dates)):
    #     print(dates[i].text)
    #driver.close()

LaunchBrowser()

#Current month Calendar: May: /html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div
#Next month Calendar: June: /html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]