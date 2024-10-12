import fastf1.core

import gripf1.core
from gripf1.plotting.time_series_plot import TimeSeriesPlot


class LapTimeChart(TimeSeriesPlot):
    """
        A class used to create a chart of the lap time progression of one or more drivers
        Inherits from TimeSeriesPlot.

        ...

        Attributes
        ----------
        title_session
            Session object for automatic generation of the second title line (default: None)
        driver
            Driver object to get the data from
        excluded_laps
            List of laps to exclude from the chart (default: None)
        legend
            Boolean for legend visibility (default: False)
        mark_sc
            Boolean to enable highlighting of Safety Car periods (default: False)
        mark_vsc
            Boolean to enable highlighting of Virtual Safety Car periods (default: False)
        mark_yellow_flag
            Boolean to enable highlighting of Yellow Flag periods (default: False)

        Methods
        -------
        add_driver(driver: gripf1.core.Driver, excluded_laps: list = None):
            Adds a data line for the specified driver to the chart
        mark_laps(driver: gripf1.core.Driver, mark_sc: bool = False, mark_vsc: bool = False, mark_yellow_flag: bool = False):
            Marks Safety Car, Virtual Safety Car and Yellow Flag periods on the chart
    """

    def __init__(self, title_session: fastf1.core.Session, driver: gripf1.core.Driver,
                 excluded_laps: list = None, legend: bool = False, mark_sc: bool = False,  # Optional parameters
                 mark_vsc: bool = False, mark_yellow_flag: bool = False):  # Optional parameters
        x_label = "Lap Number"
        y_label = "Lap Time [min:sec.ms]"
        title = driver.name + " Lap Time Progression"
        super().__init__(x_label, y_label, title, title_session, legend)
        self.mark_laps(driver, mark_sc, mark_vsc, mark_yellow_flag)
        self.add_driver(driver, excluded_laps)

    def add_driver(self, driver: gripf1.core.Driver,
                   excluded_laps: list = None):  # Optional parameters
        """
        Adds a data line for the specified driver to the chart
        :param driver: Driver object to get the data from
        :param excluded_laps: List of laps to exclude from the chart (default: None)
        :return:
        """

        if excluded_laps is None:  # TODO: Move this funktion to the core module and rename it to exclude_datapoints
            excluded_laps = []

        self.create_plot_line(driver.laps['LapNumber'], driver.laps['LapTime'], driver.name, driver.color, excluded_laps)

    def mark_laps(self, driver: gripf1.core.Driver,
                  mark_sc: bool = False, mark_vsc: bool = False, mark_yellow_flag: bool = False):  # Optional parameters
        """
        Marks Safety Car, Virtual Safety Car and Yellow Flag periods on the chart
        :param driver: Driver object to get the data from
        :param mark_sc: Boolean to enable highlighting of Safety Car periods (default: False)
        :param mark_vsc: Boolean to enable highlighting of Virtual Safety Car periods (default: False)
        :param mark_yellow_flag: Boolean to enable highlighting of Yellow Flag periods (default: False)
        :return:
        """
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

                        # Is set to True after the first yellow flag is marked. This is to avoid multiple labels
                        yellow_flag_label_added = True
                    else:
                        self.mark_x_axis(lap['LapNumber'], "#FFFF00", "")
