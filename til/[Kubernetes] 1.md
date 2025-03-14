# [Kubernetes] 1

> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 5회까지 반복하고 해결 안 되면 도움 요청.)

> 실습은 천천히, 하지만 robust하게 하세요. 

# Q&A

- 사이드카가 뭐야?
  - 하나의 Pod 내부에서 메인 컨테이너와 함께 실행되는 보조 컨테이너.
- 왜 사이드카를 사용해?
  - 기능분리: 어플리케이션 코드와 무관하게 새로운 기능을 추가할 수 있음.
  - 유지보수 용이: 애플리케이션을 수정하지 않고 새로운 기능을 추가할 수 있음
- 리플리카셋이 뭐야?
  - 쿠버네티스에서 동일한 Pod를 일정 개수만큼 유지하는 컨트롤러.
  - 리플리카셋만 따로 쓰는 경우는 잘 없고, 디플로이먼트 컨트롤러 안에 포함시켜서 쓴다.
- 디플로이먼트도 컨트롤러인데, 같은 컨트롤러인 리플리카셋도 디플로이먼트 안에 있다고? 컨트롤러 안에 컨트롤러가 있는 셈인가?
  - 맞다.
- 드레이닝이 뭐야?
  - 쿠버네티스에서 특정 노드를 비우는 과정. 해당 노드에서 실행중인 모든 Pod를 종료하고 다른 노드로 이동시키는 작업
  - 사용자가 결제를 하던 중 파드가 내려가버리면 파드(컨테이너들)의 데이터가 날아가며 문제가 생길 수 있음. 안전을 위해 트래픽을 비우는 과정이 드레이닝.
- 디플로이먼트 전략이 뭐야?
  - 애플리케이션의 새로운 버전을 배포할 때, 기존 버전과 새로운 버전을 어떻게 교체할지 결정하는 방식.
- 롤링 업데이트 전략에서 maxSurge와 maxUnavailable 전략 설명
  - maxSurge: 새롭게 생성할 수 있는 추가 Pod 개수 (최대 몇 개 더 만들 수 있는지)
  - maxUnavailable: 동시에 비활성화될 수 있는 기존 Pod 개수(한 번에 몇 개 삭제할 수 있는지)
- 쿠버네티스에서 서비스의 정의
  - 동적으로 변경되는 Pod들의 네트워크 접근을 안정적으로 제공하는 네트워크 오브젝트.
  - 변하는 Pod들의 IP 대신, 클러스터 내부 또는 외부에서 항상 동일한 방식으로 접근할 수 있도록 해주는 역할.
- 서비스 타입의 정의와 종류
  - 서비스 타입은 말 그대로 서비스의 타입.
  - 종류로는, ClusterIP, NodePort, LoadBalancer, ExternalName이 있다.
- EKS2048이 뭐야?
  - Amazon Elastic Kubernetes Service(EKS)에서 2048 게임을 배포하여 EKS 기능을 학습하고 실습하는데 사용도는 샘플 애플리케이션
- 잉그레스의 정의
  - 쿠버네티스에서 클러스터 외부의 HTTP(S) 트래픽을 내부 서비스로 라우팅하는 역할을 하는 리소스
- 잉그레스가 있으면 서비스가 필요 없나?
  - 아니, 잉그레스는 트래픽을 직접 Pod로 보내지 못하고 반드시 서비스를 통해야 한다. 따라서 잉그레스는 외부 트래픽을 쿠버네티스 내부의 서비스로 전달하는 역할만 수행할 뿐, 서비스 없이 단독으로 존재할 수 없음.
- 왜 디플로이먼트 상태를 확인하는 코드가 kubectl get deploy,po야?
  - deploy: deployment의 단축 이름. 배포 리소스를 의미.
    - 그렇다면 여기서 deployment는 배포 리소스이지 컨트롤러가 아니란 말인가? 그렇다. deployment 배포 리소스는 애플리케이션의 원하는 상태를 선언적으로 정의하는 객체이지, deployment 컨트롤러와는 다르다.
  - po: pods의 약어. pods는 워낙 자주 쓰는 자원이기 때문에 네 글자 밖에 안 됨에도 이렇게 단축했다고 한다. 그런데 사실 이해가 안 된다. pods나 po나. 언어적 사회성을 고려하지 않은 형편없는 단축어다.
- Manifest의 정의
  - 클러스터 리소스의 구성과 상태를 선언적으로 기술한 설정 파일
  - 그렇다면 리소스를 생성할 때 가장 먼저 manifest를 작성해야겠군? 맞다.


# 테이블: 서비스 타입



