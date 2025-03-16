# [Algorithm] Do It! 자료구조와 함께 배우는 알고리즘 입문 -파이썬 편



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> #: 주제, 그림, 스텝(중요)

>  정렬 부분은 다 한번 해봤지만 기억이 안 남. → 그럼 그냥 해. 알면 빨리 될 것이고, 그렇지 않으면 느리겠지. 코드는 타이핑하고 그림은 따라 그리기.

> 💡 추천 학습법:

# 버블정렬

## 단순 버블 정렬

### 그림: 버블정렬 pass 

pass: 일련의 비교 교환 과정. 버블 정렬에서는 첫 번째 패스로 가장 작은 원소를 구할 수 있음.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/db2cb1a5-5d4c-4ea7-933e-5797c5871104/IMG_9884.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=b4a4e5a07de51b484f880d7f82b2276109a0b29f814136051821285b29506ce7&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


```

## 버블정렬 개선 1

### 코드: 교환 횟수 감지해서 성능 올리기

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    for i in range(n-1):
		    exchng = 0 # exchange time in a pass
        for j in range(n-1, i, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
    if exchng == 0:
			break
```

## 버블정렬 개선 2

아래와 같은 상태일 때 스캔 범위(비교 범위)를 좁히는 부분 추가.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/4bb85350-4f4a-4c1c-8c0a-0f24ba97063b/IMG_9885.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=44a8fd242c051273c1972afd9d4dc43198e1dc09ba1bee865cef5c28bdec16e3&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 스캔 범위 제한

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1    
        for j in range(n-1, k, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j # update last. we can mark maximum area that should be scanned.
        k = last



```

## 셰이커 정렬

밀크 셰이크 먹고 싶다.

위와 같은 경우 거의 정렬이 다 됐지만 빠르게 마칠 수 없음. 9가 맨 끝에 있어서. 아이디어: 9를 맨 뒤로 이동시키면 정렬이 훨씬 빠르겠지?

### 코드: 셰이커 정렬

```python
from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
```

### 그림: 셰이커 정렬 패스

일단 스킵

# 단순 선택 정렬

# 단순 삽입 정렬

# 셸 정렬

# 퀵 정렬

## 기본 개념

### 그림: 퀵 정렬의 예

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/daac6dc7-7587-4378-a249-39ce32d19c09/IMG_9899.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=c422c7625f9f8cff504b63e8ca2b41d78df8bce5b6f0eadc42eff1e25621a78e&X-Amz-SignedHeaders=host&x-id=GetObject)

# 병합 정렬

## 기본 개념

### 그림: 정렬을 마친 배열의 병합

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/57d32329-254c-46b7-85eb-6c7905b86749/IMG_9897.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=f4fa25ad27b646c01735134e4067da6dd7e7b23b1d8bd56d3cb6356aa3e9b501&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 해당 그림을 구현한 코드

```python
from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence):
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소 수

    while pa < na and pb < nb: # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pa]:
            c[pc] = a[pa]
            pa += 1
        else:
            pb += 1
    # 떨이요~ 떨이
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    # 떨이요~ 떨이
    while pb < na:
        c[pc] = a[pb]
        pb += 1
        pc += 1


   
```

이 내용은 사실 쉬워서 더 볼 필요 없을 거 같다.

### 그림: 병합 정렬하는 방법

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/6b5838ad-1623-41fc-93d6-ddd0d95255a5/IMG_9898.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=928ee4a96d43f7e432f523320a07de7f6ff2da12837f4a898485c14de140453d&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 병합정렬

```python
from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합정렬
            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[i] <= a[i]
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1) # 배열 전체를 병합 정렬.
    del buff

