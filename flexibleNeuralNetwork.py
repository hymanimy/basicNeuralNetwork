from matrixClass import *
import math
import matplotlib.pyplot as plt

def sigmoid(x):
    # Classic activation function
    return 1/(1 + math.e**-x)

def dsigmoid(y):
    # Derivative of Sigmoid function
    # sigmoid(x) = sigmoid(x) * (1 - sigmoid(x)), but since in backprop method
    # the outputs have already had sigmoid applied to them,
    # we simply do the input * (1 - input). DO NOT SIGMOID AGAIN
    return y * (1 - y)

class neuralNetwork:
    def __init__(self, nodes):
        #pass an array of integers, where nodes[0] = numOfInputs
        #nodes[1] = numOfHidden1 etc...
        self.nodes = nodes
        self.layers = len(nodes)

        #self.weights is an array of weight matrices where self.weights[i] refers to the weight matrix between ith and (i + 1 )th layer
        #e.g. self.weights[0] is the weight matrix between input and hidden1 layer
        self.weights = [randMatrix(nodes[i + 1], nodes[i]) for i in range(self.layers - 1)]
        self.biases = [randMatrix(nodes[i + 1], 1) for i in range(self.layers - 1)]

        #activation function
        self.activation = sigmoid
        self.activation_derivative = dsigmoid
        self.learning_rate = 2

    def feedforward(self, input):
        #output holds the output vector of the current layer, at first the output of the 1st layer is the input
        output = input
        if(len(input.m) == self.nodes[0]):
            for i in range(self.layers - 1):
                #update the output and loop until final layer
                # weighted sum with biases can be achieved using dot product and matrices
                output = (self.weights[i].dot(output) + self.biases[i]).apply(self.activation)
            return output
        else:
            print("Input vector must have same number of elements as the input nodes. Require " + str(self.nodes[0]) + " nodes.")

    def backprop(self, input, target):
        #outputs is an array of every layers' outputs. outputs[0] = input, outputs[1] = hidden1_output etc...
        outputs = [input]

        #Feedforward and record every layers outputs
        for i in range(self.layers - 1):
            outputs.append( (self.weights[i].dot(outputs[i]) + self.biases[i]).apply(self.activation) )

        #record all error vectors in array.
        #for an L layered network, there will be L-1 error vectors, since input nodes have no error

        #Calculate final layer error
        errors = [outputs[-1].apply(self.activation_derivative) * (outputs[-1] - target)]

        #Backpropogate error from k+1th layer to find kth layers error
        for i in range(self.layers - 2):
            errors.append(outputs[-(2 + i)].apply(self.activation_derivative) * ((self.weights[-(1 + i)].transpose().dot(errors[i]))))

        # Reverse the errors array since we want errors[0] = hidden1_errors
        errors = errors[::-1]


        # Create gradient lists, gradient is the errors DOT outputs(transposed)
        # Gradients are a matrix of partial derivatives of the error function with respect to the specific weight
        #Transposing creates a matrix of these partial derivatives

        gradients = []

        for i in range(self.layers - 1):
            #recall output[i] is the ith layers output, but errors[i] is i+1th layers error, since the input layer has no errors
            #thus errors[0] is hidden1 yet output[0] is inputs.
            gradients.append(errors[i].dot(outputs[i].transpose()))

        #update the weights by subtracting a scaled version of the gradient, to minimise error
        #update the biases by subtracting a scaled version of the error, to minimise error
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] - gradients[i] * self.learning_rate
            self.biases[i] = self.biases[i] - errors[i] * self.learning_rate

    def error(self, input, target):
        predicted = self.feedforward(input)
        return ((predicted - target).apply(lambda x : x ** 2) * 0.5).average()

#Initialise neuralNetwork, and training + target data
nn = neuralNetwork([2,4,4,1])

x0 = listToMatrix([0,0])
y0 = listToMatrix([0])

x1 = listToMatrix([1,0])
y1 = listToMatrix([1])

x2 = listToMatrix([0,1])
y2 = listToMatrix([1])

x3 = listToMatrix([1,1])
y3 = listToMatrix([0])

inp = [x0, x1, x2, x3]
targ = [y0, y1, y2, y3]

errors = []
epochs = []

# Backpropagate errors and update weights/biases
for i in range(10000):
    randIndex = int(random.random() * 4)
    nn.backprop(inp[randIndex], targ[randIndex])
    epochs.append(i)
    errors.append(nn.error(inp[randIndex], targ[randIndex]))


# Create a plot of errors vs epochs of the net.

plt.plot(epochs, errors)
plt.xlabel("Epochs")
plt.ylabel("Average Network Error")
plt.title("Average error vs epochs")
plt.show()
