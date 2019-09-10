# -*- coding: utf-8 -*-
import os
from environs import Env

env = Env()
env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "tests", "resources", "assets")

# Application

DEBUG = env.bool("PYFACEBOOK_DEBUG", default=False)
HEADER_AUTH_KEY = "Authorization"
HEADER_AUTH_VAL_PREFIX = "Bearer"

# Workplace
WORKPLACE_URL = env.str("PYFACEBOOK_URL", default="https://www.facebook.com/scim/")
WORKPLACE_API_VERSION = env.str("PYFACEBOOK_API_VERSION", default="v1")
WORKPLACE_API_URL = env.str(
    "PYFACEBOOK_API_URL",
    default="https://developers.facebook.com/scim/{}/".format(WORKPLACE_API_VERSION),
)
WORKPLACE_ACCESS_TOKEN = env.str("PYFACEBOOK_ACCESS_TOKEN", default="")

FACEBOOK_GRAPH_VERSION = env.str("PYFACEBOOK_GRAPH_VERSION", default="v2.6")
FACEBOOK_GRAPH_TOKEN = env.str("PYFACEBOOK_GRAPH_TOKEN", default="")
FACEBOOK_GRAPH_URL = env.str(
    "PYFACEBOOK_URL_GRAPH", default="https://graph.facebook.com/"
)
