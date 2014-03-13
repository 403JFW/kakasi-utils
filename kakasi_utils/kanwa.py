#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs


class Kanwa(object):
    def __init__(self):
        self.table = {}

    def merge(self, input_dicts, output_dict):
        for input_dict in input_dicts:
            self._merge_file(input_dict)
        with codecs.open(output_dict, 'w', 'euc_jp') as out_file:
            for line in self.table:
                out_file.write(line)

    def _merge_file(self, input_dict):
        with codecs.open(input_dict, 'rU', 'euc_jp') as in_file:
            for line in in_file:
                self._add_word(line)

    def _add_word(self, word):
        if word[0:2] == ';;':
            return
        if not word in self.table:
            self.table[word] = True
