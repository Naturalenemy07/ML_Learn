import math

class Node: 
    def __sig(self, temp_value):
        return (1 / (1 + math.e ** temp_value))
    
    def __relu(self, temp_value):
        return max(0, temp_value)

    def __init__(self, input_vector, weight = [], bias = 0.0, value = 0.0):
        self.value = value
        self.weights = weight
        self.bias = bias
        self.input_vector = input_vector

    def print_value(self):
        print(self.value)
        return
    
    def calc_value(self):
        temp_sum = 0
        end = len(self.input_vector)
        for i in range(end):
            temp_sum += self.input_vector[i] * self.weight[i]
        if self.acti == 'sig':
            return self.__sig(temp_sum - self.bias)
        elif self.acti == 'relu':
            return self.__relu(temp_sum - self.bias)
    
class Input_Layer:
    def __create_layer(self):
        if self.size == 0:
            for i in range(self.size):
                self.layer.append(Node())
        else:
            for i in range(self.size):
                self.layer.append(Node(value=self.inda[i]))

    def __init__(self, inda = []):
        self.size = len(inda)
        self.layer = []
        self.inda = inda
        self.__create_layer()
    
    def print_layer(self):
        for i in self.layer:
            print(i.value)

class Hidden_Layer:
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
input_layer = Input_Layer(inda=X)
hidden_layer = Hidden_Layer(input_layer, size=1)
input_layer.print_layer()
hidden_layer.print_layer()

print(type(hidden_layer.layer[0].calc_value()))
