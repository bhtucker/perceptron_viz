# -*- coding: utf-8 -*-
"""
    perceptron
    ~~~~~~~~~~

    Module for our learning node logic
"""

import numpy as np
from string import ascii_lowercase
VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}


class Perceptron(object):
    """Basic Perceptron functionality:
    store weights, apply them to points, update weights based on error
    """
    def __init__(self, learning_rate=.1, input_width=11):
        self.learning_rate = learning_rate
        self.input_width = input_width
        self.w = np.random.random(input_width)

    def predict(self, point):
        return 1. if np.dot(self.w, point) > .5 else 0.

    def update(self, point, error):
        self.w += point * error * self.learning_rate


class VowelPerceptron(Perceptron):
    """Vowel-detection specific methods for perceptron"""
    def __init__(self, *args, **kwargs):
        super(VowelPerceptron, self).__init__(**kwargs)
        self.count = 0
        if 'to_vec' in kwargs:
            self.to_vec = kwargs['to_vec']
        else:
            self.to_vec = lambda v: np.array(map(int, str(hash(v))))

    def handle_letter(self, letter, update=True):
        point = self.to_vec(letter)
        pred = self.predict(point)
        if update:
            error = is_vowel(letter) - pred
            self.update(point, error)
            self.count += 1
        return pred

def is_vowel(letter):
    return 1. if letter in VOWELS else 0.
