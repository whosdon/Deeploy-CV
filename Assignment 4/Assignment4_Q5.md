1. Initialize weights \( W^l \) and biases \( b^l \) for all layers \( l = 1, ..., K+1 \).
2. For each training example \( (x, y) \):
   3. **Forward Pass**:
      4. Set \( a^0 = x \).
      5. For \( l = 1 \) to \( K+1 \):
         6. Compute \( z^l = W^l a^{l-1} + b^l \).
         7. Compute \( a^l = \sigma(z^l) \).
   8. **Compute Loss**:
      9. Compute \( \mathcal{L} = \frac{1}{2} \| a^{K+1} - y \|^2 \).
   10. **Backpropagation**:
       11. Compute \( \delta^{K+1} = (a^{K+1} - y) \odot \sigma'(z^{K+1}) \).
       12. For \( l = K \) down to \( 1 \):
           13. Compute \( \delta^l = ((W^{l+1})^T \delta^{l+1}) \odot \sigma'(z^l) \).
           14. Compute gradients:
               15. \( \frac{\partial \mathcal{L}}{\partial W^l} = \delta^l (a^{l-1})^T \).
               16. \( \frac{\partial \mathcal{L}}{\partial b^l} = \delta^l \).
   17. **Update Weights and Biases**:
       18. For \( l = 1 \) to \( K+1 \):
           19. \( W^l = W^l - \eta \frac{\partial \mathcal{L}}{\partial W^l} \).
           20. \( b^l = b^l - \eta \frac{\partial \mathcal{L}}{\partial b^l} \).
