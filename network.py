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
    def __init__(self, size, activation):
        self.size = size
        self.activation = activation

class Network:
    def __init__(self, input_data, labels):
        self.input_data = input_data
        self.labels = labels
    
