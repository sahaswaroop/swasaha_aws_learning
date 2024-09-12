import json

def lambda_handler(event):
    # TODO implement
    print('event',event)
    #print('context',context)
    print(event['Records'][0])
    print(event['Records'][0]['s3']['bucket']['name'])
    print(event['Records'][0]['s3']['object']['key'])
    print(event['Records'][0]['s3']['object']['size'])
    
    if (event['Records'][0]['s3']['object']['size'] <=200):
        return {
            'status code':200,
            'body': {'s3 bucket name':event['Records'][0]['s3']['bucket']['name'],
                     's3 file name':event['Records'][0]['s3']['object']['key'],
                     's3 file size':event['Records'][0]['s3']['object']['size']
                }
        }
    else:
        return {
        'statusCode': 413,
        'body': 'File size exceeded 100MB'
    }

event={'Records': [
{'eventVersion': '2.1', 
'eventSource': 'aws:s3', 
'awsRegion': 'ap-south-1', 
'eventTime': '2024-09-07T18:30:17.175Z', 
'eventName': 'ObjectCreated:Put', 
'userIdentity': {'principalId': 'AWS:AIDA45Y2RYHB2O2OT5NRP'}, 
'requestParameters': {'sourceIPAddress': '49.37.131.183'}, 
'responseElements': {'x-amz-request-id': 'EG1691P38TF3CA1W', 'x-amz-id-2': 'bWTwTeSg1oBG+AJvMywmKH/3qcl8nQbecw/lGlpoLe5NpfU6g0OlkKJaOoewQYUK+L/z9zFwt9Iv73dVaTEgeLIBDeSREODY'}, 
's3': {'s3SchemaVersion': '1.0', 'configurationId': 'd0bce9d6-ba29-4e6f-91a3-b75442a66f69', 'bucket': {'name': 'gds-assignment-first', 'ownerIdentity': {'principalId': 'AAJ7YE3TO4UNP'}, 'arn': 'arn:aws:s3:::gds-assignment-first'}, 
'object': {'key': 'store_data.csv', 'size': 205, 'eTag': 'ea80dca37ad6212e5b69da09939d9679', 'versionId': 'q1dIFaquqBA.m98z0qVXNGznm9dQSnFU', 'sequencer': '0066DC9BB92791B527'}}}
]}

print(lambda_handler(event))
