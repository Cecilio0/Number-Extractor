def extract_from_folder(folder: str):
    import os

    # Extract data from csv files
    with open('output.txt', 'w', encoding='utf-8') as file:
        for file_name in os.listdir(folder):
            if file_name.endswith(".csv"):
                file_path = f"{folder}/{file_name}"
                extract_from_csv(file_path, file)

    # Clean output
    with open('output.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    content = content[:-3]
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Listo el pollo')

def extract_from_csv(file_path: str, file):
    import pandas as pd
    df = pd.read_csv(file_path)
    key = df.keys()[0]

    # Extract data from csv
    df[key] = df[key].str.split('_').str[1]

    # Write data to file
    for index, row in df.iterrows():
        file.write(f"{row[key][:5]} + ")


if __name__ == '__main__':
    csv_dir = 'files'
    extract_from_folder(csv_dir)
