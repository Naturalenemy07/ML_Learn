import random

class Input_Node:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, value, weights):
        self.value = value
        self.weights = weights

class Input_Layer:
    def __init__(self, input_data):
        self.input_data = input_data

class Layer:
    def __init__(self, size, num_inputs, activation):
        self.size = size
        self.num_inputs = num_inputs
        self.activation = activation
        self.bias = []
        self.values = []
        self.weights = self.__random_weights()

    def __random_weights(self):
        list_all_weights = []
        for j in range(self.size):
            temp_weights = []
            for i in range(self.num_inputs):
                temp_weights.append(random.random())
            list_all_weights.append(temp_weights)
        return list_all_weights

class Network:
    def __init__(self, input_data, labels):
        self.input_data = input_data
        self.labels = labels

    def forward(self):
        pass
    
test_layer = Layer(3, 2, 'relu')
test_weights = test_layer.weights
print(test_weights)


