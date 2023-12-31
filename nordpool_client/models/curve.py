# coding: utf-8

"""
    Auction API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Curve(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'contract_id': 'str',
        'curve_points': 'list[CurvePoint]'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'curve_points': 'curvePoints'
    }

    def __init__(self, contract_id=None, curve_points=None):  # noqa: E501
        """Curve - a model defined in Swagger"""  # noqa: E501
        self._contract_id = None
        self._curve_points = None
        self.discriminator = None
        if contract_id is not None:
            self.contract_id = contract_id
        if curve_points is not None:
            self.curve_points = curve_points

    @property
    def contract_id(self):
        """Gets the contract_id of this Curve.  # noqa: E501

        Contract id.  # noqa: E501

        :return: The contract_id of this Curve.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this Curve.

        Contract id.  # noqa: E501

        :param contract_id: The contract_id of this Curve.  # noqa: E501
        :type: str
        """

        self._contract_id = contract_id

    @property
    def curve_points(self):
        """Gets the curve_points of this Curve.  # noqa: E501

        List of curve points.  # noqa: E501

        :return: The curve_points of this Curve.  # noqa: E501
        :rtype: list[CurvePoint]
        """
        return self._curve_points

    @curve_points.setter
    def curve_points(self, curve_points):
        """Sets the curve_points of this Curve.

        List of curve points.  # noqa: E501

        :param curve_points: The curve_points of this Curve.  # noqa: E501
        :type: list[CurvePoint]
        """

        self._curve_points = curve_points

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Curve, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Curve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
