# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyfacebook.message import Message

RECIPIENT_ID = 10000000
URL = ""


def test_send_message():

    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Message(**params)

    args = {"recipient_id": RECIPIENT_ID, "message": "Hola Mundo"}
    assert_that(message.send_message(**args), not_none())

    body = {
        "message": "Hola Mundo",
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


def test_send_text_message():
    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Message(**params)
    args = {"recipient_id": RECIPIENT_ID, "message": "o/ World"}
    assert_that(message.send_text_message(**args), not_none())

    body = {
        "message": {"text": "o/ World"},
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


def test_send_quick_replies_message():
    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Message(**params)
    args = {
        "recipient_id": RECIPIENT_ID,
        "message": "o/ World",
        "quick_replies": [
            {
                "content_type": "text",
                "title": "Search",
                "payload": "<POSTBACK_PAYLOAD>",
                "image_url": "http://example.com/img/red.png",
            }
        ],
    }
    assert_that(message.send_quick_replies_message(**args), not_none())

    body = {
        "message": {
            "text": "o/ World",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Search",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "http://example.com/img/red.png",
                }
            ],
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


def test_send_quick_replies_multiple_message():
    params = {"version": "v2.8", "access_token": "this is my token"}
    message = Message(**params)
    args = {
        "recipient_id": RECIPIENT_ID,
        "message": "o/ World",
        "quick_replies": [
            {
                "content_type": "text",
                "title": "Title1",
                "payload": "<POSTBACK_PAYLOAD-1>",
                "image_url": "http://example.com/img/1.png",
            },
            {
                "content_type": "text",
                "title": "Title2",
                "payload": "<POSTBACK_PAYLOAD-2>",
                "image_url": "http://example.com/img/2.png",
            },
        ],
    }
    assert_that(message.send_quick_replies_message(**args), not_none())

    body = {
        "message": {
            "text": "o/ World",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Title1",
                    "payload": "<POSTBACK_PAYLOAD-1>",
                    "image_url": "http://example.com/img/1.png",
                },
                {
                    "content_type": "text",
                    "title": "Title2",
                    "payload": "<POSTBACK_PAYLOAD-2>",
                    "image_url": "http://example.com/img/2.png",
                },
            ],
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
