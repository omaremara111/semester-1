
import httpx
import pandas as pd
import matplotlib.pyplot as plt

api_key="My key"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code (should be checked)
print(response.status_code)

if response.status_code != 200:
    print("Error:", response.status_code)
    print(response.text)
    exit()

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']

print(temp_data)

# use pandas to convert data to dataframe
df = pd.DataFrame(temp_data)

df[["tempmin", "temp", "tempmax"]] = (
    df[["tempmin", "temp", "tempmax"]] - 32
) * 5 / 9

print(df)

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs

df.plot(x="datetime", y=["tempmin", "temp", "tempmax"])

plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.title("Daily Temperatures in Leeds")

plt.show()

# annotate the graph with axis labels

# note that temperature is in Fahrenheit (F)
# convert to Celsius before plotting

# using the documentation explore other data, eg. rainfall
