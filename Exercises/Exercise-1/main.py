import requests
import os
import pandas as pd
from zipfile import ZipFile
from zipfile import BadZipfile
import io


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_data(url_number):

    filepath = "Exercises/Exercise-1/Downloads"

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    response = requests.get(download_uris[url_number])

    file_name = download_uris[url_number].split("/")[-1]
    file_name = file_name.split(".")[0] + ".csv"
    print("converting " + file_name + " to csv")

    try:
        with ZipFile(io.BytesIO(response.content)) as myzip:
            with myzip.open(myzip.namelist()[0]) as myfile:
                response_data = pd.read_csv(myfile)

        response_data.to_csv(filepath + "/" + file_name)
        print(file_name + " saved to Downloads")
        pass

    except BadZipfile:
        print(file_name + " is not a zipfile")




def main():
    n_of_files = len(download_uris)
    current_file = 0

    for current_file in range(n_of_files):
        print("processing file number ", current_file)
        download_data(current_file)
        current_file = current_file + 1
    pass

if __name__ == "__main__":
    main()
