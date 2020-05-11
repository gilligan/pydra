# coding: utf-8

"""
    Hydra API

    Specification of the Hydra REST API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hydra_client.configuration import Configuration


class Evaluations(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'first': 'str',
        'next': 'str',
        'last': 'str',
        'evals': 'list[dict(str, JobsetEval)]'
    }

    attribute_map = {
        'first': 'first',
        'next': 'next',
        'last': 'last',
        'evals': 'evals'
    }

    def __init__(self, first=None, next=None, last=None, evals=None, local_vars_configuration=None):  # noqa: E501
        """Evaluations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first = None
        self._next = None
        self._last = None
        self._evals = None
        self.discriminator = None

        if first is not None:
            self.first = first
        if next is not None:
            self.next = next
        if last is not None:
            self.last = last
        if evals is not None:
            self.evals = evals

    @property
    def first(self):
        """Gets the first of this Evaluations.  # noqa: E501

        first list of results  # noqa: E501

        :return: The first of this Evaluations.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Evaluations.

        first list of results  # noqa: E501

        :param first: The first of this Evaluations.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def next(self):
        """Gets the next of this Evaluations.  # noqa: E501

        next list of results  # noqa: E501

        :return: The next of this Evaluations.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Evaluations.

        next list of results  # noqa: E501

        :param next: The next of this Evaluations.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def last(self):
        """Gets the last of this Evaluations.  # noqa: E501

        last list of results  # noqa: E501

        :return: The last of this Evaluations.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Evaluations.

        last list of results  # noqa: E501

        :param last: The last of this Evaluations.  # noqa: E501
        :type: str
        """

        self._last = last

    @property
    def evals(self):
        """Gets the evals of this Evaluations.  # noqa: E501

        List of evaluations  # noqa: E501

        :return: The evals of this Evaluations.  # noqa: E501
        :rtype: list[dict(str, JobsetEval)]
        """
        return self._evals

    @evals.setter
    def evals(self, evals):
        """Sets the evals of this Evaluations.

        List of evaluations  # noqa: E501

        :param evals: The evals of this Evaluations.  # noqa: E501
        :type: list[dict(str, JobsetEval)]
        """

        self._evals = evals

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Evaluations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Evaluations):
            return True

        return self.to_dict() != other.to_dict()
