import pandas as pd

def test_should_pass():
    print("This will always pass!")
    assert True

def test_get_column_names():
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    assert cols == ['name', 'age', 'state', 'balance']

def test_get_columns_of_type():
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_columns_of_type(df, 'object')
    print(f"Columns of type 'object': {cols}")
    assert cols == ['name', 'state']
    cols = get_columns_of_type(df, 'int64')
    print(f"Columns of type 'int64: {cols}")
    assert cols == ['age']

def test_get_unique_values():
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    vals = get_unique_values(df, 'state')
    print(f"Unique values of 'state': {vals}")
    assert vals == ['NY', 'PA', 'NJ']


def test_get_file_extension():
    assert get_file_extension('/some/file/data.csv') == 'csv'
    assert get_file_extension('/home/important_grades.xlsx') == 'xlsx'
    assert get_file_extension('countries.json') == 'json'

def test_load_file():
    df = load_file('data/grades.csv', 'csv')
    assert df.shape == (8, 5)
    df = load_file('data/grades.xlsx', 'xlsx')
    assert df.shape == (8, 5)
    df = load_file('data/grades.json', 'json')
    assert df.shape == (8, 5)
