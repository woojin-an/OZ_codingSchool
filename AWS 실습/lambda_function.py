def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name', 'World')
    message = f"Hello, {name}!"
    return {
        'statusCode': 200,
        'body': message
    }
