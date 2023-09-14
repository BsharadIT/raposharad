def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName="bob2")
    print(response)
