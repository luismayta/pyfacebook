# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyfacebook.graph import Group

COMMUNITY_ID = 10000000
EMAIL = "slovacus@gmail.com"


def test_get_all_members_without_fields():

    params = {
        "version": "v2.8",
        "access_token": "this is my token",
        "community_id": COMMUNITY_ID,
    }
    group = Group(**params)

    assert_that(group.get_all_members(), not_none())
    response = {
        "url": "https://graph.facebook.com/v2.8/{}/members".format(COMMUNITY_ID),
        "params": group.fields,
        "headers": {"access_token": params["access_token"]},
        "method": "get",
    }
    assert_that(response, has_entries(group.response))


def test_get_all_members_with_fields():
    FIELDS = {"fields": "id,name"}

    params = {
        "version": "v2.8",
        "access_token": "this is my token",
        "community_id": COMMUNITY_ID,
    }
    group = Group(**params)

    assert_that(group.get_all_members(fields=FIELDS), not_none())
    response = {
        "url": "https://graph.facebook.com/v2.8/{}/members".format(COMMUNITY_ID),
        "params": FIELDS,
        "headers": {"access_token": params["access_token"]},
        "method": "get",
    }
    assert_that(response, has_entries(group.response))


def test_add_member():

    params = {
        "version": "v2.8",
        "access_token": "this is my token",
        "community_id": COMMUNITY_ID,
    }
    group = Group(**params)
    args = {"email": EMAIL}

    assert_that(group.add_member(**args), not_none())
    response = {
        "url": "https://graph.facebook.com/v2.8/{}/members".format(COMMUNITY_ID),
        "data": {"email": EMAIL},
        "headers": {"access_token": params["access_token"]},
        "method": "post",
    }
    assert_that(response, has_entries(group.response))


def test_remove_member_group():
    params = {
        "version": "v2.8",
        "access_token": "this is my token",
        "community_id": COMMUNITY_ID,
    }
    group = Group(**params)
    args = {"email": EMAIL}

    assert_that(group.remove_member(**args), not_none())
    response = {
        "url": "https://graph.facebook.com/v2.8/{}/members".format(COMMUNITY_ID),
        "data": {"email": EMAIL},
        "headers": {"access_token": params["access_token"]},
        "method": "delete",
    }
    assert_that(response, has_entries(group.response))
