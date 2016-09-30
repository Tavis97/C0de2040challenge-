import requests
info_rmation = { 'github':"https://github.com/Tavis97/C0de2040challenge-", 'token':" http://challenge.code2040.org/api/register"}
url = "http://challenge.code2040.org/api/register"
r = requests.post( url , info_rmation)

