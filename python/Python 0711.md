# Intro

## 컴퓨터 프로그래밍 언어



- **컴퓨터**(Computer) *Caculation + Remember*

​		계산을 하고 기억을 한다.

1. 계산
2. 기억

- **프로그래밍**(programming)

​		명령어의 모음(집합)

- **언어**

  자신의 생각을 나타내고 전달하기 위해 사용하는 체계

  문법적으로 맞는 말의 집합



컴퓨터 프로그래밍 언어 : 컴퓨터에게 생각을 나타내고 전달하기 위한 `명령어`

✔ 컴퓨터에게 명령하기 위한 약속



선언적 지식과 명령적 지식

- 선언적 지식(declarative knowledge) : 사실에 대한 내용
- 명령적 지식(imperative knowledge) : "How-to"

💡 <u>내가 무슨 명령을 하려고 했는지 잊지 않는 것이 중요</u>





# 파이썬 개발 환경

#### 파이썬(Python)이란?

- Easy to learn : 변수에 별도의 타입지정이 필요없음 => 동적 타이핑 언어

​								문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음

​								예) 문장을 구분할 때 중괄호(`[,]`) 대신 들여쓰기를 사용

- Expressive Language : C나 자바로 작성할 때보다 더 간결하게 작성 가능

- 크로스 플랫폼 언어 : Windows, macOS, Linux, Unix 등 다양한 운영체제에서 실행 가능



####  파이썬의 특징

- 인터프리터 언어 (Interpreter)  : 컴파일 과정 없이 바로 실행 가능

  ​														코드를 <u>대화하듯 한 줄 입력하고 실행</u>한 후, 바로 확인 가능

- **객체 지향 프로그래밍** :  모든것이 객체로 구현되어 있음

  ​										객체(object) : 숫자, 문자, 클래스 등 `값`을 가지고 있는 모든 것<어떠한 `것`, `대상`>

#### 파이썬 기본 인터프리터 : IDLE(Intergrated Development and Learning Environment)



## 기초 문법

