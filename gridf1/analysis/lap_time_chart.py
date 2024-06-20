import fastf1.core

import gridf1.core
import gridf1.plotting.time_series_plot
from gridf1.plotting.time_series_plot import TimeSeriesPlot


# DEPRECATED
'''
def create_lap_time_chart(session: fastf1.core.Session, driver: gridf1.core.Driver, *additional_drivers: gridf1.core.Driver) -> None:
    lap_times = {driver.name: [driver.laps['LapNumber'], driver.laps['LapTime'],
                               driver.color]}  # Create dictionary with x-, y-data and driver color
    if additional_drivers:  # Check if additional drivers are provided
        title = "Lap Time Progression"
        for driver in additional_drivers:  # Add additional drivers to dictionary
            lap_times[driver.name] = [driver.laps['LapNumber'], driver.laps['LapTime'], driver.color]
    else:
        title = driver.name + " Lap Time Progression"

    virtual_safety_car_laps = []
    for index, lap in driver.laps.iterrows():
        if lap['TrackStatus'].find('6') != -1 or lap['TrackStatus'].find('7') != -1:
            virtual_safety_car_laps.append(lap['LapNumber'])

    safety_car_laps = []
    for index, lap in driver.laps.iterrows():
        if lap['TrackStatus'].find('4') != -1:
            safety_car_laps.append(lap['LapNumber'])

    gridf1.plotting.time_series_plot.create_time_series_plot(lap_times, "Lap Number", "Lap Time", title,
                                                             virtual_safety_car_laps, safety_car_laps,
                                                             session, True)
'''


class LapTimeChart(TimeSeriesPlot):
    def __init__(self, title_session: fastf1.core.Session, driver: gridf1.core.Driver,
                 legend: bool = False, mark_sc: bool = False, mark_vsc: bool = False, mark_yellow_flag: bool = False):
        x_label = "Lap Number"
        y_label = "Lap Time"
        title = driver.name + " Lap Time Progression"
        super().__init__(x_label, y_label, title, title_session, legend)
        self.mark_laps(driver, mark_sc, mark_vsc, mark_yellow_flag)
        self.add_driver(driver)

    def add_driver(self, driver: gridf1.core.Driver):
        self.create_plot_line(driver.laps['LapNumber'], driver.laps['LapTime'], driver.name, driver.color)

    def mark_laps(self, driver: gridf1.core.Driver, mark_sc: bool = False, mark_vsc: bool = False, mark_yellow_flag: bool = False):
        if mark_sc:
            sc_label_added = False
            for index, lap in driver.laps.iterrows():
                if '4' in str(lap['TrackStatus']):
                    if not sc_label_added:
                        self.mark_x_axis(lap['LapNumber'], "#FF6A00", "Safety Car")
                        sc_label_added = True
                    else:
                        self.mark_x_axis(lap['LapNumber'], "#FF6A00", "")
        if mark_vsc:
            vsc_label_added = False
            for index, lap in driver.laps.iterrows():
                if '6' in str(lap['TrackStatus']) or '7' in str(lap['TrackStatus']) or '56' in str(lap['TrackStatus']):
                    if not vsc_label_added:
                        self.mark_x_axis(lap['LapNumber'], "#A600A6", "Virtual Safety Car")
                        vsc_label_added = True
                    else:
                        self.mark_x_axis(lap['LapNumber'], "#A600A6", "")
        if mark_yellow_flag:
            for index, lap in driver.laps.iterrows():
                if '2' in str(lap['TrackStatus']):
                    yellow_flag_label_added = False
                    if not yellow_flag_label_added:
                        self.mark_x_axis(lap['LapNumber'], "#FFFF00", "Yellow Flag")
                        yellow_flag_label_added = True
                    else:
                        self.mark_x_axis(lap['LapNumber'], "#FFFF00", "")
