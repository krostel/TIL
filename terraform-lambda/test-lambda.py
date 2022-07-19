import boto3
import json
from moto import mock_s3


@mock_s3
def test_lambda_handler(monkeypatch):

	# set up src test bucket
	s3_client = boto3.client('s3')
	test_bucket_name_src = '		'
	test_data = b'col_1,col_2\n1,2\n3,4\n'
	test_object_key = f'example/s3/path/key/test_data.csv'

	s3_client.create_bucket(Bucket=test_bucket_name_src)    
	s3_client.put_object(Body=test_data, Bucket=test_bucket_name_src, Key=test_object_key)

	# set up dst test bucket
	test_bucket_name_dst = 'test_bucket_dst'
	s3_client.create_bucket(Bucket=test_bucket_name_dst)

	monkeypatch.setenv('DST_BUCKET', test_bucket_name_dst)
	from lambda_handler.index import handler

	test_s3_event = {
	    "Records": [{
	        "s3": {
	            'bucket': {'name': test_bucket_name_src},
	            'object': {
	                'key': test_object_key
	            }
	        }
	    }]}

	response = handler(event=test_s3_event, context={})

	copied_object = s3_client.get_object(Bucket=test_bucket_name_dst, Key=test_object_key)
	copied_object_data = copied_object['Body'].read()

	assert response['status'] == 'ok'
	assert copied_object_data == test_data

