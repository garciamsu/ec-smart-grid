#https://www.timeanddate.com/time/map/
#https://www.coordenadas-gps.com/

from pvlib import location
from pvlib import irradiance
import pandas as pd
from matplotlib import pyplot as plt

class Irradiance:

    def __init__(self, tz, lat, lon):
        # For this example, we will be using Golden, Colorado
        self.tz = tz
        self.lat = lat
        self.lon = lon

        # Create location object to store lat, lon, timezone
        self.site = location.Location(lat, lon, tz=tz)


    # Calculate clear-sky GHI and transpose to plane of array
    # Define a function so that we can re-use the sequence of operations with
    # different locations
    def get_irradiance(self, date, tilt, surface_azimuth):
        # Creates one day's worth of x min intervals
        times = pd.date_range(date, freq='1min', periods=60*24,
                            tz=self.site.tz)

                           
        # Generate clearsky data using the Ineichen model, which is the default
        # The get_clearsky method returns a dataframe with values for GHI, DNI,
        # and DHI
        clearsky = self.site.get_clearsky(times)
        # Get solar azimuth and zenith to pass to the transposition function
        solar_position = self.site.get_solarposition(times=times)
        # Use the get_total_irradiance function to transpose the GHI to POA
        POA_irradiance = irradiance.get_total_irradiance(
            surface_tilt=tilt,
            surface_azimuth=surface_azimuth,
            dni=clearsky['dni'],
            ghi=clearsky['ghi'],
            dhi=clearsky['dhi'],
            solar_zenith=solar_position['apparent_zenith'],
            solar_azimuth=solar_position['azimuth'])
        # Return DataFrame with only GHI and POA
        return pd.DataFrame({'GHI': clearsky['ghi'],
                            'POA': POA_irradiance['poa_global']})







