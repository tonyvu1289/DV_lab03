# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


############################## Your code for loading and preprocess the data ##
import os
import urllib.request



DATA_PATH = "./household_power_consumption.txt"

# download the data if it is not already downloaded

if not os.path.exists(DATA_PATH):
    URL = "https://nymph332088.github.io/CIS4340/labassignments/Lab3/household_power_consumption.zip"
    print(f"Data has not downloaded yet, download data at: {URL}")

    from io import BytesIO
    from zipfile import ZipFile
    print("Retrieving the infomation")
    res = urllib.request.urlopen(URL)
    zipfile = ZipFile(BytesIO(res.read()))
    zipfile.extractall(path="./")
else:
    print(f"Data was downloaded")


df = pd.read_csv(DATA_PATH, sep=";", na_values="?")

# As suggested, we convert the Date columns following the format DD/MM/YYYY.
df.Date = pd.to_datetime(df.Date, format="%d/%m/%Y")

# Settings the filter for choosing the date that we care about, here is 01.02.2007 and 02.02.2007
start_date = '2007-02-01'
end_date = '2007-02-02'
filt = (df.Date >= start_date) & (df.Date <= end_date)
selected_df = df.loc[filt]


selected_df.Time = pd.to_datetime(selected_df.Date.astype(str)+' ' + selected_df.Time)

############################ Complete the following 4 functions ###############
import matplotlib.dates as mdates

# create a directory for saving plots
if not os.path.exists("./figures"):
    os.mkdir("./figures")


############################ Complete the following 4 functions ###############
def plot1():
    plt.figure(figsize=(10,10))
    
    plt.hist(selected_df.Global_active_power, bins=15, color="red", edgecolor="#000")
    
    plt.title("Global Active Power")
    plt.xlabel("Global Active Power (kilowatts)")
    plt.ylabel("Frequency")
    plt.savefig("./figures/plot1.png")
    plt.show()


def plot2():
    plt.figure(figsize=(10,10))
    # config the xaxis following the format in https://www.w3schools.com/python/python_datetime.asp
    # and the web we got https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/
    # The docs can be found on the main page of matplotlib
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator()) 
    plt.plot(selected_df.Time, selected_df.Global_active_power, color="#000") 
    plt.ylabel("Global Active Power (kilowatts)") 
    plt.savefig("./figures/plot2.png") 
    plt.show()



def plot3():
    fig, ax = plt.subplots(figsize=(10, 10))


    # re-config
    fig.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    fig.gca().xaxis.set_major_locator(mdates.DayLocator())
     
    plt.plot(selected_df.Time, selected_df.Sub_metering_1, color="#000", label="Sub_metering_1")
    plt.plot(selected_df.Time, selected_df.Sub_metering_2, color="red", label="Sub_metering_2")
    plt.plot(selected_df.Time, selected_df.Sub_metering_3, color="blue", label="Sub_metering_3")
    plt.ylabel("Energy sub metering") 
    ax.legend(loc='upper right', shadow=True, fontsize='x-large')
    plt.savefig("./figures/plot3.png") 
    plt.show()


def plot4():
    (n_rows, n_cols) = (2, 2)
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 10))

    ax[0, 0].plot(selected_df.Time, selected_df.Global_active_power, color="#000")
    ax[0, 0].set_ylabel("Global Active Power (kilowatts)")
    ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    ax[0, 0].xaxis.set_major_locator(mdates.DayLocator())


    ax[0, 1].plot(selected_df.Time, selected_df.Voltage, color="#000")
    ax[0, 1].set_xlabel("datetime")
    ax[0, 1].set_ylabel("Voltage")
    ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    ax[0, 1].xaxis.set_major_locator(mdates.DayLocator())

    
    ax[1, 0].xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    ax[1, 0].xaxis.set_major_locator(mdates.DayLocator())
    ax[1, 0].plot(selected_df.Time, selected_df.Sub_metering_1, color="#000", label="Sub_metering_1")
    ax[1, 0].plot(selected_df.Time, selected_df.Sub_metering_2, color="red", label="Sub_metering_2")
    ax[1, 0].plot(selected_df.Time, selected_df.Sub_metering_3, color="blue", label="Sub_metering_3")
    ax[1, 0].set_ylabel("Energy sub metering")
    ax[1, 0].legend(loc='upper right', shadow=True, fontsize='x-large')


    ax[1, 1].plot(selected_df.Time, selected_df.Global_reactive_power, color="#000")
    ax[1, 1].set_xlabel("datetime")
    ax[1, 1].set_ylabel("Global_reactive_power")
    ax[1, 1].xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    ax[1, 1].xaxis.set_major_locator(mdates.DayLocator())


    plt.savefig("./figures/plot4.png")
    plt.show()
plot1()
plot2()
plot3()
plot4()
