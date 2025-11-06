import numpy as np


class HebbianNetwork:
    def __init__(self, input_size, output_size):
        self.wt = np.zeros(2)
        self.bi = 0
        print(f"w={self.wt}, b={self.bi}")

    def train(self, X, y):
        for i in range(len(X)):
            print(f"iter{i}--processing {X[i]}")
            t = np.dot(self.wt, X[i]) + self.bi
            y_p = 1 if t >= 0 else -1
            print(f"y={y[i]}, pred={t}->{y_p}")
            self.wt += X[i] * y[i]
            self.bi += y[i]
            print(f"weight={self.wt}, bias={self.bi}")

    def predict(self, X):
        l = []
        for i in range(len(X)):
            t = np.dot(self.wt, X[i]) + self.bi
            y_p = 1 if t >= 0 else -1
            l.append(y_p)
        return l


# Example usage

# Define input and output patterns
X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
y = np.array([-1, -1, -1, 1])

print("\n now for AND logic______\n", X, y)
network = HebbianNetwork(input_size=2, output_size=1)
network.train(X, y)
print("final prediction=", network.predict(X))


print("\n now for OR logic______\n", X, y)

# Define input and output patterns
X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
y = np.array([-1, 1, 1, 1])
network.train(X, y)
print("final prediction=", network.predict(X))


""" 
output 
```````````````````````````````````````````````````````````````
 now for AND logic______
 [[-1 -1]
 [-1  1]
 [ 1 -1]
 [ 1  1]] [-1 -1 -1  1]
w=[0. 0.], b=0
iter0--processing [-1 -1]
y=-1, pred=0.0->1
weight=[1. 1.], bias=-1
iter1--processing [-1  1]
y=-1, pred=-1.0->-1
weight=[2. 0.], bias=-2
iter2--processing [ 1 -1]
y=-1, pred=0.0->1
weight=[1. 1.], bias=-3
iter3--processing [1 1]
y=1, pred=-1.0->-1
weight=[2. 2.], bias=-2
final prediction= [-1, -1, -1, 1]

 now for OR logic______
 [[-1 -1]
 [-1  1]
 [ 1 -1]
 [ 1  1]] [-1 -1 -1  1]
iter0--processing [-1 -1]
y=-1, pred=-6.0->-1
weight=[3. 3.], bias=-3
iter1--processing [-1  1]
y=1, pred=-3.0->-1
weight=[2. 4.], bias=-2
iter2--processing [ 1 -1]
y=1, pred=-4.0->-1
weight=[3. 3.], bias=-1
iter3--processing [1 1]
y=1, pred=5.0->1
weight=[4. 4.], bias=0
final prediction= [-1, 1, 1, 1]

"""
