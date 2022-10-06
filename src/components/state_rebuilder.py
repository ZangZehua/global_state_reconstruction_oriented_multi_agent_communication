import torch.nn as nn


class BaseStateRebuilder(nn.Module):
    def __init__(self, obs_dim, state_dim):
        super(BaseStateRebuilder, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, 1024),
            nn.ReLU(),
            nn.Linear(1024, 2048),
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, state_dim)
        )

    def forward(self, obs):
        state = self.net(obs)
        return state

