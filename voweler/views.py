# -*- coding: utf-8 -*-
"""
    views
    ~~~~~

    Routes & views for this app!
"""

from flask import (

    Blueprint, render_template, jsonify, request, current_app
)
import voweler
from string import ascii_lowercase
import json

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


def render_score(score):
    return "{0:.0f}%".format(score * 100.)


@simple_page.route('/')
def base():
    return render_template(
        'show.html',
        letters=ascii_lowercase
    )


@simple_page.route('/state')
def state():
    """
    Optionally update model via 'update' querystring arg
    Returns (after update):
        weights of model
        current predicted vowel list
    """
    next_letter = request.args.get('update')
    current_app.vp.get_state()
    if next_letter:
        current_app.vp.handle_letter(next_letter)
        current_app.vp.set_state()

    vocab = [
        (e, current_app.vp.handle_letter(e, update=False))
        for e in ascii_lowercase
    ]

    current_score = voweler.separability \
        .get_perceptron_accuracy(current_app.vp)

    scatter_data = voweler.separability.project_to_1d(
        current_app.vp.to_vec, current_app.vp.w
    )

    return jsonify(
        weights=[round(x, 2) for x in current_app.vp.w],
        vowels=[
            l
            for l in ascii_lowercase
            if current_app.vp.handle_letter(l, update=False) == 1.
        ],
        scatter_data=scatter_data,
        current_score=render_score(current_score)
    )



@simple_page.route('/size')
def set_size():
    size = request.args.get('size')
    perceptron_kwargs = {}
    if size:
        perceptron_kwargs['input_width'] = int(size)
    current_app.vp = voweler.perceptron.VowelPerceptron(**perceptron_kwargs)
    current_app.vp.set_state()
    (x_data, y_data, score) = voweler.separability.assess_embedding(
        current_app.vp.to_vec)
    return jsonify(
        reset=True,
        scatter_data=voweler.separability.get_c3_payload(x_data, y_data),
        score=render_score(score)
    )
