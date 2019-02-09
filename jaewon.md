> 여태까지 배운 내용들을 복습해보는 시간을 가집시다.

현재까지 저희가 만든 사이트입니다. 저커버그 우는 소리가 여기까지 들리네요!!
![Snulion-Screenshot](https://raw.githubusercontent.com/leegakyeong/djangostudy/master/Snulion-Screenshot.png)

Feeds 앱으로 페이스북 뺨 치는 사이트를 구현해보았으니 이번에는 Travels라는 앱을 활용해 [에어비앤비 사이트](https://www.airbnb.co.kr)를 개선해보도록 하겠습니다.

저희의 사이트는 다음과 같은 기능을 가질 것입니다:
1. 유저의 여행 만들기/보기/수정/삭제
2. 회원가입/로그인/로그아웃
3. 여행에 리뷰 남기기
4. 기존 여행 참가

이를 저희가 배운 내용을 토대로 풀어서 쓰면 다음과 같이 되겠지요:  
1. [Travel 모델에 대한 CRUD 구현](#user-content-CRUD-구현하기)  
2. [Django User Authentication](#user-content-User-Authentication)  
3. [Travel 모델과 Review 모델 간의 1:N 관계](#user-content-1:N-구현하기)  
4. [Membership 모델을 매개로 한 User (Leader, Participant)들 간의 M:N 관계](#user-content-M:N-구현하기)

네, 그럼 에어비앤비를 만들러 가볼까요?

## 1. CRUD 구현하기
일단 `travels`앱을 만들어봅시다.

> 잠깐, 앱과 프로젝트 간의 차이는 무엇일까요? [정답보기](#user-content-프로젝트-vs.-앱)

## 2. User Authentication

## 3. 1:N 구현하기

## 4. M:N 구현하기

(레일즈로 개발을 했던 사람들에게 유용할수도 있는) 꿀팁 한 가지
```python
python manage.py runserver 3000
```
이렇게 입력하면 로컬 서버를 localhost:3000에서 확인할 수 있어서 자동완성된 주소를 활용해 0.0023초 정도 빠르게 접근이 가능하다.

```python
Event.objects.get(event_text__startswith="birthday")
Event.objects.filter(event_text__startswith="birthday")
```
get은 rails의 find (주로 하나의 queryset object가 예상될 때 사용)와 유사, filter은 where (하나 이상의 query set을 예상하는 경우 사용)과 유사. 

```python
Question.objects.get(pub_date__year=current_year)
```

시드 파일 (factory boy)
testing
authentication

Airbnb

[MTV란](https://www.notion.so/Django-BASIC-1-2-MVT-145eeb65d5d44a0ba3f9d56958231605)

```python
get_list_or_404()
get_object_or_404()
```

adding url namespace

~~does this get removed~~

```python
from models import Question, Choice
~~Event.objects.choice_set.all()~~
```

커스텀 모델 매니저? (p.68)

모델 API 몇 가지 소개하기
[쿼리 표현식](https://docs.djangoproject.com/en/2.1/ref/models/expressions/)
[데이터베이스 함수](https://docs.djangoproject.com/en/2.1/ref/models/database-functions/)

[FBV vs. CBV](https://goo.gl/images/8jQg8i)

[Generic View](https://github.com/django/django/tree/master/django/views/generic)

DB drop `./manage.py sqlflush`

### 정답 보기
#### 프로젝트 vs. 앱
- project 와 app 은 무엇이 다를까요?   
    - app 은 (블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱과 같은) 특정한 기능을 수행하는 웹 어플리케이션을 말합니다. project 는 이런 특정 웹 사이트를 위한 app 들과 각 설정들을 한데 묶어놓은 것 입니다. project 는 다수의 app 을 포함할 수 있고, app 은 다수의 project 에 포함될 수 있습니다. [출처](https://docs.djangoproject.com/ko/2.1/intro/tutorial01/)