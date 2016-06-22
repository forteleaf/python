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
    session = requests.session()

    print("free-learing 주소를 얻어 오는 중...")
    base_url = "https://www.packtpub.com/"
    authentication_url = "https://www.packtpub.com/packt/offers/free-learning"
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.post(authentication_url, headers=header)
    r.encoding = 'utf-8'

    # 무료책 받는 url 찾기
    bs4_packt = BeautifulSoup(r.text, "html.parser")
    getBook_url = base_url + bs4_packt.find('a', attrs={'class': 'twelve-days-claim'})['href']
    print("freelearning-claim url : " + getBook_url)

    # Cookie 를 저장
    cj = http.cookiejar.LWPCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # 정보입력
    value = {
        'op': 'Login',
        'email': email,
        'password': password
        'form_build_id': '',
        'form_id': 'packt_user_login_form'
    }

    print('책 얻어오는 중...')
    data = urllib.parse.urlencode(value)
    data = data.encode('UTF-8')
    req = urllib.request.Request(base_url, data)
    resp = urllib.request.urlopen(req)
    # resp = opener.open(req)

    cookie = resp.headers.get('Set-Cookie')
    contents = resp.read()

    # 확인용
    print(getBook_url)
    print(cookie)
    # print(contents)

    # request = urllib.request.Request(getBook_url)
    # response = urllib.request.urlopen(request)
    #
    request = urllib.request.Request(getBook_url)
    response = opener.open(req)

print('packtpub 무료책을 자동으로 받아오기')
# 사용자정보
# user_email = input("email 을 입력해 주세요.\n")
# email 형식 체크
# EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
# if not EMAIL_REGEX.match(user_email) or user_email == "":
#     print('email이 형식이 틀렸습니다..')
#     sys.exit()
# user_pass = input('비밀번호를 입력해 주세요.\n')
# getbook = getbook(user_email, user_pass)
getbook = getbook("forteleaf@gmail.com", "shuria40")
print("완료 되었습니다.")
