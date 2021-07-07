import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B087JYRGDG/ref=s9_acss_bw_pg_test_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=MRJDB4H3X3WEG8B0YG3J&pf_rd_t=101&pf_rd_p=07c8eea2-45a4-49d0-a0e9-a329f311aa90&pf_rd_i=22817284031'
# you can use any url of your choice ,which ever product's price you would like to track
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html-parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="pricebloc_ourprice").get_text()

    converted_price = float(price[0:5])

    if(converted_price < "your_price"):
       sendmail()

def sendmail():
    server = smtlib.SMTP('smtp.gmail.com', 587)
    servor.ehlo()
    server.starttls()
    server.ehlo()
   
    server.login('username@gmail.com', 'password')
    
    subject = 'Price fell down'
    body = 'check the link (link)'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('username@gmail.com', msg)
    
    server.quit()

while(True):
     check_price()
     time.sleep(60 * 60)
