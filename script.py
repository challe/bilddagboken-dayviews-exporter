import requests
import json
import urllib.request
import time
import os
from retrying import retry

diaryName = "Accountname"
imageId = "xxxxxxxx"

def get_data(imageId):
    url = "http://dayviews.com/p/ajax.html?action=getJsonImage&id=" + imageId + "&diaryname=" + diaryName + "&read_exif=0&json=1"

    print(url)

    response = request_with_retry(url)

    if response.status_code == 200:
        try:
            data = response.json()
            
            folder = "output"
            imageName = data["year"] + "-" + data["month"] + "-" + data["day"] + " " + data["imageInfo"]["id"]
            path = folder + "/" + imageName + ".png"

            if not os.path.exists(path):
                urlretrieve_with_retry(data["HDSizeSRC"], path)
                time.sleep(3)
            
            time.sleep(3)

            if not data["nextImageId"] is None:
                get_data(data["nextImageId"])
                
        except json.decoder.JSONDecodeError:
            print("Could not parse JSON for url: " + url)

    else:
        print(response.text)
        print(response.status_code)

@retry(stop_max_attempt_number=5, wait_fixed=2000)
def request_with_retry(url):
    return requests.get(url)

@retry(stop_max_attempt_number=5, wait_fixed=2000)
def urlretrieve_with_retry(url, path):
    return urllib.request.urlretrieve(url, path)

get_data(imageId)
