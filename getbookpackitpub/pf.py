# https://www.packtpub.com/packt/offers/free-learning 무료로 받는 곳 주소
# 2016.06.14 https://www.packtpub.com/freelearning-claim/20039/21478
# 2016.06.15 https://www.packtpub.com/freelearning-claim/14254/21478
# 2016.06.16 https://www.packtpub.com//freelearning-claim/16590/21478

from bs4 import BeautifulSoup
import urllib
import http.cookiejar
import requests

def getbook(email, password):
    # 정보입력
    base_url = "https://www.packtpub.com/"
    authentication_url = "https://www.packtpub.com/packt/offers/free-learning"
    # https://www.packtpub.com//freelearning-claim/20079/21478

    data = {
        'op' : 'Login',
        'email' : email,
        'password' : password
    }
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.post(authentication_url, headers=header)
    r.encoding = 'utf-8'
    bs4_packt = BeautifulSoup(r.text, "html.parser")
    getBook_url = base_url + bs4_packt.find('a', attrs={'class': 'twelve-days-claim'})['href']
    print("claim: " + getBook_url)

    cj = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [{'User-Agent': 'Mozilla/5.0'}]
    urllib.request.install_opener(opener)
    value = urllib.parse.urlencode(data)
    binary_data = value.encode('UTF-8')

    req = urllib.request.Request(getBook_url, binary_data)
    resp = urllib.request.urlopen(req)
    contents = resp.read()
    print(contents)


print('packtpub 무료책을 자동으로 받아오기')
book = getbook("forteleaf@gmail.com", "shuria40")
print("완료 되었습니다.")
