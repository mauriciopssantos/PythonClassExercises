import numpy as np
X = np.array([1,2,3]).reshape((1,-1))
Y = np.array([2,2,3,]).reshape((1,-1))
if X.size == Y.size:
    greaterA = np.greater(X,Y)
    greaterEqualA = np.greater_equal(X,Y)
    lessA = np.less(X,Y)
    lessEqualA = np.less_equal(X,Y)
else: 
    raise Exception