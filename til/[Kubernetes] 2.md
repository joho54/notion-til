# [Kubernetes] 2

> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

# 탑다운1: 사이드카 패턴

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/d29f4c4a-e84b-4f54-9826-a32ff87330b8/IMG_0415.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXPQVLJQ%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAKwTW61PuNRX8p4MMBdHDnLR4Wb9JHoBEictQ0PwjeeAiAY%2F91OK%2F4vuBlZAP7Mm%2F3eBXHv4Iknt0iKAZCAqPnlOyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiJ0CVMuFejgVQOHAKtwDJlsORvLgtqmWiYYuBbI54oJzThIwTL6Ef3PPTSkyQtIdv7FKZuzAXDkwxkvgzWVE92Rwrz3h0AP084ytHYEATGUdD1QhUEw0o6PDfppRTXtSx5wC97GyGVX8iHZmuxyz9IgTnbAhVAmauCjwlasCr8G009xB8T3M6caVqL5TQddH1xNNtgCx7W6q4kIN%2BNUOngQHyJYhGT3vLwyb9dYppCBuM0H4%2FlW31o%2FKdU2XSDWoga5FDRf0ACobeqqiP36xoyb8%2BmYKcTJEI7QjXoVSIBnnrCDmqzdzXQqlC5%2BkzcMbL9tDDoBrE7EIyggiSy5F253kY8NII5Pb3V%2Bqsqii7Mn06MwA0T5P9OGP6C%2BV1hRXnjcIvlgs1XJax%2BsVH%2FThPDalpgY2uy%2FyOi1x6WBEWHWS3rvlC%2B2fZX6V1utZwkYqAx4ZZTPk6CJfuVqyvk2NFlhrIhspkL2o0J00ogZYBJryWjZEgPNbHRRIhnvXa4Cmzx5v6MuWwP%2FzxofQFCDypTzKH6Ymi498Gqu0z0gQxYfM79dyNx%2FHtciOH90cB7btc2IRbrL3hOoNhoi0i%2B3hbITo5%2F4SuM6Z1T4MlCn5h%2FFIkegHAz0X8c%2Bx2MXnV7vTjnRWPI1M1x7HLxowjO7NvgY6pgHqPpKIg%2FKheGFHZQQX4TxK21cJ7N9eKzah%2B1wu%2BR5ag4iMR9ZwRPbP1wVUseM1wRA9ek8IwR4EngyMQ7WFybjEkD1NhQ3H%2Fw5Vzkq2JIv5psJ4WCgCSbV4iT4y1tpJyOrX2fgdHYndTOzWtMjw5KwEJAA0ZlPs3h9b5eTjXG1XYy1%2BzKqf31UL4vs6ZrY6ni9pILvM468WU3igsgfU7VH%2FwBJuVNih&X-Amz-Signature=dd795bbdb92177fddf27d5ed8abf99d2177d92dc0ba18c5a7b2d4fe28bab5b1e&X-Amz-SignedHeaders=host&x-id=GetObject)

## nginx-sidecar.yml

```markdown
vapiVersion: v1
kind: Pod
metadata:
  name: nginx-busybox-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    volumeMounts:
    - mountPath: /var/log/nginx
      name: log-volume

  - name: busybox
    image: busybox:latest
    command: ["/bin/sh", "-c", "while true; do wget -qO- http://localhost:80; sleep 10; done"]
    volumeMounts:
    - mountPath: /var/log/nginx
      name: log-volume

  - name: log-checker
    image: busybox:latest
    command: ["/bin/sh", "-c", "tail -f /var/log/nginx/access.log"]
    volumeMounts:
    - mountPath: /var/log/nginx
      name: log-volume

  volumes:
  - name: log-volume
    emptyDir: {}

```

코드 설명

이 구성은 nginx 웹 서버의 로그를 다른 컨테이너와 공유하여,

•	nginx: 실제 웹 서버 역할을 수행하며 로그를 기록

•	busybox: 주기적으로 웹 서버에 요청을 보내 로그를 생성

•	log-checker: 실시간으로 로그 파일을 모니터링하는 역할

를 동시에 수행함으로써, 하나의 Pod 내에서 통합된 로그 모니터링 및 서비스 동작을 확인할 수 있도록 설계되어 있습니다.

```markdown
command:
        [
          "/bin/sh",
          "-c",
          "while true; do wget -qO- http://localhost:80; sleep 10; done",
        ]
```

