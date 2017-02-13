import os
import asyncio
import aiobotocore

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


async def go(loop):
    bucket = 'vodiybozor'
    filename = '563245235_1489327598.jpg'
    folder = 'houses'
    key = '{}/{}'.format(folder, filename)

    session = aiobotocore.get_session(loop=loop)
    client = session.create_client('s3', region_name='us-east-1',
                                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    # upload object to amazon s3
    # data = b'\x01' * 4096
    with open('huvaydo.jpg', 'rb') as data:
        resp = await client.put_object(Bucket=bucket, Key=key, Body=data)
        print('-------->', resp)

loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
