import math

class Node:
    ''' The node is a unit used to build a layer in ML model

    Attributes:
        input_vector: A list of values indicating the inputs to the node class.
        weights: A list of values that is applied to each input value.
        bias: a float that is used at the end of a forward propogation operation for the node.
        value: a float representing the output value of the node following forward propagation.
    '''
    def __weights_gen(self):
        'Generates weights as a list of ones'
        return [1] * len(self.input_vector)

    def __init__(self, input_vector = [], bias = 0.0, value = 0.0):
        'Initialize Node class'
        self.value = value
        self.bias = bias
        self.input_vector = input_vector
        self.weights = self.__weights_gen()
    
    def calc_value(self):
        'Calculate dot product of weights and inputs'
        temp_sum = 0
        end = len(self.input_vector)
        for i in range(end):
            temp_sum += self.input_vector[i] * self.weights[i]
        self.value = temp_sum + self.bias
        return self.value

class Layer:
    ''' The Layer is a set of nodes that undergo the same activation function before outputs
        are passed to the next layer.

    Attributes:
        layer_size: an integer representing how many nodes are in the layer.
        inputs: a list of numbers that is the input to each node in the layer.
        activation: the activation function of the layer
        _______
        output: the set of values that represent the output of each node in the layer
        layer: the set of Nodes in the layer
    '''
    def __sig(self, input_value):
        'Returns output when inputted into sigmoid function'
        return (1 / (1 + math.e ** input_value))
    
    def __relu(self, input_value):
        'Returns zero if input is negative, or input is positive'
        return max(0, input_value)
    
    def __create_layer(self):
        'Creates layer'
        for i in range(self.layer_size):
            self.layer.append(Node(input_vector=self.inputs, value=self.inputs[i]))

    def print_layer(self):
        'Prints layer values'
        for i in self.layer:
            print(i.value)
    
    def forward_propagate(self):
        'calculates dot product, feeds into activation function'
        for item in self.layer:
            temp_value = item.calc_value()
            self.output.append(self.__relu(temp_value))
        return self.output

    def __init__(self, layer_size, inputs = [], activation = 'relu'):
        'initializes the layer'
        self.layer = []
        self.inputs = inputs
        self.layer_size = layer_size
        self.output = []
        self.activation = activation
        self.__create_layer()


X = [2, 4]

inputLayer = Layer(layer_size=len(X), inputs=X)
inputLayer.print_layer()
hiddenLayer = Layer(layer_size=3, inputs = inputLayer.forward_propagate(),activation='relu')
