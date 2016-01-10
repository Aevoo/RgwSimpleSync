# RgwSimpleSync

##Not a complet sync
Copy buckets source to buckets destination

### Used to replicate 135 million objets in > 2300 buckets

###Requires :
 - 2 configured  clusters ceph
 - Buckets already created on the destination

Only buckets defined on the destination are copied

##Use with caution !

  1. cp default.json_sample /etc/ceph/RgwSimpleSync/default.json (and set)
  2. mkdir -p /var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/
  3. Launch metadata collect : ./write_meta_bucket.py
  4. ./_sync.py

##Description /var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/*.dict

[
  "BucketName",
  {
    "key1":"md5",
    "key2":"md5",
    ...
}]
