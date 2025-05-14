import numpy as np
class vector_2d:
    arr = np.array([1,2,3])  
    print(arr)
    vector2 = np.array([[1,2],[3,4],[5,6]])
    print(vector2)

class vector_3d(vector_2d):

    def __init__(self):
        vector3 = np.array([
            [[1,2],[3,4]],
            [[5,6],[7,8]],
            [[9,10],[11,12]]
            ])
        print(vector3)

ob = vector_3d()
ob