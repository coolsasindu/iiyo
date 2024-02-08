import csv
import os

class CustomDictionary:
    def __init__(self, csv_file):
        self.dictionary = self.load_dictionary(csv_file)

    def load_dictionary(self, csv_file, encoding='utf-8-sig'):
        dictionary = {}
        with open(csv_file, 'r', encoding=encoding) as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                key = row['wordKey']
                data = row['Data']
                if key in dictionary:
                    dictionary[key].append(data)
                else:
                    dictionary[key] = [data]
        return dictionary

    def search_exact_key(self, search_key):
        return self.dictionary.get(search_key, ['Key not found'])

def word(search_key, csv_file_path=None):
    # If csv_file_path is not provided, use the current working directory
    csv_file_path = csv_file_path or os.path.join(os.path.dirname(__file__), 'Data.csv')

    my_dictionary = CustomDictionary(csv_file_path)
    return my_dictionary.search_exact_key(search_key)
