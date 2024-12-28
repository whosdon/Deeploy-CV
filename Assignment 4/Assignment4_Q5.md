# Backpropagation Algorithm Pseudocode

1. Initialize weights (W^l) and biases (b^l) for all layers (l = 1 to K+1).
2. For each training example (x, y):
   3. **Forward Pass**:
      4. Set a^0 = x (input layer activations).
      5. For each layer l = 1 to K+1:
         6. Compute z^l = W^l * a^(l-1) + b^l.
         7. Compute a^l = activation_function(z^l).
   8. **Compute Loss**:
      9. Calculate loss L = (1/2) * ||a^(K+1) - y||^2 (mean squared error loss).
   10. **Backpropagation**:
       11. Compute delta^(K+1) = (a^(K+1) - y) * activation_derivative(z^(K+1)).
       12. For each layer l = K to 1:
           13. Compute delta^l = (W^(l+1)^T * delta^(l+1)) * activation_derivative(z^l).
           14. Compute gradients:
               15. Grad_W^l = delta^l * (a^(l-1))^T.
               16. Grad_b^l = delta^l.
   17. **Update Weights and Biases**:
       18. For each layer l = 1 to K+1:
           19. Update W^l = W^l - eta * Grad_W^l.
           20. Update b^l = b^l - eta * Grad_b^l.
