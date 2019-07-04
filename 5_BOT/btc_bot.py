import gym
import pandas as pd
import numpy as np
from gym import spaces
from sklearn import preprocessing


class BitcoinTradingEnv(gym.Env):
    #Bitcoin trading environment for openAI "gym"
    metadata = {'render.modes': ['live', 'file', 'none']}
    scaler = preprocessing.MinMaxScaler()
    viewer = None
