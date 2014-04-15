#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import unittest

from kakasi_utils.kanwa import Kanwa


class TestKanwa(unittest.TestCase):
    def test_merge(self):
        """Test merge"""
        # Get dict file paths
        data_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
        in_files = [
            data_dir + "test_kanwa_input_a.txt",
            data_dir + "test_kanwa_input_b.txt"
        ]
        out_file = data_dir + "test_kanwa_output.txt"

        # Run merge
        kanwa = Kanwa()
        kanwa.merge(in_files, out_file)

        # Assert result
        for in_file in in_files:
            self._assert_dict_in_dict(in_file, out_file)

        # Check duplication
        self._load_dict(out_file, check_duplication=True)

        os.remove(out_file)

    def _assert_dict_in_dict(self, file_child, file_parent):
        """Assert that child dict files item in parent dict file"""
        dict_child = self._load_dict(file_child)
        dict_parent = self._load_dict(file_parent)
        for item in dict_child.keys():
            if item not in dict_parent:
                raise AssertionError("'%s' not exists in %s" % (
                    item, dict_parent))

    def _load_dict(self, in_dict_file, check_duplication=False):
        """Load KAKASI dict file and return python dict"""
        table = {}
        with codecs.open(in_dict_file, 'rU', 'euc_jp') as in_file:
            for line in in_file:
                line = line.rstrip()
                if line[0:2] == ';;':
                    continue
                if check_duplication and (line in table):
                    raise AssertionError("'%s' duplicates" % line)
                table[line] = True
        return table