# 그림들

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/5c9fc2f9-9415-4fdc-b602-f1893fab2d19/IMG_0411.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=616272ae531838f2cb68332512e6d385241ba9f43451811d86dcdbdacdcd96f2&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/0c30b65b-dfaf-4882-9524-f3deba03a892/IMG_0412.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=1d7dec5ee3285b3672c4b704a7c38cc441711899b4ce6dd2ea0195142364a6e5&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b551cc34-85ab-466a-84dd-033d0da92e30/IMG_0413.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=a298a48b3e877032e3dec1f0abf2d2143631cc29a6ec59fc79ab76f816ecee99&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/af080495-804c-4f3d-a266-d8c00e01471c/IMG_0414.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=42fcecf9d8eba978bfc29dd942ee0e0d1caa930867caa82c0266a30fe64dd378&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/d29f4c4a-e84b-4f54-9826-a32ff87330b8/IMG_0415.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=49fe666b59b6484e7357a464378eae9498810142ed7b0c24fe27a70eedad7335&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/11414685-4deb-4d6e-89c5-eef023d41acc/IMG_0416.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=ddf1f5beb9c10e1c62b2a04ef4885b9d6f715f9418109a32bd29a20467b799ad&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/dd5e7820-3629-41f4-82f0-7d244b65eff6/IMG_0417.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=e35a005f879c13ff9eb696fd72509fbb0fc957f86c2d7a749cc87c8145d49056&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b40ec820-bb57-406e-b7d6-7fa78e9dd025/IMG_0418.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=4ee63fbcece2f2e94802bdc21e262e7b37cf1be4951888f175879d65bb7183e9&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/30992f9d-ffbd-4175-961d-6644dedf533f/IMG_0419.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=c6711d73e1631bdc94f00d7f783e9109a844f3b505d997705d1799c3f53f8669&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b8a9c172-aede-4285-8c00-f204cd39a74b/IMG_0420.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=bbb6d579996f15bec78dcebea5bcc0d5ea77616b78a9ada1c5837d0ca81713e3&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a009fcb3-4a4f-45f0-8ca3-bc31f28600e0/IMG_0421.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=b6a331201e0c0e4b539981c645124811c9b26f1e53138980720edca10bcfd23e&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a6b57ba5-3603-4789-91a5-5098e59b9523/IMG_0422.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=c13963166422db4eddbd6e0e7a9872c9b84590515f3c335c3d3f117c75b11b8c&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/47d542ef-64fd-4b65-86ab-17057016d277/IMG_0423.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=116de93e704a40e60569a2a34295225a715a9ac47d2450edb625a7ac6c0adff8&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05d14ce2-1012-4dc5-bee5-98d64d9363fb/IMG_0424.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=47a5bb4f1522517131f84e0c60e1225fdd587fadf25c9bde302334da5f2471b5&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/580ca0d7-a640-4200-86a4-b4490487745c/IMG_0425.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=ed67d7613d4fd1f24cafb21142920d27d415e5d3578fbc8946bcb121eb194a39&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/af800c0d-c783-44cb-9494-8ed59b972bd6/IMG_0426.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C63GYIV%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHpY9%2FkUZ%2BrdvIMxFrkoNFpchjdNRvGEpXlcovMYXbSQIgEqZvkhJi4maZaiLuKLKFL050YpTbwU4aMXer4VTaP3gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiEUMPdywc0f22c4SrcA%2FqjbIW7NsjPROmLWnMVMt7AsPWa199CE71RzswX8M%2BzybRBASB6jrGBx8zyWaEiulJkj%2Bc0Od8NfcZ1zO501ucjpcOFaLzttRUHm0WEqOjXE2G2aOugLQm25yznVFzuBBRcIRKCN9QNWTpSTlU7fpXT3W%2FlKHlUEs1VEk58nskLj2FI8edQ0iF1xuxwL6smOqusglWoi%2BeMqZi6v9yRv95SJPoR20F95NfXsY732X3Eehi1lgbS8ZzT0HSoskzx2fWUFDzWs%2BNBnlzlxU8W%2FNtcf6bzyhSV9MGoa6kKL4Y13Uv%2BpZNHPCMEjzV1UVjJ6oZ%2Bv9j13iQ7uZGKvM%2FC7xopPKqvvNi2eJVJ1seR%2FvOTQrVY3a9bIETqRB6yvgLc%2Bwc%2Fi8zknihrKiYjv76nW%2Bcj3mOV5%2Bb%2FFrqHMxJGqCMP6YheZznNe26YqTmAbZGdn9LyfnWPqvp%2FwbVR%2F9PY%2BMme4g27K3JTzQf%2FxHG7QbQk6ZIpqQEug17v5yJSPWAoSuG%2Bk7NAYKknwSWT63X0vcdgilehQhABRbp3Y7QUIETNWocXUW4CQTo8ykNA1DUZhXUKACtLmgnGfCBN3XOXR5po%2FeqaOxup90dGTQPGdMHknkCo1W2nhy7oWsTiMNHuzb4GOqUBOP%2BEJ%2B2KBy%2BH8MJR0QhElqMW38HVzX3E7YULEUvZwyC1EANQgS9bTDUCtYxjxTBsKuTL5Y1eapsogBmBUL2%2BGr8O9EQ7YMtaQfqmlrmB%2BPgjyIL7e8tMbUr%2BUzBui97i%2BUllCGKoj1ioBM6TMNBheCQxjhdGA1AalWCLYbaEZTrZZVixo%2BBaWrY4ALJrLegeM2NZrFWiKClL%2FNtnSWUP%2F%2B9d%2FHvO&X-Amz-Signature=5690485c587e1c71fe8959df327cbae2635c8acf7b9554a51fb815c547a7e8d6&X-Amz-SignedHeaders=host&x-id=GetObject)

# 이름들

- 쿠버네티스 API: 쿠버네티스 조작은 모두 API로 동작한다.CLI kubectl을 통해 마스터 노드 kube-apiserver에게 YAML 혹은 JSON 형식으로 전송한다.
- 오브젝트: K8s 클러스터 내부의 엔티티로, 파드, 컨트롤러, 서비스 등의 인스턴스를 의미. 쿠버네티스 API의 리소스 종류에 맞게 설정 및 생성된다. (그럼 모든 파드, 컨트롤러, 서비스는 공통 조상을 가지는가? 아니, 객체지향 개념은 아니다. 오브젝트들이 동일한 API에서 kind만 달리 설정된다는 의미다. 파드와 컨트롤러는 같은 메뉴판에 있는 파스타와 스테이크의 관계 같은 거지.) 
- kube-system 네임스페이스: K8s 시스템 관련 기능을 하는 오브젝트들은 이 네임 스페이스에서 만들어짐.
- 쿠버네티스에서의 네임 스페이스: 오브젝트들은 kind 안에서 유일한 이름을 가져야 함.
- 워크로드: 컨테이너, 파드, 컨트롤러의 그룹. 컨테이너 실행을 관리하기 위해 사용.
- 컨테이너: 쿠버네티스에서는 컨테이너만 독자적으로 실행하는 것이 불가능하며, 파드 내에 실행해야 한다. 컨테이너 가동 시 이미지의 이름, 실행 명령어, 실행 인자, 환경 변수, 리소스 요청/상한 값이 설정된 대로 생성되겠지
- 파드: 컨테이너를 실행하기 위한 한 개 또는 여러 개의 컨테이너. 매우 중요한 오브젝트임
- 컨트롤러: 파드를 제어하는 오브젝트
# 탑다운1

목표: Minikube 클러스터를 로컬에서 실행하고, 간단한 Nginx 웹 서버를 배포한 후, 외부에서 접근할 수 있도록 서비스로 노출합니다.

## 1.  클러스터 생성

```shell
# 클러스터 1개 생성
minikube start
```



## 2. 메니페스트 작성

nginx-deployment.yaml

```shell
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        
```

## 3. Nginx Service Manifest 작성

nginx-service.yaml

```shell
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: NodePort
```

## 4. 메니페스트를 클러스터에 적용

```shell
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml
```

## 5. 서비스 접근 확인

```shell
minikube service nginx-service
```



# 이슈: 지금 클러스터에 할당된 Elastic IP와 다른 주소로 서비스 url이 생성

## Phase1

환경: ubuntu 22, amd, EC2, minikube

로그: 없음

변경사항: nginx-serivce.yaml, nginx-deployment.yaml 생성 후 클러스터 적용

## Phase2-1

확인: 서비스 타입이 NodePort로 지정됨. NodePort 타입의 서비스는 클러스터 노드의 아이피와 지정된 포트를 통해 외부에 노출. 이 과정에서 Elastic IP가 아닌 기본 네트워크 인터페이스 아이피가 사용된 것으로 보임. 

externalIPs 필드를 활용하면 서비스로 외부 접근 가능하다고 함

시도: 

```shell
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
  externalIPs:
    - 43.200.202.183
```

결과 분석: 실패

클러스터 적용과 서비스 확인을 진행하였음

```shell
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml
minikube service nginx-service
```

```shell
ubuntu@ip-172-31-27-11:~/manifest$ minikube service nginx-service
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | nginx-service |          80 | http://192.168.49.2:32594 |
|-----------|---------------|-------------|---------------------------|
🎉  Opening service default/nginx-service in default browser...
👉  http://192.168.49.2:32594
```

