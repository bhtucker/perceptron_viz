# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~
    voweler wsgi module
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import voweler

application = DispatcherMiddleware(voweler.create_app())

if __name__ == "__main__":
    run_simple(
        '0.0.0.0', 5000, application,
        use_reloader=True, use_debugger=True)
