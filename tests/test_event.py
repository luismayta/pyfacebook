# -*- coding: utf-8 -*-
import json

from hamcrest import assert_that
from hamcrest import equal_to

from pyfacebook.event import Event


def test_event_message():
    payload = """
        {"sender":{"id":"sender"},"recipient":{"id":"recipient"},"timestamp":1472026867080,
        "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"o/ world"}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(event.sender_id), "sender")
    assert_that(equal_to(event.recipient_id), "recipient")
    assert_that(equal_to(event.message_text), "o/ world")


def test_event_postback():
    payload = """
        {"sender": {"id": "sender"},
        "recipient": {"id": "recipient"}, "timestamp": 1472028006107,
        "postback": {"payload": "DEVELOPED_DEFINED_PAYLOAD"}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(event.sender_id), "sender")
    assert_that(equal_to(event.recipient_id), "recipient")
    assert_that(equal_to(event.postback), "DEVELOPED_DEFINED_PAYLOAD")
    assert_that(equal_to(True), event.is_postback)


def test_quick_reply():
    payload = """
        {"sender": {"id": "sender"}, "recipient": {"id": "recipient"},
        "timestamp": 1472028637825, "message": {"quick_reply": {"payload": "PICK_ACTION"},
        "mid": "mid.1472028637817:ae2763cc036a664b43", "seq": 834, "text": "Action"}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(event.sender_id), "sender")
    assert_that(equal_to(event.recipient_id), "recipient")
    assert_that(equal_to(event.quick_reply), "PICK_ACTION")
    assert_that(equal_to(False), event.is_postback)
    assert_that(equal_to(True), event.is_quick_reply)
    assert_that(equal_to(True), event.is_message)
    assert_that(equal_to(event.message_text), "Action")
    assert_that(event.quick_reply_payload, event.quick_reply.get("payload"))


def test_postback_referral():
    payload = """
        {"sender":{"id":"sender"},"recipient":{"id":"recipient"},
        "timestamp":1472028006107,"postback":{"payload":"DEVELOPED_DEFINED_PAYLOAD",
        "referral":{"ref":"REFTEST","source":"SHORTLINK","type": "OPEN_THREAD"}}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(True), event.is_postback)
    assert_that(equal_to(True), event.is_postback_referral)
    assert_that(equal_to(event.sender_id), "sender")
    assert_that(equal_to(event.recipient_id), "recipient")
    assert_that(equal_to(event.postback), "DEVELOPED_DEFINED_PAYLOAD")
    assert_that(equal_to(event.message), None)
    assert_that(equal_to(event.postback_payload), event.postback.get("payload"))
    assert_that(equal_to(event.postback_referral), event.postback.get("referral"))
    assert_that(equal_to(event.postback_referral_ref), "REFTEST")
