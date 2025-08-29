
import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain exactly 9 numbers.")
    
    arr = np.array(list).reshape(3, 3)
    
    functions = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    

    Calculations = {}
    for name, func in functions.items():
        Calculations[name] = [

            func(arr, axis=0).tolist(),
            func(arr, axis=1).tolist(),
            func(arr).tolist()
        ]

    return calculations
 
