import numpy as np

def calculate(list):
    ##a = np.matrix(input())
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    else:
        b = np.array(list)
        a = b.reshape(3, 3)
        mean = [[np.mean(a[:,[0]]), np.mean(a[:,[1]]), np.mean(a[:,[2]])],
[np.mean(a[0]), np.mean(a[1]), np.mean(a[2])], np.mean(a)]
        var = [[np.var(a[:,[0]]), np.var(a[:,[1]]), np.var(a[:,[2]])], [np.var(a[0]), np.var(a[1]), np.var(a[2])], np.var(a)]
        sd = [[np.std(a[:,[0]]), np.std(a[:,[1]]), np.std(a[:,[2]])], [np.std(a[0]), np.std(a[1]), np.std(a[2])], np.std(a)]
        max = [[np.max(a[:,[0]]), np.max(a[:,[1]]), np.max(a[:,[2]])], [np.max(a[0]), np.max(a[1]), np.max(a[2])], np.max(a)]
        min = [[np.min(a[:,[0]]), np.min(a[:,[1]]), np.min(a[:,[2]])], [np.min(a[0]), np.min(a[1]), np.min(a[2])], np.min(a)]
        sum = [[np.sum(a[:,[0]]), np.sum(a[:,[1]]), np.sum(a[:,[2]])], [np.sum(a[0]), np.sum(a[1]), np.sum(a[2])], np.sum(a)]
        calculations = {
            'mean': mean, 
            'variance': var, 
            'standard deviation': sd, 
            'max': max, 
            'min': min, 
            'sum': sum 
        }
        return calculations