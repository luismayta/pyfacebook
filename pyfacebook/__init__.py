# -*- coding: utf-8 -*-
"""
Pyfacebook - For workplace.

"""
__version__ = "0.0.0"
__author__ = "Luis Mayta"
__email__ = "slovacus@gmail.com"
__licence__ = "Mit"

import json
import re

from .event import Event


class Page:

    _webhook_handlers = {}

    _quick_reply_callbacks = {}
    _button_callbacks = {}

    _quick_reply_callbacks_key_regex = {}
    _button_callbacks_key_regex = {}

    _after_send = None

    def __init__(self, page_access_token, **options):
        """ Webhook_handlers.
            contains optin, message, echo, delivery, postback, read,
            account_linking, referral.
        """
        self.page_access_token = page_access_token
        self._after_send = options.pop("after_send", None)

    def _call_handler(self, name, func, *args, **kwargs):
        if func is not None:
            func(*args, **kwargs)
        elif name in self._webhook_handlers:
            self._webhook_handlers[name](*args, **kwargs)
        else:
            print("there's no {} handler".format(name))

    def handle_webhook(
        self,
        payload,
        optin=None,
        message=None,
        echo=None,
        delivery=None,
        postback=None,
        read=None,
        account_linking=None,
        referral=None,
    ):

        data = json.loads(payload)

        # Make sure this is a page subscription
        if data.get("object") != "page":
            print("Webhook failed, only support page subscription")
            return False

        def get_events(data):
            for entry in data.get("entry"):
                for messaging in entry.get("messaging"):
                    event = Event(messaging)
                    yield event

        for event in get_events(data):
            if event.is_optin:
                self._call_handler("optin", optin, event)
            elif event.is_echo:
                self._call_handler("echo", echo, event)
            elif event.is_quick_reply:
                event.matched_callbacks = self.get_quick_reply_callbacks(event)
                self._call_handler("message", message, event)
                for callback in event.matched_callbacks:
                    callback(event.quick_reply_payload, event)
            elif event.is_message and not event.is_echo and not event.is_quick_reply:
                self._call_handler("message", message, event)
            elif event.is_delivery:
                self._call_handler("delivery", delivery, event)
            elif event.is_postback:
                event.matched_callbacks = self.get_postback_callbacks(event)
                self._call_handler("postback", postback, event)
                for callback in event.matched_callbacks:
                    callback(event.postback_payload, event)
            elif event.is_read:
                self._call_handler("read", read, event)
            elif event.is_account_linking:
                self._call_handler("account_linking", account_linking, event)
            elif event.is_referral:
                self._call_handler("referral", referral, event)
            else:
                print("Webhook received unknown messagingEvent: {}".format(event))

    """
    decorations
    """

    def handle_optin(self, func):
        self._webhook_handlers["optin"] = func

    def handle_message(self, func):
        self._webhook_handlers["message"] = func

    def handle_echo(self, func):
        self._webhook_handlers["echo"] = func

    def handle_delivery(self, func):
        self._webhook_handlers["delivery"] = func

    def handle_postback(self, func):
        self._webhook_handlers["postback"] = func

    def handle_read(self, func):
        self._webhook_handlers["read"] = func

    def handle_account_linking(self, func):
        self._webhook_handlers["account_linking"] = func

    def handle_referral(self, func):
        self._webhook_handlers["referral"] = func

    def after_send(self, func):
        self._after_send = func

    _callback_default_types = ["QUICK_REPLY", "POSTBACK"]

    def callback(self, payloads=None, types=None):
        if types is None:
            types = self._callback_default_types

        if not isinstance(types, list):
            raise ValueError("callback types must be list")

        for type in types:
            if type not in self._callback_default_types:
                raise ValueError('callback types must be "QUICK_REPLY" or "POSTBACK"')

        def wrapper(func):
            if payloads is None:
                return func

            for payload in payloads:
                if "QUICK_REPLY" in types:
                    self._quick_reply_callbacks[payload] = func
                if "POSTBACK" in types:
                    self._button_callbacks[payload] = func

            return func

        return wrapper

    def get_quick_reply_callbacks(self, event):
        callbacks = []
        for key in self._quick_reply_callbacks.keys():
            if key not in self._quick_reply_callbacks_key_regex:
                self._quick_reply_callbacks_key_regex[key] = re.compile(key + "$")

            if self._quick_reply_callbacks_key_regex[key].match(
                event.quick_reply_payload
            ):
                callbacks.append(self._quick_reply_callbacks[key])

        return callbacks

    def get_postback_callbacks(self, event):
        callbacks = []
        for key in self._button_callbacks.keys():
            if key not in self._button_callbacks_key_regex:
                self._button_callbacks_key_regex[key] = re.compile(key + "$")

            if self._button_callbacks_key_regex[key].match(event.postback_payload):
                callbacks.append(self._button_callbacks[key])

        return callbacks
