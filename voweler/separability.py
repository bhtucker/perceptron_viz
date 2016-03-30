# -*- coding: utf-8 -*-
"""
    separability
    ~~~~~~~~~~~~

    Reproject data to assess linear separability
"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from letters import is_vowel
from string import ascii_lowercase
import numpy as np

PLOT_SCALE = 2.5
CONS_SERIES_NAME = 'consonant'
VOWEL_SERIES_NAME = 'vowel'

def get_perceptron_accuracy(vp):
	return np.mean(np.array([
		is_vowel(x) == vp.handle_letter(x, update=False)
		for x in ascii_lowercase]))


def get_x_y_matrices(to_vec):
	x_data = np.array(map(to_vec, ascii_lowercase))
	y_data = np.array(map(is_vowel, ascii_lowercase))
	return (x_data, y_data)	


def assess_embedding(to_vec):
	"""
	Returns LDA classification score and projected data
	"""
	(x_data, y_data) = get_x_y_matrices(to_vec)

	lda = LDA(n_components=2)
	x_prime = lda.fit_transform(x_data, y_data)
	score = lda.score(x_data, y_data)

	return (x_prime.reshape(26, ), y_data, score)


def project_to_1d(to_vec, weights):
	"""
	Projection and scaling of alphabet for c3 rendering purposes
	Embeds letters via to_vec and projects via weights
	"""
	(x_data, y_data) = get_x_y_matrices(to_vec)	
	x_prime = np.dot(x_data, weights)
	return get_c3_payload(x_prime, y_data)


def _get_c3_series(x_prime, y_data, filter_, series_name):
	"""
	Returns (x coord, y coord) for c3 scatter plot
	"""
	series_x = [x for x, y in zip(x_prime, y_data) if filter_(y)]
	series_y = (
		np.random.random(len(series_x)) * .05 + np.ones(len(series_x))
	).tolist()

	return (
		[series_name + '_x'] + series_x,
		[series_name] + series_y
	)

def _scale_x_prime(x_prime):
	max_magnitude = max(map(abs, x_prime))
	x_prime_scaled = x_prime * (PLOT_SCALE / max_magnitude)
	return x_prime_scaled	


def get_c3_payload(x_data, y_data, scale=True):
	if scale:
		x_data = _scale_x_prime(x_data)
	(cons_x, cons_y) = _get_c3_series(
		x_data,
		y_data,
		filter_=lambda y: y < .5,
		series_name=CONS_SERIES_NAME
		)
	(vowel_x, vowel_y) = _get_c3_series(
		x_data,
		y_data,
		filter_=lambda y: y > .5,
		series_name=VOWEL_SERIES_NAME
		)
	return [cons_x, vowel_x, cons_y, vowel_y]
