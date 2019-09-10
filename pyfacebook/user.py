# -*- coding: utf-8 -*-
from pyfacebook.core import Workplace


class User(Workplace):
    """Actions for resources Users
    https://developers.facebook.com/docs/workplace/account-management/api
    """

    endpoint = "Users"

    def filter_by_email(self, email):
        """Filter by email
        https://developers.facebook.com/scim/v1/Users?filter=userName%20eq%20%22juliusc@example.com%22
        Input:
          email: email of user
        Output:
          Response from API as <dict>
        """
        kwargs = {"params": {"filter": 'userName+eq+"{}"'.format(email)}}
        return self.send_raw(**kwargs)

    def get_by_id(self, user_id):
        """Get by user_id
        https://developers.facebook.com/scim/v1/Users/{{user_id}}
        Input:
          user_id: user id
        Output:
          Response from API as <dict>
        """
        kwargs = {}
        kwargs["url_request"] = "/{}".format(user_id)
        return self.send_raw(**kwargs)

    def update(self, user_id, data):
        """Update
        https://www.facebook.com/scim/v1/Users/{Workplace-assigned user id}
        Input:
          user_id: id de facebook user
          data: payload json data
        Output:
          Response from API as <dict>
        """
        kwargs = {}
        kwargs["url_request"] = "/{}".format(user_id)
        kwargs["data"] = data
        kwargs["method"] = "put"
        return self.send_raw(**kwargs)
