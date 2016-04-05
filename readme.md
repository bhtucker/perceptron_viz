




## Perceptron Learning

A perceptron is the simplest form of 'neural network' learning. 

The 'neuron' is simply a vector that can be multiplied against data points to say 1 or 0. 

This perceptron tries to learn which letters are vowels, ie, we draw 26 points in space and say some are one class and the rest are another.


## Visualization App

You can:

* select what letter (or groups of letters) to feed to the perceptron next
* watch it's learning pattern (initially, moving left after consonants, right after vowels)
* see the weight vector at bottom of page
* see the current accuracy as compared to a benchmark accuracy from a linear algebra class separation solution (LDA)
* adjust the dimensionality


## To run

Requires numpy/scipy (if you need these look up anaconda distribution)

Install python dependencies with

```
pip install .
```

from base directory.

Build JS app from `viz` directory

```
npm install
npm run build
```

After building, `/voweler/dist/` should exist

Run `python wsgi.py` to run app simply.

Cross-request state persistence is available via shared memory managed by `uwsgi`: see the [multiapp branch](https://github.com/bhtucker/perceptron_viz/tree/multiapp)


