# [DL] 밑바닥부터 배우는 딥러닝



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# Two Layer Net

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        
        return x
        
    # x : 입력 데이터, t : 정답 레이블
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x : 입력 데이터, t : 정답 레이블
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads
        
    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

        return grads

```





# 챕터: 학습 관련 기술들

> 해당 챕터는 개념 중심이라 타이틀, 개념, 예시, 코멘트 형식으로 작성할 것.

## SGD(stochastic gradient descent) 개념

개념: SGD란 매개 변수의 기울기를 이용해서 기울어진 방향으로 매개변수 값을 갱신하는 일을 몇 번이고 반복해서 점점 최적의 값에 다다르는 것. 매개변수 갱신 방법이다.

$$
W \leftarrow W - \eta \frac{\sigma L}{\sigma W}
$$

$\frac{\eta L}{\eta W}$: W에 대한 손실 함수의 기울기.

← : 우변의 값으로 좌변의 값을 갱신한다는 뜻. 

$\eta$: 학습률

```python
class SGD:
	def __init__(self, lr=0.01):
		self.lr = lr
	def update(self, params, grads):
		for key in params.keys():
			params[key] -= self.lr * grads[key]
```

- lr: learning rate
> SGD 클래스를 사용하면 신경망 매개변수의 진행을 다음과 같이 수행할 수 있다.

```python
network = TwoLayerNet(...)
optimizer = SGD()

for i in range(10000):
	...
	x_batch, t_batch = get_mini_batch(...) # mini batch
	grads = network.gradient(x_batch, t_batch)
	params = network.params
	optimizer.update(params, grads)
```

## SGD의 단점

주어진 로스 함수가 다음과 같다고 하자. 

$$
f(x, y) = \frac{1}{20}x^2 + y^2
$$

그러면 기울기는 아래와 같이 x값을 매우 더디게 갱신하는 형태가 된다. 아마 x 매개변수 갱신이 y보다 10배쯤 느리지 않을까? 

### GPT의 설명

SGD(Stochastic Gradient Descent)의 단점 중 하나는 매개변수 갱신 속도의 불균형인데, 주어진 로스 함수에서 이를 확인할 수 있습니다.

1. 기울기 계산

2. SGD 업데이트 식

$$
x_{t+1} = x_t - \eta \frac{\partial f}{\partial x} = x_t - \eta \frac{1}{10} x_t
$$

$$
y_{t+1} = y_t - \eta \frac{\partial f}{\partial y} = y_t - 2\eta y_t
$$

즉, x는 $\eta/10$만큼 변화하고, y는 $2\eta$만큼 변화합니다.

3. 갱신 속도의 차이

비교해보면 y에 대한 갱신이 x에 대한 갱신보다 10배 빠르다는 것을 확인할 수 있습니다.

즉, 기울기가 작은 방향(이 경우 x 방향)으로는 갱신이 매우 느려지는 문제가 발생합니다.



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/3c536962-c9d4-4af6-b261-82125e201ebf/Screenshot_2025-03-06_at_3.17.51_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWR2XV4J%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T002759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzSUB8Igu4jKsMkri1sNgIPBFNnYF%2FpcVRZ5WvNuFyTAiEAuW%2B1JZnZVAZnbjt3krJrOPxDDorTWKOw6Q7%2BRTWaRKsqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMBlCdTYSGX9Y4nOxSrcA8ccAay%2BJwsC8fIGQUc1KXundV%2ByAMByOg90SmD29S81yZCltsa7QEuyF86GOjUz11PL29xRu%2FjXoC%2FwJxIMm4QUqC%2BxLA8Ng84eFm9bO0g1dDfrzxifFkGGDq3eUJ1HbwjvSAWh1ttKJwQHDr9wIGmdIkBAohVwLCBpWvNqynZugOCdt1%2BkDQ8MEyW8AURFF3UJgr9gCF8R44cf0dBS3oF141luHcndsVdE7M5IphHlCTdv5ltFa80ZNqJJYPX7CS9RfrfnoqihnPaV8yy%2Bj8AjMw7gTEZKePEcTpheohrEVthFP6OmuumjyJ5QrBpe4ZikUlSm1cNh4WiKOA6nYN2uKPKy7zRZWZpO110c%2BYlVS1IDO2snDbfe5e55BYc20L45qwYAVhYYQK75uUblBeevaNRYqGhdu1utUkACwWTtmO94oYQxZ%2BF5NOTKxHeSEWKCXuclDPdIcM5vGAAD9nlgBhDRmAPqP3bkkE5SLMas%2BRcKaoGN5ScOoufjDrCKpXqFS0pSF9h0pT6rC5njhq6ldyNZPgvClEBuJ0wWWtCupS6z0ePV6YvM4I4ptyFtEDtO1SMGujEYpwLLNMel0PjF%2Fy1QirgT%2B33%2Fv5omidnm4LsTSp0Z7e5qLRm5MKzuzb4GOqUB43PkG0ym5fGHie2MkD76mbqhtGqAne7I9codjME2jpLNK5Fo83SmdNyEhZ7rXD%2BpYQujm39ZtXDXsPLH5%2Fslr6s%2F4rdYjlxrh5tKizBGEPi3AzgP1xCFjLNHigN%2BrGzd169JoWCa%2FYuYnHtWLLUMm2k7RoHXfcZ09iq8ynHObTDPyJ2otG%2FezVkDB4DUOzu2rLjVXmpEw9aumATq1iTIcfepZicm&X-Amz-Signature=d734e10ea2356509139024e645b1aced502ef96b246a328dec79b35539b074f1&X-Amz-SignedHeaders=host&x-id=GetObject)

## SGD의 대안: 모멘텀

### 수식

$$
v \leftarrow av - \eta \frac{\sigma L}{\sigma W}
$$

$$
W \leftarrow W + v
$$

v라는 변수가 새로 나오는데, 이는 물리에서 말하는 속도에 해당함. av항은 물체가 아무런 힘을 받지 않을 때 서서히 하강시키는 역할을 함. (a = 0.9 등으로 설정. 중력 가속도랑 같은 건가? 아니다. 반대로 속도를 줄이는 저항의 역할이다.) 물리에서의 지면 마찰이나 공기 저항에 해당하는 개념. (즉 하강 속도를 줄이는 항이다.)

### 코드

```python
class Momentum:
	def __init__(self, lr=0.01, momentum=0.9):
		self.lr = lr
		self.momentum = momentum
		self.v = None 
	
	def update(self, params, grads):
		if self.v is None:
			self.v = {}
			for key, val in params.items():
				self.v[key] = np.zeros_like(val)
			
		for key in params.keys():
			self.v[key] = self.momentum*self.v[key] - self.lr*grads[key]
			params[key] += self.v[key]
