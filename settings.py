"""Module for project hyper parameters"""

ENV_PATH = './data/Tennis.app'
ACTOR_NETWORK_LINEAR_SIZES = "512,256"
CRITIC_NETWORK_LINEAR_SIZES = "512,256"
CRITIC_SECOND_NETWORK_LINEAR_SIZES = "512,256"
WARM_UP_STEPS = 0
ACTOR_LEARNING_RATE = 1e-3
CRITIC_LEARNING_RATE = 1e-3
CRITIC_UPDATE_EVERY = 1
POLICY_UPDATE_EVERY = 1
BUFFER_SIZE = int(2e6)          # replay buffer size
BATCH_SIZE = 512               # minibatch size
UPDATE_EVERY = 1               # how often to update the network
GAMMA = 0.98                    # discount factor
TAU = 1e-3                      # for soft update of target parameters
CRITIC_BATCH_NORM = True        # apply batch norm for critic network
ACTOR_BATCH_NORM = True         # apply batch norm for actor network
LEARN_TIMES = 1
CRITIC_GRADIENT_CLIPPING_VALUE = 0
ACTOR_GRADIENT_CLIPPING_VALUE = 0

def printvars():
   tmp = globals().copy()
   [print(k,' = ',v) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

printvars()