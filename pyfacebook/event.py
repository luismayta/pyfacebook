# -*- coding: utf-8 -*-


class Event(object):
    def __init__(self, messaging=None):
        if messaging is None:
            messaging = {}

        self.messaging = messaging
        self.matched_callbacks = []

    @property
    def sender_id(self):
        return self.messaging.get("sender", {}).get("id", None)

    @property
    def recipient_id(self):
        return self.messaging.get("recipient", {}).get("id", None)

    @property
    def timestamp(self):
        return self.messaging.get("timestamp", None)

    @property
    def message(self):
        return self.messaging.get("message", {})

    @property
    def message_text(self):
        return self.message.get("text", None)

    @property
    def message_attachments(self):
        return self.message.get("attachments", [])

    @property
    def quick_reply(self):
        return self.messaging.get("message", {}).get("quick_reply", {})

    @property
    def postback(self):
        return self.messaging.get("postback", {})

    @property
    def postback_referral(self):
        return self.messaging.get("postback", {}).get("referral", {})

    @property
    def optin(self):
        return self.messaging.get("optin", {})

    @property
    def account_linking(self):
        return self.messaging.get("account_linking", {})

    @property
    def delivery(self):
        return self.messaging.get("delivery", {})

    @property
    def read(self):
        return self.messaging.get("read", {})

    @property
    def referral(self):
        return self.messaging.get("referral", {})

    @property
    def message_mid(self):
        return self.messaging.get("message", {}).get("mid", None)

    @property
    def message_seq(self):
        return self.messaging.get("message", {}).get("seq", None)

    @property
    def is_optin(self):
        return "optin" in self.messaging

    @property
    def is_message(self):
        return "message" in self.messaging

    @property
    def is_text_message(self):
        return self.messaging.get("message", {}).get("text", None) is not None

    @property
    def is_attachment_message(self):
        return self.messaging.get("message", {}).get("attachments", None) is not None

    @property
    def is_echo(self):
        return self.messaging.get("message", {}).get("is_echo", None) is not None

    @property
    def is_delivery(self):
        return "delivery" in self.messaging

    @property
    def is_postback(self):
        return "postback" in self.messaging

    @property
    def is_postback_referral(self):
        return self.is_postback and "referral" in self.postback

    @property
    def is_read(self):
        return "read" in self.messaging

    @property
    def is_account_linking(self):
        return "account_linking" in self.messaging

    @property
    def is_referral(self):
        return "referral" in self.messaging

    @property
    def is_quick_reply(self):
        return self.messaging.get("message", {}).get("quick_reply", None) is not None

    @property
    def quick_reply_payload(self):
        return (
            self.messaging.get("message", {}).get("quick_reply", {}).get("payload", "")
        )

    @property
    def postback_payload(self):
        return self.messaging.get("postback", {}).get("payload", "")

    @property
    def referral_ref(self):
        return self.messaging.get("referral", {}).get("ref", "")

    @property
    def postback_referral_ref(self):
        return self.messaging.get("postback", {}).get("referral", {}).get("ref", "")
