import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Samsung-C24F396FHU-Curved-Monitor-schwarz/dp/B01DMDKZTC/ref=sr_1_4?dchild=1&keywords=monitor&qid=1591685976&sr=8-4'


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").get_text()
price = soup.find(id = "priceblock_ourprice").get_text()
converted_price = float(price[0:5])

if (converted_price < 100):
    send_mail()


print(converted_price)
print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("thomcord@gmail.com", "updamdntdrpfnldw")
    
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