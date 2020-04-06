#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.factory import create_app
from api.utils.config import DevelopmentConfig, ProductionConfig
import os

if __name__ == '__main__':
    if os.environ.get('WORK_ENV') == 'DEBUG':
        app = create_app(DevelopmentConfig)
        app.run(port=8080, host="0.0.0.0", use_reloader=True, use_debugger=True, debug=True)
    else:
        app = create_app(ProductionConfig)
        app.run(port=8080, host="0.0.0.0", use_reloader=False)
