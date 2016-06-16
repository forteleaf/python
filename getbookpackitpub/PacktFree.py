# 컨셉은 로그인 쿠키를 저장하고 이를 갖고 버튼을 눌러지게 하는 방법
# https://www.packtpub.com/packt/offers/free-learning 무료로 받는 곳 주소
# 2016.06.14 https://www.packtpub.com/freelearning-claim/20039/21478
# 2016.06.15 https://www.packtpub.com/freelearning-claim/14254/21478
# 2016.06.16 https://www.packtpub.com//freelearning-claim/16590/21478

# 파이선
from bs4 import BeautifulSoup
import urllib, http.cookiejar
import requests
import PyQt5

#사용자정보
user_email = ''
user_pass = ''

# geturl and getbook
def getbook(email, password):
    base_url = "https://www.packtpub.com/"
    authentication_url = "https://www.packtpub.com/packt/offers/free-learning"
    header = {'User-Agent':'Mozilla/5.0'}
    r=requests.post(authentication_url,headers=header)
    r.encoding='utf-8'

    # 무료책 받는 url 찾기
    bs4_packt = BeautifulSoup(r.text,"html.parser")
    getBook_url = base_url+bs4_packt.find('a',attrs={'class':'twelve-days-claim'})['href']

    # Cookie 를 저장
    cj = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # 정보입력
    value = {
        'op':'Login',
        'email': user_email,
        'password': user_pass
    }

    data = urllib.parse.urlencode(value)
    data = data.encode('UTF-8')
    req = urllib.request.Request(authentication_url, data)
    resp = urllib.request.urlopen(req)
    cookie = resp.headers.get('Set-Cookie')

    contents = resp.read()

    #확인용
    # print(getBook_url)
    # print(cookie)
    # print(contents)
