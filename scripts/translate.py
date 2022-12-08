import requests
import os
import argparse

# Get environment variables
translator_endpoint = os.environ["AZURE_TRANSLATOR_ENDPOINT"]
translator_region = os.environ["AZURE_TRANSLATOR_REGION"]
translator_key = os.environ["AZURE_TRANSLATOR_SUBSCRIPTION_KEY"]

# Get input arguments
parser = argparse.ArgumentParser(description='Translate a JSON file')
parser.add_argument('--input-file-name', dest='file_name_in', action='store',
                    help='you need to supply file name where your JSON to be translated is located')
parser.add_argument('--output-file-name', dest='file_name_out', action='store',
                    help='you need to supply file name where the translated JSON will be saved')
parser.add_argument('--verbose', dest='verbose', action='store_true',
                    default=False,
                    help='run in verbose mode (default: False)')
args = parser.parse_args()

# Get JSON
try:
    with open(file_name_in) as f:
        checklist = json.load(f)
except Exception as e:
    print("ERROR: Error when processing JSON file", file_name_in, "-", str(e))
    sys.exit(1)

# Go over all keys and translate them if required
for (k, v) in checklist.items():
    print(k, type(v))