```

# 힙 정렬

## 기본 개념

### 그림: 힙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/00b0f9c1-8f4e-4d1b-9d3f-b94d9a18d4bc/IMG_9890.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=f24c0a14affe500cfa8e614c16242a6e90cfc8979405da62e56597fdd757fdf8&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 루트노드 삭제하고 힙 업데이트 하는 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/fc323225-8952-40bd-af97-788fef3539bb/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=eda5606ecab97da7633a6e59d9469384a462a34d6a8c0238be832a8b482a5a0a&X-Amz-SignedHeaders=host&x-id=GetObject)

큰 값을 가진 자식과 위치를 교환. (이하 생략)

### 순서: 힙 정렬 알고리즘

1. 힙의 루트 a[0]에 위치한 최댓값 10을 꺼내 배열의 맨 끝 원소인 a[9]와 교환합니다.
1. 최댓값을 a[9]로 이동하면 a[9]는 정렬을 마칩니다. 앞에서 살펴본 순서대로 a[0] ~ a[8]의 원소를 힙으로 만듭니다. 그 결과 두 번째로 큰 값인  9가 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값 9를 꺼내 아직 정렬하지 않은 부분의 맨 끝 원소인 a[8]과 교환합니다.
1. 두 번째로 큰 값을 a[8]로 이동한 결과 a[8]~a[9]가 정렬을 마칩니다. 앞의 단계와 마찬가지로 a[0]~a[7]의 원소를 힙으로 만듭니다. 그 결과 세 번째로 큰 값인 8이 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값을 꺼내 아직 정렬하지 않은 맨 끝 원소인 a[7]과 교환합니다.
1. 이 과정을 반복하면 배열의 맨 끝에 최댓값부터 순서대로 하나씩 저장됩니다.
### 그림: 힙 정렬 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/45579a74-22f3-44cc-9040-cfe92f1e407b/IMG_9892.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=2c141eb547bbe8f69eed49b9df0f19462d79c36c0c82e2f372fc180e903b86c9&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/9d650163-c6f4-4f18-9b53-13a425a25ccc/IMG_9893.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=c0d7b889659c2f2cca43699f4d4645e366e770750e3cacb6a24d4c7220881ff0&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: A는 힙이 아니고 B, C는 힙이다

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/472ae03c-8298-4ea1-8357-fecc60bf247c/IMG_9894.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=8ce800fa40d9042fd61b780651c6b6e6181a1ee274910d2316f943c0bf890f21&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 정렬되지 않은 서브트리를 힙으로 만드는 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/f318a344-9231-4017-a950-59930627a59d/IMG_9895.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=5941159140681ce77153ff6f938184a1e506e4d31cff9a883c2d89473a7247bb&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/0c24fd7b-146e-486d-826a-a3479c2988eb/IMG_9896.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=3070f0e8103a1891e1a78356ee0ea68869e2f4eeb793f3a9a9a03f137b7ad636&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 힙 정렬

> 힙은 사실 그렇게 복잡하지 않다. 솔루션에 모듈이 많아서 복잡해 보이는 거지.

```python
from typing import MutableSequence

def heap_sort(a: MutableSequence):

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left] # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl # choose larger child
            if temp >= a[child]:
                break 
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)
    
    
    for i in range((n - 1) // 2, -1, -1): # a[i] ~ a[n-1]을 힙으로 만들기 
        down_heap(a, i, n - 1) # 밑에서부터 차례대로 올라가며 힙으로 만드는 과정.


    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] # 최댓값인 a[0]과 마지막 원소를 교환
        down_heap(a, 0, i - 1) # a[0] ~ a[i-1]을 힙으로 만들기
```

> 머리가~ 안 돌아~ 가서~ 주석을~ 포함한~ 코드를~ 필사하세요! 

### 코드설명

- down_heap(): 배열 a에서 a[left] ~ a[right] 원소를 힙으로 만듭니다. a[left] 이외에는 모두 힙 상태라고 가정하고 a[left]를 아랫부분의 알맞은 위치로 옮겨 힙 상태를 만듭니다.
- 궁금증: 그럼 a[right]는 어떻게 힙 정렬을 하나요?
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/fc323225-8952-40bd-af97-788fef3539bb/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=eda5606ecab97da7633a6e59d9469384a462a34d6a8c0238be832a8b482a5a0a&X-Amz-SignedHeaders=host&x-id=GetObject)

- heap_sort()함수
  - 원소 수가 n인 배열 a를 힙 정렬하는 함수입니다. 다음과 같이 2단계로 구성됩니다.
  - 1단계: down_heap() 함수를 호출하여 배열 a를 힙으로 만듭니다.
  - 2단계: 최댓값인 루트 a[0]을 꺼내 배열의 마지막 원소와 교환하고, 배열의 남은 부분을 다시 힙으로 만드는 과정을 반복하여 정렬을 수행합니다.
## 힙 정렬의 시간 복잡도

이 부분 내용은 좀 부실함. 다른 교재를 참고하여 정리할 것.

# 도수 정렬

## 기본 개념

### 그림: 도수분포표 작성

그냥 간단함. 주어진 값의 최대값을 크기로 하는 배열을 만들고 각 값을 인덱스로 해당 칸을 1 더하면 됨.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/5b251fbd-b065-4d1d-b407-40139302c8f6/IMG_9886.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=7b7b73301c7a0e3f8d6e228506e1411e131151ba512a9363f4fb176e02e59608&X-Amz-SignedHeaders=host&x-id=GetObject)

이에 대한 Prefix Sum 배열을 구하면 누적 도수 분포표를 구할 수 있음. 이를 통해 작업용 배열을 만들면 되는데, 아래와 같음

### 그림: 작업용 배열 만들기

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/80e796a5-1525-403e-a91f-6acd21d88998/IMG_9887.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=b689e5a32134d760a3d8c8c696f06df80612ca271369a730bcacd14b156ad01a&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 위 그림을 수행하는 코드

```python
for i in range(n - 1, -1 ,-1):
	f[a[i]] -= 1
	b[f[a[i]]] = a[i]
