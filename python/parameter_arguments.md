# 매개변수

> 📺 [7월 13일 python 03. 함수]([(2) KDT 실무 맞춤형 풀스택 개발 - 7월 13일 - YouTube](https://www.youtube.com/watch?v=Qr_8XKacOOI))

<hr>

매개변수에 대한 개념이 제대로 잡혀있지 않아 이번 기회에 정리하고자 한다.

<hr>

## 함수 기초

### 선언과 호출

1. 함수의 선언은 `def` 키워드를 활용한다.

2. 들여쓰기를 통해 `Function body(실행될 코드 블록)`을 작성한다

   ````
   Docstring은 함수 body 앞에 
   """선택적으로
   
   			작성가능"""
   Docstring 이란 Python에 있어서 클래스나 메소드에 대한 설명을 기재한 주석을 의미
   ````

   > [python docstring 작성법](https://engineer-mole.tistory.com/136)

3. 함수는 `parameter`를 넘겨줄 수 있다.
4. 함수는 동작 후에 `return`을 통해 결과값을 전달한다.

5. 함수는 `함수명()`으로 호출한다

   `parameter`가 여러 개라면 `함수명(값1, 값2, ,,)`으로 호출

   ````
   def add(x,y) :
   	return x + y
   ````

 ### 예시

```python
num1 = 0
num2 = 1

def func1(a, b):
	return a + b
	
def func2(a, b):
	return a - b

def func3(a, b):
	return func1(a, 5) + func2(5, b)

result = func3(num1, num2)
print(result)
# 9
```



### 함수의 결과값(Output)

> *함수는 반드시 값을 하나만 반환한다.*

1. 함수는 반드시 값을 하나만 `return` 한다.

   명시적인 return이 없는 경우에도 *`None`을 반환한다.*

2. 함수는 return과 동시에 *실행이 종료*된다.

3. return값을 두 개 주고 싶다면?

   > 한개의 *튜플로* 묶어서 반환한다

   ```
   def minus_and_product(x, y):
   	return x - y, x * y
   ```

   ```
   minus_and_product(4, 5)
   ```

   ```
   (-1, 20)
   ```

- return vs print

    return 은 함수 안에서 값을 반환하기 위해 사용되는 키워드

    print는 출력을 위해 사용되는 함수

    > print 함수는 `None`을 반환한다



### 함수의 입력(Input)

#### 🔥 parameter vs argument

- Parameter: 함수를 *실행할 때*, 함수 내부에서 사용되는 식별자

  ```
  def function(ham):
  	return ham
  ```

- Argument : 함수를 *호출할 때*, 넣어주는 값

  ```
  function('spam')
  ```



### Argument

> 함수 '호출'시 함수의 parameter를 통해 전달되는 값

Argumment는 소괄호 안에 할당한다

```
func_name(argument)
```

- **필수 Argument** : 반드시 전달되어야 하는 argument
- **선택 Argument** : 값을 전달하지 않아도 되는 경우는 기본 값이 전달



**positional arguments**

기본적으로 함수 호출 시 Argument는 *위치*에 따라 함수 내에 전달됨.

```
def add(x, y):
	return x + y
```

x, y의 위치와 동일하게 `(2, 3)`

```
add(2, 3)
```



**keyword arguments**

직접 변수의 이름으로 특정 Argument를 전달할 수도 있는데, 이를 키워드 인자라고 함.

<u>Keyword Argument 다음에는 Positional Argument를 활용할 수가 없음.</u>

```
def add(x, y):
	return x + y
```



변수의 이름으로 특정 argument를 전달 가능

```
add(x=2, y=5)
```

```
add(2, y=5)
```



키워드 인자 다음으로 위치 인자가 오는 경우 => 안됨.❌

```
add(x=2, 5)
```

뒤에 위치한 `5`의 위치인자의 의미가 없다. 이미 앞에서 `x=2`라는 키워드 인자를 사용했기 때문이다.



**default arguments values**

기본값을 지정하여, 함수 호출 시 argument 값을 설정하지 않도록 한다

​	정의된 것보다 더 적은 개수의 argument들로 호출될 수 있다.



`y=0`으로 기본값을 지정하였을 경우,

```python
def add(x, y=0):
	return x + y
```

정의된 것`(x, y)` 2 개보다 더 적은 한 개의 인자로도 호출이 가능하다.

```python
add(2) # 2
```

따로 인자를 추가하지 않을 경우 넘어가는 인자의 값이기 때문에, 설정하면 설정한 값이 인자로 넘어가기 된다.

```python
add(2, 5) # 7
```



### 예시(`print()`)

`print('hi', 'hello')`를 한 결과가

```
hi hello
```

인 이유는 `print()` 자체에 기본 인자 값으로`sep=" "` 띄어쓰기가 선언되어 있기 때문이다.

키워드 인자로 `sep`를 바꿔서 호출 가능하다.`sep='-'`

```python
print('hi', 'hello', sep='-') # hi-hello
```



그렇다면, `print()`는 인자가 몇 개가 들어올 줄 알고, 다 출력해내는 걸까?



***정해지지 않은 개수***의 arguments

> **args*

*여러 개의 Positional Argument를 하나의 **필수 parameter**로 받아서 사용*한다

몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

```python
def add(*args):
	for arg in args:
	print(arg)
```

```python
add(2)
```

```python
add(2, 3, 4, 5)
```

```
def my_add(*numbers):
	return numbers

result = my_add(1, 2, 3)
```

```python
print(result, type(result))
```

정해지지 않은 개수의 인자는 내부적으로 tuple의 타입으로 반환된다.

```python
(1, 2, 3) <class 'tuple'>
```



***정해지지 않은 개수*의 keyword arguments**

> ***kwargs*

함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정

Argument들은 딕셔너리로 묶여서 처리되며, parameter에 `**`를 붙여 표현

```python
def family(**kwargs):
	for key, value in kwargs:
		print(key, ":", value)
```

```python
family(father='Jhon', mother='Jane', me='Jhon Jr.')
```

```python
def my_func(**kwargs):
	return kwargs
	
result = my_func(name='홍길동', age='100', gender='M')
```

```python
print(result, type(result))
```

```python
{'name':'홍길동', 'age':'100', 'gender':'M'}
```
