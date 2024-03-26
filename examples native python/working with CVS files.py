import csv
filename = "C:/py_files/routerlist.cvs"
def read_csv(filename: str) -> list:
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents
    a row in the CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
        Each dictionary contains the column headers as keys and the column values as values.

    Raises:
        FileNotFoundError: If the file cannot be found.
        ValueError: If the file is not a CSV file.
    """
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        data = [dict(row) for row in reader]
    return data


data_dict = read_csv (filename)
print (data_dict[0]["IP address"])

def write_csv(data: list, filename: str) -> None:
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        data (list): A list of dictionaries, where each dictionary represents a row in the CSV file.
        filename (str): The path to the CSV file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the file cannot be found.
        ValueError: If the file is not a CSV file.
    """
    if not isinstance(data, list):
        raise ValueError("data must be a list of dictionaries")

    if not isinstance(filename, str):
        raise ValueError("filename must be a string")

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


