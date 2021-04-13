# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyfacebook.core import Base


def test_base_default():
    """Test Base default"""
    base = Base()
    assert_that("v1", equal_to(base.version))
    assert_that("https://www.facebook.com/scim/v1/", equal_to(base.url))
