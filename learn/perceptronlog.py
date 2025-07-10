import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.01, n_iter=100):
        self.lr = learning_rate
        self.epochs = n_iter
        self.wt = None
        self.bi = None

    def init_weight_bias(self, num_x):
        self.wt = np.zeros(num_x)
        self.bi = 0
        print("initil weights and bias => ", self.wt, self.bi)

    def neuron(self, x):
        return np.dot(self.wt, x) + self.bi

    def activation_func(self, x):
        return 1 if x >= 0 else 0

    def propagate(self, x):
        linear_output = self.neuron(x)
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def calc_error(self, y_target, y_pred):
        print("-------eror is: ", y_target - y_pred)
        return y_target - y_pred

    def update_weight_bias(self, x, yt, yp):
        updt = self.lr * self.calc_error(yt, yp)
        print("------update to: ", updt)
        self.wt += updt * x
        self.bi += updt
        print(f"after update-> weight={self.wt}, bias={self.bi}")

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.init_weight_bias(n_features)

        for i in range(self.epochs):
            print("\n iteraion..............", i)
            all_correct = True
            for idx, x in enumerate(X):
                y_predicted = self.propagate(x)
                print(f"in_data={x} (actual,pred)=({y[idx]},{y_predicted})")
                self.update_weight_bias(x, y[idx], y_predicted)
                # Check if the prediction was incorrect
                if y_predicted != y[idx]:
                    all_correct = False
            # If all predictions are correct, stop training
            if all_correct:
                print(f"Training stopped early at epoch {i + 1}")
                break

    def predict(self, X):
        predictions = []
        for x in X:
            predictions.append(self.propagate(x))
        print(predictions)
        return np.array(predictions)


# Sample data (AND problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND is linearly separable

print("data is====", X)
perceptron = Perceptron(learning_rate=0.1, n_iter=10)
perceptron.fit(X, y)
predictions = perceptron.predict(X)
print(predictions)


"""
output log.......................



data is==== [[0 0]
 [0 1]
 [1 0]
 [1 1]]
initil weights and bias =>  [0. 0.] 0

 iteraion.............. 0
in_data=[0 0] (actual,pred)=(0,1)
-------eror is:  -1
------update to:  -0.1
after update-> weight=[0. 0.], bias=-0.1
in_data=[0 1] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0. 0.], bias=-0.1
in_data=[1 0] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0. 0.], bias=-0.1
in_data=[1 1] (actual,pred)=(1,0)
-------eror is:  1
------update to:  0.1
after update-> weight=[0.1 0.1], bias=0.0

 iteraion.............. 1
in_data=[0 0] (actual,pred)=(0,1)
-------eror is:  -1
------update to:  -0.1
after update-> weight=[0.1 0.1], bias=-0.1
in_data=[0 1] (actual,pred)=(0,1)
-------eror is:  -1
------update to:  -0.1
after update-> weight=[0.1 0. ], bias=-0.2
in_data=[1 0] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.1 0. ], bias=-0.2
in_data=[1 1] (actual,pred)=(1,0)
-------eror is:  1
------update to:  0.1
after update-> weight=[0.2 0.1], bias=-0.1

 iteraion.............. 2
in_data=[0 0] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.2 0.1], bias=-0.1
in_data=[0 1] (actual,pred)=(0,1)
-------eror is:  -1
------update to:  -0.1
after update-> weight=[0.2 0. ], bias=-0.2
in_data=[1 0] (actual,pred)=(0,1)
-------eror is:  -1
------update to:  -0.1
after update-> weight=[0.1 0. ], bias=-0.30000000000000004
in_data=[1 1] (actual,pred)=(1,0)
-------eror is:  1
------update to:  0.1
after update-> weight=[0.2 0.1], bias=-0.20000000000000004

 iteraion.............. 3
in_data=[0 0] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.2 0.1], bias=-0.20000000000000004
in_data=[0 1] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.2 0.1], bias=-0.20000000000000004
in_data=[1 0] (actual,pred)=(0,0)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.2 0.1], bias=-0.20000000000000004
in_data=[1 1] (actual,pred)=(1,1)
-------eror is:  0
------update to:  0.0
after update-> weight=[0.2 0.1], bias=-0.20000000000000004
Training stopped early at epoch 4
[0, 0, 0, 1]
[0 0 0 1]

"""
