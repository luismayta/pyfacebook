# -*- coding: utf-8 -*-
import mock
from hamcrest import assert_that
from hamcrest import equal_to

from pyfacebook import Page


def test_page_access_token():
    page = Page(**{"page_access_token": "this is my token"})
    assert_that(equal_to(page.page_access_token), "this is my token")


def test_handle_webhook_errors():
    page = Page(**{"page_access_token": "this is my token"})
    payload = """
        {
            "object":"not_page",
            "entry":[
                {"id":"1691462197845448","time":1472026867114,
                "messaging":[
                    {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                     "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
                ]}
            ]
        }
        """
    assert_that(False, equal_to(page.handle_webhook(payload)))

    payload = """
    {
        "object":"page",
        "entry":[
            {"id":"1691462197845448","time":1472026867114,
            "messaging":[
                {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                    "unknown":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
            ]}
        ]
    }
    """

    page.handle_webhook(payload)

    @page.callback
    def unknown():
        pass


def test_handle_webhook_message():
    page = Page(**{"page_access_token": "this is my token"})
    payload = """
    {
        "object":"page",
        "entry":[
            {"id":"1691462197845448","time":1472026867114,
            "messaging":[
                {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                    "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
            ]}
        ]
    }
    """
    counter = mock.MagicMock()
    page.handle_webhook(payload)

    @page.handle_message
    def handler1(event):
        assert_that(True, equal_to(event.is_message))
        assert_that(True, equal_to(event.is_text_message))
        assert_that(False, equal_to(event.is_attachment_message))
        assert_that(False, equal_to(event.is_quick_reply))
        assert_that(False, equal_to(event.is_echo))
        assert_that(False, equal_to(event.is_read))
        assert_that(False, equal_to(event.is_postback))
        assert_that(False, equal_to(event.is_postback_referral))
        assert_that(False, equal_to(event.is_optin))
        assert_that(False, equal_to(event.is_delivery))
        assert_that(False, equal_to(event.is_account_linking))
        assert_that(False, equal_to(event.is_referral))
        assert_that(1472026867080, equal_to(event.timestamp))
        assert_that(equal_to(event.sender_id), "1134343043305865")
        assert_that(equal_to(event.recipient_id), "1691462197845448")
        assert_that(equal_to(event.message_text), "hello world")
        counter()

    page.handle_webhook(payload)
    assert_that(1, equal_to(counter.call_count))

    counter2 = mock.MagicMock()

    def handler2(event):
        counter2()

    page.handle_webhook(payload, message=handler2)
    assert_that(1, equal_to(counter2.call_count))


def test_handle_webhook_quickreply_callback():
    page = Page(**{"page_access_token": "this is my token"})
    payload = """
        {"object":"page","entry":[{"id":"1691462197845448","time":1472028637866,
        "messaging":[{
            "sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472028637825,
            "message":{"quick_reply":{"payload":"PICK_ACTION"},"mid":"mid.1472028637817:ae2763cc036a664b43","seq":834,"text":"Action"}}]}]}
        """
    counter1 = mock.MagicMock()
    counter2 = mock.MagicMock()

    @page.handle_message
    def handler1(event):
        assert_that(equal_to(event.is_message), True)
        assert_that(equal_to(event.is_text_message), True)
        assert_that(equal_to(event.is_attachment_message), False)
        assert_that(equal_to(event.is_quick_reply), True)
        assert_that(equal_to(event.is_echo), False)
        assert_that(equal_to(event.is_read), False)
        assert_that(equal_to(event.is_postback), False)
        assert_that(equal_to(event.is_postback_referral), False)
        assert_that(equal_to(event.is_optin), False)
        assert_that(equal_to(event.is_delivery), False)
        assert_that(equal_to(event.is_account_linking), False)
        assert_that(equal_to(event.is_referral), False)
        assert_that(equal_to(event.timestamp), 1472028637825)
        assert_that(equal_to(event.sender_id), "1134343043305865")
        assert_that(equal_to(event.recipient_id), "1691462197845448")
        assert_that(equal_to(event.message_text), "Action")
        assert_that(
            equal_to(event.quick_reply_payload), event.quick_reply.get("payload")
        )
        counter1()

    @page.callback(["PICK_ACTION"], types=["QUICK_REPLY"])
    def button_callback(payload, event):
        counter2()

    page.handle_webhook(payload, postback=handler1)

    assert_that(1, equal_to(counter1.call_count))
    assert_that(1, equal_to(counter2.call_count))

    payload = """
        {"object":"page","entry":[{"id":"1691462197845448","time":1472028637866,
        "messaging":[{
            "sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472028637825,
            "message":{"quick_reply":{"payload":"PICK_COMEDY"},"mid":"mid.1472028637817:ae2763cc036a664b43","seq":834,"text":"Action"}}]}]}
        """
    page.handle_webhook(payload, postback=handler1)
    assert_that(2, equal_to(counter1.call_count))
    assert_that(1, equal_to(counter2.call_count))
