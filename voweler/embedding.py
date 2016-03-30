# -*- coding: utf-8 -*-
"""
    embedding
    ~~~~~~~~~

    Representing letters in a particular feature space
"""
import numpy as np
import math
from string import ascii_lowercase


def get_embedding(salt):
    """
    Help embed lower case chars into feature space by hashing against salt
    Returns (converted function, dimensions of vector space)
    """
    hash_with_salt = lambda char: str(abs(hash(char + salt)))
    basic_to_vec = lambda char: np.array(map(int, hash_with_salt(char)))
    vecs = map(basic_to_vec, ascii_lowercase)
    lens = map(len, vecs)
    if len(set(lens)) == 1:
        return (basic_to_vec, lens[0])
    max_len = max(map(len, vecs))

    def to_vec(char):
        hash_string = hash_with_salt(char)
        repeated_hash_string = hash_string * int(
            math.ceil(max_len / float(len(hash_string)))
        )
        return np.array(map(int, repeated_hash_string[:max_len]))
    return (to_vec, max_len)
