# -*- coding: utf-8 -*-
"""
    letters
    ~~~~~~~

    Letter logic utilities
"""

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}


def is_vowel(letter):
    return 1. if letter in VOWELS else 0.
