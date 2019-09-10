# -*- coding: utf-8 -*-
import os

from hamcrest import assert_that
from hamcrest import equal_to
from mock import patch

from pyfacebook.config import WORKPLACE_API_URL
from pyfacebook.config import WORKPLACE_API_VERSION


def test_api_version_default():
    assert_that("v1", equal_to(WORKPLACE_API_VERSION))


def test_workplace_default_url():
    assert_that("https://developers.facebook.com/scim/v1/", equal_to(WORKPLACE_API_URL))


# @patch.multiple(pyfacebook.config, WORKPLACE_API_VERSION='v2')
@patch.dict(os.environ, {"WORKPLACE_API_VERSION": "v2"})
def test_workplace_api_url():
    assert_that(equal_to(WORKPLACE_API_URL), "https://developers.facebook.com/scim/v2/")
