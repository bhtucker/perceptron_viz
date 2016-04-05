# -*- coding: utf-8 -*-
"""
    voweler.factory
    ~~~~~~~~~~~~~~~~
    voweler factory module
"""

from flask import Flask
import logging
from views import simple_page
from perceptron import VowelPerceptron


def create_app(package_name, package_path, settings_override=None):
    """Returns a :class:`Flask` application instance
    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    """
    app = Flask(package_name, instance_relative_config=True, static_folder='dist')

    app.config.from_object('voweler.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)
    app.vp = VowelPerceptron()
    app.vp.set_state()
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('access.log')
    logger.addHandler(handler)
    app.logger.addHandler(handler)
    app.register_blueprint(simple_page)
    app.debug = True
    return app