결과로 생성된 url에 externalURL은 반영되지 않음. 그냥 elastic IP를 바로 접속하면? 이것도 안 됨

## Phase2-2: 다른 이슈 발견

확인: nginx-service.yaml의 externalURL 설정은 서비스 url과 무관함. 이와 관련한 GPT 문답

> externalIPs 필드는 Kubernetes 클러스터 내에서 노드가 특정 IP(예: 탄력적 IP)로 들어오는 트래픽을 서비스로 전달하도록 추가적인 라우팅 규칙을 설정하는 역할을 합니다. 하지만 이 필드가 있다고 해서 Kubernetes API나 관련 도구가 자동으로 서비스 URL을 그 외부 IP로 변경해주지는 않습니다.

노드 포트는 말 그대로 노드의 포트를 지정하는 서비스 타입. 노드는 여전히 호스트의 아이피로 설정될 수밖에 없다. 그래서 로드 밸런서를 쓰는 것이 일반적. 그러나 로드 밸런서는 추가 비용을 유발할 수 있다고 한다. 왜? 로드 밸런서 리소스는 따로 인스턴스처럼 생성이 된다. 그래서 직접 비활성화 시켜주는 조치가 필요하다. 일단 로드 밸런서로 서비스 타입을 변환해보자.

시도

nginx-service.yaml을 다음과 같이 변경

```shell
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

이를 클러스터에 적용하면 AWS 에서 제공하는 로드 밸런서가 생성된다. 이는 AWS 콘솔에서 확인 가능

결과분석: 솔루션이 제대로 적용안 됨.(솔루션 자체의 문제가 아님)

현재 externalIP가 pending 상태. AWS 콘솔에서도 아무것도 확인 안 됨. kubectl에서 매니페스트 적용한 것과 별개로 AWS 콘솔에서 별도의 조작을 해줘야 하는가? 그렇지는 않지만, AWS와 클러스터 통합 여부에 따라 안 될 수도 있다. 그런데 해결이 안 되고 있으니, 별도의 이슈를 생성하도록 한다.

# 이슈: 로드 밸런서가 생성되지 않음

## Phase1

환경: unbuntu, EC2, 

로그: 없음

변경사항: nginx-service.yaml을 통해 로드 밸런서 타입을 지정하였음.

## Phase2-1: 다른 이슈 발견

확인: AWS와 쿠버네티스 클러스터 연동 확인

```shell
# 각 노드 정보 표기. 연동이 제대로 됐으면 각 노드에 AWS 관련 정보 표기
kubectl get nodes -o wide
#  failure-domain.beta.kubernetes.io/zone 또는 
# topology.kubernetes.io/region 표기가 있는지 확인
kubectl describe node minikube | grep topology
```

관련 표기가 없음. AWS와 쿠버네티스 클러스터(minikube)가 연동되지 않았다. 

> Minikube는 로컬 개발 및 테스트 용도로 만들어진 Kubernetes 클러스터이기 때문에, AWS와의 통합(예: AWS 리소스 자동 프로비저닝, IAM 역할 연동, AWS 관련 노드 라벨 등)이 자동으로 이루어지지 않습니다.

시도: 

그렇다면 minikube로는 EC2에서 로드 밸런서를 생성할 수 없군. 

결과분석: 원천 불가

그냥 노드 포트 타입으로 다시 바꾸고, 잠깐 인스턴스 아이피 보안 설정을 열어서 서비스 접속 테스트를 하고 다음 실습으로 넘어가도록 하자. → 이조차도 안 된다.

# 이슈: 노드포트 서비스로 접속이 안 됨

## Phase1

환경: ubuntu 22, amd, EC2, minikube, elastic IP 사용 중

로그: 없음

변경사항: nginx-serivce.yaml에 노드 포트 설정하여 클러스터에 적용, http://192.168.49.2:32594로 서비스 링크 생성 됨. AWS 인스턴스의 보안 그룹에서 해당 포트를 모든 TCP 요청에 대해 허가하도록 인바운드 규칙을 설정함. 그럼에도 http://<할당된 탄력적IP>:노드포트 로 접속이 불가능함. 

## Phase2-2: 대안 발견(curl)

확인: Minikube의 특성을 생각해야 함.

> Minikube를 EC2 인스턴스에서 실행할 경우, Minikube 클러스터는 기본적으로 독자적인 가상 네트워크 내에서 동작합니다.  서비스 링크로 보이는 http://192.168.49.2:32594는 Minikube 내부에서 할당된 IP이며, EC2 인스턴스에 할당된 탄력적 IP와는 별개의 네트워크 인터페이스에 매핑되어 있습니다.

→ 즉, 아무리 AWS 보안 설정을 지지고 볶아도 외부에서 Minikube 클러스터 서비스를 이용할 수는 없다는 소리. 대신 미니쿠베의 가상 네트워크로  http://192.168.49.2:32594 접속해야 한다. 그런데 이건 당연히 외부 접속이 불가능한 네트워크다. 

> 외부 접근을 원한다면 minikube tunnel을 사용하는 방법이 가장 일반적입니다.

시도

1. 포트 설정: 그대로 놔 두면 됨
1. LoadBalancer로 서비스 타입 다시 변경
1. 터널은 계속 터미널을 점유하고 있어야 함
결과 분석:

이것도 안 된다. 미니쿠베로는 외부 접속이 안 되는 거 같다.

대신, curl로 EC2 호스트 인스턴스에서 접속하여 html을 확인할 수  있다. 일단은 이렇게 사용할 수 있다. 다음 단계 실습은, 미니쿠베로 외부 클라이언트 접속을 우선적으로 해보자. → 하긴 그래서 잉그레스가 있는 거지. 서비스의 아이피가 외부 호스팅이 가능해야 한다는 생각이 이상한 것이다.



# 탑다운2

목표: 다음은 실습 난이도를 한 단계 높여서 Ingress 컨트롤러와 TLS 종료, 그리고 경로 기반 라우팅을 사용하는 프로젝트 예시입니다.

## 1. 잉그레스 컨트롤러 설치

ingress 컨트롤러를 이렇게 설치할 수 있다.

```shell
minikube addons enable ingress
```

실행 확인

```shell
kubectl get pods -n ingress-nginx
```

## 2. 두 개의 애플리케이션 배포

### 1) Nginx Deployment and service

nginx-deployment.yaml

```shell
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

### 2) node.js 간단한 웹 배포

node-deployment.yaml

```shell
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-deployment
  labels:
    app: node-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: node-app
  template:
    metadata:
      labels:
        app: node-app
    spec:
      containers:
      - name: node-app
        # 예시용 간단한 Node.js 이미지 (실제 테스트를 위해 간단한 이미지 필요)
        image: hashicorp/http-echo
        args:
          - "-text=Hello from Node.js app"
        ports:
        - containerPort: 5678
---
apiVersion: v1
kind: Service
metadata:
  name: node-service
spec:
  selector:
    app: node-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5678
  type: ClusterIP
```

