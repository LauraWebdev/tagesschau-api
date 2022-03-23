"""
    Tagesschau API

    Die Tagesschau ist eine Nachrichtensendung der ARD (Abkürzung für Arbeitsgemeinschaft der öffentlich-rechtlichen Rundfunkanstalten der Bundesrepublik Deutschland), die von ARD-aktuell in Hamburg produziert und mehrmals täglich ausgestrahlt wird. ARD-aktuell ist seit 1977 die zentrale Fernsehnachrichtenredaktion der ARD, bei welcher es sich wiederum um einen Rundfunkverbund handelt, der aus den Landesrundfunkanstalten und der Deutschen Welle besteht.<br>Über die hier dokumentierte API stehen auf [www.tagesschau.de](https://www.tagesschau.de) aktuelle Nachrichten und Medienbeiträge im JSON-Format zur Verfügung.<br>  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.tagesschau.model.homepage_response_regional import (
    HomepageResponseRegional,
)
from deutschland.tagesschau.model.news_response_news import NewsResponseNews

from deutschland import tagesschau

globals()["HomepageResponseRegional"] = HomepageResponseRegional
globals()["NewsResponseNews"] = NewsResponseNews
from deutschland.tagesschau.model.news_response import NewsResponse


class TestNewsResponse(unittest.TestCase):
    """NewsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNewsResponse(self):
        """Test NewsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NewsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
