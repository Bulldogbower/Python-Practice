from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys


#driver = webdriver.Chrome(executable_path=".\chromedriver.exe")#,options=chrome_options)

def SearchCriteria():
    # q1=input("Does the Part have a letter in front?(y/n) ")
    # if q1=="y":
    w="P"#input("Letter Before PN ")

    # q2=input("Does the Part have a unique ending (i.e '-001')?(y/n) ")
    # if q2=="y":
    z="-001"#input("Enter ending ")

    x=input("Lower limit for PN")
    y=input("Upper limit for PN")
    parts_list=range(int(x),int(y)) #(10000,99999)
    LaunchBrowser(parts_list,w,z)



def LaunchBrowser(parts_list,w,z):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://partsurfer.hpe.com/search.aspx")
    #driver.maximize_window()
    #print("here")
    location=driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")
    location.send_keys("united states")
    location.send_keys(Keys.RETURN)
    #time.sleep(2)
    Search(driver,parts_list,w,z,)

def Search(driver,parts_list,w,z,):
    for i in parts_list:
        try:
            driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')
        except:
            driver.get("https://partsurfer.hpe.com/search.aspx")

        try:
            elem = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')  # Find the search box
            elem.send_keys(Keys.CONTROL,"A")
            elem.send_keys(Keys.DELETE)
            elem.send_keys(w,i,z)
            elem.send_keys(Keys.RETURN)
        except:
            pass

        time.sleep(1)
#Below finds the definition for the part number
        try:
            desc = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_gvGeneral_ctl02_lblpartdesc1').text  # Try to find the part description
            print(w,i,z, " ; ", desc,sep="")
        except:
            pass                                                                                                # If no description field, it continues on
    print("Search Complete")


SearchCriteria()