이 커맨드는 BusyBox 컨테이너가 수행하는 명령어지만, “로그 수집”을 직접 하는 것이 아니라 nginx 서버에 반복적으로 요청을 보내서 로그가 생성되도록 하는 역할을 해요.

구체적으로 설명하면:

•	/bin/sh -c는 셸을 통해 다음 명령어를 실행합니다.

•	while true; do wget -qO- http://localhost:80; sleep 10; done

•	while true: 무한 루프로 계속 실행합니다.

•	wget -qO- http://localhost:80: wget을 사용하여 http://localhost:80 에 GET 요청을 보내고, 결과를 표준 출력으로 출력합니다. -q 옵션은 출력 메시지를 최소화하며, -O-는 파일 대신 결과를 출력합니다.

•	sleep 10: 10초 간격으로 요청을 반복합니다.

이 명령은 nginx 컨테이너가 제공하는 웹 페이지에 주기적으로 접근함으로써, nginx 컨테이너의 /var/log/nginx 경로에 로그가 남도록 유도합니다.

그리고 별도의 log-checker 컨테이너가 이 로그 파일을 모니터링하도록 설정되어 있습니다.

## 테스트

```markdown
kubectl apply -f nginx-sidecar.yml
kubectl get pod
kubectl logs -f nginx-busybox-pod -c log-checker
```

- kubectl logs: Pod의 로그를 출력하는 기본 명령어입니다.
- -f (or –follow): 로그를 실시간으로 계속 출력하도록 하는 옵션입니다. 로그가 추가될 때마다 터미널에 업데이트되어 출력됩니다. 
- nginx-busybox-pod: 로그를 조회할 대상 Pod의 이름입니다. 
- -c log-checker: Pod 내에 여러 컨테이너가 있는 경우, 특정 컨테이너의 로그를 선택하기 위한 옵션입니다. 여기서는 log-checker라는 이름의 컨테이너를 지정합니다.
# 의문: BusyBox가 뭐야?

BusyBox는 경량화된 유닉스 도구 모음으로, 여러 기본적인 명령어들을 하나의 실행 파일로 제공하는 소프트웨어입니다. 주로 다음과 같은 특징을 가지고 있어요:

•	소형 및 경량화:

BusyBox는 제한된 리소스 환경(임베디드 시스템 등)에서 사용하기 적합하도록 설계되어 있어, 일반적인 리눅스 배포판에 포함된 많은 명령어들을 매우 작은 크기로 구현합니다.

•	다양한 유틸리티 제공:

하나의 바이너리 파일에 수십 가지의 명령어(예: ls, cp, mv, cat, sh 등)를 포함하고 있어, 시스템 관리, 스크립트 작성, 디버깅 등 다양한 작업을 수행할 수 있습니다.

•	컨테이너 환경에서의 활용:

컨테이너 이미지를 최소화하고자 할 때 BusyBox를 기반으로 한 이미지가 자주 사용됩니다. 이는 빠른 배포와 작은 이미지 크기를 가능하게 합니다.

즉, BusyBox는 리눅스 환경에서 필수 유틸리티들을 단일 바이너리로 제공하는 도구로, 특히 임베디드 시스템이나 컨테이너와 같이 리소스가 제한된 환경에서 유용하게 사용됩니다.



