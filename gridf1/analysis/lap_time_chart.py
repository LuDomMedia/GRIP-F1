import fastf1.core

import gridf1.plotting.time_series_plot


def create_lap_time_chart(session: fastf1.core.Session, driver: gridf1.core.Driver,
                          *additional_drivers: gridf1.core.Driver) -> None:
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