## 3. Ingress 리소스 생성

### a) TLS 인증서 생성

> Minikube는 테스트 용도로 Self-Signed 인증서를 사용할 수 있습니다. 아래 명령어를 통해 인증서와 키를 생성합니다.



```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -out tls.crt -keyout tls.key \
  -subj "/CN=example.com/O=example.com"
```

인증서를 쿠버네티스 secret으로 생성

```shell
kubectl create secret tls tls-secret --key tls.key --cert tls.crt
```

### b) Ingress 리소스 생성

ingress.yaml

```shell
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: advanced-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - example.com
    secretName: tls-secret
  rules:
  - host: example.com
    http:
      paths:
      - path: /nginx
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
      - path: /node
        pathType: Prefix
        backend:
          service:
            name: node-service
            port:
              number: 80
```



> 이 Ingress 설정은:
•	example.com 도메인에 대해 TLS를 적용
•	/nginx 경로는 Nginx 서비스로 라우팅
•	/node 경로는 Node.js (http-echo) 서비스로 라우팅



> 실제 테스트에서는 /etc/hosts 파일에 example.com을 Minikube IP(예: minikube ip)로 매핑하거나, 브라우저에서 해당 도메인으로 접속해 테스트할 수 있습니다.

## 4. 리소스 적용 및 테스트

각 야멜 파일을 클러스터에 적용

```shell
kubectl apply -f nginx-deployment.yaml
kubectl apply -f node-deployment.yaml
kubectl apply -f ingress.yaml
```

리소스가 잘 배포됐는지 확인

```shell
kubectl get all
kubectl get ingress
```

Ingress에 할당된 아이피 확인

```shell
minikube ip
```

192.168.49.2

중요: 로컬 호스트 파일 수정

/etc/hosts 파일에 아래 항목 추가

```shell
<minikube_ip>   example.com
```

로컬 브라우저에서 접속 테스트→ EC2에서는 어떻게 하지?

https://example.com/nginx → curl https://example.com/nginx -k
https://example.com/node



## 의문점들

### Q1.

잉그레스 쓰는게 외부 클라이언트에서도 서비스 접속할 수 있게 해주는 거 아닌가? 미니쿠베라는 이유로 잉그레스 써도 외부 클라이언트 접속이 안 되면, 미니쿠베로는 대체 뭘 할 수 있는가? 터널 안 쓰면 아무것도 못 하는 거 아닌가?

A.

Minikube는 로컬 개발 및 테스트용으로 만들어진 도구이므로,

실제 퍼블릭 클라우드 환경(예: AWS, GCP)에서의 Ingress처럼 외부 IP나 로드 밸런서를 자동으로 생성해 주지 않습니다.

결과적으로 “Ingress를 정의하면 외부에서도 접근 가능”이라는 Kubernetes 일반론이, Minikube 환경에서는 제한적으로만 적용됩니다.

1. 왜 Minikube에서 Ingress를 써도 외부 접속이 어려운가?

1.	Minikube의 네트워크 구조

•	Minikube는 내부적으로 VM이나 컨테이너 네트워크를 사용해 로컬 환경에서 Kubernetes를 실행합니다.

•	“외부 IP”가 없는 상태이므로, Ingress를 만들었다 해도 외부(인터넷)에서 직접 접속할 수 없습니다.

2.	LoadBalancer 연동 부재

•	클라우드 환경에서는 Ingress 컨트롤러가 클라우드의 로드 밸런서를 만들고 퍼블릭 IP를 할당합니다.

•	Minikube에는 그런 기능이 없어서, Ingress를 정의해도 “로컬 전용”으로만 동작합니다.

2. 그렇다면 Minikube로 Ingress를 쓰는 이유는?

1.	개발/테스트 환경 시뮬레이션

•	실제 클라우드 환경에서 Ingress를 사용하기 전, 로컬 환경에서 Ingress 리소스(YAML) 구성을 미리 시험해 볼 수 있습니다.

•	예: 경로 기반 라우팅, TLS 설정 등을 로컬에서 빠르게 검증할 수 있습니다.

2.	여러 서비스 라우팅 테스트

•	한 도메인(또는 IP) 아래 여러 서비스(/app1, /app2 등)로 트래픽을 분기하는 로직을 로컬에서 확인할 수 있습니다.

3. Minikube에서 외부 접근하려면 어떻게 해야 하나?

A. minikube tunnel 사용 (LoadBalancer 타입 서비스 테스트)

•	LoadBalancer 타입의 서비스를 생성하고,

•	minikube tunnel 명령어를 실행하면,

Minikube가 로컬 머신(또는 EC2 인스턴스)의 네트워크 인터페이스를 통해 외부에서 접근 가능한 포트를 열어줍니다.

장점: 로컬 개발 환경에서 LoadBalancer 테스트 가능

단점: tunnel 프로세스를 계속 실행해 두어야 하며, 도메인 기반 접근은 /etc/hosts 등 추가 설정이 필요

B. NodePort + SSH 포트 포워딩 (또는 NAT)

•	NodePort로 서비스를 노출한 뒤, SSH 포트 포워딩을 통해 로컬 브라우저에서 테스트할 수 있습니다.

•	혹은 Minikube가 동작하는 호스트(EC2 등)에서 OS 레벨 NAT를 설정해 외부 IP/포트를 NodePort로 매핑할 수도 있습니다.

C. /etc/hosts로 도메인 매핑 (로컬 테스트)

•	로컬 PC나 Minikube 실행 호스트의 /etc/hosts를 수정해 example.com을 Minikube IP로 매핑하면, 로컬에서 해당 도메인으로 접근 가능합니다.

•	여전히 인터넷 전체에는 노출되지 않고, 해당 호스트(혹은 로컬 PC) 내부에서만 유효합니다.

4. 정리

•	Minikube는 프로덕션 환경에서 외부 트래픽을 받아들일 용도로 설계된 것이 아니라, 로컬에서 K8s를 학습하고 테스트하기 위한 도구입니다.

•	Ingress를 사용해도 **“로컬(또는 Minikube 호스트) 내부”**에서만 동작하며, 외부 접근이 필요하면 추가적인 터널링이나 포트 포워딩 설정을 해야 합니다.

•	실제로 외부(인터넷)에서 접근 가능한 Kubernetes 환경을 만들려면, EKS, GKE, AKS 같은 클라우드-managed Kubernetes나, 자체 클러스터에 cloud-controller(AWS, OpenStack 등)를 설정해야 합니다.

결국, Minikube에서 Ingress는 “기능적 학습”을 위한 것이지, 실제 퍼블릭 접근을 위한 솔루션이 아니다라고 이해하시면 됩니다.

따라서 터널링이나 포트 포워딩 같은 추가 작업 없이 “외부에서 바로 접근”하기는 어렵고,

