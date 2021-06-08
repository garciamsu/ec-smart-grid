import pandas as pd

class Building: 
    def __init__(self, file, start_date, end_date):
        self.file = file
        self.start_date = start_date
        self.end_date = end_date
        self.loadData()                

    def loadData(self):
        #load data from file
        self.data = pd.read_csv(self.file)
        
        #convert data
        self.data['Global_active_power'] = pd.to_numeric(self.data['Global_active_power'], errors = 'coerce')
        self.data['Global_reactive_power'] = pd.to_numeric(self.data['Global_reactive_power'], errors = 'coerce')
        self.data['Voltage'] = pd.to_numeric(self.data['Voltage'], errors = 'coerce')
        self.data['Global_intensity'] = pd.to_numeric(self.data['Global_intensity'], errors = 'coerce')
        self.data['Sub_metering_1'] = pd.to_numeric(self.data['Sub_metering_1'], errors = 'coerce')
        self.data['Sub_metering_2'] = pd.to_numeric(self.data['Sub_metering_2'], errors = 'coerce')
        self.data['Sub_metering_3'] = pd.to_numeric(self.data['Sub_metering_3'], errors = 'coerce')
        self.data['Sub_metering_3'] = pd.to_numeric(self.data['Sub_metering_3'], errors = 'coerce')
        self.data['Date_Time'] = pd.to_datetime(self.data['Date']+ " " + self.data['Time'])
        #del(self.data['Date'])
        #del(self.data['Time'])
        after_start_date = self.data['Date_Time'] >= self.start_date
        before_end_date = self.data['Date_Time'] <= self.end_date
        between_two_dates = after_start_date & before_end_date
        self.filtered_dates = self.data.loc[between_two_dates]
               

    def showData(self):
        print(self.data)
        print(self.filtered_dates)

