import requests
from requests_html import HTMLSession    
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime


email_sent = 0

items_to_watch = ['']
print('---------------------------')

url = f"https://PRODUCTURL.com/item/"

while email_sent == 0:
    try:
        session = HTMLSession()
        response = session.get(url)
        item = response.html.find('div')
        # total_products_found = len(response.html.find('div'))
        # for i in range(totalProductsFound):
        #     print(item[i].text)
        #     itemsAvailable =+ item
        print('Checking Stock again..')
        print('---------------------------')
        # nth div item. number my differ slightly from chrome console. - BL
        # check document.getElementsByTagName("div") or document.getElementsByTagName("div")[76] in chrome console - BL
        if item[76].text == "Sold out online.":
            print('Sold out online.')
            now = datetime.now()
            print(now.strftime("%H:%M:%S"))
            time.sleep(60)
        else:
            print('In stock!')
            gmail_user = 'youremail@email.com'
            gmail_password = 'yourpassword'

            sent_from = gmail_user
            to = ['youremail@email.com']
            subject = 'Item in stock'

            try:
                # send email to gmail
                # make sure "Less Secure Apps" is enabled in test gmail account to use SMTP - BL
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, "ITEM IN STOCK")
                server.close()

                print ('Email sent!')
                now = datetime.now()
                print(now.strftime("%H:%M:%S"))
                email_sent += 1
                print('closing program.')
            except:
                print ('Something went wrong...')
            
    except requests.exceptions.RequestException as e:
        print(e)

