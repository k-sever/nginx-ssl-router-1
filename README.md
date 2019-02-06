# nginx-ssl-router

[![CircleCI](https://circleci.com/gh/verygood-ops/nginx-ssl-router.svg?style=svg)](https://circleci.com/gh/verygood-ops/nginx-ssl-router)

This role configures nginx as a reverse proxy for terminating custom ssl certificates and forwarding the requests on to an existing cluster of servers that are running generic hostnames.

In order to use this we need to follow a specific data structure for storing data.

Certificates must be stored in the `ssl_router_s3_bucket` S3 bucket on AWS. Within there they must reside within a folder prefixed by `ssl_router_s3_path`. The next portion of the path name is the backend server to send the traffic to and then within this folder must exist a file containing both the server key and certificate as well as any intermediate certificates that are required in the trust chain.

As an example given `ssl_router_s3_bucket`="foo" and `ssl_router_s3_path`="ssl/" for a site with a backend called test.sandbox.verygoodproxy.com and a custom CNAME host of vault.customer.com we would use a path like "s3://foo/ssl/test.sandbox.verygoodproxy.com/vault.customer.com" where the file "vault.customer.com" would look something like

```
-----BEGIN RSA PRIVATE KEY-----
<vault.customer.com key here>
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
<vault.customer.com certificate here>
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
<trust chain certificate here>
-----END CERTIFICATE-----
```

**NOTE** If the cert file is invalid it will cause nginx to fail to reload which will abort this playbook.

Test like `AWS_PROFILE=vg AWS_DEFAULT_REGION=us-west-2 ansible-playbook -i localhost tests/test.yml`

License
-------

AGPL

Author Information
------------------

Very Good Group

