# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TAGGED(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, tokens: str=None, tags: str=None):  # noqa: E501
        """TAGGED - a model defined in Swagger

        :param tokens: The tokens of this TAGGED.  # noqa: E501
        :type tokens: str
        :param tags: The tags of this TAGGED.  # noqa: E501
        :type tags: str
        """
        self.swagger_types = {
            'tokens': str,
            'tags': str
        }

        self.attribute_map = {
            'tokens': 'tokens',
            'tags': 'tags'
        }

        self._tokens = tokens
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'TAGGED':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TAGGED of this TAGGED.  # noqa: E501
        :rtype: TAGGED
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tokens(self) -> str:
        """Gets the tokens of this TAGGED.


        :return: The tokens of this TAGGED.
        :rtype: str
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens: str):
        """Sets the tokens of this TAGGED.


        :param tokens: The tokens of this TAGGED.
        :type tokens: str
        """
        if tokens is None:
            raise ValueError("Invalid value for `tokens`, must not be `None`")  # noqa: E501

        self._tokens = tokens

    @property
    def tags(self) -> str:
        """Gets the tags of this TAGGED.


        :return: The tags of this TAGGED.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags: str):
        """Sets the tags of this TAGGED.


        :param tags: The tags of this TAGGED.
        :type tags: str
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags
