import time


def create_table(client):

    client.create_table(
        TableName='Data',
        KeySchema=[
            {
                'AttributeName': 'fit/predict',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'time',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'fit/predict',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'time',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )


def add_data_to_db(client, table_name, data, purpose):
    client.put_item(
        TableName=table_name,
        Item={
            'fit/predict':  {'S': purpose},
            'time':         {'S': time.strftime('%b %d %Y %H:%M:%S')},
            'data':         {'NS': data}
        }
    )

    return 'ok'
