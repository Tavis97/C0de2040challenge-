import requests
info_rmation = { 'github':"https://github.com/Tavis97", 'token':" http://challenge.code2040.org/api/register"}
r = requests.put ( "http://challenge.code2040.org/api/register", info_rmation)

