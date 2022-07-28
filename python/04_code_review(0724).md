# 04. 영화 조회 및 추천 영화 조회 코드 수정
```python
BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR',
        'query' : title      
    }
        

    response = requests.get(BASE_URL + path, params=params).json()
    if len(response) == 0:
        return None
    # response에 값이 없다면 None을 반환하며 함수 종료
    #response의 타입은 딕셔너리
    result = response['results']
    # result는 리스트
    # for dict in result:
    # result 안의 딕셔너리를 순회하면서
    # 첫 번째 영화의 id 값만 가져오면 되니까 for 문 필요 없음
    id = result[0].get('id','None')
    if id == 'None':
        reommend_list = []
    # id를 path_recommend 에 추가한다
    path_recommend = f'/movie/{id}/recommendations'
    params_2 = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR'        
    }
    # 값을 요청해서 받아오면
    response = requests.get(BASE_URL + path_recommend, params=params_2).json()
    recommend_list = []
    for t in response['results']:
        recommend_list += [t.get('title')]
```



## 1. reponse 값이 없다면 None을 반환하며 함수 종료

```python
response = requests.get(BASE_URL + path, params=params).json()
    if len(response) == 0:
        return None
    
====================================================================

Traceback (most recent call last):
    pprint(recommendation('검색할 수 없는 영화'))
    id = result[0].get('id','None')
IndexError: list index out of range
```

🍰 내가 원한 값 : `None`을 반환하며  함수 종료



🤷‍♀️ 결과 : 함수가 종료되지 않고 계속 진행하여 `id = result[0].get('id','None')`에 도달하여 `'검색할 수 없는 영화'`를 입력받았을 때 `result[0]`의 값을 가져올 수 없으므로 `IndexError`발생



✔ 원인 : `reqeusts.get`이 반환하는 값은 찾는 값이 없으면 `None`을 반환한다. `len(None)`은 0이 아니므로 함수가 계속 진행된 것.



💡 오류 수정 : 

`id = result[0].get('id', 'None')` 에서 `result[0]`의 과정을 전 단계로 올려본다.

`response`의 할당 값을 조정 => <u>딕셔너리가 아닌 리스트로 타입이 조정</u>, 즉 이후 코드의 수정이 필요

```python
response = requests.get(
        URL, params=params).json().get('results')
if len(response) == 0:
        return 
# resquests.get으로 요청한 값의 형태는 딕셔너리이므로 .get 함수를 사용해 'results' 키로 접근하여 값을 가져옴. 'results' 키의 값은 리스트 형태이므로 리스트(값)가 없기 때문에 함수가 종료되며 None을 반환
```





## 2. result 안의 딕셔너리를 순회하면서

```python
#response의 타입은 딕셔너리
    result = response['results']
    # result는 리스트
    id = result[0].get('id','None')
    if id == 'None':
        recommend_list = []
    # id를 path_recommend 에 추가한다
    path_recommend = f'/movie/{id}/recommendations'
```

🍰 내가 원한 값 :

1️⃣ `response`의 타입은 딕셔너리이므로 `response`에서 `'results'`를 키로 하는 값인 리스트를 `result` 에 할당하고, 

2️⃣ 이는 리스트의 형태이므로 인덱스로 접근이 가능하기 때문에 첫 번째의 영화의 정보가 있는 딕셔너리 값을 인덱스 `[0]`으로 접근하고,

3️⃣ `[0]`인덱스의 값이 딕셔너리이므로 다시 `.get`으로 `id` 키로 접근하여 그 값을 `id`에 할당. 키값이 없으면 `'None'`으로 반환.

4️⃣ 만약 `id`에 할당된 값이 `None`이라면, `recommend_list`의 값은 빈 리스트.

 입력값 `'그래비티'`(추천 영화가 없을 경우)에 대한 경우 코드를 생성.



🤷‍♀️, ✔ 결과 및 원인 : 하지만 이전에 1번 오류에서 `response`의 타입은 리스트로 조정되었으므로 해당 코드는 불필요.



💡 오류 수정 : 

그러면 `path_recommend`에 들어갈 `id`의 값은 어떻게 접근하는가?

`response`의 값이 리스트이므로 인덱스부터 접근하면 된다.

**이때, 주의할 점은 따옴표**

```python
path_recommend = f'/movie/{response[0].get("id")}/recommendations'
SyntaxError: f-string: unmatched '(' # 따옴표의 종류를 다르게 써줘야 한다.
```





### ✍ 다음부터는

1. 딕셔너리와 리스트를 접근할 때 찾는 값이 아니라면 상/하위 수준에서 조정을 해 본다.
2. 상단에서 타입이 조정되면 이후 코드도 바뀌게 되고 불필요한 코드를 제거할 수 있다.
   1. ex) 리스트를 굳이 할당할 필요가 없을 경우
3. 이후 코드도 `response` 수준에서 조정을 하면, 처음부터 `results`키의 값인 리스트에 접근할 수 있다.

```python
response = requests.get(BASE_URL + path_recommend, params=params_2).json()
    recommend_list = []
    for t in response['results']:
        recommend_list += [t.get('title')]
========================================================================================
response = requests.get(BASE_URL + path_recommend, params=params_2).json().get('results')
    recommend_list = []
    for t in response:
        recommend_list += [t.get('title')]
        # 혹은 recommend_list.append(t.get('title'))
    return recommend_list
```