```

이를 통해 최적화를 하게 되면 최적화 갱신이 SGD의 지그재그 모양 대신 완만한 곡선을 그리며 진행된다.

> 모멘텀의 갱신 경로는 공이 그릇 바닥을 구르듯 움직입니다. 이는 x축의 힘은 아주 작지만 방향은 변하지 않아서 한 방향으로 일정하게 가속하기 때문입니다.(기울기가 일정하면 갈수록 미끄러지는 속도가 빨라지는 당연한 현상). 거꾸로 y축의 힘은 크지만 위아래로 번갈아 받아서 상충하여 y축 방향의 속도는 안정적이지 않습니다. 전체적으로는 SGD보다 x축 방향으로 빠르게 다가가 지그재그 움직임이 줄어들게 됩니다.(물론 y축 갱신이 조금 느려지는 trade-off가 있다.)

## AdaGrad

신경망 학습에서는 당연히 학습률이 아주 중요한데, 이 값을 일정하게 유지하는 대신 학습 진행 상황에 따라 줄여나가는 기법이 있다. 이를 학습률 감소(learning rate decay)라고 한다. 처음에는 크게 학습하다가 조금씩 작게.

학습률을 서서히 낮추는 가장 간단한 방식은 당연히 ‘전체’의 학습률 값을 일괄적으로 낮추는 것이겠죠? 

```python
	for key in params.keys():
		params[key] -= self.lr * grads[key]
```

여기서 self.lr을 그냥 확 줄여버려서 모든 파라메터 갱신 정도를 낮추는 것.  

이보다 유식한 방법이 바로 AdaGrad이다. 

### 수식

$$
h \leftarrow h + \frac{\sigma L}{\sigma W} \odot \frac{\sigma L}{\sigma W}
$$

$$
W \leftarrow W - \eta \frac{1}{\sqrt h}\frac{\sigma L}{\sigma W}
$$

여기서 h라는 변수가 새로 등장. 기존 기울기값을 제곱하여 계속 더한 값. 글고 매개변수를 갱신할 때 $\frac{1}{\sqrt h}$를 곱해서 학습률을 조정. 이게 의미하는 바: 매개변수의 원소 중에서 많이 움직인(크게 갱신된) 원소는 학습률이 낮아진다는 뜻. h는 기울기에 비례, $\frac{1}{\sqrt h}$는 기울기에 당연히 반비례하므로, 기울기를 통해 크게 갱신되고 나면 다음 학습률을 낮추는 효과가 있음.

### 코드

```python
class AdaGrad:
	def __init__(self, lr = 0.01):
		self.lr = lr
		self.h = None 
	
	def update(self, params, grads):
		if self.h is None:
			self.h = {}
			for key, val in parmas.items():
				self.h[key] = np.zeros_like(val)

		for key in params.keys():
			self.h[key] += grads[key] * grads[key]
			params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
```





