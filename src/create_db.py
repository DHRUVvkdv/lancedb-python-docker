import lancedb
import pandas as pd

# Create a new LanceDB database in the /tmp folder
db = lancedb.connect('tmp/my_lancedb')

# Create a table named 'users' with some sample data
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [28, 35, 42],
    'city': ['New York', 'San Francisco', 'London']
}

df = pd.DataFrame(data)

# Create a new table named 'users' and add the data
table = db.create_table('users', df)

print("Data added to the 'users' table:")
print(table.to_pandas())