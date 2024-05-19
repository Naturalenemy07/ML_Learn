import math

class Node:
    def __check_inputs(self):
        # if len(self.weight) != len(self.inputs):
        #     raise IndexError
        pass
    
    def __sig(self, temp_value):
        return (1 / (1 + math.e ** temp_value))
    
    def __relu(self, temp_value):
        return max(0, temp_value)

    def __init__(self, weights = [], bias = 0.0, value = 0.0):
        self.value = value
        self.weights = weights
        self.bias = bias
        self.__check_inputs()        

    
    def print_value(self):
        print(self.value)
        return
    
    def calc_value(self):
        temp_sum = 0
        end = len(self.inputs)
        for i in range(end):
            temp_sum += self.inputs[i] * self.weight[i]
        if self.acti == 'sig':
            return self.__sig(temp_sum - self.bias)
        elif self.acti == 'relu':
            return self.__relu(temp_sum - self.bias)
    
class Layer:
    def __create_layer(self):
        for i in range(self.size):
            self.layer.append(Node())

    def __init__(self, size):
        self.size = size
        self.layer = []
        self.__create_layer()
    
    def print_layer(self):
        for i in self.layer:
            print(i.value)
        

# first_layer = Layer(3)
# first_layer.print_layer()

input = [2, 4]
