#!/usr/bin/python
# coding: utf-8

import _connect, _get_meta_buckets

warningProd=_connect.get_rgw_conn('source', 1)

for _b in warningProd.get_all_buckets():
  _d=_get_meta_buckets.get_buckets_dict(warningProd, _b.name)
  _get_meta_buckets.dump_buckets_dict(_d.name)

