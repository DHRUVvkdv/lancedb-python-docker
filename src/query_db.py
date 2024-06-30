import json
import lancedb
import asyncio
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/users")
async def get_users():
    # Connect to the existing LanceDB database
    db = lancedb.connect('tmp/my_lancedb')

    # Get the 'users' table
    users_table = db.open_table('users')

    # Fetch all data from the table
    all_users = users_table.to_pandas()

    # Convert DataFrame to list of dictionaries for JSON serialization
    users_list = all_users.to_dict(orient='records')

    return {"users": users_list}

# Handler for AWS Lambda
mangum_handler = Mangum(app)

def lambda_handler(event, context):
    # Create the database if it doesn't exist
    import create_db

    # Check if the event is from API Gateway
    if 'requestContext' in event and 'http' in event['requestContext']:
        # If it's from API Gateway, use Mangum handler
        return mangum_handler(event, context)
    else:
        # If it's a direct Lambda invocation, handle it ourselves
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(get_users())