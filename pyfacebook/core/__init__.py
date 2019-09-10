# -*- coding: utf-8 -*-
import requests

from pyfacebook.config import DEBUG
from pyfacebook.config import FACEBOOK_GRAPH_TOKEN
from pyfacebook.config import FACEBOOK_GRAPH_URL
from pyfacebook.config import FACEBOOK_GRAPH_VERSION
from pyfacebook.config import HEADER_AUTH_KEY
from pyfacebook.config import HEADER_AUTH_VAL_PREFIX
from pyfacebook.config import WORKPLACE_ACCESS_TOKEN
from pyfacebook.config import WORKPLACE_API_VERSION
from pyfacebook.config import WORKPLACE_URL
from pyfacebook.core.enum import BaseEnum
from pyfacebook.mixins import BaseMixin


class NotificationType(BaseEnum):
    regular = "REGULAR"
    silent_push = "SILENT_PUSH"
    no_push = "NO_PUSH"


class SettingType(BaseEnum):
    greeting = "greeting"
    call_to_actions = "call_to_actions"


class ThreadState(BaseEnum):
    new_thread = "new_thread"
    existing_thread = "existing_thread"


class Base(BaseMixin):
    """Base Workplace Wrapper
    https://developers.facebook.com/docs/workplace/
    """

    _auth_args = None
    _after_send = None
    _response = None
    _request_endpoint = None

    version = None
    access_token = None
    endpoint = None
    url = None

    def __init__(self, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
            url
        """

        self.version = kwargs.get("version", WORKPLACE_API_VERSION)
        self.access_token = kwargs.get("access_token", WORKPLACE_ACCESS_TOKEN)
        self.url = "{}{}/".format(WORKPLACE_URL, self.version)

    def _send(self, **kwargs):
        """Make request for request by method
        Input:
            request: recipient id to send to
        Output:
            Response from API as <dict>
        """
        if DEBUG:
            self._response = kwargs
            return self._response

        if kwargs.get("method"):
            kwargs["method"] = kwargs.get("method").upper()

        self._response = requests.request(**kwargs)
        return self._response

    @property
    def auth_args(self):
        """Make auth args validation
        https://developers.facebook.com/docs/workplace/
        """
        if not self._auth_args:
            self._auth_args = {
                HEADER_AUTH_KEY: "{} {}".format(
                    HEADER_AUTH_VAL_PREFIX, self.access_token
                )
            }
        return self._auth_args

    @property
    def request_endpoint(self):
        return self.url + self.endpoint

    @property
    def response(self):
        return self._response or None

    @response.setter
    def response(self, value):
        raise NotImplementedError("Not Implemented")

    def send_raw(self, **kwargs):
        """Make raw request for facebook
        Input:
            resource: recipient id to send to
            method: (get, put, post)
            data: data content
        Output:
            Response from API as <dict>
        """
        kwargs["headers"] = kwargs.get("headers", self.auth_args)
        kwargs["url"] = self.request_endpoint
        if kwargs.get("url_request"):
            kwargs["url"] = "{}{}".format(kwargs["url"], kwargs["url_request"])
            del kwargs["url_request"]

        return self._send(**kwargs)

    def send_message(
        self, recipient_id, message, notification_type=NotificationType.regular
    ):
        return self.send_recipient(
            recipient_id, {"message": message}, notification_type
        )

    def send_recipient(
        self, recipient_id, payload, notification_type=NotificationType.regular
    ):
        payload["recipient"] = {"id": recipient_id}
        payload["notification_type"] = notification_type.value
        return self.send_raw(**{"payload": payload})


class Facebook(Base):
    endpoint = "/me/messages"

    @property
    def auth_args(self):
        """Make auth args validation
        """
        if not self._auth_args:
            self._auth_args = {"access_token": self.access_token}
        return self._auth_args

    def __init__(self, *args, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
            url
        """

        self.version = kwargs.get("version", FACEBOOK_GRAPH_VERSION)
        self.access_token = kwargs.get("access_token", FACEBOOK_GRAPH_TOKEN)
        self.url = "{}{}/".format(FACEBOOK_GRAPH_URL, self.version)

    def send_raw(self, **kwargs):
        """Make raw request for facebook
        Input:
            url: url request endpoint
            json: payload
        Output:
            Response from API as <dict>
        """
        kwargs["url"] = "{}{}".format(self.url, self.endpoint)
        kwargs["params"] = self.auth_args
        kwargs["json"] = kwargs.pop("payload")
        kwargs["headers"] = {"Content-type": "application/json"}
        kwargs["method"] = "post"

        return self._send(**kwargs)


class Workplace(Base):
    pass
