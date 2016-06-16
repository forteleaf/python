# 컨셉은 로그인 쿠키를 저장하고 이를 갖고 버튼을 눌러지게 하는 방법
# https://www.packtpub.com/packt/offers/free-learning 무료로 받는 곳 주소
# 2016.06.14 https://www.packtpub.com/freelearning-claim/20039/21478
# 2016.06.15 https://www.packtpub.com/freelearning-claim/14254/21478
# 2016.06.16 https://www.packtpub.com//freelearning-claim/16590/21478

# 파이선
from bs4 import BeautifulSoup
import urllib, http.cookiejar
import requests

base_url = "https://www.packtpub.com/"
get_url = "https://www.packtpub.com/packt/offers/free-learning"
header = {'User-Agent':'Mozilla/5.0'}
r=requests.post(get_url,headers=header)
r.encoding='utf-8'

bs4_packt = BeautifulSoup(r.text,"html.parser")
# 무료책 받는 url
getBook_url = base_url+bs4_packt.find('a',attrs={'class':'twelve-days-claim'})['href']
print(getBook_url)

#### 로그인해서 파일 받아오기

#사용자정보
user_email = 'forteleaf@hotmail.com'
user_pass = 'shuria40'

# Cookie 를 저장
cj = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

authentication_url = 'https://www.packtpub.com/packt/offers/free-learning'
# authentication_url = getBook_url

value = {
    'op':'Login',
    'email': user_email,
    'password': user_pass
}

data = urllib.parse.urlencode(value)
data = data.encode('UTF-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
# res = opener.open(req)
cookie = resp.headers.get('Set-Cookie')
# res = opener.open(getBook_url)
print(cookie)

contents = resp.read()
#확인용
print(contents)

# url = "http://www.pixiv.net/member_illust.php?mode=big&illust_id=29525941"
# req = urllib2.Request(url)
# req.add_header("Referer", "http://www.pixiv.net/member_illust.php?mode=medium&illust_id=29525941")
# res = opener.open(req)
#
# html = read.read()
# print(html)