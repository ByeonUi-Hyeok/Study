'''
상황1.클라이언트가 서버측에 페이지를 요청할때(브라우저에 주소치고 엔터치고) 데이터를 전달하고 싶을때
      => 대표적인 케이스 == 로그인, 검색, 게시판(글상세보기), 게시판 내 페이지이동(2p,3p...)
데이터를 서버로 보내는 방식 == method(메소드)
   1. 메소드의 방식
       - GET  : 가장 일반적 / 형식: 주소뒤에 ?키=값&키=값 ... // 데이터가 크면 짤려서 보내지게됨(헤더로 보냄)
       - POST : 보안에 우수(데이터가 숨겨져서 전송), 대량의 데이터 전송가능
       - 등등 
   2. 동적파라미터 방식
       - URL에 실어서 전송
       - 동적파라미터 방식은 메소드 방식은 메소드 방식과 혼용해서 사용 가능하다.
           - ex : GET + 동적파라미터 // POST + 동적 파라미터
       
    - 데이터 전달 과정 (TCP/IP 참고)
        - 데이터는 HTTP 프로토콜 기반으로 전송되는데 패킷단위로 전송이 된다. 이 패킷의 해더에 데이터가 세팅된다.
           - GET, 동적파라미터 방식은 헤더에 세팅된다.
        - 대량의 데이터 및 숨겨야 할 데이터는 패킷의 body를 통해서 전달된다.
           - ex: POST
           - 해더는 고정적인 크기이고 바디는 가변적이다. 즉 해더는 많은양을 담을 수 없고 바디는 많은양을 담을 수 있다.
'''
# 동적 파라미터방식 실습

from flask import Flask

app = Flask(__name__)

# 기본 홈화면 127.0.0.1:5000
@app.route('/')
def home() :
    return '<h1>127.0.0.1 포트 5000</h1>'
    

# 동적 파라미터 적용 / 기본
## 아래의 동적인 부분/news_id나 news_title을 공란으로 주니까 들어가지지 않눈..
@app.route('/news/<news_id>')             # /<news_id> : 여기에 뉴스 아이디를 넣어서 주소창에 넣으면 된다.
                                          # 즉 주소형식이 == 127.0.0.1:5000/news/965464asd 이나 127.0.0.1:5000/news/1021305490
                                          # 이런식으로 되야함
                                          # 여기의 <news_id>가
def news(news_id) :                       # 여기 인자로들어가서         
    return f'클라이언트가 전달한 데이터 [{news_id}]'       # 여기서 리턴           

# 데이터를 1개 이상 서버측으로 전달 가능한가?
@app.route('/news2/<news_id>/<news_title>')    #주소형식 == 127.0.0.1:5000/news/임의의 입력값/임의의 입력값
def news2(news_id, news_title) :
    return f'클라이언트가 전달한 데이터 [{news_id}] [{news_title}]'

# 타입 제한 == 입력 값의 타입을 int, float, path 으로 제한
## 타입제한 == int
@app.route('/news3/<int:news_id>')               # news_id는 정수값으로만 와야한다. (입력값을 정수로 바꾼다는것보단)
                                                 # 입력값을 정수로 입력해야한다.                  
def news3(news_id) :                             ## 즉 알파벳이나 한글 특수문자 등은 들어올 수 없다.
                                                 ## 형식을 지키지 않고 요청하면 404 Not Found(해당페이지는 없다) 반환됨.
    return f'클라이언트가 전달한 데이터 [{news_id}] '            


## 타입제한 == PATH
### 서버측으로 전달할 내용을 무한대로 가변적으로 확정할 수 있다.
@app.route('/news4/<path:news_id>')               # /(슬래시 구분자로) 주소 계속 들어감 == PATH
                                                  # 즉 127.0.0.1:5000/news4/임의값/임의값/임의값... 가능
                                                  # 임의값/임의값/임의값... 부분이 == PATH

def news4(news_id) :                              
    datas = news_id.split('/') 
    return f'클라이언트가 전달한 데이터 [{news_id}] [{datas[0:2]}] ' ## 데이터를 추출하고 사용을 리스트의 인덱싱형색으로 사용

if __name__ == '__main__' : 
    app.run( debug=True )
