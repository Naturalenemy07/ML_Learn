import random

class Input_Node:
    ''' The inputs to network represented as nodes

    Attributes:
        value: a float representing the input value.
    '''
    def __init__(self, value):
        self.value = value

class Node:
    ''' The building block of a network. At this time, the class is not being used, instead the information 
        is being represented in the Layer class as matrices and vectors. Still determining how to best build 
        a network to maximize transparency-possible a node class is needed for this goal. 

    Attributes:
        value: float representing the calculated value of the node following forward propagation.
        weights: a list of floats representing the weights assigned to each input value for the node.
    '''
    def __init__(self, value, weights = []):
        self.value = value
        self.weights = weights

class Input_Layer:
    def __init__(self, input_data = []):
        self.values =  input_data

class Layer:
    def __init__(self, size, num_inputs, activation):
        self.size = size
        self.num_inputs = num_inputs
        self.activation = activation
        self.bias = self.__random_bias()
        self.values = []
        self.weights = self.__random_weights()

    def __random_weights(self):
        all_temp_weights = []
        for j in range(self.size):
            temp_weights = []
            for i in range(self.num_inputs):
                temp_weights.append(random.random())
            all_temp_weights.append(temp_weights)
        return all_temp_weights
    
    def __random_bias(self):
        temp_bias = []
        for i in range(self.size):
            temp_bias.append(random.randrange(10))
        return temp_bias

class Network:
    def __init__(self, input_data = [], labels = []):
        self.input_data = input_data
        self.labels = labels
        self.layers = []
        self.__input()

    def forward(self):
        pass

    def __input(self):
        self.layers.append(Input_Layer(self.input_data).values)

    def dense(self, size, activation):
        # temp_layer = Layer()
        pass
    
# test_layer = Layer(3, 2, 'relu')
# test_weights = test_layer.weights
# print(test_weights)

test_input = [1,2,3,4,5]
test_labels = [0,1]
test_network = Network(test_input, test_labels)
print(test_network.layers)


