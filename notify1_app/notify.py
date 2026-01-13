import email
import imaplib
from email.parser import BytesParser
from email.header import decode_header
import requests
import time
import os 


memail = os.getenv ("msk1734811@gmail.com")
app_pass= os.getenv ("yndupaypaslhuret")
IMAP_SERVER = ("imap.gmail.com")


keywords= ["jobs", "hiring", "vacancy", "project",
    "salary", "deal", "wage", "account", "linked", "hats", "weekly"]

Telegram_chat_ID= os.getenv("7575524175")
Telegram_Bot_Token = os.getenv("7950022254:AAGD34I85A5L3GjeHnvBRy9-SDzIn21PV70")


def tele(text):
    try: 
        url= f"https://api.telegram.org/bot{Telegram_Bot_Token}/sendMessage"
        data= {"chat_id" : Telegram_chat_ID, "text": text}
        requests.post(url, data= data, timeout=10)
    except requests.exceptions.RequestException as e:
        print("telegram error", e)


def keyword_match(text):
    text = text.lower()
    return any (k in text for k in keywords)

def read_mails():
    mail= imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(memail, app_pass)
    mail.select("inbox")

    status, message = mail.search(None, "UNSEEN")
    email_ids= message[0].split()

    for eid in email_ids:
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg= email.message_from_bytes(msg_data[0][1])
        subject, encoding = decode_header(msg["subject"])[0]
        
        if isinstance (subject, bytes):
            subject= subject.decode(encoding or 'utf-8' )

        body= ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type()=="text/plain":
                    body= part.get_payload(decode=True).decode(errors="ignore")
                    print(body)
                    break
        else:
            body= msg.get_payload(decode=True).decode(errors="ignore")
            print(body)
        
        full_text= f"{subject}{body}"
        print("sending to telegram")

        if keyword_match(full_text):
            send_to_telegram = (f"EMAIL ALERT:\n\n {subject} ")
            tele(full_text)
    mail.logout()

def main(): 
    while True:
        read_mails()
        print("checking done")
        time.sleep(60)

if __name__=="__main__":

    main()
