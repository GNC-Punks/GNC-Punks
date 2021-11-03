import os
import requests
import json
import time

ITERATE_LOOPS = 200

for iteration in range(ITERATE_LOOPS):

    # GET OFFSET (IGNORE .DS_Store)
    json_directory = './assets'

    files = os.listdir(json_directory)

    FILES_LENGTH = 0
    limit = 50

    for file in files:
        if not file == ".DS_Store":
            FILES_LENGTH += 1

    args_dict = {
        "files_length": FILES_LENGTH,
        "limit": limit
    }

    # SAVE FILES AS JSON
    url = "https://api.opensea.io/api/v1/assets?order_direction=asc&offset={files_length}&limit={limit}&collection=gncpunks".format(**args_dict)

    response = requests.request("GET", url)
    response_str = str(response.text)

    response_json = json.loads(response_str)

    assets = response_json["assets"]

    for asset in assets:
        filename = 'assets/' + str(asset['id']) + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(asset, f, ensure_ascii=False, indent=4)
        
    time.sleep(5)
    print("fetched json records!!!")