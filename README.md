### Instructions for verifying the GNC Punks collection on Opensea:

- make sure you have python installed
- in a terminal and the root of this repo run `python3 -m venv venv` to create a virtual environment
- `source venv/bin/activate` to activate the virtual environment
- `pip install -r requirements.txt` to install dependencies in the virtual environment
- create a folder in the root call 'assets'
- `python3 scripts/opensea-downloader.py` to download the json files for the whole 10k GNC Punks collection. Note, this will take a few minutes.
- `python3 scripts/find_missing_find_dupes.py` to check all the GNC Punks for duplicates and missing serial numbers from 0 to 9999.
