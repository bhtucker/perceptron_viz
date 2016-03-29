
## Perceptron Learning

A perceptron is the simplest form of 'neural network' learning. 

The 'neuron' is simply a vector that can be multiplied against data points to say 1 or 0. 

![Weights](weights.png)

Learning consists of exposing the perceptron to data, and if it's wrong, adjusting the vector in the other direction. 

This app uses core python's hash function to convert characters into 11 digit numbers, which are then the learning space for the perceptron's 11-weight model.

At the moment you get a VowelPerceptron just for importing the module:

```
In [8]: voweler.vp.to_vec('h')
Out[8]: array([1, 3, 3, 1, 2, 0, 4, 0, 0, 4, 1])
```

Each page load gets predictions (red vowel, blue consonant) for the full alphabet from the current perceptron state, as well as a graph of that state.

Click a letter to teach the perceptron! (Only errors count)

![Graph](perceptron_state.png)