import fastf1.core

import gridf1.core
import gridf1.plotting.time_series_plot
from gridf1.plotting.time_series_plot import TimeSeriesPlot


class SpeedChart(TimeSeriesPlot):
    def __init__(self, title_session: fastf1.core.Session, driver: gridf1.core.Driver, lap_number: int,
                 legend: bool = False):  # TODO: maybe add lap marking options
        x_label = "Time [s]"  # TODO: Change this to be more specific
        y_label = "Speed [km/h]"
        title = driver.name + " Speed Analysis | Lap " + str(lap_number)
        if lap_number == 0:
            title = driver.name + " Speed Analysis | Fastest Lap"
        super().__init__(x_label, y_label, title, title_session, legend)
        self.add_driver(driver, lap_number)

    def add_driver(self, driver: gridf1.core.Driver, lap_number: int = 0):  # Default behavior is to plot the fastest
        if lap_number == 0:
            lap = driver.laps.pick_fastest()
            self.create_plot_line(lap.get_telemetry()['Time'], lap.get_telemetry()['Speed'], driver.name, driver.color,
                                  marker=None)
        else:
            for index, lap in driver.laps.iterrows():
                if lap['LapNumber'] == lap_number:
                    self.create_plot_line(lap.get_telemetry()['Time'], lap.get_telemetry()['Speed'], driver.name, driver.color, marker=None)
                    break
