def extract_from_folder(folder: str):
    import os

    with open('output.txt', 'w', encoding='utf-8') as file:
        for file_name in os.listdir(folder):
            if file_name.endswith(".csv"):
                file_path = f"{folder}/{file_name}"
                extract_from_csv(file_path, file)

    content: str = ""
    with open('output.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    content = content[:-3]
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(content)

def extract_from_csv(file_path: str, file):
    import pandas as pd
    df = pd.read_csv(file_path)
    print(df.keys()[0])
    print(df.head())
    key = df.keys()[0]
    df[key] = df[key].str.split('_').str[1]
    for index, row in df.iterrows():
        # print(f"{row['Collection: Etereo'][:5]} + ", end='')
        file.write(f"{row[key][:5]} + ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_dir = 'files'
    extract_from_folder(csv_dir)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
