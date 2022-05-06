from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import sys

q1=input("Does the Part have a letter in front?(y/n)")
if q1=="y":
    w=input("Letter Before PN")

q2=input("Does the Part have a unique ending (i.e '-001')?(y/n)")
if q2=="y":
    z=input("Enter ending")

x=input("Lower limit for PN")
y=input("Higher limit for PN")

parts_list=range(int(x),int(y)) #(10000,99999)

def LaunchBrowser():
    import time
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://partsurfer.hpe.com/search.aspx")
    driver.maximize_window()
    #print("here")
    location=driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")
    location.send_keys("united states")
    location.send_keys(Keys.RETURN)
    time.sleep(2)
    while True:
        for i in parts_list:
            #print("Here2")
            #print("P",i)
            elem = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')  # Find the search box
            elem.send_keys(Keys.COMMAND,"A")
            elem.send_keys(Keys.DELETE)
            elem.send_keys(w,i,z)
            elem.send_keys(Keys.RETURN)
            time.sleep(3)
            try:
                desc = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_gvGeneral_ctl02_lblpartdesc1').text  # Find the Column for last comment date
                print(w,i,z, desc)
            except:
                print(w,i,z, "doesn't exist")


LaunchBrowser()



# for i in parts_list:
#     print(i)
#     elem = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')  # Find the search box
#     elem.send_keys(str(i),"-001" + Keys.RETURN)
#     time = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_gvGeneral_ctl02_lblpartdesc1')  # Find the Column for last comment date
#     print(time)