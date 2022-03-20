
x = [r''] # src
y = r"User:Example" #dest
#print(x)
uname = r"" #username
botpw = "" #Bot password
summary = "Example"

import requests
import urllib.request
import re

S = requests.Session()

URL = "https://zh.wikipedia.org/w/api.php"

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action':"login",
    'lgname':uname,
    'lgpassword':botpw,
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
urlstr1 = r"https://zh.wikipedia.org/w/api.php?action=query&prop=revisions&titles="
urlstr2 = r"&rvslots=*&rvprop=content&formatversion=2&format=json"
#n1 = urllib.request.urlopen(urlstr1)
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to edit a page

for text in x:
    urlstr3 = urlstr1 + text + urlstr2
    #print(urlstr3)
    html = dict((S.get(urlstr3)).json())
    html2 = html["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
    #print (html2)
    #print(type(html))
    html3 = html2
    PARAMS_3 = {
    "action": "edit",
    "title": (y + "/" + text[12:]),
    "token": CSRF_TOKEN,
    "format": "json",
    "text": html3,
    "summary": summary
    }

    R = S.post(URL, data=PARAMS_3)
    DATA = R.json()

    print(DATA)
    #break
    
#print(html.json())
#html = html.decode("utf-8")
