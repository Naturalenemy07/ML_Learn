import math

class Node:
    ''' The node is a unit used to build a layer in ML model

    Attributes:
        input_vector: A list of values indicating the inputs to the node class.
        weights: A list of values that is applied to each input value.
        bias: a float that is used at the end of a forward propogation operation for the node.
        value: a float representing the output value of the node following forward propagation.
    '''
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
a = Node([],[],0,0)
