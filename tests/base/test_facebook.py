# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyfacebook.core import Facebook


def test_facebook_default():
    """Make instance facebook."""
    facebook = Facebook()
    assert_that(equal_to(facebook.version), "v2.6")
    assert_that(equal_to(facebook.url), "https://graph.facebook.com/")


def test_facebook_change():
    """Make instance facebook change"""
    params = {"version": "v2.8", "access_token": "this is my token"}
    facebook = Facebook(**params)
    assert_that(equal_to(facebook.version), "v2.8")
    assert_that(equal_to(facebook.access_token), "this is my token")
