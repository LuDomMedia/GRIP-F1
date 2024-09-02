import fastf1.core

import gridf1.plotting.time_series_plot
from gridf1.plotting.time_series_plot import TimeSeriesPlot


class SpeedChart(TimeSeriesPlot):
    """
        A class used to create a chart of the speed of a driver in a specific lap
        Inherits from TimeSeriesPlot.

        ...

        Attributes
        ----------
        title_session
            Session object for automatic generation of the second title line (default: None)
        driver
            Driver object to get the data from
        lap_number
            Number of the lap to plot (default: 0)
        legend
            Boolean for legend visibility (default: False)

        Methods
        -------
        add_lap(driver: gridf1.core.Driver, lap_number: int = 0):
            Adds a lap to the chart. If lap_number is 0, the fastest lap is plotted

    """

    def __init__(self, title_session: fastf1.core.Session, driver: gridf1.core.Driver, lap_number: int = 0,
                 legend: bool = False):  # Optional parameters
        x_label = "Time [s]"  # TODO: Change this to be more specific
        y_label = "Speed [km/h]"
        title = driver.name + " Speed Analysis | Lap " + str(lap_number)
        if lap_number == 0:
            title = driver.name + " Speed Analysis | Fastest Lap"
        super().__init__(x_label, y_label, title, title_session, legend)
        self.add_lap(driver, lap_number)

    def add_lap(self, driver: gridf1.core.Driver, lap_number: int = 0):
        """
        Adds a lap to the chart. If lap_number is 0, the fastest lap is plotted (default: 0)
        :param driver: Driver object to get the data from
        :param lap_number: Number of the lap to plot (default: 0)
        :return:
        """

        if lap_number == 0:
            lap = driver.laps.pick_fastest()
            self.create_plot_line(lap.get_telemetry()['Time'], lap.get_telemetry()['Speed'], driver.name, driver.color)
        else:
            for index, lap in driver.laps.iterrows():
                if lap['LapNumber'] == lap_number:
                    self.create_plot_line(lap.get_telemetry()['Time'], lap.get_telemetry()['Speed'], driver.name, driver.color)
                    break
