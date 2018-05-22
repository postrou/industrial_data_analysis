# import time


def create_table(client):
    client.create_table(
        TableName='Requests',
        KeySchema=[
            {
                'AttributeName': 'request',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'request',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )


def add_request_to_db(client, table_name, request):
    client.put_item(
        TableName=table_name,
        Item={
            'request': {'S': request},
        }
    )

    return 'ok'


def get_request_from_db(client, table_name, request):
    client.get_item(
        TableName=table_name,
        Key={
            'name': {'S': request},
        }
    )