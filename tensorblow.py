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
    
    def calc_value(self):
        temp_sum = 0
        end = len(self.input_vector)
        for i in range(end):
            temp_sum += self.input_vector[i] * self.weights[i]
        self.value = temp_sum + self.bias
        return self.value

class Layer:
    def __sig(self, input_value):
        return (1 / (1 + math.e ** input_value))
    
    def __relu(self, input_value):
        return max(0, input_value)
    
    def __create_layer(self):
        for i in range(self.layer_size):
            self.layer.append(Node(input_vector=self.inputs))

    def __init__(self, layer_size, inputs = [], activation = 'relu'):
        self.layer = []
        self.inputs = inputs
        self.layer_size = layer_size
        self.output = []
        self.activation = activation
        self.__create_layer()

    def forward_propagate(self):
        for item in self.layer:
            temp_value = item.calc_value()
            self.output.append(self.__relu(temp_value))
        return self.output

    def print_layer(self):
        for i in self.layer:
            print(i.value)

X = [2,4,3]
Y = [1,1,1]
a = Node(X, Y, 2)
value = a.calc_value()
print(value)

b = Layer(layer_size=3, inputs=X)
print(b.layer_size)
