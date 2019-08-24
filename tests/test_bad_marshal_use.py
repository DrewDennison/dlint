#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadMarshalUse(dlint.test.base.BaseTest):

    def test_bad_marshal_usage(self):
        python_node = self.get_ast_node(
            """
            import marshal
            """
        )

        linter = dlint.linters.BadMarshalUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadMarshalUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
