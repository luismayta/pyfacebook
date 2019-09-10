# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyfacebook.message import Template

RECIPIENT_ID = 10000000
URL = ""


def test_send_generic_template():

    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Template(**params)

    args = {
        "recipient_id": RECIPIENT_ID,
        "elements": [
            {
                "title": "Title",
                "image_url": "https://luismayta.com/image1.png",
                "subtitle": "subtitle.",
                "default_action": {
                    "type": "web_url",
                    "url": "https://luismayta.com/item/103",
                    "messenger_extensions": True,
                    "webview_height_ratio": "tall",
                    "fallback_url": "https://luismayta.com/",
                },
                "buttons": [
                    {"type": "web_url", "url": "https://url.com", "title": "title"},
                    {"type": "postback", "title": "title", "payload": "payload"},
                ],
            }
        ],
    }
    assert_that(message.send_generic_message(**args), not_none())
    body = {
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Title",
                            "image_url": "https://luismayta.com/image1.png",
                            "subtitle": "subtitle.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://luismayta.com/item/103",
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://luismayta.com/",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://url.com",
                                    "title": "title",
                                },
                                {
                                    "type": "postback",
                                    "title": "title",
                                    "payload": "payload",
                                },
                            ],
                        }
                    ],
                },
            }
        },
        "recipient": {"id": RECIPIENT_ID},
        "notification_type": "REGULAR",
    }

    response = {
        "url": "https://graph.facebook.com/v2.8/me/messages",
        "params": {"access_token": params["access_token"]},
        "json": body,
        "headers": {"Content-type": "application/json"},
        "method": "post",
    }
    assert_that(response, has_entries(message.response))


def test_send_generic_template_multiple():

    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Template(**params)

    args = {
        "recipient_id": RECIPIENT_ID,
        "elements": [
            {
                "title": "Title",
                "image_url": "https://luismayta.com/image1.png",
                "subtitle": "subtitle.",
                "default_action": {
                    "type": "web_url",
                    "url": "https://luismayta.com/item/103",
                    "messenger_extensions": True,
                    "webview_height_ratio": "tall",
                    "fallback_url": "https://luismayta.com/",
                },
                "buttons": [
                    {"type": "web_url", "url": "https://url.com", "title": "title"},
                    {"type": "postback", "title": "title", "payload": "payload"},
                ],
            },
            {
                "title": "Title2",
                "image_url": "https://luismayta.com/image2.png",
                "subtitle": "subtitle.",
                "buttons": [
                    {"type": "postback", "title": "title", "payload": "payload"}
                ],
            },
        ],
    }
    assert_that(message.send_generic_message(**args), not_none())
    body = {
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Title",
                            "image_url": "https://luismayta.com/image1.png",
                            "subtitle": "subtitle.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://luismayta.com/item/103",
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://luismayta.com/",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://url.com",
                                    "title": "title",
                                },
                                {
                                    "type": "postback",
                                    "title": "title",
                                    "payload": "payload",
                                },
                            ],
                        },
                        {
                            "title": "Title2",
                            "image_url": "https://luismayta.com/image2.png",
                            "subtitle": "subtitle.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "title",
                                    "payload": "payload",
                                }
                            ],
                        },
                    ],
                },
            }
        },
        "recipient": {"id": RECIPIENT_ID},
        "notification_type": "REGULAR",
    }

    response = {
        "url": "https://graph.facebook.com/v2.8/me/messages",
        "params": {"access_token": params["access_token"]},
        "json": body,
        "headers": {"Content-type": "application/json"},
        "method": "post",
    }
    assert_that(response, has_entries(message.response))


def test_send_button():

    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Template(**params)

    args = {
        "recipient_id": RECIPIENT_ID,
        "message": "button",
        "buttons": [{"type": "postback", "title": "title", "payload": "POSTBACK"}],
    }
    assert_that(message.send_button(**args), not_none())
    body = {
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "button",
                    "buttons": [
                        {"type": "postback", "title": "title", "payload": "POSTBACK"}
                    ],
                },
            }
        },
        "recipient": {"id": RECIPIENT_ID},
        "notification_type": "REGULAR",
    }

    response = {
        "url": "https://graph.facebook.com/v2.8/me/messages",
        "params": {"access_token": params["access_token"]},
        "json": body,
        "headers": {"Content-type": "application/json"},
        "method": "post",
    }
    assert_that(response, has_entries(message.response))
