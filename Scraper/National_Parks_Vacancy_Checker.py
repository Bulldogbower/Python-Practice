from contextlib import nullcontext
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager







def LaunchBrowser():
    f=open("National_Parks_Avaiability.txt", "w")
    available_days=[]
    count=0

    driver = webdriver.Firefox()
    #driver.implicitly_wait(3)
    driver.get("https://www.recreation.gov/camping/campgrounds/232491")
    #sleep(999)
    pop_up=driver.find_element_by_css_selector("button.sarsa-modal-close-button").click()
    start_date=driver.find_element_by_css_selector("input.DateInput_input_1").click()
    
    # months=driver.find_elements_by_class_name("CalendarMonth_caption.CalendarMonth_caption_1")
    # for i in range(len(months)):
    #     print(months[i].text)

    # dates=driver.find_elements_by_class_name("CalendarDay__default_2")
    # for i in range(len(dates)):
    #     print(dates[i].text)

    #Click to go to next page
    next_page=driver.find_element_by_class_name("sarsa-day-picker-range-controller-month-navigation-button.right")

    #May
    month_0=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div")
    month_0_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table")
    month_0_days_list=[]
    #June
    month_1=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div")
    month_1_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/table")
    #July
    month_2=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div")
    month_2_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/table")
    
    f.write("Month_0:" + month_0.text + "\n" + month_0_days.text + "\n")
    f.write("Month_1:" + month_1.text + "\n" + month_1_days.text + "\n")
    f.write("Month_2:" + month_2.text + "\n" + month_2_days.text + "\n")
    
    driver.implicitly_wait(3)

    #Click to go to next page
    next_page.click()
    #Wait time for elements to load
    driver.implicitly_wait(3)
    
    #August
    month_3=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div")
    month_3_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/table")

    driver.implicitly_wait(3)

    f.write("Month_3:" + month_3.text + "\n" + month_3_days.text + "\n")
    
    driver.implicitly_wait(3)

    f.close()
    #print("Currernt Month Days: ", current_month_days.text)

    # for i in range(len(month_0_days.text)):
    #     if month_0_days.text[i] =="A":
    #         print(month_0_days.text[i-3], month_0_days.text[i-2])

    #next_page.click(3)
    # for i in range(len(months)):
    #     print(months[i].text)
    # for i in range(len(dates)):
    #     print(dates[i].text)
    #driver.close()
    f.close()
    driver.close()
    driver.quit()
LaunchBrowser()

#Current month Calendar: May: /html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div
#Next month Calendar: June: /html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]