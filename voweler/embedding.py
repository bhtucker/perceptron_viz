# -*- coding: utf-8 -*-
"""
    embedding
    ~~~~~~~~~

    Representing letters in a particular feature space
"""
import numpy as np
import math
from string import ascii_lowercase


def get_embedding(size):
	letter_map = {l: np.random.random(size) for l in ascii_lowercase}
	def to_vec(char):
		return letter_map[char]
	to_vec.__doc__ = """
		Returns a {size}-length vector corresponding to the lowercase letter :char
		""".format(size=size)
	return to_vec