이는 Minikube의 근본적인 설계(로컬 테스트용) 때문입니다

### Q2

1. 개발/테스트 환경 시뮬레이션
•	실제 클라우드 환경에서 Ingress를 사용하기 전, 로컬 환경에서 Ingress 리소스(YAML) 구성을 미리 시험해 볼 수 있습니다.
•	예: 경로 기반 라우팅, TLS 설정 등을 로컬에서 빠르게 검증할 수 있습니다.
1. 여러 서비스 라우팅 테스트
•	한 도메인(또는 IP) 아래 여러 서비스(/app1, /app2 등)로 트래픽을 분기하는 로직을 로컬에서 확인할 수 있습니다.
이런 기능들은 잉그레스를 써야만 할 수 있는 것들인가보지?

A

네, 맞습니다.
Ingress는 여러 서비스에 대한 경로 기반 라우팅, TLS 종료, 도메인 기반 라우팅 등을 통합적으로 관리할 수 있게 해 주므로,
이런 기능들을 효율적으로 구현하고 테스트하려면 Ingress를 사용하는 것이 일반적입니다.

물론 NodePort나 LoadBalancer 서비스를 각각 따로 설정하여 일부 기능을 구현할 수는 있지만,
Ingress는 중앙 집중식으로 여러 라우팅 규칙과 TLS 설정을 한 곳에서 관리할 수 있는 장점이 있습니다.

# 이슈: nginx-deployment.yaml 클러스터 적용 오류

## Phase1

환경: EC2, AMD, Ubuntu, minikube

로그: error: error validating "nginx-deployment.yaml": error validating data: failed to download openapi: Get "https://192.168.49.2:8443/openapi/v2?timeout=32s": dial tcp 192.168.49.2:8443: connect: no route to host; if you choose to ignore these errors, turn validation off with --validate=false

변경사항: nginx-deployment.yaml 작성 후 kubectl apply -f nginx-deployment.yaml 실행

## Phase2-1: 해결

확인: 192.168.49.2:8443이 무슨 아이피인지 모르겠다. 클러스터 아이피인가? 일단 로그 자체의 의미는 야멜 파일을 클러스터에 적용하는 과정에 validation에서 문제가 생겼다는 것으로 보인다. 

즉, 내부에서 라우팅이 안 됐던 것이다. minikube status로 확인 결과 컨트롤 플레인이 stop 상태인 것을 확인.

시도: minikube start

결과 분석: 성공. 

# 탑다운3

다음은 쿠버네티스의 다양한 고급 기능(다중 서비스, Ingress, TLS, 네트워크 정책, Persistent Volume, Horizontal Pod Autoscaler 등)을 활용하는 고난이도 실습 예시입니다.

## 1. 네임스페이스 생성

모든 리소스를 격리할 네임스페이스를 생성합니다.

```markdown
apiVersion: v1
kind: Namespace
metadata:
  name: advanced-demo
```

```markdown
kubectl apply -f namespace.yaml
```

## 2. ConfigMap, Secret 생성

백엔드 서비스에서 사용할 설정 값과 데이터베이스 접속 정보를 관리

```markdown
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend-config
  namespace: advanced-demo
data:
  LOG_LEVEL: "info"
  FEATURE_FLAG: "true"
```

```markdown
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: advanced-demo
type: Opaque
data:
  # base64 인코딩된 값으로 입력 (예: echo -n "mypassword" | base64)
  DB_PASSWORD: bXlwYXNzd29yZA==
```

```markdown
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
```

## 3. DB deploy(including persistent storage)

```markdown
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
  namespace: advanced-demo
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  namespace: advanced-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_PASSWORD
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysql-data
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-data
        persistentVolumeClaim:
          claimName: db-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: mysql-service
  namespace: advanced-demo
spec:
  selector:
    app: mysql
  ports:
  - protocol: TCP
    port: 3306
    targetPort: 3306
  clusterIP: None  # Headless service (DB 클러스터 내 연결 테스트용)
```

```markdown
kubectl apply -f db-deployment.yaml
```

## 4. 백엔드 서비스 배포

backend-deployment.yaml

```markdown
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: advanced-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: nginxdemos/hello # 데모용 이미지
        ports:
        - containerPort: 8080
        env:
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: backend-config
              key: LOG_LEVEL
        - name: FEATURE_FLAG
          valueFrom:
            configMapKeyRef:
              name: backend-config
              key: FEATURE_FLAG
        - name: DB_HOST
          value: mysql-service.advanced-demo.svc.cluster.local
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_PASSWORD
---
apiVersion: v1
kind: Service
metadata:
  name: backend-service
  namespace: advanced-demo
spec:
  selector:
    app: backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP
```

클러스터 적용하기

## 5. 프론트엔드 서비스 배포

```markdown
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: advanced-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  namespace: advanced-demo
spec:
  selector:
    app: frontend
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

```markdown
kubectl apply -f frontend-deployment.yaml
```

## 6. 네트워크 정책

```markdown
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-db
  namespace: advanced-demo
spec:
  podSelector:
    matchLabels:
      app: mysql
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: backend
    ports:
    - protocol: TCP
      port: 3306
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: advanced-demo
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```

```markdown
kubectl apply -f networkpolicy.yaml
```

## 7. Ingress와 TLS 구성

### a. TLS 인증서 생성 (Self-Signed)

```markdown
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -out tls.crt -keyout tls.key \
  -subj "/CN=advanced-demo.local/O=advanced-demo"
