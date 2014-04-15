#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from kakasi_utils.converters import _convert_item_from_google_to_kakasi


class TestConverters(unittest.TestCase):
    def test_convert_item_from_google_to_kakasi(self):
        input_item = "きょうと\t京都\t名詞\tコメント\n"
        expected_output = "きょうと 京都"
        output_item = _convert_item_from_google_to_kakasi(input_item)
        self.assertEqual(output_item, expected_output)
