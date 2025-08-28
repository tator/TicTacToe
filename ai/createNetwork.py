import random
import json
import numpy as np

class CreateNework():

    @staticmethod
    def create():
        w1 = np.array([[random.random()*2-1 for _ in range(9)] for _ in range(36)])
        b1 = np.array([random.random()*2-1 for _ in range(36)])
        w2 = np.array([[random.random()*2-1 for _ in range(36)] for _ in range(36)])
        b2 = np.array([random.random()*2-1 for _ in range(36)])
        w3 = np.array([[random.random()*2-1 for _ in range(36)] for _ in range(9)])
        b3 = np.array([random.random()*2-1 for _ in range(9)])
        
        data = {
            "w1": w1.tolist(),
            "b1": b1.tolist(),
            "w2": w2.tolist(),
            "b2": b2.tolist(),
            "w3": w3.tolist(),
            "b3": b3.tolist()
        }

        with open("ai/Network.json", "w") as f:
            json.dump(data,f,indent=4)