```

### 그림: 작업용 배열 만들기 2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/c8614daa-8dc9-4387-89eb-14e313f8a985/IMG_9888.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=66a0dc411b61734c815ffa654d27a7a55a0ccf2863f7ada116d4acaaf31c80e0&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 작업용 배열 만들기 3

f 테이블의 요소 값을 줄여주는 덕분에 중복 값이 알아서 잘 처리되는 모습을 볼 수 있다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b158ccf2-c130-4f6e-a389-4c06d1997a13/_.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNAVHNUP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICECupT9KZJ695oCUPGsx4sWl3VnxXbT3YZqpRw02apPAiAjlTxIahwL5NbnGl%2FXMRbLvSPnM9H9mR513dbX5x%2BdIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMj0AKPD7LUpGyqGOZKtwDDCxCi0LPQEpyBa8hrdpICNmU%2BhbZl45ulAY3FN5iftWOEjsVI1l9O4GN8MyecGACYNwRwJazzFh9Wz6ouPeMbIBIMDjpseXpj%2BwOfO4l1mOedoed46MpKVqOOIwx5gW1cY1yXopa%2B4HYeqjCyOLICUR7nkdKd%2BgJrxNe476%2FNwhrUduSPpwY3c4RhTUNixK8X7Un31jGKdHkIfVRrlIgQB61pwuCX5rm2X6tyX287S%2B1WXgRi%2B%2BIsee%2F3aY52ZWec91P%2BvHjCq4oUovaP%2F6zwjZ0bGzKnC9xtgeqLwKTwgu1CNi1pq6K97gEwNlLMW8bABZ%2BwsUfX%2FAT7bU5EOq9TZ8X71ky%2FrrfylwgxHzAYcnfcDreSiPW2M44%2BzJEDQ6eoekdE%2BGZTBIo1beKQsA5wZMKymEtKquz%2B1SHE36Am%2FfgMgOGWzmekJLCi20Cv7mzc8uSkrWWbCmInlA6NPqlWBLK2Lf26ShJ7p6C9mYuQoXvBp4fRI5KZbM%2FMc%2FTn7WoVF2m0JbzKKVIM%2FRI3Dd%2BqYg21wajrW6JY4TL1TnaSCf38%2B3T8jvgxAeq7ymiCYwvrVWKTJNdkG1pJH%2BMqIesxJD3EPFu%2BUheFaTkXIXaJEoV8zRz25GKw4xZ23ww1YHYvgY6pgFUw4zL1Lf3KxOUpe7QBALA0%2FAOcAXHe5SA9rBNHIzN%2Bvb%2FFlTHrIGeFLKcihWg3tY3dmVRD%2Frn%2BmcM6%2Fp6oQXvkXcoGCyN%2FUSPdS8VQTxV7r2ruFs0Ovi%2Foxjt42WQgVeaf1aiXZ0X0DzWrmGw0j0NpvuwXmtc6VXeFKhda7tX4b%2B76YbW23c1OtpFo%2BxQ8AnbO5RyBKfPU6sLgfe8ZuPD7JnTsdcz&X-Amz-Signature=f7a21e1ec443a06b66cfd436365b5f4f194bf08929274d80fe78dac4e95004e6&X-Amz-SignedHeaders=host&x-id=GetObject)

거꾸로 하자. 너무 지루하고 그러니까.

그리고 일단 이 내용 정리한 다음 정렬은 마무리하자.





