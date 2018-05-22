
def create_table(client):

    client.create_table(
        TableName='Data',
        KeySchema=[
            {
                'AttributeName': 'fit/predict',
                'KeyType': 'HASH'
            },
            # {
            #     'AttributeName': 'time',
            #     'KeyType': 'RANGE'
            # },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'fit/predict',
                'AttributeType': 'S'
            },
            # {
            #     'AttributeName': 'time',
            #     'AttributeType': 'S'
            # },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )


def add_fit_data_to_db(client, table_name, X, y):
    client.put_item(
        TableName=table_name,
        Item={
            'fit/predict':  {'S': 'fit'},
            # 'time':         {'S': time.strftime('%b %d %Y %H:%M:%S')},
            'X':            {'B': X},
            'y':            {'B': y},
        }
    )

    return 'ok'


def add_predict_data_to_db(client, table_name, X):
    client.put_item(
        TableName=table_name,
        Item={
            'fit/predict':  {'S': 'predict'},
            # 'time':         {'S': time.strftime('%b %d %Y %H:%M:%S')},
            'X':            {'B': X},
        }
    )

    return 'ok'


# def get_data_from_db(client, table_name, type_of):
#     data = client.get_item(
#         TableName=table_name,
#         Key={
#             'fit/predict': {'S': type_of},
#         },
#     )
#     return data['Item']['X']['S']