```

쿠버네티스 시크릿 생성

```markdown
kubectl create secret tls tls-secret --key tls.key --cert tls.crt -n advanced-demo
```

### b. Ingress 리소스 작성

```markdown
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: advanced-ingress
  namespace: advanced-demo
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - advanced-demo.local
    secretName: tls-secret
  rules:
  - host: advanced-demo.local
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
```

이것도 클러스터에 적용.

## 8. HPA 설정

예를 들어, 백엔드 서비스에 대해 CPU 사용량이 50%를 초과하면 자동으로 Pod 수를 증가시키도록 설정합니다.

```markdown
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
  namespace: advanced-demo
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend
  minReplicas: 2
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```

```markdown
kubectl apply -f hpa.yaml
```



## 9. 테스트 및 검증

### 모든 리소스 상태 확인

```markdown
kubectl get all -n advanced-demo
kubectl get ingress -n advanced-demo
```

### 잉그레스 접속 테스트

/etc/hosts 파일에 minikube ip와 advanced-demo.local 매핑 추가

```markdown
<minikube ip> advanced-demo.local # 192.168.49.2
```

https://advanced-demo.local로 접속 시 기본 경로는 프론트엔드로, /api 경로는 백엔드 api 서비스로 라우팅.

### HPA 테스트

백엔드 서비스에 부하를 발생시키거나, kubectl top pod -n advanced-demo 명령어로 CPU 사용량을 모니터링 하여 HPA 동작 확인

# 이슈: 클러스터 잉그레스 connection refused

## Phase1

환경: AMD, Ubuntu, Ec2, minikube
로그: curl: (7) Failed to connect to advanced-demo.local port 443 after 0 ms: Connection refused

변경사항: 

1. backend-deployment, conifgmap, db-deployment, frontend-deployment, hpa, ingress, namespace, networkpolicy, secret 야멜 파일들을 통해 리소스를 설정하고 클러스터에 적용.
1. /etc/hosts 파일에 minikube ip를 advanced-demo.local에 할당. 192.168.49.2 advanced-demo.local
## Phase2-1

확인:	 

1. 네임스페이스 advanced-demo에 Ingress 리소스가 올바르게 생성되었는지 확인: 정상
  1. kubectl get ingress -n advanced-demo
    1. advanced-ingress   <none>   advanced-demo.local             80, 443   22m
1. Minikube에서 Ingress 애드온이 활성화되어 있고, Ingress 컨트롤러(NGINX Ingress)가 실행 중인지 확인: 비정상(ingress
  1. kubectl get pods -n ingress-nginx
    1. No resources found in ingress-nginx namespace.
    1. 잉그레스 애드온을 클러스터에 따로 활성화시켜야 하는데 아까 클러스터를 삭제하고 다시 시작한 후 활성화를 안 했다.
  1. 의문: 잉그레스는 ingress-nginx라는 별도의 네임스페이스를 쓰는가?
    1. 네, 보통 ingress-nginx 컨트롤러는 별도의 네임스페이스(대개 ingress-nginx)에 배포됩니다. 예를 들어, Minikube에서 Ingress 애드온을 활성화하면, 기본적으로 ingress-nginx 네임스페이스에 컨트롤러 Pod들이 생성됩니다. 물론, 설치 방법이나 환경에 따라 네임스페이스 명은 달라질 수 있습니다
시도

```markdown
minikube addons enable ingress
kubectl get pods -n ingress-nginx
```

정상적으로 추가됨. 

결과 분석: 성공

# 탑다운4: 헬스체크

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/de7bc274-ce1c-4c4f-8aa4-c14d1d161115/IMG_0429.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF43KDJT%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwJ9JT%2F%2F7FaCx2CmM%2FWD7tLH1q3ow%2BLAiL1RTyXtN5TAiEAwYeZgZAoMZ%2B4MZj0AFCNPUQFy3NQlQAuIY6Zfo3n8YEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKUvb6Vgna8u7Swe5yrcAzz%2FSMK%2F%2BOT9D2Odut8llmiYGitbJn6CcWW5gy%2BxkYhvQiK7bradCocl7EMx0Lc%2FkLYl4XUTXvzRw%2BrTnRtEeSaYxussqqAEaHUbpJhSVkQ7lQPE1EtpJuX%2BhK2h%2FI%2FXKAEkMrhPgn3K7MNeOz43XymkG3GK88Pu9jteOT%2B05eEASat2GsEs8P92ZCj5ZUsIULmUERDAbTvUKh4vxIiBRE0RjpfsoMwOB9r%2B2dC4FTtzubgyxsWk67fTu1JwBtHC%2F2BcX2Fir4TqB8j79ex8gVlbYD%2FC3Psy6XlXOm1ONQiJX%2BRHc0a5DHE1BBJOSBsxxSWlgLS6nrGeu3ePcyMcznU05gHSMZlqIxX0ZgjHZs2e0DtEvO%2Ffi3cUNm6jV4vZb2DAd51Voyu4a8RzGIdgsMmhiC32Un1CuwVi%2BuDNO8jZI%2FNl1%2FYbaVwHRKWTEgHaiM5OYtBWWThnY2VL2SuYkG4rT31WhlbkpUXpc2pJvDA0gHIPyapNNhYMvAK2PBr3I48PpCGc8rS5o4QrXsydm%2BvT8IQt6hmb7zHtRRW6f2AdDsCKjfB1hcdsRF%2FYvXKu7iMk7JgPC5ftrEfzFLWb8Ts%2FO0cysPcrtuHY%2Bg0HMskg10SinAzUyUJ9pWIqMI7uzb4GOqUB%2FPYaFOSJ4%2FELPCJFjbfOuvAUOL8I9295Cc05ApXYZy%2Bnhv0PEu2QsMwb7wVBKxMas6wbFA1k%2FU1ABYqAFQcQGiQRnKlP8spVZKy4E79XfLa4ewvj74%2BP6Z%2FafPfEQlKRW%2FpD%2F5iAn45gag6nScDPLS8Fd5I7Imt0XjbcvAMwlwRY26AfIc20vYgwc%2FwuLcG2m1HIcJjvK07quXyNYuBQ%2Bbbn5MwF&X-Amz-Signature=0ddc46f82142de9077cb9114cd73b5b277a732903036fbdeef83070d0d4eedf4&X-Amz-SignedHeaders=host&x-id=GetObject)

## 1. ./webapl-pod.yml 파일

```markdown
apiVersion: v1
kind: Pod
metadata:
  name: webapl
spec:
  containers:
    - name: webapl
      image: maho/webapl:0.1
      livenessProbe:
        httpGet:
          path: /healthz
          port: 3000
        initialDelaySeconds: 3
        periodSeconds: 5
      readinessProbe:
        httpGet:
          path: /ready
          port: 3000
        initialDelaySeconds: 15 # 프로브 검사 시작 전 대기 시간
        periodSeconds: 6 # 검사 간격

