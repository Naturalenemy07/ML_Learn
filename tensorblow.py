import math

class Node: 
    def __init__(self, input_vector = [], weights = [], bias = 0.0, value = 0.0):
        self.value = value
        self.weights = weights
        self.bias = bias
        self.input_vector = input_vector

    def value(self):
        return self.value
    
    def forward_propagation(self):
        temp_sum = 0
        end = len(self.input_vector)
        for i in range(end):
            temp_sum += self.input_vector[i] * self.weights[i]
        return temp_sum + self.bias
    
class Layer:
    def __sig(self, temp_value):
        return (1 / (1 + math.e ** temp_value))
    
    def __relu(self, temp_value):
        return max(0, temp_value)
    
    def __create_layer(self):
        for i in range(self.size):
            self.layer.append(Node(value=1, weights=1))

    def __init__(self, size):
        self.layer = []
        self.size = size
        self.__create_layer()

    def print_layer(self):
        for i in self.layer:
            print(i.value)

X = [2,4,3]
hidden_layer = Layer(X, size=1)
hidden_layer.print_layer()

# print(type(hidden_layer.layer[0].calc_value()))
