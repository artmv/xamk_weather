import csv
import statistics
mylist, newlist, newdate = [], [], []

# Function 1: choose between Helsinki, Tampere or Turku. import data from csv to list
def menu_file():
    name = input("Give name of the file: ")
    if name == "helsinki.csv":
        print("Loaded weather data from Helsinki")
        with open('helsinki.csv', newline='') as file:
            for row in csv.reader(file):
                mylist.append(row[0])
    if name == "tampere.csv":
        print("Loaded weather data from Tampere")
        with open('tampere.csv', newline='') as file:
            for row in csv.reader(file):
                mylist.append(row[0])
    if name == "turku.csv":
        print("Loaded weather data from Turku")
        with open('turku.csv', newline='') as file:
            for row in csv.reader(file):
                mylist.append(row[0])
# replace "; with ," in list, i.e. split one list to sublists to ease search of elements
    for i in mylist:
        newlist.append(i.split(';'))

# Function 2: select date
def menu_date():
    date = input("Give a date (dd.mm): ")
# convert user input from "Day.Month" to "Month-Day" format to ease date matching
    day = str(date[3:5] + "-" + date[0:2])
# match user input with dates in list
    for i in range(1,len(newlist)):
        if (newlist[i][0])[5:10] == day:
            print("The weather on", date, "was on average", newlist[i][2], "centigrade")
            print("The lowest temperature was", newlist[i][3], "and the highest temperature was", newlist[i][4])
            print("There was", newlist[i][1], "mm rain")

# Function 3: print averages
def menu_stats():
    mean, min, max = [], [], []
# calculate mean of tempreture means, mins and maxs
    for i in range(1,len(newlist)):
        mean.append(float(newlist[i][2]))
        ave_mean = round(statistics.mean(mean),1)
    for i in range(1,len(newlist)):
        min.append(float(newlist[i][3]))
        ave_min = round(statistics.mean(min),1)
    for i in range(1,len(newlist)):
        max.append(float(newlist[i][4]))
        ave_max = round(statistics.mean(max),1)
# print results
    print("The average temperature for the", len(newlist) - 1, "day period was", ave_mean)
    print("The average lowest temperature was", ave_min)
    print("The average highest temperature was", ave_max)

# Function 4: scatterplot (with matplotlib)
def menu_plot():
    import matplotlib.pyplot as plt
    x_data, y_data = [], []
# make lists for x and y
    for i in range(1,len(newlist)):
        x_data.append(str(newlist[i][0])[0:10])
    for i in range(1,len(newlist)):
        y_data.append(float(newlist[i][2]))
# draw and show the plot
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.scatter(x_data, y_data, s = 10)
    ax.set_xlabel('Date')
    ax.set_ylabel('Mean temperature')
    plt.show()

# Main menu: loop
while True:
    print("ACME WEATHER DATA APP")
    print("1) Choose weather data file")
    print("2) See data for selected day")
    print("3) Calculate average statistics for the data")
    print("4) Print a scatterplot of the average temperatures")
    print("0) Quit program")
    choice = input("Choose what to do: ")
    if choice == "0":
        break
    elif choice == "1":
        menu_file()
    elif choice == "2":
        menu_date()
    elif choice == "3":
        menu_stats()
    elif choice == "4":
        menu_plot()
    else:
        print("Invalid selection!")
    print()
