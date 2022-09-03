# rrrratblog
[![](https://img.shields.io/badge/Python-3.8+-green.svg)]()
[![](https://img.shields.io/badge/Django-3.2.5-green.svg)]()
[![](https://img.shields.io/badge/Version-1.0-green.svg)]()
[![](https://img.shields.io/badge/COS_SDK-1.9.8-green.svg)]()
[![](https://img.shields.io/badge/Django_MDeditor-0.1.18-green.svg)]()
#### 介绍
##### rrrrat Blog，当前使用sqlite数据库，后期会迁移至MySQL 支持markdown编写文章，文章文类，内容分享，正在逐步完善
##### material风格，此项目纯属娱乐，如果有人觉得不错就告诉我，我继续优化
#### 演示站
```
http://rrrrat.rwwww.cn/
测试账号：test
测试密码：test
```
#### 安装教程
```python
# 修改参数配置
# utils/upload.py

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import uuid


secret_id = '*****'  # 修改为自己的secret_id
secret_key = '*****'  # 修改为自己的secret_key
region = 'ap-beijing'  # 修改为自己的region
token = None
scheme = 'https'
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)
source_url = 'http://cos.rwwww.cn'  # 修改为自己的source_url


def upload(dir, body, img_type=None):
    if img_type is None:
        img_type = body.__str__().split('.')[-1]
    guid = uuid.uuid4()
    ckey = '/' + dir + '/' + guid.__str__() + '.' + img_type
    response = client.put_object(
        Bucket='rwwww-1258128945',  # 修改为自己的Bucket
        Body=body,
        Key=ckey,
        StorageClass='STANDARD',
        EnableMD5=False
    )
    return source_url + ckey

```
```bash
1.导入虚拟环境
conda env create -f rrrrat.yaml
2.进入虚拟环境
conda activate rrrratblog
3.运行项目
python3 manage.py runserver 0.0.0.0:8080
```
```
退出虚拟环境
conda deactivate
```

#### 待完善

```
1.SEO优化
2.整体安全优化
3.资讯功能，伪链接
4.头像编码格式导致页面卡顿，预计下个版本优化
```
