#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なんか書いとけ
"""
from bottle import route, run, debug

@route('/login')
def do_login():
    """
    login page
    """
    return "hi!"

debug(True)
run(host='localhost', port=8080, reloader=True)
