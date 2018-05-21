def create_table(client):
    client.create_table(
        TableName='Models',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            # {
            #     'AttributeName': 'time',
            #     'AttributeType': 'S'
            # }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )


def add_model_to_db(client, table_name, model, name='linear_regression'):
    client.put_item(
        TableName=table_name,
        Item={
            'name':     {'S': name},
            'model':    {'B': model},
        }
    )

    return 'ok'


def get_model_from_db(client, table_name, name='linear_regression'):
    model = client.get_item(
        TableName=table_name,
        Key={
            'name': {'S': name},
        },
    )
    return model['Item']['model']['B']
