# [DL] Tensorflow metal



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# Tensorflow 환경 구축

## 1. 3.9.x 파이썬 가상환경 설정 및 설치

```python
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
```

## 2. verify

### 코드

```python
import tensorflow as tf

cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()
model = tf.keras.applications.ResNet50(
    include_top=True,
    weights=None,
    input_shape=(32, 32, 3),
    classes=100,)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64)
```

### 설명

아래 코드는 TensorFlow와 Keras를 이용해서 CIFAR-100 데이터셋을 다운로드하고, ResNet50 모델을 처음부터(랜덤 초기화) 학습하는 예시입니다. 각 부분을 단계별로 설명하면 다음과 같습니다:

1. 패키지 임포트

```plain text
import tensorflow as tf
```

•	tensorflow 라이브러리를 불러옵니다.

2. 데이터셋 준비

```plain text
cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()
```

•	CIFAR-100 데이터셋을 불러옵니다.

•	x_train과 y_train은 학습용(트레이닝) 이미지와 레이블,

x_test와 y_test는 테스트용 이미지와 레이블을 의미합니다.

•	CIFAR-100은 32×32 크기의 컬러 이미지 60,000장(훈련 50,000장, 테스트 10,000장)으로 이루어지며, 100개의 클래스로 구성된 데이터셋입니다.

3. 모델 정의 (ResNet50)

```plain text
model = tf.keras.applications.ResNet50(
    include_top=True,
    weights=None,
    input_shape=(32, 32, 3),
    classes=100,
)
```

•	ResNet50 아키텍처를 tf.keras.applications.ResNet50로부터 가져옵니다.

•	주요 인자들:

•	include_top=True: 최종 분류 레이어(fully-connected layer)까지 포함한 구조를 사용

•	weights=None: ImageNet 등 사전 학습 가중치를 사용하지 않고, 처음부터 랜덤 초기화한다는 의미

•	input_shape=(32, 32, 3): CIFAR-100 이미지가 32×32 크기의 RGB 이미지이므로 입력 크기를 이렇게 지정

•	classes=100: CIFAR-100은 100개 클래스로 구성되어 있으므로 최종 출력 노드 수도 100개로 설정

주의: 일반적으로 ResNet50은 224×224 사이즈 입력으로 사전 학습된 모델을 많이 사용하는데, 여기서는 CIFAR-100에 맞춰 직접 32×32로 학습시키고 있습니다.

4. 모델 컴파일

```plain text
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
```

•	손실 함수(loss_fn): SparseCategoricalCrossentropy

•	Sparse 버전이므로, 원-핫 벡터가 아니라 정수 형태의 클래스 레이블(예: 0~99)을 직접 사용.

•	from_logits=False는 모델 출력이 이미 확률(softmax)이기 때문에 로짓 값으로 해석하지 않는다는 설정입니다.

•	최적화 함수: Adam

•	모델 평가지표: accuracy

5. 모델 학습

```plain text
model.fit(x_train, y_train, epochs=5, batch_size=64)
```

•	데이터셋(x_train, y_train)을 이용해 5 에폭(epoch) 동안 학습을 진행합니다.

•	batch_size=64는 한 번의 파라미터 업데이트마다 64개의 샘플을 묶어서 학습하겠다는 의미입니다.

•	학습 도중에 훈련 진행 상황(손실, 정확도)이 로그로 출력됩니다.

요약

1.	CIFAR-100 데이터셋(32×32, 100 클래스)을 불러옵니다.

2.	ResNet50 모델을 사전 학습 없이(가중치 초기화), 입력 크기 32×32로 정의합니다.

3.	Adam 옵티마이저와 SparseCategoricalCrossentropy 손실을 사용해 모델을 컴파일합니다.

4.	5 에폭 동안, 배치 크기 64로 모델을 학습하여 CIFAR-100 분류 모델을 훈련합니다.

위 코드는 ResNet50을 간단히 CIFAR-100에 적용하는 예시이며,

추가적으로 데이터 전처리, 정규화, 학습률 스케줄링 등을 설정하면 더 나은 성능을 기대할 수 있습니다.

### 실행 결과

학습 데이터 다운로드

![](./images/Screenshot_2025-03-03_at_11.04.07_PM.png)

