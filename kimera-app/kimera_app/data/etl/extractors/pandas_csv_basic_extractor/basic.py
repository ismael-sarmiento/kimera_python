import kimera_data.components.etl as kimera_etl


def extract_csv_file():
    extractor = kimera_etl.extractor().engine('pandas').format('csv').option("filepath_or_buffer", 'basic.csv').option('sep', ';')
    return extractor.read()


if __name__ == '__main__':
    data = extract_csv_file()
    print(f"Extractor: \n{data}")
