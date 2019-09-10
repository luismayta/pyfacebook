# -*- coding: utf-8 -*-
from pyfacebook import utils


class BaseMixin:
    def to_json(self):
        return utils.to_json(self)