# 탑다운2: 리플리카셋 테스트

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/11414685-4deb-4d6e-89c5-eef023d41acc/IMG_0416.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXPQVLJQ%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAKwTW61PuNRX8p4MMBdHDnLR4Wb9JHoBEictQ0PwjeeAiAY%2F91OK%2F4vuBlZAP7Mm%2F3eBXHv4Iknt0iKAZCAqPnlOyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiJ0CVMuFejgVQOHAKtwDJlsORvLgtqmWiYYuBbI54oJzThIwTL6Ef3PPTSkyQtIdv7FKZuzAXDkwxkvgzWVE92Rwrz3h0AP084ytHYEATGUdD1QhUEw0o6PDfppRTXtSx5wC97GyGVX8iHZmuxyz9IgTnbAhVAmauCjwlasCr8G009xB8T3M6caVqL5TQddH1xNNtgCx7W6q4kIN%2BNUOngQHyJYhGT3vLwyb9dYppCBuM0H4%2FlW31o%2FKdU2XSDWoga5FDRf0ACobeqqiP36xoyb8%2BmYKcTJEI7QjXoVSIBnnrCDmqzdzXQqlC5%2BkzcMbL9tDDoBrE7EIyggiSy5F253kY8NII5Pb3V%2Bqsqii7Mn06MwA0T5P9OGP6C%2BV1hRXnjcIvlgs1XJax%2BsVH%2FThPDalpgY2uy%2FyOi1x6WBEWHWS3rvlC%2B2fZX6V1utZwkYqAx4ZZTPk6CJfuVqyvk2NFlhrIhspkL2o0J00ogZYBJryWjZEgPNbHRRIhnvXa4Cmzx5v6MuWwP%2FzxofQFCDypTzKH6Ymi498Gqu0z0gQxYfM79dyNx%2FHtciOH90cB7btc2IRbrL3hOoNhoi0i%2B3hbITo5%2F4SuM6Z1T4MlCn5h%2FFIkegHAz0X8c%2Bx2MXnV7vTjnRWPI1M1x7HLxowjO7NvgY6pgHqPpKIg%2FKheGFHZQQX4TxK21cJ7N9eKzah%2B1wu%2BR5ag4iMR9ZwRPbP1wVUseM1wRA9ek8IwR4EngyMQ7WFybjEkD1NhQ3H%2Fw5Vzkq2JIv5psJ4WCgCSbV4iT4y1tpJyOrX2fgdHYndTOzWtMjw5KwEJAA0ZlPs3h9b5eTjXG1XYy1%2BzKqf31UL4vs6ZrY6ni9pILvM468WU3igsgfU7VH%2FwBJuVNih&X-Amz-Signature=f9306dbcfe2943db89940f43c2aea84d0e442ddf91c8480ec8bf0a107f5c71bd&X-Amz-SignedHeaders=host&x-id=GetObject)

## myreplicaset.yml

```markdown
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myreplicaset
spec:
  replicas: 2
  selector:
    matchLabels:
      run: nginx-rs
  template:
    metadata:
      labels:
        run: nginx-rs
    spec:
      containers:
        - name: nginx
          image: nginx

```

## 테스트

```bash
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl apply -f myreplicaset.yaml 
replicaset.apps/myreplicaset created
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get rs
NAME           DESIRED   CURRENT   READY   AGE
myreplicaset   2         2         2       79s
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
myreplicaset-7ks6p   1/1     Running   0          87s
myreplicaset-mtzc9   1/1     Running   0          87s
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl scale rs --replicas 4 myreplicaset
replicaset.apps/myreplicaset scaled
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get rs
NAME           DESIRED   CURRENT   READY   AGE
myreplicaset   4         4         4       2m10s
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
myreplicaset-7ks6p   1/1     Running   0          2m17s
myreplicaset-mtzc9   1/1     Running   0          2m17s
myreplicaset-sxp8l   1/1     Running   0          15s
myreplicaset-wdcb7   1/1     Running   0          15s
ubuntu@ip-172-31-27-11:~/deployment-replica$ 
```

해석

레플리카셋을 생성한다. 처음에는 파드를 2로 설정. kubectl get rs를 통해 레플리카셋 오브젝트의 상태를 확인할 수 있다. 

kubectl scale rs -replicas <number> <name> 으로 레플리카셋의 desired 값을 조절할 수도 있다. 

```bash
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
myreplicaset-7ks6p   1/1     Running   0          2m17s
myreplicaset-mtzc9   1/1     Running   0          2m17s
myreplicaset-sxp8l   1/1     Running   0          15s
myreplicaset-wdcb7   1/1     Running   0          15s
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl delete pod myreplicaset-7ks6p
pod "myreplicaset-7ks6p" deleted
ubuntu@ip-172-31-27-11:~/deployment-replica$ kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
myreplicaset-btsn4   1/1     Running   0          3s
myreplicaset-mtzc9   1/1     Running   0          5m55s
myreplicaset-sxp8l   1/1     Running   0          3m53s
myreplicaset-wdcb7   1/1     Running   0          3m53s
```

위와 같이 파드를 하나 죽여도, 레플리카셋이 다른 파드를 살려내는 모습을 볼 수 있다.

번외

kubectl delete rs --all: 모든 레플리카셋 삭제

# 탑다운3: 디플로이먼트 테스트

## mydeployment.yml

```markdown

apiVersion: apps/v1
kind: Deployment
metadata:
  name: mydeploy
spec:
  replicas: 10
  selector:
    matchLabels:
      run: nginx
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 25%  
      maxSurge: 25%
  template:
    metadata:
      labels:
        run: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
```

## 클러스터 적용



