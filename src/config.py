import json


def get_src_path():
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        return data.get('paths').get('source')


if __name__ == '__main__':
    print(get_src_path())
