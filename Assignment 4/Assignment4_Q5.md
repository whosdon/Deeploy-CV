1. Initialize weights and biases randomly for each layer.
2. For each training example (x, y):
    - a. Perform forward propagation: Calculate activations for each layer.
    - b. Calculate the error at the output layer (loss).
    - c. Perform backward propagation: Calculate gradients for weights and biases.
    - d. Update weights and biases using the gradients and learning rate.
3. Repeat for multiple epochs until convergence.