# import time
#
# import requests
#
# TWOCAPTCHA_API_KEY = '699ec90c07808e7be4d7f128d4a0b3ba'
#
#
# class CaptchaSolver:
#
#     def recaptcha(self):
#         url = 'http://2captcha.com/in.php'
#         files = {'file': open('foo.png', 'rb')}
#         data = {'key': TWOCAPTCHA_API_KEY, 'method': 'post'}
#         r = requests.post(url, files=files, data=data)
#         # print(r)
#         if r.ok and r.text.find('OK') > -1:
#             reqid = r.text[r.text.find('|') + 1:]
#             # print("[+] Capcha id: " + reqid)
#             for timeout in range(40):
#                 r = requests.get(
#                     'http://2captcha.com/res.php?key={0}&action=get&id={1}'.format(TWOCAPTCHA_API_KEY, reqid))
#                 # print("req", r.text[r.text.find('|') + 1:])
#                 if r.text.find('CAPCHA_NOT_READY') > -1:
#                     print(r.text)
#                     time.sleep(3)
#                 if r.text.find('ERROR') > -1:
#                     return []
#                 if r.text.find('OK') > -1:
#                     return r.text[r.text.find('|') + 1:]

import base64
import requests


class Captcha:
    def __init__(self):
        self.url = 'http://api.captcha.guru/in.php'
        self.api_key = '6ba2e16514850409e3a33b479f8a9e92'

    def solve(self):
        with open("foo.png", "rb") as image_file:
            b64 = base64.b64encode(image_file.read())
        data = {'method': 'base64', 'key': self.api_key, 'body': b64}
        response = requests.post(self.url, data=data)
        tst = response.text.split('OK|')[1]
        while True:
            response = requests.get(
                "http://api.captcha.guru/res.php?key=6ba2e16514850409e3a33b479f8a9e92&action=get&id=" + tst)
            if 'OK' in response.text: break
        captcha_text = response.text.split('|')[1].upper()
        # print(captcha_text)
        return captcha_text


def main():
    obj = Captcha()
    obj.solve()


if __name__ == '__main__':
    main()

