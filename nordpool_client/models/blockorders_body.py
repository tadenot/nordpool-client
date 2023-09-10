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

class BlockordersBody(object):
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
        'auction_id': 'str',
        'portfolio': 'str',
        'area_code': 'str',
        'comment': 'Comment',
        'blocks': 'list[Block]'
    }

    attribute_map = {
        'auction_id': 'auctionId',
        'portfolio': 'portfolio',
        'area_code': 'areaCode',
        'comment': 'comment',
        'blocks': 'blocks'
    }

    def __init__(self, auction_id=None, portfolio=None, area_code=None, comment=None, blocks=None):  # noqa: E501
        """BlockordersBody - a model defined in Swagger"""  # noqa: E501
        self._auction_id = None
        self._portfolio = None
        self._area_code = None
        self._comment = None
        self._blocks = None
        self.discriminator = None
        self.auction_id = auction_id
        self.portfolio = portfolio
        self.area_code = area_code
        if comment is not None:
            self.comment = comment
        self.blocks = blocks

    @property
    def auction_id(self):
        """Gets the auction_id of this BlockordersBody.  # noqa: E501

        Auction id.  # noqa: E501

        :return: The auction_id of this BlockordersBody.  # noqa: E501
        :rtype: str
        """
        return self._auction_id

    @auction_id.setter
    def auction_id(self, auction_id):
        """Sets the auction_id of this BlockordersBody.

        Auction id.  # noqa: E501

        :param auction_id: The auction_id of this BlockordersBody.  # noqa: E501
        :type: str
        """
        if auction_id is None:
            raise ValueError("Invalid value for `auction_id`, must not be `None`")  # noqa: E501

        self._auction_id = auction_id

    @property
    def portfolio(self):
        """Gets the portfolio of this BlockordersBody.  # noqa: E501

        Portfolio name.  # noqa: E501

        :return: The portfolio of this BlockordersBody.  # noqa: E501
        :rtype: str
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this BlockordersBody.

        Portfolio name.  # noqa: E501

        :param portfolio: The portfolio of this BlockordersBody.  # noqa: E501
        :type: str
        """
        if portfolio is None:
            raise ValueError("Invalid value for `portfolio`, must not be `None`")  # noqa: E501

        self._portfolio = portfolio

    @property
    def area_code(self):
        """Gets the area_code of this BlockordersBody.  # noqa: E501

        Area code  # noqa: E501

        :return: The area_code of this BlockordersBody.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this BlockordersBody.

        Area code  # noqa: E501

        :param area_code: The area_code of this BlockordersBody.  # noqa: E501
        :type: str
        """
        if area_code is None:
            raise ValueError("Invalid value for `area_code`, must not be `None`")  # noqa: E501

        self._area_code = area_code

    @property
    def comment(self):
        """Gets the comment of this BlockordersBody.  # noqa: E501


        :return: The comment of this BlockordersBody.  # noqa: E501
        :rtype: Comment
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this BlockordersBody.


        :param comment: The comment of this BlockordersBody.  # noqa: E501
        :type: Comment
        """

        self._comment = comment

    @property
    def blocks(self):
        """Gets the blocks of this BlockordersBody.  # noqa: E501

        List of order blocks.  # noqa: E501

        :return: The blocks of this BlockordersBody.  # noqa: E501
        :rtype: list[Block]
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this BlockordersBody.

        List of order blocks.  # noqa: E501

        :param blocks: The blocks of this BlockordersBody.  # noqa: E501
        :type: list[Block]
        """
        if blocks is None:
            raise ValueError("Invalid value for `blocks`, must not be `None`")  # noqa: E501

        self._blocks = blocks

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
        if issubclass(BlockordersBody, dict):
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
        if not isinstance(other, BlockordersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