```

역할: 이 구성 파일은 maho/webapl:0.1 이미지를 사용하는 Pod를 생성하고, 해당 컨테이너의 상태를 주기적으로 확인하여 Liveness Probe를 통해 컨테이너가 정상적으로 실행 중인지 감시하고, Readiness Probe를 통해 서비스 준비 상태를 확인하여 트래픽을 전달할 수 있는지를 판단합니다.

## 2. webapl/Dockerfile

```markdown
FROM alpine:latest
## Node.js  https://pkgs.alpinelinux.org/package/edge/main/x86_64/nodejs
RUN apk update && apk add --no-cache nodejs npm
## 의존 모듈
WORKDIR /
ADD ./package.json /
RUN npm install
ADD ./webapl.js /
## 애플리케이션 기동
CMD node /webapl.js
```

역할: 이 Dockerfile은 경량 Alpine Linux 이미지를 기반으로 Node.js 환경을 구성하고, 애플리케이션의 의존성을 설치한 후, webapl.js 파일을 실행하여 애플리케이션을 시작하는 과정을 자동화합니다



## 3. webapl/package.json

```markdown
{
    "name": "webapl",
    "version": "1.0.0",
    "description": "",
    "main": "webapl.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
        "express": "^4.16.3"
    }
}
```

역할: 이 package.json 파일은 “webapl” 애플리케이션의 기본 설정 정보를 담고 있으며, 프로젝트 이름, 버전, 메인 파일, 스크립트, 그리고 Express와 같은 의존성 패키지들을 관리합니다. 이를 통해 Node.js에서 해당 애플리케이션을 빌드, 테스트, 실행할 수 있게 도와줍니다.



## 4. webapl/webapl.js

```markdown
// 모의 애플리케이션
//
const express = require('express')
const app = express()
var start = Date.now()
// Liveness 프로브 핸들러
// 기동 후 40초가 되면, 500 에러를 반환한다.
// 그 전까지는 HTTP 200 OK를 반환한다.
// 즉, 40초가 되면, Liveness프로브가 실패하여 컨테이너가 재기동한다.
//
app.get('/healthz', function (request, response) {
    var msec = Date.now() - start
    var code = 200
    if (msec > 40000) {
        code = 500
    }
    console.log('GET /healthz ' + code)
    response.status(code).send('OK')
})
// Rediness 프로브 핸들러
// 애플리케이션의 초기화 시간으로
// 기동 후 20초 지나고 나서부터 HTTP 200을 반환한다.
// 그 전까지는 HTTPS 200 OK를 반환한다.
app.get('/ready', function (request, response) {
    var msec = Date.now() - start
    var code = 500
    if (msec > 20000) {
        code = 200
    }
    console.log('GET /ready ' + code)
    response.status(code).send('OK')
})
// 첫 화면
//
app.get('/', function (request, response) {
    console.log('GET /')
    response.send('Hello from Node.js')
})
// 서버 포트 번호
//
app.listen(3000);
```

역할: 노드 기반의 간단한 웹 서버를 구성하며, Kubernetes와 같은 환경에서 Liveness 및 Readiness Probe를 테스트하는 용도로 사용됩니다.



## 5. 테스트

### 테스트 순서

1. 파드 배포하기
1. 파드 상태 확인
  1. kubectl get pods
1. 로그 분석으로 프로브 동작 확인
  1. kubectl logs webapl
  1. kubectl describe pod webapl


### 테스트 결과 로그

```markdown
Events:
  Type     Reason          Age                   From               Message
  ----     ------          ----                  ----               -------
  Normal   Scheduled       42m                   default-scheduler  Successfully assigned default/webapl to minikube
  Normal   Pulling         42m                   kubelet            Pulling image "maho/webapl:0.1"
  Normal   Pulled          42m                   kubelet            Successfully pulled image "maho/webapl:0.1" in 5.272s (5.272s including waiting). Image size: 51079110 bytes.
  Warning  Unhealthy       39m                   kubelet            Readiness probe failed: Get "http://10.244.0.18:3000/ready": dial tcp 10.244.0.18:3000: connect: connection refused
  Normal   Created         35m (x6 over 42m)     kubelet            Created container: webapl
  Normal   Started         35m (x6 over 42m)     kubelet            Started container webapl
  Normal   Pulled          23m (x8 over 40m)     kubelet            Container image "maho/webapl:0.1" already present on machine
  Warning  Unhealthy       21m (x11 over 41m)    kubelet            Readiness probe failed: HTTP probe failed with statuscode: 500
  Normal   Pulling         15m                   kubelet            Pulling image "johoo54/webapl:0.1"
  Warning  Unhealthy       11m (x37 over 41m)    kubelet            Liveness probe failed: HTTP probe failed with statuscode: 500
  Normal   Killing         11m (x13 over 41m)    kubelet            Container webapl failed liveness probe, will be restarted
  Warning  BackOff         6m44s (x75 over 32m)  kubelet            Back-off restarting failed container webapl in pod webapl_default(cdd4de9d-dddb-464a-927b-3148e19751cc)
  Normal   Pulled          5m22s (x5 over 13m)   kubelet            Container image "johoo54/webapl:0.1" already present on machine
  Normal   SandboxChanged  114s                  kubelet            Pod sandbox changed, it will be killed and re-created.
  Warning  Unhealthy       54s (x3 over 64s)     kubelet            Liveness probe failed: HTTP probe failed with statuscode: 500
  Normal   Killing         54s                   kubelet            Container webapl failed liveness probe, will be restarted
  Normal   Pulled          24s (x2 over 109s)    kubelet            Container image "johoo54/webapl:0.1" already present on machine
  Normal   Created         24s (x2 over 109s)    kubelet            Created container: webapl
  Normal   Started         24s (x2 over 108s)    kubelet            Started container webapl
  Warning  Unhealthy       4s (x3 over 94s)      kubelet            Readiness probe failed: HTTP probe failed with statuscode: 500
