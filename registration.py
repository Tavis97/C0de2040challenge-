import requests
token = "314aed9130cfb67037d554260470b4b3"
def registration():
  info_rmation = {'token': token , 'github':"https://github.com/Tavis97/C0de2040challenge-"}
  url = "http://challenge.code2040.org/api/register"
  r = requests.post( url , info_rmation)

stringt = {'token': token, 'string': 'http://challenge.code2040.org/api/reverse'}
url= 'http://challenge.code2040.org/api/reverse'
mystring = requests.post( url, stringt)
string = mystring[::-1]
url_1 = "http://challenge.code2040.org/api/reverse"
info = {'token': token , 'string': string}
re = requests.post( url_1, info)
url_1 = "http://challenge.code2040.org/api/reverse/validate"


