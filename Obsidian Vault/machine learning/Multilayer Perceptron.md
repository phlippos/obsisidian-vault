# Artificial Neural Networks - Multilayer Perceptrons

_INF502 Machine Learning - 2024-2025 Spring, Lecture 9_

## Introduction to Artificial Neural Networks

- **Basic Structure**: ANNs consist of simple processors called neurons, analogous to biological neurons in the brain
- **Connections**: Neurons are connected by weighted links passing signals from one neuron to another
- **Signal Propagation**: Output signals are transmitted through outgoing connections that split into branches, terminating at incoming connections of other neurons

## Multilayer Neural Networks

- **Definition**: A multilayer perceptron is a feedforward neural network with one or more hidden layers
- **Architecture**: Consists of an input layer of source neurons, at least one middle/hidden layer of computational neurons, and an output layer
- **Signal Flow**: Input signals propagate forward on a layer-by-layer basis
- **Hidden Layers**: "Hide" their desired output - cannot be observed through input/output behavior
    - Capture and transform input data, learning important features
- **Scale**: Commercial ANNs typically have 3-4 layers with 10-1000 neurons per layer
    - Experimental networks may have 5-6 layers with millions of neurons

## Back-Propagation Neural Network

- **Learning Process**: Similar to perceptron learning
    1. Training set of input patterns is presented to the network
    2. Network computes output pattern
    3. If there's an error (difference between actual and desired output), weights are adjusted to reduce this error
- **Two Phases**:
    1. **Forward Phase**: Input pattern propagates from layer to layer until output is generated
    2. **Backward Phase**: If output differs from desired output, error is calculated and propagated backward through the network from output to input layer, modifying weights

## The Back-Propagation Training Algorithm

### Step 1: Initialization

- Set weights and threshold levels to random numbers uniformly distributed in a small range:
    - [-2.4/Fi, +2.4/Fi] where Fi is the total number of inputs of neuron i
    - Initialization is done on a neuron-by-neuron basis

### Step 2: Activation

- Apply inputs and desired outputs
- Calculate actual outputs of neurons in hidden layer using sigmoid activation function
- Calculate actual outputs of neurons in output layer

### Step 3: Weight Training

- Update weights by propagating backward the errors associated with output neurons
- For output layer:
    - Calculate error gradient
    - Calculate weight corrections
    - Update weights
- For hidden layer:
    - Calculate error gradient
    - Calculate weight corrections
    - Update weights

### Step 4: Iteration

- Increase iteration count by one
- Repeat process until the selected error criterion is satisfied

## Example: XOR Problem Using Three-Layer Network

- **Problem**: Implementing XOR operation (a task single-layer perceptrons cannot solve)
- **Network**: Input layer (2 nodes), hidden layer (2 nodes), output layer (1 node)
- **Thresholds**: Represented by weights connected to fixed inputs of -1
- **Training**: Continues until sum of squared errors is less than 0.001
- The network successfully creates appropriate decision boundaries to solve the XOR problem

## Accelerating Learning

### Hyperbolic Tangent Activation

- Networks learn faster when using hyperbolic tangent sigmoid functions:
    - f(net) = a tanh(b × net) where a = 1.716 and b = 0.667

### Momentum Term

- Adding momentum to the delta rule:
    - Δwjk(p) = α × Δwjk(p-1) + η × yj(p) × δk(p)
    - Where α is the momentum constant (typically 0.95)
- Reduces training time from 224 epochs to 126 epochs for XOR example

### Adaptive Learning Rate

- Heuristics:
    1. If sum of squared errors has the same algebraic sign for several consecutive epochs, increase learning rate
    2. If sign alternates for several consecutive epochs, decrease learning rate
- Implementation:
    - If current error exceeds previous by more than predefined ratio (typically 1.04), decrease learning rate (multiply by 0.7)
    - If error is less than previous, increase learning rate (multiply by 1.05)
- Further reduces training time to 103 epochs

### Combined Approach

- Using both momentum and adaptive learning rate provides the fastest convergence
- Reduces training time to 85 epochs for XOR example