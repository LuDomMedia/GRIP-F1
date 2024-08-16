import fastf1.core

import gridf1.core
import gridf1.plotting.time_series_plot
from gridf1.plotting.time_series_plot import TimeSeriesPlot


class SeasonPointsPlot(TimeSeriesPlot):
    def __init__(self, season):
        x_label = ""
        y_label = ""
        title = ""
        super().__init__(x_label, y_label, title)