```

- 해석: 쿠버네티스가 제대로 동작하고 있음
이 이벤트 로그는 Pod의 생애 주기 동안 헬스체크(리드니스, 라이브니스)와 관련된 문제들이 발생하여 컨테이너가 재시작되고 있는 상황을 보여줘요. 각 이벤트의 의미를 단계별로 분석하면 다음과 같습니다:

1. 초기 스케줄링 및 이미지 풀링

•	Scheduled & Pulling & Pulled

•	default-scheduler가 Pod를 minikube 노드에 할당했고,

•	지정된 이미지 "maho/webapl:0.1"을 정상적으로 풀링해 컨테이너를 생성 및 시작했습니다.

2. Readiness Probe 실패 (초기)

•	Warning: Unhealthy - Readiness probe failed: connection refused

•	초기에는 /ready 엔드포인트에 접근 시 연결이 거부(refused)된 것으로 보입니다.

•	이는 애플리케이션이 아직 준비되지 않았거나 포트가 열리지 않았기 때문일 수 있습니다.

3. 컨테이너 생성 및 재시작 반복

•	Created & Started

•	여러 차례 컨테이너가 생성되고 시작되었음을 알 수 있습니다.

•	Warning: Unhealthy - Readiness probe failed: HTTP probe failed with statuscode: 500

•	일정 시간이 지난 후에도 Readiness Probe가 HTTP 500 에러를 반환하고 있습니다.

•	이는 애플리케이션의 /ready 핸들러에서 20초 이전에는 500 상태를 반환하도록 설계된 점과 연관될 수 있음.

4. 이미지 변경 시도

•	Pulling image “johoo54/webapl:0.1”

•	어느 시점에 "johoo54/webapl:0.1" 이미지로 변경하여 풀링을 시도하는 이벤트가 발생했어요.

•	이는 이전 이미지(maho/webapl:0.1) 대신 다른 이미지로 교체했음을 의미합니다.

5. Liveness Probe 실패 및 컨테이너 재시작

•	Warning: Unhealthy - Liveness probe failed: HTTP probe failed with statuscode: 500

•	Liveness Probe도 HTTP 500 응답을 받아 실패하고, 그 결과 컨테이너가 재시작됩니다.

•	Killing & BackOff

•	Liveness Probe 실패로 인해 컨테이너가 여러 번 종료되고 재시작되다가, 결국 “Back-off restarting failed container” 메시지로 컨테이너가 재시작되지 않는 상태에 이릅니다.

•	Back-off는 일정 시간 간격을 두고 재시작 시도를 하는데, 반복 실패 후 점점 대기시간이 늘어나는 상황을 의미합니다.

6. 최종 상황

•	최근 이벤트에서는 여전히 Liveness Probe 실패와 Readiness Probe 실패가 반복되며, 컨테이너가 재시작되고 있습니다.

•	로그에 따르면 /healthz (라이브니스)와 /ready (리드니스) 핸들러가 계속 HTTP 500 상태를 반환하고 있어, 애플리케이션 상태가 정상적으로 개선되지 않은 상태입니다.

종합 분석

•	Readiness Probe:

•	초반에는 포트 연결 거부(connection refused) 문제가 있었으나, 이후에는 500 상태를 반환하는 것으로 변경됨.

•	이는 애플리케이션이 준비 상태가 되지 않았음을 의미하며, 서비스에 트래픽을 전달하지 않게 됩니다.

•	Liveness Probe:

•	40초 이후 의도된 동작대로 500 상태를 반환하여 컨테이너가 재시작되도록 유도하고 있습니다.

•	그러나 계속 반복되는 실패와 재시작으로 인해 Back-off 상태에 진입하게 되었습니다.

•	이미지 변경:

•	중간에 이미지가 "maho/webapl:0.1"에서 "johoo54/webapl:0.1"로 변경된 것이 보이는데, 이는 테스트나 배포 과정에서 새로운 버전의 이미지를 사용하려는 시도일 수 있습니다.

결론

이 로그는 헬스체크 프로브 설정에 따라 애플리케이션의 /healthz와 /ready 엔드포인트가 의도된 대로 동작하고 있음을 보여주지만, 실제로는 계속해서 HTTP 500 상태를 반환하여:

•	Readiness Probe: 초기화 이후에도 실패 상태로 남아 서비스 트래픽이 전달되지 않음.

•	Liveness Probe: 40초 이후 실패로 인해 컨테이너가 반복적으로 재시작되고, 결국 재시작이 Back-off 상태로 이어짐.

따라서, 애플리케이션의 헬스체크 핸들러가 의도한 동작(예: 초기 준비 상태와 일정 시간이 지난 후 재시작)을 올바르게 시뮬레이션하고 있는지, 그리고 그에 따라 Kubernetes가 올바르게 대응하는지를 확인할 수 있습니다. 추가로, 실제 운영 환경에서는 이러한 헬스체크 조건이 적절한지, 또는 로직을 수정해야 하는지를 검토할 필요가 있습니다.

### 의문: Liveness Probe vs Readiness Probe

Kubernetes에서 Liveness Probe와 Readiness Probe는 각각 다른 목적을 가지고 있어요. 아래에서 차이점을 정리하고, 의문을 해결해볼게요.

🔹 Liveness Probe (생존 확인)

목적: 컨테이너가 정상적으로 실행되고 있는지 확인

실패하면: 컨테이너를 재시작함

📌 언제 사용?

•	컨테이너가 응답하지 않는 상태(Hang, Deadlock 등) 가 되었을 때 자동으로 재시작

•	애플리케이션이 완전히 멈추거나, 더 이상 정상적으로 동작하지 않는 경우 감지

📌 예제 (코드와 연결해서 이해)

이전에 사용한 webapl.js 코드에서:

```plain text
app.get('/healthz', function (request, response) {
    var msec = Date.now() - start
    var code = 200
    if (msec > 40000) {  // 40초가 지나면 500 반환
        code = 500
    }
    console.log('GET /healthz ' + code)
    response.status(code).send('OK')
})
```

•	처음 40초 동안은 HTTP 200을 반환 → 정상적으로 동작

•	40초 이후 HTTP 500을 반환 → Liveness Probe 실패 → Kubernetes가 컨테이너 재시작

📌 Liveness Probe 동작 방식

1.	/healthz 경로에 요청

2.	HTTP 200이면 정상, 500이면 실패

3.	실패하면 Kubernetes가 컨테이너를 재시작함

🔹 Readiness Probe (준비 상태 확인)

목적: 애플리케이션이 트래픽을 받을 준비가 되었는지 확인

실패하면: 해당 Pod는 서비스에서 제외되며, 트래픽을 받지 않음 (재시작하지 않음)

📌 언제 사용?

•	애플리케이션이 초기화 중이거나, 특정 작업이 끝날 때까지 트래픽을 받지 않아야 할 때

•	DB 연결, 설정 로드 등 준비가 완료되기 전에는 클라이언트 요청을 받으면 안 되는 경우

📌 예제 (코드와 연결해서 이해)

이전에 사용한 webapl.js 코드에서:

```plain text
app.get('/ready', function (request, response) {
    var msec = Date.now() - start
    var code = 500
    if (msec > 20000) {  // 20초가 지나야 200 반환
        code = 200
    }
    console.log('GET /ready ' + code)
    response.status(code).send('OK')
})
```

•	시작 후 20초 동안 HTTP 500 반환 → Readiness Probe 실패 → 트래픽 받지 않음

•	20초 이후 HTTP 200 반환 → Readiness Probe 성공 → 트래픽 받기 시작

📌 Readiness Probe 동작 방식

1.	/ready 경로에 요청

2.	HTTP 200이면 트래픽을 받을 준비 완료 → 서비스에 추가됨

3.	HTTP 500이면 아직 준비되지 않음 → 트래픽에서 제외됨

🔹 Liveness Probe vs Readiness Probe 비교

🔹 의문 해결: 왜 둘 다 필요한가?

1.	Readiness Probe가 없으면?

•	애플리케이션이 아직 준비되지 않았는데 클라이언트 요청을 받을 수도 있음

•	초기 설정이 필요한 애플리케이션(DB 연결 등)에서는 요청이 실패할 가능성이 높음

2.	Liveness Probe가 없으면?

•	애플리케이션이 죽거나 무한 루프에 빠져도 Kubernetes가 감지하지 못해 계속 서비스됨

•	사용자가 직접 Pod를 재시작해야 할 수도 있음

3.	같은 엔드포인트를 사용하면 안 되나?

•	가능하지만 권장되지 않음

•	Readiness Probe는 일시적인 준비 상태 확인, Liveness Probe는 지속적인 상태 확인이 목적이기 때문에 구분해서 설정하는 것이 좋음

🔹 최종 결론

•	Readiness Probe는 초기 준비 상태를 확인하여, 준비되지 않은 Pod에 트래픽을 전달하지 않음.

•	Liveness Probe는 컨테이너가 비정상 상태에 빠졌을 때 자동 재시작하여 복구 가능하게 함.

•	둘 다 설정하면 트래픽 손실을 최소화하고 안정적인 서비스 운영이 가능함.

✅ Readiness Probe는 “준비될 때까지 트래픽을 안 주는 것”

✅ Liveness Probe는 “죽으면 컨테이너를 다시 시작하는 것”



