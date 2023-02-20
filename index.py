from requests import Session
from bs4 import BeautifulSoup as bs
import requests
import vonage
import time
import config
from pprint import pprint

headers={"User-agent":'Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'}



#sms sender
def smssender(file_path, key, secret, msg, _from):
    client = vonage.Client(key=key, secret=secret)
    sms = vonage.Sms(client)
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()
        for number in numbers:
            responseData = sms.send_message(
                {
                    "from": _from,
                    "to": number,
                    "text": msg,
                }
            )
            if responseData["messages"][0]["status"] == "0":
                print(f"Message sent successfully to {number}.")
            else:
                print(f"Message failed to {number} with error: {responseData['messages'][0]['error-text']}")




def telegram(msg):
    bot_id = config.App_bot_id
    chat_id = config.App_chat_id
    telegram_url=f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id=-{chat_id}&text={msg}'
    requests.get(telegram_url,headers)

            
while True:
    try:
        
        smssender(config.App_file_path,config.App_Key, config.App_Secret, config.App_sms_content, config.App_from_name)
        telegram("another bulk sms sent successfully!")
        time.sleep(100)
    except:
        
        telegram("hi I am smsender_bot for bulk sms sending , there is a problem :)")
        print("there is a problem sending")
        time.sleep(100)
   

    
    
        
        
        
          
            
    