import pickle

def get_buckets_dict(conn, _bucket):
  _buckets_dict=[_bucket, {}]
  for _key in conn.get_bucket(_bucket):
    _buckets_dict[1][_key.name] = _key.etag[1:-1]
  return _buckets_dict

def dump_buckets_dict(_buckets_dict):
  _file='/var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/'+_buckets_dict+'.dict'
  pickle.dump(_buckets_dict, open(_file, 'wb'))

def load_buckets_dict(_buckets_dict):
  _file='/var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/'+_buckets_dict+'.dict'
  return pickle.load(open(_file, 'rb'))

import os.path
def exist_buckets_dict(_buckets_dict):
  return os.path.isfile('/var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/'+_buckets_dict+'.dict') 

def is_bucket_sync(_buckets_dict):
  return os.path.isfile('/var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/'+_buckets_dict+'.dict.sync')

def bucket_is_sync(_buckets_dict):
  return open('/var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/'+_buckets_dict+'.dict.sync', 'w').close() 

def get_bucket_wrong_key_dict(_bucketsource, _bucketdestination):
  _bucket_wrong_key_dict=[_bucketsource[0], []]
  _bucket_wrong_key_dict[1]=[k for k in _bucketsource[1] if not _bucketdestination[1].has_key(k) or _bucketsource[1][k] != _bucketdestination[1][k]]
  return _bucket_wrong_key_dict
