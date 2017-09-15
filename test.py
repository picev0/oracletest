# -*- coding: utf-8 -*-
# cx_Oracleを用いたPythonでのORACLE操作
#1.Oracleクライアントをインストールする
#この際、開発者用環境を作る
#(おそらく、OCIが必要?)
#2.以下からダウンロードしてインストールするか、easu_installする
#cx_Oracle
#http://cx-oracle.sourceforge.net/

import os
import cx_Oracle
os.environ["NLS_LANG"] = "JAPANESE_JAPAN.AL32UTF8"
try:
    tns = cx_Oracle.makedsn("127.0.0.1", 1521, "orcl")
    conn = cx_Oracle.connect("SYS", "oracle" ,tns, mode=cx_Oracle.SYSDBA)
    cur = conn.cursor()
    cur.execute("SELECT * FROM 商品マスタ")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    
except (cx_Oracle.DatabaseError) as ex:
    error,=ex.args
    print(error.message)