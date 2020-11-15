import hashlib
import json
import requests

# def main():
#     headers = {'Content-Type': 'application/json'}
#     data = {"nickname":"大段位","gender":"男"}
#     sign = md5(data)
#     sign = algorithmSign(sign)
#     adata = {"data":data,"sign":sign}
#     a = json.dumps(adata)
#     print(a)
#     res = requests.post(url="http://127.0.0.1:6050/uploadInfo",data=json.dumps(adata),headers=headers)
#     print("服务器返回结果:%s" %res.text)


def md5(string):
    strings = hashlib.md5()
    strings.update(str(string).encode("utf8"))
    return strings.hexdigest()
def algorithmSign(sign):
    sign = sign.replace('a','c')
    sign = sign.replace('6','8')
    sign = sign.replace('f','z')
    sign = sign.replace('e','a')
    sign = sign.replace('3','6')
    sign = sign.replace('1','3')
    sign = sign.replace('5','7')
    sign = sign.replace('8','9')
    return sign
def createSign(data):
    sign = md5(data)
    sign = algorithmSign(sign)
    return sign
print(createSign({"nickname": "小憨憨","gender": "男","game":"王者荣耀","belong_key":"1"}))