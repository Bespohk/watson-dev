# -*- coding: utf-8 -*-
import os
from watson.dev.middleware import StaticFileMiddleware
from tests.watson.dev.support import sample_app, sample_environ, sample_start_response


class TestStaticFileMiddleware(object):

    def test_create(self):
        mw = StaticFileMiddleware(sample_app, os.path.dirname(__file__))
        assert mw.app == sample_app
        assert mw.initial_dir == os.path.dirname(__file__)

    def test_execute(self):
        mw = StaticFileMiddleware(sample_app, os.path.dirname(__file__))
        environ = sample_environ(PATH_INFO='/sample.css')
        response = mw(environ, sample_start_response)
        assert response == [b'html, body { background: red; }']

    def test_run_app(self):
        mw = StaticFileMiddleware(sample_app, os.path.dirname(__file__))
        environ = sample_environ(PATH_INFO='/blah')
        mw(environ, sample_start_response)
