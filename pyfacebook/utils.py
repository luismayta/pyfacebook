# -*- coding: utf-8 -*-
import json


def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)
