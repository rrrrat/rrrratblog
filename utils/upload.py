# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   upload.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/26 1:50 下午
@Software       :   PyCharm
@Show           :
"""
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import uuid


secret_id = 'secret_id'
secret_key = 'secret_key'
region = 'region'
token = None
scheme = 'https'
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)
source_url = 'source_url'


def upload(dir, body, img_type=None):
    if img_type is None:
        img_type = body.__str__().split('.')[-1]
    guid = uuid.uuid4()
    ckey = '/' + dir + '/' + guid.__str__() + '.' + img_type
    response = client.put_object(
        Bucket='Bucket',
        Body=body,
        Key=ckey,
        StorageClass='STANDARD',
        EnableMD5=False
    )
    return source_url + ckey
