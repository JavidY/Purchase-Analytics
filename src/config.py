import json
import os

# get root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# get config filename
CONFIG_FILE = "{0}/src/{1}".format(ROOT_DIR, 'config.json')


# retrieves folder name for input csv files
def get_input_folder():
    with open(CONFIG_FILE) as json_data_file:
        data = json.load(json_data_file)
        return "{0}/{1}".format(ROOT_DIR,
                                data.get('paths').get('input_folder_name'))


if __name__ == '__main__':
    print(get_input_folder())
