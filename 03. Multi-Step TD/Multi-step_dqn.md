# Multi-Step DQN
기존의 DQN의 경우 다음 스텝의 보상이 Discount된 최대의 가치를 더해서 타겟을 값을 구했다
- DQN target  = $R_t + \gamma max q^{-}_{\theta}(S_{t+1},a')$