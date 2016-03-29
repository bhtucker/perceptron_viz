# -*- coding: utf-8 -*-
"""
    views
    ~~~~~
 
    Routes & views for this app!
"""

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import voweler
from string import ascii_lowercase
import json

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/<letter>')
def base(letter):
	perceptron_response = voweler.vp.handle_letter(letter)
	vocab = [
		(e, voweler.vp.handle_letter(e, update=False))
		for e in ascii_lowercase
	]

	return render_template('show.html', entries=[
		letter,
		perceptron_response,
		voweler.vp.count],
		vocab=vocab,
		weights=json.dumps([round(x, 2) for x in voweler.vp.w])
		)
