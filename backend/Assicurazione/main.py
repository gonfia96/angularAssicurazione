# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=False)


@app.route('/json', methods=['GET'])
def apiClient():
    stringa = ''
    first_name = 'matte'
    last_name = 'gigi'

    return jsonify({
        'success': True,
        'firstName': first_name,
        'lastName': last_name
    })


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
