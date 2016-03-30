# -*- coding: utf-8 -*-
"""
    views
    ~~~~~
 
    Routes & views for this app!
"""

from flask import Blueprint, render_template, abort, jsonify, request
from jinja2 import TemplateNotFound
import voweler
from string import ascii_lowercase
import json

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

def render_score(score):
	return "{0:.0f}%".format(score * 100.)


@simple_page.route('/')
def base():
	return render_template('show.html', 
		letters=ascii_lowercase)


@simple_page.route('/state')
def state():
	"""
	Optionally update model via 'update' querystring arg
	Returns (after update):
		weights of model
		current predicted vowel list
	"""
	next_letter = request.args.get('update')
	if next_letter:
		perceptron_response = voweler.vp.handle_letter(next_letter)

	vocab = [
		(e, voweler.vp.handle_letter(e, update=False))
		for e in ascii_lowercase
	]
	current_score = voweler.separability.get_perceptron_accuracy(voweler.vp)
	scatter_data = voweler.separability.project_to_1d(
		voweler.vp.to_vec, voweler.vp.w
	)

	return jsonify(
		weights=[round(x, 2) for x in voweler.vp.w],
		vowels=[
			l
			for l in ascii_lowercase
			if voweler.vp.handle_letter(l, update=False) == 1.
		],
		scatter_data=scatter_data,
		current_score=render_score(current_score)
	)


@simple_page.route('/salt')
def set_salt():
	salt = request.args.get('salt', '')
	voweler.vp = voweler.perceptron.VowelPerceptron(salt=salt)
	(x_data, y_data, score) = voweler.separability.assess_embedding(
		voweler.vp.to_vec)
	print "%s: %s" % (salt, score)
	return jsonify(
		reset=True,
		scatter_data=voweler.separability.get_c3_payload(x_data, y_data),
		score=render_score(score)
	)
