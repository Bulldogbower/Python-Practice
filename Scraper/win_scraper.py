from contextlib import nullcontext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys


#driver = webdriver.Chrome(executable_path=".\chromedriver.exe")#,options=chrome_options)

def SearchCriteria():
    q1=input("Does the Part have a letter in front?(y/n) ")         # [P]30906
    if q1=="y":
        w=input("Letter Before PN: ")
    else:
        w=None

    q2=input("Does the Part have a unique ending (i.e '-001')?(y/n) ") # P30906[-001]
    if q2=="y":
        z=input("Enter ending: ")
    else:
        z=None

    q3=input("Is there a minimum amount of characters?(y/n) ")         # P[000030906]
    if q3=="y":
        v=int(input("How many digits? "))
    


    x=input("Lower limit for PN: ")
    y=input("Upper limit for PN: ")
    parts_list=range(int(x),(int(y)+1)) # P[10000]-001 to P[99999]-001
    LaunchBrowser(parts_list,w,z,v)



def LaunchBrowser(parts_list,w,z,v):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://partsurfer.hpe.com/search.aspx")
    #driver.maximize_window()
    #print("here")
    location=driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")               # Find country selection
    location.send_keys("united states")
    location.send_keys(Keys.RETURN)
    #time.sleep(2)
    Search(driver,parts_list,w,z,v)

def Search(driver,parts_list,w,z,v):
    import platform
    for i in parts_list:
        i=str(i).zfill(v)
        try:
            driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')
        except: 
            driver.get("https://partsurfer.hpe.com/search.aspx")

        try:
            elem = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_SearchText_TextBox1')  # Find the search box
            if platform.system() == "Windows":
                elem.send_keys(Keys.CONTROL,"A")
                elem.send_keys(Keys.DELETE)
            if platform.system()=="Darwin":
                elem.send_keys(Keys.COMMAND,"A")
                elem.send_keys(Keys.DELETE)
            if z==None and w!=None:
                elem.send_keys(w,i)
            if w==None and z!=None:                                                                    # If w and z are defined, send w,i,z. Else: send i
                elem.send_keys(i,z)
            if w and z ==None:
                elem.send_keys(i)
            else:
                elem.send_keys(w,i,z)
            elem.send_keys(Keys.RETURN)
        except:
            pass

        #time.sleep(1)
#Below finds the definition for the part number
        try:
            desc = driver.find_element_by_id('ctl00_BodyContentPlaceHolder_gvGeneral_ctl02_lblpartdesc1').text  # Try to find the part description
            if z==None and w!=None:
                print(w,i, " ; ", desc,sep="")
            if w==None and z!=None:                                                                             # Send non "None" variables
                print(i,z, " ; ", desc,sep="")
            if w and z ==None:
                print(i, " ; ", desc,sep="")
            else:
                print(w,i,z, " ; ", desc,sep="")
        except:
            pass                                                                                                # If no description field, it continues on
    print("Search Complete")


SearchCriteria()
