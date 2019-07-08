import json
import os


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
CONFIG_FILE = "{0}\\src\\{1}".format(ROOT_DIR, 'config.json')


# retrieves path to input files from app directory
def get_input_path():
    with open(CONFIG_FILE) as json_data_file:
        data = json.load(json_data_file)
        return "{0}\\{1}".format(ROOT_DIR, data.get('paths').get('source'))


if __name__ == '__main__':
	print(get_input_path())
