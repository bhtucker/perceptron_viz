# -*- coding: utf-8 -*-
"""
    voweler
    ~~~~~~~~
    voweler flask app
"""

from . import factory, separability, embedding
from perceptron import VowelPerceptron

vp = VowelPerceptron()


def create_app(**kwargs):
    return factory.create_app(__name__, __path__)
