# Rainbow
레인보우에서는 DQN의 6가지 변형 알고리즘을 실험하고, 알고리즘들의 조합을 연구한다. 이런 조합들을 통해서 아타리
게임에서 최고 기록을 기록했다. 

## DQN의 발전
DQN이 나온 이후 연속적이고 복잡한 문제에 대해 빠른 시작점이 되어 왔고 그로 인해 강화 학습 확대에 많은 영향을 주었다. 
DQN은 Q-learning과 CNN(Convolutional Neural Network)과 결합하고, Experience Replay을 사용해 큰 성능 향상을
이끌었다. 
#### DQN의 확장 알고리즘 6가지
    - Double DQN: Q-learning의 overestimation 문제를 해결
    - Perioritized experience replay: 리플레이 버퍼에서 데이터 샘플링시 우선 순위를 부여해 데이터 효율을 높임. 
    - Dueling Network: action을 value와 action advantage를 분리 함으로써 모델 개선
    - A3C:
    - Distributional Q-Learning: Retrun값을 일반적으로 사용하는 평균이 아닌 categorical distribution으로 학습 
    - Noisy Network: 웨이트에 Noisy를 추가함으로써 exploration을 더 잘 할 수 있게 개선 

## 레인보우 
레인보우는 DQN에서 위 6가지 요소들을 하나로 결합.

### Step 1. Multi-step distributinonal loss: 1-step distibutional loss를 multi-step variant로 대체
    : target distiribution은 value distribution을 cumulative discount에 따라서 $S_{t+n}$으로 구성하고 `n-step`
    discounted return으로 이동한다.
### Step 2. Combine Multi-step distributinonal loss with Double Q-learning  
    

# References
- https://brunch.co.kr/@chris-song/102