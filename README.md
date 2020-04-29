# basicNeuralNetwork
Basic neural network Python code. No Numpy. All built from scratch. 

Neural Network updates the weights and biases using Gradient Descent via Backpropagation. If we calculate the partial derivatives of the error function with respect to a singular weight or bias, then we subtract a scaled version of that from the weight or bias, then we can tweak them in such a way in order to minimise the error function. 

This is made more compact by employing matrices as weighted sums are equivalent to dot products of input matrices and weight matrices. 

Of course the code will be quite inefficient due to the lack of use of libraries such as Numpy which have optimised their calculations for GPUs. I wanted to make this from scratch so I could fully grasp the mathematics behind a neural network. 
