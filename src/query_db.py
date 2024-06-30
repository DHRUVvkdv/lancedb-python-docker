import lancedb

# Connect to the existing LanceDB database
db = lancedb.connect('/data/my_lancedb')

# Get the 'users' table
users_table = db.open_table('users')

# Fetch all data from the table
all_users = users_table.to_pandas()
print("All users:")
print(all_users)

# # Perform a simple query (e.g., users older than 30)
# older_users = users_table.to_pandas(filter="age > 30")
# print("\nUsers older than 30:")
# print(older_users)

# # Perform a more complex query (e.g., users from New York or London)
# city_users = users_table.to_pandas(filter="city = 'New York' OR city = 'London'")
# print("\nUsers from New York or London:")
# print(city_users)

# # Search for a specific user by name
# alice = users_table.to_pandas(filter="name = 'Alice'")
# print("\nUser named Alice:")
# print(alice)