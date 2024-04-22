from selenium import webdriver
import smtplib
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# for now()
import datetime
 
# for timezone()
import pytz

# print(element)
def run(check:bool):
#launch browser
      if(check):
         ele3=driver.find_element(By.CLASS_NAME,"retreive-slots")
         ele3.click()
      time.sleep(4)
      element2=driver.find_element(By.ID,"tip_msg")
      table=driver.find_element(By.ID,"slots-info")
      # print(element.text)
      current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

      if('no' in element2.text.lower()):
         # sendmail(element2.text,table.text) 
         sendmail("checking online deploy",table.text) 
         print(table.text,element2.text,current_time) 
         pass
      else:
         print(table.text,element2.text)
         sendmail(element2.text,table.text)
      time.sleep(200)
      run(True)

def sendmail(msg:str,tb):
# creates SMTP session
   s = smtplib.SMTP("smtp.gmail.com", 587)
   s.ehlo()
   s.starttls()
   s.ehlo()

   # Authentication
   s.login("abc@gmail.com", "cuplkwovpiywseiy")

   # message to be sent
   message = 'Subject: {}\n\n{}'.format(msg, tb)

   # sending the mail
   s.sendmail("abc@gmail.com", ["abc@gmail.com","abc@gmail.com"], message)
   print("sent mail")
   # terminating the session
   s.quit()



#object of Options class
op = Options()

#set .crx file path of extension
op.add_extension('/Users/pratikjadhav/Downloads/extension_3_0_0_0.crx')
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=op)
driver.get('chrome-extension://beepaenfejnphdgnkmccjcfiieihhogl/popup.html');
time.sleep(1)
element=driver.find_element(By.ID,"apiKey")
element.send_keys('1TOPKM')
element1=driver.find_element(By.ID,"submit")
element1.click()
run(False)
