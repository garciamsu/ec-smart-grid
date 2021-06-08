from matplotlib import pyplot as plt
import pandas as pd

#https://stackoverflow.com/questions/59108805/fixing-import-module-could-not-be-resolved-in-pyright
from consumption_profile import Building
from irradiance import Irradiance

#Define route file
url_file = 'C:/Users/MASTER/Documents/Visual Studio Code/Python/ec-smart-grid/data/household_power_consumption.csv'
start_date = "2007-06-30 00:00:00"
end_date = "2007-06-30 23:59:00"

buildings = Building(url_file, start_date, end_date)
#print(buildings.filtered_dates)

irradiance = Irradiance('MST', 39.755, -105.221)

# Get irradiance data for summer and winter solstice, assuming 25 degree tilt
# and a south facing array
summer_irradiance = irradiance.get_irradiance('06-30-2007', 25, 180)
# Convert Dataframe Indexes to Hour:Minute format to make plotting easier
summer_irradiance['Date_Time'] = summer_irradiance.index.strftime("%Y-%m-%d %H:%M:%S")

#df = pd.DataFrame()
#df['Global_active_power'] = buildings.filtered_dates['Global_active_power']
#temp = summer_irradiance['POA'].to_frame(name="irradiance")

#df['irradiance_POA'] = temp['irradiance']
#print(temp['irradiance'])

#summer_irradiance_POA = pd.DataFrame(summer_irradiance['POA'], columns = ['Irradiance', 'Date_Time'])
#summer_irradiance.index.rename('Date_Time')
#print(df)
#print(summer_irradiance['POA'])
#print(summer_irradiance_POA)
#summer_irradiance['POA'].to_frame(name="irradiance")
#print(buildings.filtered_dates)

temp = summer_irradiance['POA'].to_frame(name="irradiance")
temp['Date_Time'] = pd.to_datetime(summer_irradiance.index.strftime("%Y-%m-%d %H:%M:%S"))
#print(temp)

process = pd.merge(buildings.filtered_dates, temp, left_on='Date_Time', right_on='Date_Time')
print(process[['Date_Time', 'irradiance', 'Global_active_power']])

process['power_pv_1'] = 1*1.92*process['irradiance']
process['power_pv_2'] = 2*1.92*process['irradiance']
process['power_pv_5'] = 5*1.92*process['irradiance']
process['Global_active_power'] = 1000*process['Global_active_power']


print(process[['Date_Time', 'irradiance', 'power_pv_1', 'power_pv_2', 'power_pv_5', 'Global_active_power']])

fig, (ax1) = plt.subplots(1, sharey=True)
process['power_pv_1'].plot(ax=ax1, label='power_pv_1')
process['power_pv_2'].plot(ax=ax1, label='power_pv_2')
process['power_pv_5'].plot(ax=ax1, label='power_pv_5')
process['Global_active_power'].plot(ax=ax1, label='Global_active_power')

ax1.set_xlabel('Time of day')
ax1.set_ylabel('Power')
ax1.legend()
plt.show()


#print(summer_irradiance)

# Plot GHI vs. POA for winter and summer
#fig, (ax1) = plt.subplots(1, sharey=True)
#summer_irradiance['GHI'].plot(ax=ax1, label='GHI')
#summer_irradiance['POA'].plot(ax=ax1, label='POA')

#ax1.set_xlabel('Time of day (Summer)')
#ax1.set_ylabel('Irradiance ($W/m^2$)')
#ax1.legend()

#plt.show()


#https://unipython.com/analisis-de-series-temporales-con-la-libreria-pandas/
#plt.plot(buildings.filtered_dates['Date_Time'], buildings.filtered_dates['Global_active_power'])
#plt.xlabel('Timestamp')
#plt.ylabel('Global active power')
#plt.grid(True)
#plt.show()