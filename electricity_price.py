import pandas as pd

class price: 
    def __init__(self, file, start_date, end_date):
        self.file = file
        self.start_date = start_date
        self.end_date = end_date
        self.loadData()                

    def loadData(self):
        #load data from file
        self.data = pd.read_csv(self.file)
        
        #convert data
        self.data['weight_avg'] = pd.to_numeric(self.data['weight_avg'], errors = 'coerce')
        self.data['Date_Time'] = pd.to_datetime(self.data['Date_Time'])
        after_start_date = self.data['Date_Time'] >= self.start_date
        before_end_date = self.data['Date_Time'] <= self.end_date
        between_two_dates = after_start_date & before_end_date
        self.filtered_dates = self.data.loc[between_two_dates]
               

    def showData(self):
        print(self.data)
        print(self.filtered_dates)


url_file = 'C:/Users/MASTER/Documents/Visual Studio Code/Python/ec-smart-grid/data/electricity_price_Germany.csv'
start_date = "00:00:00"
end_date = "23:59:00"

cost = price(url_file, start_date, end_date)
print(cost.showData())