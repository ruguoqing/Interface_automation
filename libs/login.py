import requests
from configs.config import HOST
from tools.getmd5 import get_md5

class Login:
    def login(self,Indata):
        url = HOST + '/api/loginS'
        res = requests.post(url=url, json=Indata)
        return res.text

if __name__ == '__main__':

    result = Login().login({"username": "20154084", "password": get_md5('123456')})
    print(result)