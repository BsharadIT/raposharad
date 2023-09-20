import boto3
iam = boto3.resource('iam') 
created_user = iam.create_user(
    UserName='thanos1'
)
print(created_user)
