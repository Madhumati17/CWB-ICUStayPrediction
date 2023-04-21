import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "subject_id": 0,
        "admittime": "2000-01-01T00:00:00.000Z",
        "admission_type": "example_value",
        "insurance": "example_value",
        "language": "example_value",
        "religion": "example_value",
        "marital_status": "example_value",
        "ethnicity": "example_value",
        "gender": "example_value",
        "dob": "2000-01-01T00:00:00.000Z",
        "AGE": 0,
        "ICUSTAY_AGE_GROUP": "example_value"
      }
    ]
  },
  "GlobalParameters": 1.0
}

body = str.encode(json.dumps(data))

url = 'http://2676d449-eaf5-4a0e-aded-78db47d0ac06.eastus.azurecontainer.io/score'


headers = {'Content-Type':'application/json'}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))