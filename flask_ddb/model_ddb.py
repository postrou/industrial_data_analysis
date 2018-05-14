import boto3
import time
import pickle


def create_table(endpoint_url="http://localhost:8000"):
    dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

    table = dynamodb.create_table(
        TableName='Models',
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


def add_model_to_db(table, model_filename='regression_model.pkl', name='linear_regression'):
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)
    table.put_item(
        Item={
            'time': time.strftime('%b %d %Y %H:%M:%S'),
            'name': name,
            'model': model
        }
    )
