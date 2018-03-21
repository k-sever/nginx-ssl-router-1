#!/usr/bin/env python

import argparse
import boto3


PREFIX = 'ssl'


def main(args):
    client = boto3.client('s3')
    response = client.list_objects(Bucket=args.bucket, Prefix=PREFIX + '/')

    for f in response['Contents']:
        src = f['Key']
        dest = rename(src)
        if not args.dry_run and dest:
            copy(src, dest, client, args.bucket)
        else:
            print(src, dest)


def copy(src, dest, client, bucket):
    copy_source = {
        'Bucket': bucket,
        'Key': src
    }
    extra_args = {
        'ServerSideEncryption': 'AES256'
    }
    result = client.copy(copy_source, bucket, dest, extra_args)
    print(result)


def rename(key):
    try:
        _, upstream, host = key.split('/')
    except:
        print('ERROR: ' + key)
        return
    parts = (
        # prefix
        PREFIX,
        # version
        '2',
        # no passthrough
        'np',
        # static upstream
        upstream.replace(upstream.split('.')[0], 'reverse'),
        # data environment
        'sandbox' if 'sandbox' in upstream else 'live',
        # tenant id
        upstream.split('.')[0],
        # custom host name
        host
    )
    return '/'.join(parts)


if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('bucket')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false')
    parser.set_defaults(dry_run=True)

    main(parser.parse_args())
