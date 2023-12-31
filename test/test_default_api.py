# coding: utf-8

"""
    Auction API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nordpool_client
from nordpool_client.api.default_api import DefaultApi  # noqa: E501
from nordpool_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auctions_auction_id_external_get(self):
        """Test case for auctions_auction_id_external_get

        Auctions Contracts  # noqa: E501
        """
        pass

    def test_auctions_auction_id_external_orders_get(self):
        """Test case for auctions_auction_id_external_orders_get

        Auctions Orders  # noqa: E501
        """
        pass

    def test_auctions_auction_id_external_portfoliovolumes_get(self):
        """Test case for auctions_auction_id_external_portfoliovolumes_get

        Auctions Portfolio Volumes  # noqa: E501
        """
        pass

    def test_auctions_auction_id_external_prices_get(self):
        """Test case for auctions_auction_id_external_prices_get

        Auctions Prices  # noqa: E501
        """
        pass

    def test_auctions_auction_id_external_trades_get(self):
        """Test case for auctions_auction_id_external_trades_get

        Auctions Trades  # noqa: E501
        """
        pass

    def test_auctions_get(self):
        """Test case for auctions_get

        Auctions by closeBidding  # noqa: E501
        """
        pass

    def test_blockorders_order_id_get(self):
        """Test case for blockorders_order_id_get

        BlockOrder by Id  # noqa: E501
        """
        pass

    def test_blockorders_order_id_patch(self):
        """Test case for blockorders_order_id_patch

        BlockOrder modify  # noqa: E501
        """
        pass

    def test_blockorders_post(self):
        """Test case for blockorders_post

        BlockOrder submit  # noqa: E501
        """
        pass

    def test_connect_token_post(self):
        """Test case for connect_token_post

        Token auction  # noqa: E501
        """
        pass

    def test_curveorders_order_id_get(self):
        """Test case for curveorders_order_id_get

        CurveOrder By Id  # noqa: E501
        """
        pass

    def test_curveorders_order_id_patch(self):
        """Test case for curveorders_order_id_patch

        CurveOrder modify  # noqa: E501
        """
        pass

    def test_curveorders_post(self):
        """Test case for curveorders_post

        CurveOrder submit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
