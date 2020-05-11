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


class Jobset(object):
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
        'fetcherrormsg': 'str',
        'nixexprinput': 'str',
        'errormsg': 'str',
        'emailoverride': 'str',
        'nixexprpath': 'str',
        'enabled': 'bool',
        'jobsetinputs': 'dict(str, JobsetInput)'
    }

    attribute_map = {
        'fetcherrormsg': 'fetcherrormsg',
        'nixexprinput': 'nixexprinput',
        'errormsg': 'errormsg',
        'emailoverride': 'emailoverride',
        'nixexprpath': 'nixexprpath',
        'enabled': 'enabled',
        'jobsetinputs': 'jobsetinputs'
    }

    def __init__(self, fetcherrormsg=None, nixexprinput=None, errormsg=None, emailoverride=None, nixexprpath=None, enabled=None, jobsetinputs=None, local_vars_configuration=None):  # noqa: E501
        """Jobset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fetcherrormsg = None
        self._nixexprinput = None
        self._errormsg = None
        self._emailoverride = None
        self._nixexprpath = None
        self._enabled = None
        self._jobsetinputs = None
        self.discriminator = None

        self.fetcherrormsg = fetcherrormsg
        if nixexprinput is not None:
            self.nixexprinput = nixexprinput
        if errormsg is not None:
            self.errormsg = errormsg
        if emailoverride is not None:
            self.emailoverride = emailoverride
        self.nixexprpath = nixexprpath
        if enabled is not None:
            self.enabled = enabled
        if jobsetinputs is not None:
            self.jobsetinputs = jobsetinputs

    @property
    def fetcherrormsg(self):
        """Gets the fetcherrormsg of this Jobset.  # noqa: E501

        contains the error message when there was a problem fetching sources for a jobset  # noqa: E501

        :return: The fetcherrormsg of this Jobset.  # noqa: E501
        :rtype: str
        """
        return self._fetcherrormsg

    @fetcherrormsg.setter
    def fetcherrormsg(self, fetcherrormsg):
        """Sets the fetcherrormsg of this Jobset.

        contains the error message when there was a problem fetching sources for a jobset  # noqa: E501

        :param fetcherrormsg: The fetcherrormsg of this Jobset.  # noqa: E501
        :type: str
        """

        self._fetcherrormsg = fetcherrormsg

    @property
    def nixexprinput(self):
        """Gets the nixexprinput of this Jobset.  # noqa: E501

        the name of the jobset input which contains the nixexprpath  # noqa: E501

        :return: The nixexprinput of this Jobset.  # noqa: E501
        :rtype: str
        """
        return self._nixexprinput

    @nixexprinput.setter
    def nixexprinput(self, nixexprinput):
        """Sets the nixexprinput of this Jobset.

        the name of the jobset input which contains the nixexprpath  # noqa: E501

        :param nixexprinput: The nixexprinput of this Jobset.  # noqa: E501
        :type: str
        """

        self._nixexprinput = nixexprinput

    @property
    def errormsg(self):
        """Gets the errormsg of this Jobset.  # noqa: E501

        contains the stderr output of the nix-instantiate command  # noqa: E501

        :return: The errormsg of this Jobset.  # noqa: E501
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        """Sets the errormsg of this Jobset.

        contains the stderr output of the nix-instantiate command  # noqa: E501

        :param errormsg: The errormsg of this Jobset.  # noqa: E501
        :type: str
        """

        self._errormsg = errormsg

    @property
    def emailoverride(self):
        """Gets the emailoverride of this Jobset.  # noqa: E501

        email address to send notices to instead of the package maintainer (can be a comma separated list)  # noqa: E501

        :return: The emailoverride of this Jobset.  # noqa: E501
        :rtype: str
        """
        return self._emailoverride

    @emailoverride.setter
    def emailoverride(self, emailoverride):
        """Sets the emailoverride of this Jobset.

        email address to send notices to instead of the package maintainer (can be a comma separated list)  # noqa: E501

        :param emailoverride: The emailoverride of this Jobset.  # noqa: E501
        :type: str
        """

        self._emailoverride = emailoverride

    @property
    def nixexprpath(self):
        """Gets the nixexprpath of this Jobset.  # noqa: E501

        the path to the file to evaluate  # noqa: E501

        :return: The nixexprpath of this Jobset.  # noqa: E501
        :rtype: str
        """
        return self._nixexprpath

    @nixexprpath.setter
    def nixexprpath(self, nixexprpath):
        """Sets the nixexprpath of this Jobset.

        the path to the file to evaluate  # noqa: E501

        :param nixexprpath: The nixexprpath of this Jobset.  # noqa: E501
        :type: str
        """

        self._nixexprpath = nixexprpath

    @property
    def enabled(self):
        """Gets the enabled of this Jobset.  # noqa: E501

        when set to true the jobset gets scheduled for evaluation  # noqa: E501

        :return: The enabled of this Jobset.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Jobset.

        when set to true the jobset gets scheduled for evaluation  # noqa: E501

        :param enabled: The enabled of this Jobset.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def jobsetinputs(self):
        """Gets the jobsetinputs of this Jobset.  # noqa: E501

        inputs configured for this jobset  # noqa: E501

        :return: The jobsetinputs of this Jobset.  # noqa: E501
        :rtype: dict(str, JobsetInput)
        """
        return self._jobsetinputs

    @jobsetinputs.setter
    def jobsetinputs(self, jobsetinputs):
        """Sets the jobsetinputs of this Jobset.

        inputs configured for this jobset  # noqa: E501

        :param jobsetinputs: The jobsetinputs of this Jobset.  # noqa: E501
        :type: dict(str, JobsetInput)
        """

        self._jobsetinputs = jobsetinputs

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
        if not isinstance(other, Jobset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Jobset):
            return True

        return self.to_dict() != other.to_dict()
