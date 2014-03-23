kakasi-utils
============

[![PyPI version](https://badge.fury.io/py/kakasi-utils.png)](http://badge.fury.io/py/kakasi-utils)

[KAKASI 漢字→かな(ローマ字)変換プログラム](http://kakasi.namazu.org) をより便利使うためのユーティリティ.

kanwa.py
--------
複数のテキスト形式の辞書ファイルを結合して, テキスト形式の辞書ファイルを出力するユーティリティ.

**mkkanwa でテキスト形式の辞書を結合してバイナリ形式の辞書を作成する場合, 重複チェックが行なわれないため, 同じ項目が複数登録されてしまうことがありますが, このユーティリティを使うことで重複する項目を1つにまとめられます.**

結合したテキスト形式の辞書を mkkanwa を用いてバイナリ形式の辞書に変換し, KAKASI で利用することが出来ます.

### 要件
* Python 2.7+
* KAKASI

### 使い方
1. `pip install kakasi-utils`
2. 結合したいテキスト形式の辞書ファイルを用意します.  
KAKASI 標準の辞書は KAKASI のソースコード内に kakasidict として入っています.  
独自の辞書を利用する場合は文字コード EUC-JP, 改行コード LF で作成します. 具体的な例は下の“テキスト形式の辞書の例”を参照してください.
3. `pykanwa merged_kakasidict kakasidict mydict1 mydict2 ` を実行すると, kakasidict と mydict1, mydict2 の3つの辞書を結合して, merged_kakasidict という名前のファイルに出力されます.
4. `mkkanwa kanwadict merged_kakasidict` を実行して, 結合したテキスト形式の辞書をバイナリ形式の辞書に変換します.
5. 出力された kanwadict を適切な場所に配置して利用します.

### テキスト形式の辞書の例
```
;; この行はコメントです
;; よみ 漢字の順に記入していきます
;; 文字コード EUC-JP, 改行コード LF で作成します
きょうと 京都
よしだ 吉田
```
