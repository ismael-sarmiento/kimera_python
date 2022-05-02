import kimera_data.components.etl as kimera_etl


def multi_extracts_csv():
    extractor1 = kimera_etl.extractor().engine('pandas').format('csv').option("filepath_or_buffer", 'basicI.csv').option('sep', ';')
    extractor2 = kimera_etl.extractor().engine('pandas').format('csv').option("filepath_or_buffer", 'basicII.csv').option('sep', ';')
    return kimera_etl.extractor().multiple([extractor1, extractor2]).read()


if __name__ == '__main__':

    data = multi_extracts_csv()

    for data, count in zip(data, range(len(data))):
        print(f"Extractor {count}: \n{data}")
