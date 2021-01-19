import time

import requests

TWOCAPTCHA_API_KEY = '699ec90c07808e7be4d7f128d4a0b3ba'


class CaptchaSolver:

    def recaptcha(self):
        url = 'http://2captcha.com/in.php'
        files = {'file': open('foo.png', 'rb')}
        data = {'key': TWOCAPTCHA_API_KEY, 'method': 'post'}
        r = requests.post(url, files=files, data=data)
        # print(r)
        if r.ok and r.text.find('OK') > -1:
            reqid = r.text[r.text.find('|') + 1:]
            # print("[+] Capcha id: " + reqid)
            for timeout in range(40):
                r = requests.get(
                    'http://2captcha.com/res.php?key={0}&action=get&id={1}'.format(TWOCAPTCHA_API_KEY, reqid))
                # print("req", r.text[r.text.find('|') + 1:])
                if r.text.find('CAPCHA_NOT_READY') > -1:
                    print(r.text)
                    time.sleep(3)
                if r.text.find('ERROR') > -1:
                    return []
                if r.text.find('OK') > -1:
                    return r.text[r.text.find('|') + 1:]
