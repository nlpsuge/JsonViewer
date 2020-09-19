import traceback
from datetime import datetime

from benedict import benedict
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

import os
base_path = os.path.abspath(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from configs import menus
from configs.settings import UnixTimestampType
from model.web_result import WebResult
from utils import string_utils

# app = Flask("json_viewer", template_folder="../../frontend/web/htmls")
app = Flask("json_viewer")

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# https://github.com/pallets/flask/issues/974
# Prevent the json result to be sorted
app.config["JSON_SORT_KEYS"] = False

# Only convert the time later than the value of date_later_than
date_later_than = '2014-01-01 0:0:0.000'
unix_timestamp_type = UnixTimestampType.SECOND


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/json', methods=['PUT'])
def update_json():
    request_data = request.get_json()
    original_json = request_data['original_json']
    if string_utils.empty_string(original_json):
        return jsonify(WebResult.success('').to_json())

    dt = datetime.strptime(date_later_than, "%Y-%m-%d %H:%M:%S.%f")
    if unix_timestamp_type == UnixTimestampType.SECOND:
        time_delta = (dt - datetime(1970, 1, 1)).total_seconds()
    elif unix_timestamp_type == UnixTimestampType.MILLISECOND:
        time_delta = (dt - datetime(1970, 1, 1)).total_seconds() * 1000

    operate_type = request_data['operate_type']
    if operate_type == 'pretty':

        try:
            # Disable the keypath functionality passing keypath_separator=None in the constructor.
            original_json_benedict = benedict(original_json, keypath_separator=None)
        except Exception as e:
            print('Failed to decode the raw json due to "' + str(e) + '"')
            print(traceback.format_exc())
            return jsonify(WebResult.failed(message=str(e)).to_json())

        def traverse_item(dct, key, value):
            if type(value) is int:

                if value > time_delta:
                    formatted_date = datetime.fromtimestamp(1598702450).strftime("%Y-%m-%d %H:%M:%S.%f")
                    print("Modifying a int type data [{}] to [{}], its key is [{}]"
                          .format(value, formatted_date, key))
                    dct[key] = formatted_date
            # print('key: {} - value: {}'.format(key, value))
        original_json_benedict.traverse(traverse_item)

        wr_json = WebResult.success(original_json_benedict)
        return jsonify(wr_json.to_json())


@app.route('/menus', methods=['GET'])
def get_menus():
    wr = WebResult.success(menus.MENUS)
    return jsonify(wr.to_json())


def run():
    app.run()


if __name__ == '__main__':
    run()

