# (a) Distance measuring modules
Distance measuring modules are modules in ML to improve performance, whether for classification tasks or clustering.
## Euclidean distance
- A measure of the straight-line distance between two points in space.
- Generally used in clustering and nearest-neighbor algorithms.
## Mahalonobis distance 
- The Mahalanobis distance is a measure of the distance between a point and a distribution.
- Mahalanobis Distance Adapts to Non-Isotropy. If one feature varies more than another, the metric adjusts by down-weighting the impact of features with high variance.
- If two features are correlated, Mahalanobis distance accounts for this dependency using the covariance matrix which describes how much two dimensions vary together.
- High variance = smaller weight (less contribution to distance). Low variance = larger weight.
## Hamming Distance
- One more distance measuring module would be Hamming distance.
- Hamming distance is a metric that measures the number of positions where two strings or vectors of equal length differ.
- Hamming distance between two strings or vectors of equal length is the number of positions at which the corresponding symbols are different. 
- It basically measures the minimum number of substitutions required to change one string into the other.
# (b) Adam optimiser
Adaptive Moment Estimation is an algorithm for optimization technique for gradient descent. The method is really efficient when working with large problem involving a lot of data or parameters. it is a combination of the ‘gradient descent with momentum’ algorithm and the ‘RMSP’ algorithm.
## Momentum
This algorithm is used to accelerate the gradient descent algorithm by taking into consideration the ‘exponentially weighted average’ of the gradients.
## RMSP
RMSP is an adaptive learning rate optimization algorithm, it works by maintaining a moving average of the squared gradients for each parameter.
# (c) Loss Function
## L2 regularised loss
- L2 regularized loss is a technique that reduces overfitting in a ML model by adding a penalty term to the loss function. 
- The penalty term is the squared sum of the coefficients, also known as the L2 norm. 
- L2 regularization encourages weights to be small, but not exactly zero. This means that less important features will still have some influence on the final prediction, but it will be small.
## Ridge Regularisation
- Ridge regression is a method of estimating the coefficients of multiple-regression models where the independent variables are highly correlated.
- It solves this issue by adding a regularization term to the ordinary least squares objective function, which penalizes large coefficients and thus reduces their variance.
- Code file named Regression.py
# (d) Cross Entropy Loss
Cross Entropy Loss Function is a loss function that has the ability to handle complex datasets and improve model accuracy.
## Binary
This is used when there are only two classes in the dataset. It is commonly used in binary classification problems. 
## Categorical
This is used when there are more than two classes in the dataset. It is commonly used in multi-class classification problems.
# (e) Activation layer
An activation layer is a component of a neural network that uses an activation function to transform a node's input signal into an output signal that is passed on to the next layer.
## Softmax
- The softmax activation layer transforms the outputs from the last dense layer of a neural network into a probability distribution.
- Generally considered as the most popular activation layer.
## Sigmoid
- Sigmoid Activation Function is characterized by ‘S’ shape. It is mathematically defined as A=1/(1+e^-x)
- It allows neural networks to handle and model complex patterns that linear equations cannot.
## Tanh
- Tanh function or hyperbolic tangent function, is a shifted version of the sigmoid, allowing it to stretch across the y-axis.
-  Enables modeling of complex data patterns.
# (f) Learning rate 
- Learning rate isa hyperparameter in ML that controls how much a model adjusts its parameters at each step of optimization.
-  The goal is to find a learning rate that's not too high or too low so that the model converges quickly and learns enough from training.
- Less than 1.0 and greater than 10^-6 is considered a good learning rate.
# (g) Batches
- Batches are the subsets of the training data.
- Large datasets often cannot fit into the memory of GPUs/CPUs. Batching allows processing smaller subsets, making training feasible.
-  data is divided into smaller subsets (batches), and the model processes these batches iteratively during training.
# (h) Gradient descents
Gradient descent is an optimization algorithm used to minimize a given function, typically the loss function in machine learning models. 
## Batch Gradient Descent
In this method, the model's weights are updated after evaluating all the training examples in a single iteration.
## Stochastic Gradient Descent
In this method, the gradient is computed for only one randomly selected partition of the shuffled dataset during each iteration.
# (i)
This table provides the most appropriate loss function and activation function for the last layer of a neural network, depending on the classification type.
## Classification Type: 1 or 2 Classes
- The classification task is binary, meaning there are only two possible classes.
- Sigmoid activation function ranges the output into [0, 1], suitable for binary probabilities.
## Classification Type: Multiclass, Single Label
- The task is categorical, meaning there are more than two classes.
- Softmax converts logits into probabilities and ensures that the sum of probabilities over all classes equals 1.
## Classification Type: Multiclass, Multilabel
- The task is categorical, but each sample can belong to multiple classes simultaneously.
- Sigmoid outputs independent probabilities for each class, making it suitable for multilabel tasks.
# (k) Basis function
- Basis functions allow modeling non linearity in the data while keeping linearity in parameters, which greatly simplifies the analysis of these models.
- Using linear combination of different basis function, we can construct complex functions and still use linear regression.