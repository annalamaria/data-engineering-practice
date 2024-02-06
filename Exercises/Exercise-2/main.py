import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

main_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
timestamp = "2024-01-19 10:17"

def find_csv_url(url_address, time):
    response = requests.get(url_address) #get all data from the provided url

    soup = BeautifulSoup(response.content, "html.parser") #parsed object

    timestamp_element = soup.find(lambda tag:tag.name=="td" and time in tag.text) # get element tagged "td" containing timestamp
    print(timestamp_element)
    row = timestamp_element.parent # get parent element of the found timestamp, which is "tr"
    print(row)

    anchor_link = row.findChild("a") # get child element of row, a = anchor link
    print(anchor_link)

    href = anchor_link["href"] # get hyperlink from the anchor
    print(href)

    new_url = main_url + href # create new url directly to the file
    print(new_url)

    return new_url



def download_data(url_number, path_csv):

    file_name = url_number.split("/")[-1]
    file_name = file_name.split(".")[0] + ".csv"

    dataframe_csv = pd.read_csv(url_number)
    dataframe_csv.head()

    dataframe_csv.to_csv(path_csv + "/" + file_name)
    print(file_name + " saved")


def find_records(path_to_file):
    weather_data = pd.read_csv(path_to_file)

    # If values cannot be converted to numeric (value is 12s, for example), coerces to NA
    weather_data["HourlyDryBulbTemperature"] = pd.to_numeric(weather_data["HourlyDryBulbTemperature"], errors="coerce")

    max_value = weather_data["HourlyDryBulbTemperature"].max()

    print(max_value)


def main():

    filepath = "Exercises/Exercise-2/Downloads"

    os.makedirs(filepath, exist_ok=True)

    full_url = find_csv_url(main_url, timestamp) # retrieve complete url to directly download a specific csv file
    print(full_url)
    download_data(full_url,filepath) # download and save the csv file to downloads folder
    find_records("Exercises/Exercise-2/Downloads/01058099999.csv") # find and print the highest value from HourlyDryBulbTemperature column



if __name__ == "__main__":
    main()
