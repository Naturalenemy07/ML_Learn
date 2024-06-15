import math
import random

class Node:
    ''' The node is a unit used to build a layer in ML model

    Attributes:
        input_vector: A list of values indicating the inputs to the node class.
        weights: A list of values that is applied to each input value.
        bias: a float that is used at the end of a forward propogation operation for the node.
        value: a float representing the output value of the node following forward propagation.
    '''
    def __weights_gen(self):
        'Generates weights as random floats between 0 and 1'
        temp_weights = []
        for i in range(len(self.input_vector)):
            temp_weights.append(random.random())
        return temp_weights

    def __init__(self, input_vector = [], bias = 0.0, value = 0.0, input_node = 0):
        'Initialize Node class'
        self.value = value
        self.bias = bias
        self.input_vector = input_vector
        self.weights = self.__weights_gen()
        self.input_node = input_node
    
    def calc_value(self):
        'Calculate dot product of weights and inputs'
        temp_sum = 0
        end = len(self.input_vector)
        for i in range(end):
            temp_sum += self.input_vector[i] * self.weights[i]
        self.value = temp_sum + self.bias
        return self.value
    
    def print_weights(self):
        print(self.weights)

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
        print('sig')
        return (1 / (1 + math.e ** input_value))
    
    def __relu(self, input_value):
        'Returns zero if input is negative, or input is positive'
        return max(0, input_value)
    
    def __create_layer(self):
        'Creates layer'
        if self.typeL == 0:
            'input layer'
            self.layer = self.inputs
        else:
            'hidden and output layer'
            for i in range(self.layer_size):
                self.layer.append(Node(input_vector=self.inputs, value=1))


    def print_layer(self):
        'Prints layer values'
        for i in self.layer:
            print("Values:",i.value)
            print("Weights:", i.weights)
    
    def forward(self):
        'determines value of each Node in layer using Node class'
        if self.typeL == 0:
            for item in self.layer:
                self.output.append(item)
        else:
            for item in self.layer:
                temp_value = item.calc_value()
                if self.activation == 'relu':
                    self.output.append(self.__relu(temp_value))
                elif self.activation == 'sig':
                    self.output.append(self.__sig(temp_value))
        return self.output

    def __init__(self, typeL, layer_size, inputs = [], activation = 'relu'):
        'initializes the layer'
        self.typeL = typeL
        self.layer = []
        self.inputs = inputs
        self.layer_size = layer_size
        self.output = []
        self.activation = activation
        self.__create_layer()

class Network:
    '''
    A collection of layers and nodes
    '''
    def __init__(self, layers, inputs):
        self.layers = layers
        self.inputs = inputs 

    def input(self):
        pass


X = [2,3]
Y = [1,0]

inputLayer = Layer(typeL = 0, layer_size=len(X), inputs=X)
hiddenLayer = Layer(typeL = 1, layer_size=3, inputs=inputLayer) # a bug exists when calling forward() with input layer as the input layer is a list-not Node
hiddenLayer1 = Layer(typeL= 1, layer_size=3, inputs=hiddenLayer.forward())
outputLayer = Layer(typeL = 1, layer_size=len(Y), inputs=hiddenLayer1.forward())

inputLayer.print_layer()

# class Test:
#     def __init__(self, other_numb, numb = 1):
#         self.other_numb = other_numb
#         self.numb = numb

#     def printNumb(self):
#         print('numb:', self.numb)
#         print('other numb:', self.other_numb)

# a = Test(other_numb = 1)
# a.printNumb()
