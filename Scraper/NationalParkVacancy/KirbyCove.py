from contextlib import nullcontext
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
content=None

def LaunchBrowser():
    #Delete cotents of file and prepare it to be written
    f=open("KirbyCoveAvailability.txt", "w")
    #Use Firefrox browser
    driver = webdriver.Firefox()
    #Go to website
    driver.get("https://www.recreation.gov/camping/campgrounds/232491")
    #Close pop-up
    pop_up=driver.find_element_by_css_selector("button.sarsa-modal-close-button").click()
    #Click "Check-in" box to open calendar
    start_date=driver.find_element_by_css_selector("input.DateInput_input_1").click()
    #Click to go to next page, will click later
    next_page=driver.find_element_by_class_name("sarsa-day-picker-range-controller-month-navigation-button.right")

    #May
    month_0=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div")
    month_0_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table")
    #June
    month_1=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div")
    month_1_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/table")
    #July
    month_2=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div")
    month_2_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/table")
    
    #I'm writing the 3 viewable months to the text file. I have to add the 4th month later. I'll explain later.
    f.write("Month_0:" + month_0.text + "\n" + month_0_days.text + "\n")
    f.write("Month_1:" + month_1.text + "\n" + month_1_days.text + "\n")
    f.write("Month_2:" + month_2.text + "\n" + month_2_days.text + "\n")
    
    #Tell firefox to wait for the page to load, then 3s. I don't think it works so I added a sleep later
    driver.implicitly_wait(3)
    
    #Click to go to next page
    next_page.click()

    #Wait time for elements to load
    driver.implicitly_wait(3)

    #Hi, here's the sleep
    sleep(2)

    #I had to wait until later because these xpaths change when the next button is clicked. You'll find July is the same as August
    #because when you click the next_page element, August takes July's position. I believe I could loop this and only look at the left
    #calendar, but click next_page 4 times, grabbing the data between clicks
    #August
    month_3=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div")
    month_3_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/table")
    
    #Wait time for elements to load
    driver.implicitly_wait(3)
    #Writing the final month to the file
    f.write("Month_3:" + month_3.text + "\n" + month_3_days.text + "\n")

    f.close()
    driver.close()
    driver.quit()
    Logging()
    
#I originally wrote 2 separate functions and had a text file between the 2. I bet I can shorten Logging() a lot by not having it it pull from
#the text file. That's for a later time.

def Logging():
    #Open file for reading
    f=open("KirbyCoveAvailability.txt")

    #Read it line by line
    lines=f.readlines()

    converted_list = []

    #To get rid of "\n"
    for i in lines:
        converted_list.append(i.strip())
    lines=converted_list
    f.close()

    #Sorting the months into seperate lists, starting with a string I hard coded "Month_x:$MONTH_NAME YYYY " 
    for i in range(len(lines)):
        if lines[i].__contains__("Month_0"):
            a=int(i)
        if lines[i].__contains__("Month_1"):
            b=int(i)
        if lines[i].__contains__("Month_2"):
            c=int(i)
        if lines[i].__contains__("Month_3"):
            d=int(i)

    #I accidentally created nested lists [[1,2,3],[4,5,6]]
    month_0=[lines[a:b]]
    #Quick way to fix it here. If you know of a better way then please show me
    month_0=month_0[0]
    #Something I may be able to loop
    month_1=[lines[b:c]]
    month_1=month_1[0]
    month_2=[lines[c:d]]
    month_2=month_2[0]
    month_3=[lines[d:]]
    month_3=month_3[0]

    #This will hold all of the available dates
    results_string=[]

    f=open("KirbyCoveAvailability.txt", "w")
    #f=open("output.txt", "w")

    #Sort through each month individually, should be able to loop this, but that's a later problem
    for i in range(len(month_0)):
        #This only looks for days that are labeled as "A" for available. There's a key on their website for different categories
        #L=Lottery, EA=Early Access, FF=First come First served, #=Unavailabe. I can change it to:
        #if i!="#":
        #   "MONTH has the NUM available"
        if month_0[i] == 'A':
            var_1=str(" on " + month_0[i-1] + month_0[0] +  " there is availability")
            results_string.append(var_1)
            f.write(" on " + month_0[i-1] + month_0[0] +  " there is availability" + "\n")
    for i in range(len(month_1)):
        if month_1[i] == 'A':
            var_1=str(" on " + month_1[i-1] + month_1[0] +  " there is availability")
            results_string.append(var_1)
            f.write(" on " + month_1[i-1] + month_1[0] +  " there is availability" + "\n")
    for i in range(len(month_2)):
        if month_2[i] == 'A':
            var_1=str(" on " + month_2[i-1] + month_2[0] +  " there is availability")
            results_string.append(var_1)
            f.write(" on " + month_2[i-1] + month_2[0] +  " there is availability" + "\n")
    for i in range(len(month_3)):
        if month_3[i] == 'A':
            var_1=str(" on " + month_3[i-1] + month_3[0] + " there is availability")
            results_string.append(var_1)
            f.write(" on " + month_3[i-1] + month_3[0] + " there is availability" + "\n")
    # DetectDifferences(results_string)
    
    
    SendEmail(results_string)
    

def SendEmail(content):
    import yagmail
    #Your email, must enable "less secure apps" within Gmail
    user = input("What email address do you want to send from? ")
    #Your password
    app_password = getpass(prompt='Password: ', stream=None)
    #Recipient of your email
    to = input("Who do you want to send an email to? ")
    #Email subject
    subject = 'Kirby Cove Availability - Sent with python'
    #Change below text if you want to hard-code the message
    # content = ['mail body content']
    

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')
    Hold(content)

def Hold(content):
    sleep(10)
    LaunchBrowser(content)

# def DetectDifferences(prev_results):
#     if prev_results==content:
#         Hold()
#     else:
#         SendEmail(content)

LaunchBrowser()
