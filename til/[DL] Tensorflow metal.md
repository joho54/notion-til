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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/5f846457-bdb1-4d02-abc3-43007f914684/Screenshot_2025-03-03_at_11.04.07_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CZGMXTZ%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv0APEyi8%2FhWR3je6%2FdD0tSEO%2B4Em63G6ZWVb2GKaTewIgNOzS4PwGaDTaFGQgtFP%2FGzG5Yit4zeCOgeUwdF2CSAkq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDFHL2c0CX8GIvdanaSrcA10W5AIxBCTIj7VAba%2B0k%2FR%2BIgNNE2FpA2jJx1ySd5PcNF7NaHZEYcf0HberAD7CvP1nuSl8KkasbV0tuwCWffLpz5yHKT%2BOWFsdi3QYUQhiHIE28SqWUzXpS%2Bbp9nWQeIaIE5uvMopFq%2BGFGBjTZEhGQcEbGbnQz0JO9JIoWvvn%2Bktlg5zJII%2BXz71AM6dwOC7YbZLrJAl5kkGRG2dJgFPRFjLAaFIzfNn4in4dgTH%2B13mLLYC4foz99ljbTeaO0so1DV5gBjalBTgRw1GpMMRIyAiRGgUkVXSIxex2ys8493IDyjE7W3jTHQHN%2FmXLe%2BfuqS%2B0oxvD0tsgdaUW9THfLzkivgwvmVzRmjm96QhLyuTW8o3CTO1vbHorIXt6oQX4R%2FdhTlQTfDDR53AXGRR9ETjjwMoBe%2BKXFXQdknqIIJ27hn6mAPM2EYBrDlkKneExRUiR1m1bqhSGqIIO%2BgdiftKUIqJHs86EHbq%2Bzy2VMfMnBP5r50jDucItUTTk2cFUmTt%2BphZe%2F2tz25tVhlkMuYtBjUqI0zVnXMftOtUg5QGuBKHtTGGhHrF4hzteB7zQGGzSKpZ5GHIUI9PnmhO7JC0Llw0a6iHMi1M0HLJ0HREPuLdPeq66H%2BT%2FML3E1L4GOqUBFZTffE5wQXfGggyIDg%2FlcFUUIQvl2OcpmcdN%2BuPDsW8JxwIskKh0WpFpf1ztxeqJ15vABCsazZNdUGQMmTh%2FUlrD%2BypWzPl55AdAiiDiXtGKA7KSrjNqahfKSW1GUkkS7VfwkQaIJLITR0fPB5z1iuEByEKpd1a9kttmAMNEPR4Sd55ytcGteyHsasfDNmS4cMxoPo%2BXEHu0TbmAU1wMMXRmoDTa&X-Amz-Signature=d3f1994d5ccd4ba78f462641c9008b036d94f30100abbe232e3a2c3d2bb6df72&X-Amz-SignedHeaders=host&x-id=GetObject)

metal plug in 실행 확인 및 학습 진행

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/30e809d3-ade8-4866-ac41-fd1574d85dae/Screenshot_2025-03-03_at_11.08.27_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CZGMXTZ%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv0APEyi8%2FhWR3je6%2FdD0tSEO%2B4Em63G6ZWVb2GKaTewIgNOzS4PwGaDTaFGQgtFP%2FGzG5Yit4zeCOgeUwdF2CSAkq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDFHL2c0CX8GIvdanaSrcA10W5AIxBCTIj7VAba%2B0k%2FR%2BIgNNE2FpA2jJx1ySd5PcNF7NaHZEYcf0HberAD7CvP1nuSl8KkasbV0tuwCWffLpz5yHKT%2BOWFsdi3QYUQhiHIE28SqWUzXpS%2Bbp9nWQeIaIE5uvMopFq%2BGFGBjTZEhGQcEbGbnQz0JO9JIoWvvn%2Bktlg5zJII%2BXz71AM6dwOC7YbZLrJAl5kkGRG2dJgFPRFjLAaFIzfNn4in4dgTH%2B13mLLYC4foz99ljbTeaO0so1DV5gBjalBTgRw1GpMMRIyAiRGgUkVXSIxex2ys8493IDyjE7W3jTHQHN%2FmXLe%2BfuqS%2B0oxvD0tsgdaUW9THfLzkivgwvmVzRmjm96QhLyuTW8o3CTO1vbHorIXt6oQX4R%2FdhTlQTfDDR53AXGRR9ETjjwMoBe%2BKXFXQdknqIIJ27hn6mAPM2EYBrDlkKneExRUiR1m1bqhSGqIIO%2BgdiftKUIqJHs86EHbq%2Bzy2VMfMnBP5r50jDucItUTTk2cFUmTt%2BphZe%2F2tz25tVhlkMuYtBjUqI0zVnXMftOtUg5QGuBKHtTGGhHrF4hzteB7zQGGzSKpZ5GHIUI9PnmhO7JC0Llw0a6iHMi1M0HLJ0HREPuLdPeq66H%2BT%2FML3E1L4GOqUBFZTffE5wQXfGggyIDg%2FlcFUUIQvl2OcpmcdN%2BuPDsW8JxwIskKh0WpFpf1ztxeqJ15vABCsazZNdUGQMmTh%2FUlrD%2BypWzPl55AdAiiDiXtGKA7KSrjNqahfKSW1GUkkS7VfwkQaIJLITR0fPB5z1iuEByEKpd1a9kttmAMNEPR4Sd55ytcGteyHsasfDNmS4cMxoPo%2BXEHu0TbmAU1wMMXRmoDTa&X-Amz-Signature=775bd6c5e6179ebc5ac6dc6030b1d7766a74f6d3776724ffddfd97e8cfac08ae&X-Amz-SignedHeaders=host&x-id=GetObject)

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



