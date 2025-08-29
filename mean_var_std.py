def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain exactly 9 numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    functions = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
    results = {}
    for name, func in functions.items():
        results[name] = [
            func(arr, axis=0).tolist(),
            func(arr, axis=1).tolist(),
            func(arr).tolist()
        ]
    
    return results
