import json
import os

# get root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# get config filename
CONFIG_FILE = "{0}/src/{1}".format(ROOT_DIR, 'config.json')

# get OLTP db creds
DB_NAME_OLTP = os.environ.get("DB_NAME_OLTP")
DB_USER_OLTP = os.environ.get("DB_USER_OLTP")
DB_PASS_OLTP = os.environ.get("DB_PASS_OLTP")


# retrieves folder name for input csv files
def get_input_folder():
    with open(CONFIG_FILE) as json_data_file:
        data = json.load(json_data_file)
        return "{0}/{1}".format(ROOT_DIR,
                                data.get('paths').get('input_folder_name'))


if __name__ == '__main__':
    None
