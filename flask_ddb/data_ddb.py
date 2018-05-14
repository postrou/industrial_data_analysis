import boto3
import time


def create_table(endpoint_url="http://localhost:8000"):
    dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

    table = dynamodb.create_table(
        TableName='Fit_data',
        KeySchema=[
            {
                'AttributeName': 'time',
                'KeyType': 'HASH'  #Partition key
            },

            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'time',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table


def add_data_to_db(table, data, number=0):
    table.put_item(
        Item={
            'time': time.strftime('%b %d %Y %H:%M:%S'),
            'name': name,
            'model': model
        }
    )
