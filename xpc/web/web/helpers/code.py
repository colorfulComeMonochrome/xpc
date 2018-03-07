import random
import requests
from web.models.code import Code

SMS_API = 'http://sms-api.luosimao.com/v1/send.json'
SMS_USER = 'api'
SMS_KEY = 'd4c73a2afa7864d061e8d8e9a11a5f19'
SMS_API_AUTH = (SMS_USER, 'key-%s' % SMS_KEY)


def gen_code():
    return str(random.randint(100000, 999999))


def send_sms_code(phone, code):
    message = '您的验证码0.0是: %s, 请在收到后的10分钟内输入。 【千锋】' % code
    requests.post(SMS_API, data={
        'mobile': phone,
        'message': message
    }, auth=SMS_API_AUTH)
    print('send sms to %s: %s' % (phone, message))


def verify(phone, code):
    cm = Code.objects.filter(phone=phone, code=code).first()
    if not cm:
        return False
    return True





