#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    manager
    ~~~~~~~

    Launch script for rst2 application
"""
from flask.ext.script import Manager, Shell
from rst2 import create_app

app = create_app()
app.debug = True
manager = Manager(app)

if __name__ == '__main__':
    manager.run()


