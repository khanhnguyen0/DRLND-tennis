import torch
import torch.nn as nn
import torch.nn.functional as F

class Actor(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size: int, action_size:int, seed:float, linear_sizes:str, dropout:float=0, batch_normalization=True):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=dropout)
        linear_layer_sizes = linear_sizes.split(",")
        linear_layers = [nn.BatchNorm1d(state_size), nn.Linear(state_size, int(linear_layer_sizes[0])), self.relu, self.dropout]
        for i in range(1, len(linear_layer_sizes)):
            # batch_norm = nn.BatchNorm1d(int(linear_layer_sizes[i-1]))
            linear_layer_size = linear_layer_sizes[i]
            linear_layer = nn.Linear(int(linear_layer_sizes[i-1]), int(linear_layer_size))
            linear_layer.weight.data.uniform_(-3e-3, 3e-3)
            # if batch_normalization:
            #     # Add batch normalization for each layer
            #     linear_layers.append(batch_norm)
            linear_layers.extend([linear_layer, self.relu, self.dropout])
        self.linear = nn.Sequential(*linear_layers)
        self.output = nn.Linear(int(linear_layer_sizes[-1]), action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        output = self.linear(state)
        output = self.output(output)
        output = torch.tanh(output)
        return output



class Critic(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size: int, action_size:int, seed:float, linear_sizes:str, dropout:float=0, batch_normalization=True):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=dropout)
        linear_layer_sizes = linear_sizes.split(",")
        self.fc1 = nn.Linear(state_size, int(linear_layer_sizes[0]))
        linear_layers = [nn.BatchNorm1d(int(linear_layer_sizes[0]) + action_size), nn.Linear(int(linear_layer_sizes[0]) + action_size, int(linear_layer_sizes[1])), self.relu, self.dropout]
        for i in range(2, len(linear_layer_sizes)):
            # batch_norm = nn.BatchNorm1d(int(linear_layer_sizes[i-1]))
            linear_layer_size = linear_layer_sizes[i]
            linear_layer = nn.Linear(int(linear_layer_sizes[i-1]), int(linear_layer_size))
            linear_layer.weight.data.uniform_(-3e-3, 3e-3)
            # if batch_normalization:
                # Add batch normalization for each layer
                # linear_layers.append(batch_norm)
            linear_layers.extend([linear_layer, self.relu, self.dropout])
        self.linear = nn.Sequential(*linear_layers)
        self.output = nn.Linear(int(linear_layer_sizes[-1]), 1)

    def forward(self, state, action):
        """Build a network that maps state -> action values."""
        output = self.fc1(state)
        output = torch.cat([output, action], dim=1)
        output = self.linear(output)
        output = self.output(output)
        return output