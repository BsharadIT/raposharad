import boto3
iam = boto3.resource('iam') 
created_user = iam.create_user(
    UserName='thanos'
)
print(created_user)
