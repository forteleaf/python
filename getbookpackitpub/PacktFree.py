# https://www.packtpub.com/packt/offers/free-learning 무료로 받는 곳 주소
# 2016.06.14 https://www.packtpub.com/freelearning-claim/20039/21478
# 2016.06.15 https://www.packtpub.com/freelearning-claim/14254/21478
# 2016.06.16 https://www.packtpub.com//freelearning-claim/16590/21478

from bs4 import BeautifulSoup
import sys
import urllib
import http.cookiejar
import requests
import re

# geturl and getbook
def getbook(email, password):
    print("free-learing 주소를 얻어 오는 중...")
    base_url = "https://www.packtpub.com/"
    authentication_url = "https://www.packtpub.com/packt/offers/free-learning"
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.post(authentication_url, headers=header)
    r.encoding = 'utf-8'

    # 무료책 받는 url 찾기
    bs4_packt = BeautifulSoup(r.text, "html.parser")
    getBook_url = base_url + str(bs4_packt.find('a', attrs={'class': 'twelve-days-claim'})['href'])
    print(getBook_url)

    # Cookie 를 저장
    cj = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    # 정보입력
    value = {
        'op': 'Login',
        'email': email,
        'password': password,
        'form_id':'packt_user_login_form'
    }

    print('책 얻어오는 중...'+getBook_url)
    data = urllib.parse.urlencode(value).encode("utf-8")
    # req = urllib.request.Request(authentication_url, data=data)
    # req.add_header('User-agent', 'Mozilla/5.0')
    conn = opener.open(authentication_url, data)
    # res = urllib.request.urlopen

    # 확인용
    # cookie = res.headers.get('Set-Cookie')
    # contents = conn.read()
    # print(contents)
    # print(getBook_url)
    # print(cookie)
    # print(contents)

    conn = opener.open(getBook_url)

    # reqbuy = urllib.request.Request(getBook_url)
    # res = opener.open(reqbuy)


print('packtpub 무료책을 자동으로 받아오기')
# 사용자정보
user_email = input("email 을 입력해 주세요.\n")
# email 형식 체크
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
if not EMAIL_REGEX.match(user_email) or user_email == "":
    print('email 형식이 틀렸습니다..')
    sys.exit()
user_pass = input('비밀번호를 입력해 주세요.\n')
getbook(user_email, user_pass)
print("완료 되었습니다.")
