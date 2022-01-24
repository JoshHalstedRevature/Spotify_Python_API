import boto3
from botocore.exceptions import ClientError
import os

class AmazonS3:
    """"""
    access_key='AKIAVN5DMUWWEASRSHYO'
    secret_key='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'

    def upload(self, fileName='test_data/testS3.txt'):
        """"""
        AS3 = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key)
        try:
            response = AS3.upload_file('/home/maria_dev/testLin.txt', 'spotify-api-practice-october-batch', fileName)
            print(response)
        except ClientError as e:
            return False
        return True