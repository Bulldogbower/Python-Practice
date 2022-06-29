from contextlib import nullcontext
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

content=None


#Your email, must enable "less secure apps" within Gmail
user = input("What email address do you want to send from? ")
#Your password
app_password = getpass(prompt='Password: ', stream=None)
#Recipient of your email
to = input("Who do you want to send an email to? ")


#Use Firefrox browser
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)





def LaunchBrowser(driver):
    #Go to website
    driver.get("https://www.recreation.gov/camping/campgrounds/232491")

    #Delete cotents of file and prepare it to be written
    f=open("KirbyCoveAvailability.txt", "w")

    #Close pop-up
    try:
        pop_up=driver.find_element_by_css_selector("button.sarsa-modal-close-button").click()
    except:
        print("No pop-up Window found, continuing")
        pass
    try:
        #Click "Check-in" box to open calendar
        start_date=driver.find_element_by_css_selector("input.DateInput_input_1").click()
    except:
        #If the driver cannot find the check in box, restart at LaunchBrowser
        print("Could not find check-in box, restarting")
        LaunchBrowser(driver)

    #Find next page button, will click later
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
    f.write(month_0.text + "\n" + month_0_days.text + "\n")
    f.write(month_1.text + "\n" + month_1_days.text + "\n")
    f.write(month_2.text + "\n" + month_2_days.text + "\n")
    month_0=month_0.text
    month_1=month_1.text
    month_2=month_2.text

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
    #calendar and click next_page 4 times, grabbing the data between clicks
    #August
    month_3=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div")
    month_3_days=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/table")
    
    #Wait time for elements to load
    driver.implicitly_wait(3)
    #Writing the final month to the file
    f.write(month_3.text + "\n" + month_3_days.text + "\n")
    month_3=month_3.text
    f.close()
    #driver.close()
    #driver.quit()
    Logging(month_0,month_1,month_2,month_3)
    
#I originally wrote 2 separate functions and had a text file between the 2. I bet I can shorten Logging() a lot by not having it it pull from
#the text file. That's for a later time.

def Logging(month_0,month_1,month_2,month_3):
    #Open file for reading
    f=open("KirbyCoveAvailability.txt")
    #Read it line by line
    lines=f.readlines()
    converted_list = []

    #To get rid of "\n"
    for i in lines:
        converted_list.append(i.rstrip())
    lines=converted_list
    f.close()
    #Sorting the months into seperate lists, starting with a string I hard coded "Month_x:$MONTH_NAME YYYY " 
    for i in range(len(lines)):
        if lines[i].__contains__(month_0):
            a=int(i)
            #print("May is here ", str(i))
            #print(month_0.text)
        if lines[i].__contains__(month_1):
            b=int(i)
        if lines[i].__contains__(month_2):
            c=int(i)
        if lines[i].__contains__(month_3):
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

    from datetime import datetime
    import calendar
    print(month_0)
    #Sort through each month individually, should be able to loop this, but that's a later problem
    for i in range(len(month_0)):
        #This only looks for days that are labeled as "A" for available. There's a key on their website for different categories
        #L=Lottery, EA=Early Access, FF=First come First served, #=Unavailabe. I can change it to:
        #if i!="xx":
        #   "On WEEKDAY NUM MONTH YEAR there is availability"
        if month_0[i] == 'A':
            date_for_weekday=(str(month_0[i-1]) + " " + str(month_0[0]))
            datetime_object = datetime.strptime(date_for_weekday, '%d %B %Y')
            weekday=calendar.day_name[datetime_object.weekday()]
            var_1=str("On " + weekday + " " + month_0[i-1] + " " + month_0[0] +  " there is availability")
            results_string.append(var_1)
            f.write("On " + weekday + " " + month_0[i-1] + " " + month_0[0] +  " there is availability" + "\n")
    for i in range(len(month_1)):
        if month_1[i] == 'A':
            date_for_weekday=(str(month_1[i-1]) + " " + str(month_1[0]))
            datetime_object = datetime.strptime(date_for_weekday, '%d %B %Y')
            weekday=calendar.day_name[datetime_object.weekday()]
            var_1=str(" on " + weekday + " " + month_1[i-1] + " " + month_1[0] +  " there is availability")
            results_string.append(var_1)
            f.write("On " + weekday + " " + month_1[i-1] + " " + month_1[0] +  " there is availability" + "\n")
    for i in range(len(month_2)):
        if month_2[i] == 'A':
            date_for_weekday=(str(month_2[i-1]) + " " + str(month_2[0]))
            datetime_object = datetime.strptime(date_for_weekday, '%d %B %Y')
            weekday=calendar.day_name[datetime_object.weekday()]
            var_1=str("On " + weekday + " " + month_2[i-1] + " " + month_2[0] +  " there is availability")
            results_string.append(var_1)
            f.write("On " + weekday + " " + month_2[i-1] + " " + month_2[0] +  " there is availability" + "\n")
    for i in range(len(month_3)):
        if month_3[i] == 'A':
            date_for_weekday=(str(month_3[i-1]) + " " + str(month_3[0]))
            datetime_object = datetime.strptime(date_for_weekday, '%d %B %Y')
            weekday=calendar.day_name[datetime_object.weekday()]
            var_1=str("On " + weekday + " " + month_3[i-1] + " " + month_3[0] + " there is availability")
            results_string.append(var_1)
            f.write("On " + weekday + " " + month_3[i-1] + " " + month_3[0] + " there is availability" + "\n")
    f.close()
    #print(results_string)
    DetectDifferences(results_string)

def DetectDifferences(current):
    f=open("KirbyCoveAvailability.txt", "r")
    lines=f.readlines()

    f2=open("comparison.txt", "r")
    lines2=f2.readlines()

    if lines==lines2:
        print("No update at this time")
        Hold()
    else:
        f2.close()
        f2=open("comparison.txt", "w")
        print("Update found, send email")
        for i in lines:
            f2.write(str(i))
        f2.close()
        SendEmail(current)




def SendEmail(content):
    import yagmail
    #Your email. Must enable "less secure apps" within Gmail
    #user = input("What email address do you want to send from? ")
    #Your password
    #app_password = getpass(prompt='Password: ', stream=None)
    #Recipient of your email
    #to = input("Who do you want to send an email to? ")
    #Email subject
    subject = 'Kirby Cove Availability - Sent with python'
    #Change below text if you want to hard-code the message
    # content = ['mail body content']
    try:
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully')
    except:
        print("Email failed, check settings")
    Hold()

def Hold():
    print("Sleeing for 30 minutes")
    sleep(1800)
    LaunchBrowser(driver)

LaunchBrowser(driver)