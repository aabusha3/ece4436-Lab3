import csv #read & parse csv files
import matplotlib.pyplot as plt #calc & plots the needed graphs

#plot h1 window size vs time TCP connection with 10% loss
h1_x = [] #the time frame of h1
h1_y = [] #the window size at that time frame of h1

with open('lab3-q7-h1.csv') as csv_file: #read as csv
    csv_reader = csv.reader(csv_file, delimiter=',') #get rid of commas
    for row in csv_reader: #iterate through each row       
        if row[6].find('Win=') < 0: #skip of the columns row and all invalid data
            continue
        h1_x.append(float(row[1])) #add valid time frame
        h1_y.append(int(row[6][row[6].find('Win=')+4:row[6].find('Len=')-1])) #add valid window size at that time

plt.plot(h1_x, h1_y)  #plot x and y data sets
plt.xlabel('Time')  #set x axes names
plt.ylabel('Window Size') #set y axes names
plt.title('Window Size vs Time With 10% loss') #add a meaningful title
plt.show()  #display the plot


#plot h3 window size vs time TCP connection with 1% loss
h3_x = [] #the time frame of h3
h3_y = [] #the window size at that time frame of h3

with open('lab3-q7-h3.csv') as csv_file: #read as csv
    csv_reader = csv.reader(csv_file, delimiter=',') #get rid of commas
    for row in csv_reader: #iterate through each row       
        if row[6].find('Win=') < 0: #skip of the columns row and all invalid data
            continue
        h3_x.append(float(row[1])) #add valid time frame
        h3_y.append(int(row[6][row[6].find('Win=')+4:row[6].find('Len=')-1])) #add valid window size at that time


plt.plot(h3_x, h3_y)  #plot x and y data sets
plt.xlabel('Time')  #set x axes names
plt.ylabel('Window Size') #set y axes names
plt.title('Window Size vs Time With 1% loss') #add a meaningful title
plt.show()  #display the plot