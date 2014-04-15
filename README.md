kakasi-utils
============

[![Build Status](https://travis-ci.org/403JFW/kakasi-utils.svg?branch=master)](https://travis-ci.org/403JFW/kakasi-utils)
[![Coverage Status](https://coveralls.io/repos/403JFW/kakasi-utils/badge.png?branch=master)](https://coveralls.io/r/403JFW/kakasi-utils?branch=master)
[![PyPI version](https://badge.fury.io/py/kakasi-utils.png)](http://badge.fury.io/py/kakasi-utils)

[KAKASI 漢字→かな(ローマ字)変換プログラム](http://kakasi.namazu.org) をより便利使うためのユーティリティ.

要件
----
* Python 2.7+, Python 3.2+ or PyPy
* KAKASI

インストール
------------
```
pip install kakasi-utils
```

ユーティリティ
--------------

### pykanwa
複数のテキスト形式の辞書ファイルを結合して, テキスト形式の辞書ファイルを出力するユーティリティ.

**mkkanwa でテキスト形式の辞書を結合してバイナリ形式の辞書を作成する場合, 重複チェックが行なわれないため, 同じ項目が複数登録されてしまうことがありますが, このユーティリティを使うことで重複する項目を1つにまとめられます.**

結合したテキスト形式の辞書を mkkanwa を用いてバイナリ形式の辞書に変換し, KAKASI で利用することが出来ます.

#### 使い方
1. 結合したいテキスト形式の辞書ファイルを用意します.  
KAKASI 標準の辞書は KAKASI のソースコード内に kakasidict として入っています.  
独自の辞書を利用する場合は文字コード EUC-JP, 改行コード LF で作成します. 具体的な例は下の“テキスト形式の辞書の例”を参照してください.
2. `pykanwa merged_kakasidict kakasidict mydict1 mydict2 ` を実行すると, kakasidict と mydict1, mydict2 の3つの辞書を結合して, merged_kakasidict という名前のファイルに出力されます.
3. `mkkanwa kanwadict merged_kakasidict` を実行して, 結合したテキスト形式の辞書をバイナリ形式の辞書に変換します.
4. 出力された kanwadict を適切な場所に配置して利用します.

#### テキスト形式の辞書の例
```
;; この行はコメントです
;; よみ 漢字の順に記入していきます
;; 文字コード EUC-JP, 改行コード LF で作成します
きょうと 京都
よしだ 吉田
```

### google2kakasi
Google 日本語入力からエクスポートした辞書を, KAKASI のテキスト形式の辞書に変換するユーティリティ.

#### 使い方
1. Google 日本語入力から辞書ファイルをエクスポートします.
2. エクスポートした辞書ファイル名が google.txt のとき `google2kakasi google.txt kakasi.txt` を実行すると, kakasi.txt に KAKASI のテキスト形式の辞書が出力されます.

#### Google 日本語入力からエクスポートした辞書の例
```
きょうと<TAB>京都<TAB>地名<TAB>コメント1
よしだ<TAB>吉田<TAB>地名<TAB>コメント2
```
`<TAB>` はタブ (\t) です.
