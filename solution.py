import pandas as pd
import numpy as np


chat_id = 970839957 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    lamda = x.sum() / (len(x) * 18)
    return lamda
