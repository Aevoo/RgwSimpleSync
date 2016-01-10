# RgwSimpleSync
##Use with caution !

  1. cp default.json_sample /etc/ceph/RgwSimpleSync/default.json (and set)
  2. mkdir -p /var/lib/ceph/RgwSimpleSync/clust-X/_bucketsmeta/
  3. Launch metadata collect : ./write_meta_bucket.py
  4. ./_sync.py
