# 네이버 스토어팜 댓글 크롤링 해오기
# 오픈 api 형식 이용한 url로 접근해서 json으로 데이터 받기

import json
import requests

s_name = 'klairs' #스토어팜 이름 영문으로 작성
p_number = '119945641' #상품 번호 작성

url01 = 'http://smartstore.naver.com/'
url03 = '/products/'
url05 = '/purchasereviews/general.json?satisfactionGrade=&page.page=1&page.size=1000000'

url_all = url01 + s_name + url03 + p_number + url05

source_code = requests.get(url_all)
plain_text = source_code.text
mydatas = json.loads(plain_text)

# 보기좋게 데이터 확인하는 법
# data = json.dumps(mydatas, indent=2)

list_comment = []
for comment in mydatas['htReturnValue']['pagedResult']['content']:
    list_comment.append(comment['title'])
comment = str(list_comment)

f = open('navercomment.csv', 'w', encoding='utf-8', newline='')
f.write(comment)
f.close()

print(comment)