![](./images/Screenshot_2025-03-03_at_11.04.07_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHJAAK2X%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIA5vDld8XoYCK1PiUL4hB%2BMyvjCDXL4DWNWBvoZOt8hXAiEAyzeXyrnnB5aY7y0IsZHd0%2BwLXNfK654FFW5NZeKKHPYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJUZ6CyNgtb5IYVP3SrcAzbZcEpZbFbCn5fggFe%2F81JVUEdboNAy36BZq49uEN9jPoN9ikiaMMa%2BVZR5nx%2FzxC1zlvQ3DgH2v5yVjl36kBTmdRbA%2FXyN68Jpezmjt5uePebykzl1YPmJUF8b1EOKTIegvesX1V6jRaeSpVwijALANHH6LGoATkauiwFXudsf%2FOiIcW6TndgS4MaWIb0RT6RrEWacMUYyS%2FmfMp1zn%2BG0TlgQX%2BXGLxFpUO5dD0RR8I047rqwYLQPQSpdzI1xOjF%2BvF9qqBavx4GYGa0jdbQblfHGgoTDkVthDozj9ep3jPXSKbye6uzQTTH7gpeoLsuLUGL8kVRyJzaNU4h5WLXV1J4Mt9bzlT7Q0AsduhR0NUyksq43wndJ%2BJzoUttrLCZlNkmngmJ3ClBkvZHbarlc5vLzxpb0RjxWCiO9PEN1kqcqqrJu7TTw0jTH5XfpU6qb44TuQd7OpQjeuJfJ3XWAQOHZJG3WNYnNwh1Ej5koa%2FmqFh1skfkQI2IDLAspH%2FKg02My6BDUepYOQcMddU0tyLa6q91pwdzvoygptUXOCMgO%2FqePazaVQrQ2I%2FLo03zw7nLdBXHZQ2QYWPTnIIbogMvL7lkX8zsvnCocIHtAVEDpYeoQ%2Bt3cBiG6MJ2x574GOqUBzQE3qt4Emeo3LmBdvb%2FcAkV4eM0YfisD%2FTYHymrQWBN6P2jigkVL%2BJkTI%2BJGtPiFI%2FD4yezjS7ElDG0ur0Kz45jZGl%2Fs%2BWprRnuBNDErmuhvRtmZoUMh0EoyK%2Bwjviije6vonxls%2FU%2BhohhEdqinghdj%2BqFQxz6hfMsZoG03rdNmHIjz7ABhvR75%2BYvhXTV8PtC3cgB2Qb2%2FzQ3nfXQqGirFntxC&X-Amz-Signature=2c17c9149f0a52eb17b87fae85940a86c2328b4adf69e954f631e5967c33e267&X-Amz-SignedHeaders=host&x-id=GetObject)

metal plug in 실행 확인 및 학습 진행

![](./images/Screenshot_2025-03-03_at_11.08.27_PM.png)

![](./images/Screenshot_2025-03-03_at_11.08.27_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHJAAK2X%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIA5vDld8XoYCK1PiUL4hB%2BMyvjCDXL4DWNWBvoZOt8hXAiEAyzeXyrnnB5aY7y0IsZHd0%2BwLXNfK654FFW5NZeKKHPYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJUZ6CyNgtb5IYVP3SrcAzbZcEpZbFbCn5fggFe%2F81JVUEdboNAy36BZq49uEN9jPoN9ikiaMMa%2BVZR5nx%2FzxC1zlvQ3DgH2v5yVjl36kBTmdRbA%2FXyN68Jpezmjt5uePebykzl1YPmJUF8b1EOKTIegvesX1V6jRaeSpVwijALANHH6LGoATkauiwFXudsf%2FOiIcW6TndgS4MaWIb0RT6RrEWacMUYyS%2FmfMp1zn%2BG0TlgQX%2BXGLxFpUO5dD0RR8I047rqwYLQPQSpdzI1xOjF%2BvF9qqBavx4GYGa0jdbQblfHGgoTDkVthDozj9ep3jPXSKbye6uzQTTH7gpeoLsuLUGL8kVRyJzaNU4h5WLXV1J4Mt9bzlT7Q0AsduhR0NUyksq43wndJ%2BJzoUttrLCZlNkmngmJ3ClBkvZHbarlc5vLzxpb0RjxWCiO9PEN1kqcqqrJu7TTw0jTH5XfpU6qb44TuQd7OpQjeuJfJ3XWAQOHZJG3WNYnNwh1Ej5koa%2FmqFh1skfkQI2IDLAspH%2FKg02My6BDUepYOQcMddU0tyLa6q91pwdzvoygptUXOCMgO%2FqePazaVQrQ2I%2FLo03zw7nLdBXHZQ2QYWPTnIIbogMvL7lkX8zsvnCocIHtAVEDpYeoQ%2Bt3cBiG6MJ2x574GOqUBzQE3qt4Emeo3LmBdvb%2FcAkV4eM0YfisD%2FTYHymrQWBN6P2jigkVL%2BJkTI%2BJGtPiFI%2FD4yezjS7ElDG0ur0Kz45jZGl%2Fs%2BWprRnuBNDErmuhvRtmZoUMh0EoyK%2Bwjviije6vonxls%2FU%2BhohhEdqinghdj%2BqFQxz6hfMsZoG03rdNmHIjz7ABhvR75%2BYvhXTV8PtC3cgB2Qb2%2FzQ3nfXQqGirFntxC&X-Amz-Signature=d3b2b4b562725536e6d55a9165ab6b672aed7761d22a32f7f08c4ff3a2219626&X-Amz-SignedHeaders=host&x-id=GetObject)

# 이슈: pyenv에 tensorflow 설치가 안 됨

## Phase1

환경: macOS, M1, python virtual env, 

로그: 

ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow

최근 변경사항: 가상환경에서  python -m pip install tensorflow 실행

## Phase2-1

확인: Apple Silicon(M1) 환경에 맞춰 빌드된 공식 tensorflow 패키지가 PyPI에 존재하지 않기 때문. PyPI에서는 일반적인 tensorflow 대신 tensorflow-macos 패키지를 설치

시도: pip install tensorflow-macos

결과분석:

ERROR: Could not find a version that satisfies the requirement tensorflow-macos (from versions: none)
ERROR: No matching distribution found for tensorflow-macos

## Phase2-2: 해결

확인: Python 버전이 Apple Silicon용 TensorFlow에서 지원하지 않는 버전일 때 (예: Python 3.11처럼 아직 호환 Wheel이 없는 경우, 혹은 3.7 이하인 경우 등) tensorflow가 PyPI에 없을 수 있음.

시도: 파이썬 버전 3.9로 가상환경 생성

결과분석: 잘 설치 됨.



