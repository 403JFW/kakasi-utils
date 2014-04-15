#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs


def google_to_kakasi(google_dict, kakasi_dict):
    with codecs.open(google_dict, 'rU', 'utf-8') as in_file:
        with codecs.open(kakasi_dict, 'w', 'euc_jp') as out_file:
            for item in in_file:
                kakasi_item = _convert_item_from_google_to_kakasi(item) + '\n'
                out_file.write(kakasi_item)


def _convert_item_from_google_to_kakasi(item):
    es = item.rstrip().split('\t')
    return es[0] + ' ' + es[1]