> 코드 스타일 가이드
>
> [PEP8](https://www.python.org/dev/peps/pep-0008/)
>
> [기업, 오픈소스 등](https://google.github.io/styleguide/pyguide.html)
>
> 코드는 위에서부터 아래로 실행
>
> 코드는 오른쪽에서 왼쪽
>



- 들여쓰기(Identation)
  - Space Sensetive **문장을 구분할 때**, 들여쓰기를 사용
  - `Space` 키 4번(**4칸**) 혹은 `Tab`키 1번(**1탭**)을 입력
  - ⚠<u>한 코드 안에서는 한 종류의 들여쓰기</u>를 사용(4칸 or 1탭)
    - [PEP8](https://www.python.org/dev/peps/pep-0008/) 권장사항은 4칸 공백 사용




- 변수(Variable)

  - 변수란?

    - 컴퓨터 메모리 <u>어딘가에 저장되어 있는 객체</u>를 가져오기 위해 사용되는 이름

    - 파이썬은 객체 지향 언어, 모든 것이 객체(object, 숫자/문자/클래스 등 값을 가지고 있는 모든 것)으로 구현되어 있음

    - <u>동일 변수에 다른 객체를 언제든 할당</u>할 수 있기 때문에,

    - =참조하는 객체가 바뀔 수 있기 때문에

    - '변수'라고 불림

      

  - 변수는 할당연산자(=)를 통해 값을 할당(assignment)

    - <u>type() : 변수에 할당된 값의 타입</u> 	✔**늘 주의할 것**

    - id() : 변수에 할당된 값(객체)의 고유한 아이덴티티 값

      ```python
      x='hi'
      type(x)
      # str, 문자열
      id(x)
      # 4645387184, 0711시점 배우지 않음.
      ```

    - 변수 연산

      ```python
      i = 5
      j = 3
      s = '파이썬'
      # 1.
      print(i + j)
      # 2.
      print(i - j)
      # 3.
      j=-2
      print(i*j)
      ```

      ```python
      i = 5
      j = 3
      s = '파이썬'
      # 1. 문자열과 변수의 연산
      print('안녕' + s)
      # 2.
      print(s * 3)
      # 3. 변수랑 문자열의 연산
      s = 'Python'
      print(s + ' is fun')
      ```

    - 실습 ) x=10, y=20일 때, 각각 값을 바꿔서 저장하는 코드

       1. 임시 변수 활용
    
           ```python
           tmp = x
           x = y
           y =tmp
           print(x, y)
           ```
    
       2. Pythonic!
    
           ```python
           y, x = x, y
              print(x, y)
           ```
    
           
    

- 식별자(Identifiers)

  - 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는 데 사용하는 이름(name)

  - 규칙

    - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

    - 첫 글자에 숫자가 올 수 없다

    - 길이 제한이 없고, 대소문자를 구별한다

    - 예약된 단어로는 쓸 수 없다

    - 내장함수나 모듈 등의 이름으로도 만들면 안 된다

      ```python
      print(5)
      print = 'hi'
      print(5)
      
      # Traceback (most recent call last):
       print(5)
          line 3, in <module>
      TypeError: 'str' object is not callable
      ```

      내장 함수 print 가 아닌 식별자가 print인 문자열 hi로 활용됨




- 사용자 입력

  - input(**[prompt]**)

    - 사용자로부터 값을 즉시 입력받을 수 있는 **내장함수**

    - **[prompt]**에 문자열을 넣으면(=소괄호에 입력) 입력시,  해당 문자열을 출력

      ✔ **반환값은 항상 문자열의 형태로 반환**

      ```python
      name = input('이름을 입력해주세요 : ')
      print(name)
      print(type(name))
      
      이름을 입력해주세요 : 파이썬
      파이썬
      <class 'str'> ✔ 반환값은 항상 문자열의 형태
      ```




- 주석(Comment)

  - 중요한 점이나 다시 확인하여야 되는 부분 표시

  - 컴퓨터는 주석 인식 **안 함**(only for 사용자)

  - 쉬운 이해와 코드의 분석/수정을 위해 주석을 작성하는 습관이 중요

    - 주석은 코드 실행에 영향 안 미침.

    - 프로그램의 속도를 느리게 하지 않고, 용량을 늘리지 않음

      ```python
      # 주석(comment)입니다. 온전히 한 줄 모두 주석
      
      # print('hello')
      print('world') # 주석은 코드 뒷부분에 작성도 가능
      world # 주석은 코드 실행에 영향을 미치지 않음
      ```





## 파이썬 기본 <자료형>

#### 자료형 분류

- 불린형(Boolean Type) : True / False(참, 거짓), 비교/논리 연산
- 수치형
- 문자열
- None : 없다

- 논리연산자
- and : True and True여야만 True이고 나머지는 다 False
- or : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓
- not : 참 거짓의 반대의 결과 



- 정수(int)

  - 모든 정수의 타입은 int
  - 정수가 아닌 모든 실수는 float 타입
  - 복소수 : 사용 안 함

  

산술 연산자 : `/` 나눗셈, `//` 몫,  `**` 거듭제곱, `%` 나머지(홀,짝수 판명할 때 많이 사용)

복합 연산자 : 연산과 할당이 함께 이뤄짐

비교 연산자 : 미만 이하 초과 이상 

`!=` 같지 않음



- 문자열

  > 문자열은 따옴표를 활용하여 표기
  >
  > 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

- 따옴표 안에 따옴표를 넣고 싶을 때 

  - 중첩 따옴표(안에 넣고 싶은게 큰 따면 작따를, 그 반대면 반대를)
  - 삼중따옴표(큰따, 작따 둘다 안에 넣고 싶을 때 삼중따옴)

- 인덱싱
  - <u>인덱스를 통해 특정 값에 접근할 수 있음</u>
  - s[1]
  - 문자열 슬라이싱 : 문자열을 잘라낼 수 있다.
  - s[2:5] 2이상 5미만
  - s[2:5:2] 2이상 5미만 2씩 step
  - 파이썬은 음의 인덱스도 가지고 있다
  - 위치,,,??? 어<u>디에 위치해 있는지</u>를 나타내는 값?
  - s[:3] 3 미만
  - s[5:] 5 이상
  - s[::] 
  - s[::-1] 역순
- :3 기본 0시작, 5: 5부터 마지막까지야
- 기타 : 결합`+`, 반복`*`, 포함`in`



- 형 변환
  - 암시적 형 변환 : 파이썬이가 내부적으로 자료형을 변환
  - 명시적 형 변환 : 사용자가 의도적으로 자료형을 변환 = 형식에 맞는 문자열만 가능



- 컨테이너

  > 여러 개를 

  - 리스트 값들의 나열, 인덱스 순서로 접근
  - 딕셔너리 `{ }` 딕셔너리는 키-값의 쌍, 접근할 때 키로 접근





# 오전 회차 정리

> 파이썬에서 정리해야할 내용

변수라고 하면 

이름 = 타입의 값들을 할당

- 이름은 숫자로 시작 안되고,
- 예약어 안 되고,
- 알파벳, 기호, 숫자 안 된다.
- 알파벳에서는 대소문자를 구별한다.



프로그래밍의 규칙

- 위에서부터 아래로 순차적으로 실행
- 오른쪽의 결과를 왼쪽으로 할당



**타입** 

- 숫자(int, float, complex)
- Boolean(True, False)
- None
- 컨테이너
  - 시퀀스(순서o) : 리스트, 인덱스로 접근
  - 컬렉션(순서x) : 딕셔너리 순서가 없어서 키로만 접근.
- 타입마다 연산자가 다르게 존재한다.
  - 1+2 = 3, "hi" + "!"=hi!



컴퓨터는 숫자를 <u>0부터</u> 센다.



# 오후

## 시퀀스형 주요 공통 연산자

변경 가능한 값들의 나열된 자료형

변경이 가능하며 반복이 가능함.

값을 바꿔칠 수 있음

생성이랑 **접근**



리스트값 추가/삭제

값 추가는 .append()를 활용하여 추가하고자 하는 값을 전달

값 삭제는 .pop()를 활용하여 삭제하고자 하는 인덱스를 전달

boxes[1] [0]



Tuple

- 불변한 값들의 나열
- 변경이 불가능하며 , 반복이 가능하다



Range(레인지)

- 숫자의 시퀀스를 나타내기 위해 사용
- range(3) - 0,1,2를 포함
- 슬라이싱과 비슷하다 (이상, 미만)
- 숫자를 확인하려면 리스트 변환해서 보면 편하다



## 비시퀀스형

세트

- 유일한 값들의 모음(collection)
- 중복된 값이 없고, 순서가 없음.
  - 수학에서의 집합과 동일한 구조를 가짐
- 변경 가능하며, 반복 가능함.
- 빈 `{중괄호}`는 딕셔너리
- 내부적으로 '표현'만 똑같이 하는 방법이 있을 뿐 순서는 없다.



딕셔너리

- 불변 자료형만 가능
- key와 value가 쌍으로 이뤄진 
- 순서가 없음
- 딕셔너리에 키와 값의 쌍을 추가할 수 있음



- 시퀀스

문자열 : 문자들의 나열

리스트 : 변경 가능한 값들의 나열

튜플 : 변경 불가능한 값들의 나열

레인지 : 숫자의 나열

- 컬렉션/ 비시퀀스

세트 : 유일한 값들의 모음

딕셔너리 : 키-값들의 모음



input은 모두 string으로 저장.

숫자로 활용하기 위해서는 항상 int로 변환해야 한다



print(int(number)) 와

number = input()



.split 쪼개다



---

# 0712

## 제어문

> 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
>
> 제어문은 순서도(flow chart)로 표현이 가능
>
> 특정 상황에 따라 코드를 '선택적으로'



### 조건문

어떤 조건이 거짓인 참/거짓인 경우 <u>각각 실행</u>하는 코드블록이 있음.

if <코드> : 

identation

else : 

identation



참/거짓을 확인할 수 있는 "조건" a>=0

아닌 경우'음수'출력, 맞는 경우 '양수' 출력

```python
a = -10 # 값은 바뀔 수 잇음
if a >= 0 :
    print('양수')
else : 
    print('음수')
print(a)

#'-10'이므로 '음수'
# if : else : 띄어쓰기 4칸
```



홀수인지 확인하는 코드

```python
=>2를 나눈 나머지가 1이야?

num = int(input ())

if num % 2 == 1 :

​    print ('홀수')

else : 

​    print ('짝수')
```



💡 input()입력값은 '문자열'type 이므로 <u>int로 형 변환해줘야 한다.</u>

💡 현재 시점에서 어떤 type인 지 늘 확인

💡 콜론 잊어먹지 말기



#### 복수 조건문

복수의 조건식을 활용할 경우 `elif`를 활용하여 표현



💡 else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능

💡 조건문에서 else는 생략이 가능하다.

💡 조건식을 동시에 검사하는 게 아니라 <u>순차적으로</u> 비교한다.



#### 중첩 조건문

조건문은 다른 조건문에 중첩되어 사용될 수 있음

if 문 안에 if문이 있는 형태 (elif로 간단히 쓸 수 있음)



#### 조건 표현식 

220712 기준 중요하게 다루지 않음.

#1. 양수면 그대로

#2. 음수면 -붙여서



### 반복문

#### while 문

조건식이 참인 경우 반복적으로 코드를 실행 = 조건식이 참일 때까지만 실행

반복하면서 종료조건을 정해주는 것이 중요

a +=1

a = a+1



#### for 문

순회 가능한 객체 요소를 모두 순회

<u>처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음</u>

```python
for <변수명> in <iterable> : 
   
```

	- 문자열 순회



#### 딕셔너리 순회



#### 반복문 제어

- break
- continue 이후의 코드블록은 수행하지 않고, 다음 반복을 수행
  - continue를 만나면 코드블록은 수행되지 않는다.

- for-else 다 돌았을 때 실행되는 코드
- 
