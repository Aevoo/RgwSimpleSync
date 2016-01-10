#!/usr/bin/python
# coding: utf-8

import _connect, _get_meta_buckets
from multiprocessing import Process, Lock, Value, Pool
import time
import traceback

_num_procs=8
_num_rgw=_connect.get_num_rgw()
_effect_num_procs=_num_procs*_num_rgw

destination=_connect.get_rgw_conn("destination", 1)

_list_buckets_dest=[k.name for k in destination.get_all_buckets()]

def sync_bucket(i):
  source=_connect.get_rgw_conn("source", i%_num_rgw)
  position=0
  empty=False
  _aevooys_dict=[]
  _prodys_dict=[]
  while not empty:
    try:
      time.sleep(10)
      _next=i+position*_effect_num_procs
      position+=1
      if _next <= _list_buckets_dest.__len__():
        _bucket_dest=_list_buckets_dest[_next]
        try:
          _connect.aevooys.head_bucket(_bucket_dest)
        except:
          print _bucket_dest + ' does not exist'
          continue
        if _get_meta_buckets.is_bucket_sync('Prod', _bucket_dest):
          print _bucket_dest + ' already sync'
          continue
        try:
          _aevooys_dict=_get_meta_buckets.get_buckets_dict(destination, _bucket_dest)
          _prodys_dict=_get_meta_buckets.load_buckets_dict('Prod', _bucket_dest)
        except:
          print traceback.print_exc()
          print _bucket_dest + ' Error get_buckets_dict'
          continue
        _bucket=_get_meta_buckets.get_bucket_wrong_key_dict(_prodys_dict, _aevooys_dict)
        _source_bucket=source.get_bucket(_bucket_dest)
        _dest_bucket=destination.get_bucket(_bucket_dest)
        for _key in _bucket[1]:
          _new_key=_dest_bucket.new_key(_key)
          _new_key.set_contents_from_string(_source_bucket.get_key(_key).get_contents_as_string())
        print _bucket_dest + ' is sync'
        _get_meta_buckets.bucket_is_sync('Prod', _bucket_dest)
      else:
        empty=True
    except:
      traceback.print_exc()

if __name__ == '__main__':
  print _effect_num_procs
  pool = Pool(processes=_effect_num_procs)
  pool.map(sync_bucket, range(_effect_num_procs))
