import os

import boto3


def main():
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket='example-bucket')

    for content in response['Contents']:
        print(content['Key'])


if __name__ == '__main__':
    main()
