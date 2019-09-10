# -*- coding: utf-8 -*-
from enum import Enum


class BaseEnum(Enum):
    def __str__(self):

        return self.value
