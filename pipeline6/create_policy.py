import json

def create_iam_policy():
    iam = boto3.client('iam')

    my_managed_policy ={
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Allow",
			"Action": [
				"ec2:*"
			],
			"Resource": "*"
		}
	]
}
    response = iam.create_policy(
        PolicyName='ec2policy',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)
