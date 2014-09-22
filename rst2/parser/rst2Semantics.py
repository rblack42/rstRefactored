# -*- coding: utf-8 -*-
"""
    rst2.parser.rst2Semantics
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Semantics actions for rst2 parser
"""

class rst2Semantics(object):

    def line(self, ast):
        return 'LINE:' + ''.join(ast) + '\n'

    def blankline(self, ast):
        return 'BLANK:' + ''.join(ast) + '\n'

    def indent(self, ast):
        return 'INDENT:' + ''.join(ast) + '\n'

    def block(self, ast):
        return 'BLOCK:' + ''.join(ast) + '\n'

    def document(self, ast):
        return 'DOC:' + ''.join(ast) + '\n'

    def _default(self, ast):
        pass

