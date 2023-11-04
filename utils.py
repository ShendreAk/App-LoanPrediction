import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class Predict:
    def __init__(self,list):
        with open("/Users/akshayshendre/Desktop/Apploan/models/model.h5", "rb") as file:
            model = load_model(file)
    