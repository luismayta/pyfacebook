# -*- coding: utf-8 -*-
from pyfacebook.core import Facebook


class Graph(Facebook):

    community_id = None
    fields = {
        "fields": ",".join(
            (
                "id",
                "name",
                "members",
                "email",
                "privacy",
                "description",
                "updated_time",
                "administrator",
            )
        )
    }

    def __init__(self, *args, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
            url
            community_id
        """
        if not kwargs.get("community_id"):
            raise ValueError("community_id is required")
        super(Graph, self).__init__(*args, **kwargs)
        self.community_id = kwargs["community_id"]
        self.url = "{}{}".format(self.url, self.community_id)

    def send_raw(self, **kwargs):
        """Make raw request for facebook
        Input:
            url: url request endpoint
            json: payload
        Output:
            Response from API as <dict>
        """
        kwargs["url"] = "{}{}".format(self.url, self.endpoint)
        kwargs["headers"] = kwargs.get("headers", self.auth_args)
        return self._send(**kwargs)


class Group(Graph):
    endpoint = "/members"

    def get_all_members(self, fields=None):
        """Get all members of group.
        Input:
        Output:
            Response from API as <dict>
        """
        kwargs = {}
        kwargs["params"] = self.fields
        if fields:
            kwargs["params"] = fields
        return self.send_raw(**kwargs)

    def add_member(self, email):
        """Add member To group.
        Input:
            email
        Output:
            Response from API as <dict>
        """
        kwargs = {}
        kwargs["data"] = {"email": email}
        kwargs["method"] = "post"
        return self.send_raw(**kwargs)

    def remove_member(self, email):
        """Remove member of group.
        Input:
            email
        Output:
            Response from API as <dict>
        """
        kwargs = {}
        kwargs["data"] = {"email": email}
        kwargs["method"] = "delete"
        return self.send_raw(**kwargs)
