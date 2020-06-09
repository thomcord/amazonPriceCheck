# This program will check the price of a product on Amazon.de and send and email if a conditional is true.

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Product link
URL = 'https://www.amazon.de/Samsung-C24F396FHU-Curved-Monitor-schwarz/dp/B01DMDKZTC/ref=sr_1_4?dchild=1&keywords=monitor&qid=1591685976&sr=8-4'


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

# Function that will get the information from the URL - in this case we will get:
# productTitle and priceblock_ourprice (product price)
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if (converted_price < 100):
        send_mail()

    print(title.strip())
    print(converted_price, "€")
    

    if (converted_price <= 100):
        send_mail()
    
# Function that will send an email if the price is 'True'
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("thomcord@gmail.com", "YOUR_PASSWORD_HERE")
    
    subject = "Price fell down!"
    body = "Check the amazon link: \n https://www.amazon.de/Samsung-C24F396FHU-Curved-Monitor-schwarz/dp/B01DMDKZTC/ref=sr_1_4?dchild=1&keywords=monitor&qid=1591685976&sr=8-4 "
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        "thomcord@gmail.com",
        "thomcord@me.com",
        msg
    )
    
    print("Email has been sent")
    
    server.quit()
    
    #Calling the function
check_price()

#It is also possible to add a loop to check the price from time to time
#while(True):
#    check_price()
#    time.sleep(45)
    