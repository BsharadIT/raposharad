import boto3
import json

iam = boto3.client('iam')
def create_policy():
    with open('pipeline6/create_policy', 'r') as f:
        policy_document = json.load(f)
    response = iam.create_policy(
        PolicyName="abc",
        PolicyDocument=json.dumps(policy_document) 
    )
def create_user():
    response = iam.create_user(
        UserName='bob1'
    )
    print(response)
def attach_policy():
    response = iam.attach_user_policy(
    UserName='bob',
    PolicyArn='arn:aws:iam::430912479781:policy/xyz3'
)
create_policy()
# create_user()
# attach_policy()
