from .process_file import main
from flask import jsonify

# when file is sent to backend, it is processed and sent to api
def delegate(file):
    processed_file = main(file)
    print('this is what we have processed here')
    print (processed_file)
    return jsonify({'status': 'success', 'processed_file': processed_file})

