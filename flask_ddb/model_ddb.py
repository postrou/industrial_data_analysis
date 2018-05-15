import time


def create_table(client):
    client.create_table(
        TableName='Models',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'time',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'time',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )


def add_model_to_db(client, table_name, model, request, name='linear_regression'):
    client.put_item(
        TableName=table_name,
        Item={
            'name':     {'S': name},
            'time':     {'S': time.strftime('%b %d %Y %H:%M:%S')},
            'model':    {'B': model},
            'request':  {'S': request}
        }
    )

    return 'ok'
