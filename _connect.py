import boto
import boto.s3.connection
import json


""" default.json sample
{
  "source": {
    "urls": {
      "url1":"http://localhost:80",
      "url2":"http://localhost:81",
      "url3":"http://localhost:82"
    },
    "access_key": "XXXXXXXXXXXXXXXXXXXXX",
    "secret_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  },
  "destination": {
    "urls": {
      "url1":"http://localhost:8080"
    },
    "access_key": "XXXXXXXXXXXXXXXXXXXXX",
    "secret_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  }
}
"""
conf=json.load(open('/etc/ceph/RgwSimpleSync/default.json', 'r'))

def get_rgw_source(source_or_dest,_id):
  _s_conf=conf[source_or_dest]
  _url=_s_conf["urls"]["url"+str(_id)]
  print _s_conf["access_key"]
  print _s_conf["secret_key"]
  return boto.connect_s3(
    aws_access_key_id    =_s_conf["access_key"],
    aws_secret_access_key=_s_conf["secret_key"],
    host=_url.split(':')[-2][2:],
    port=int(_url.split(':')[-1]),
    is_secure=_url.split(':')[0] == 'https',
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),)

def get_num_rgw(source_or_dest):
  return conf[source_or_dest]["urls"].__len__()
