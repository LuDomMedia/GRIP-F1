import fastf1.core
import pandas
import numpy as np
from matplotlib import pyplot as plt


class TimeSeriesPlot:
    """
    Parent class of all time series plots in the GridF1 package.

    ...

    Attributes
    ----------
    x_label
        Label for the x-axis
    y_label
        Label for the y-axis
    title
        First title line of the plot
    title_session
        Session object for automatic generation of the second title line (default: None)
    legend
        Boolean for legend visibility (default: False)

    Methods
    -------
    set_title(title: str, title_session: fastf1.core.Session = None, fontsize: int = 12, padding: int = 10):
        Sets the title of the plot
    set_axis_labels(x_label: str, y_label: str):
        Sets the labels of the x and y axes
    create_plot_line(x_data: tuple, y_data: tuple, label: str, color: str, exclude_data: list = None, marker: str = '.'):
        Creates a data line on the plot
    mark_x_axis(lap: int, color: str, label: str, alpha: float = 0.3, linewidth: int = 6):
        Marks a vertical line (area) on the plot
    plot():
        Displays the plot

    """

    def __init__(self, x_label: str, y_label: str, title: str,
                 title_session: fastf1.core.Session = None, legend: bool = False):  # Optional parameters
        self.legend = legend
        self.fig, self.ax = plt.subplots()
        self.set_title(title, title_session)
        self.set_axis_labels(x_label, y_label)

    def set_title(self, title: str,
                  title_session: fastf1.core.Session = None, fontsize: int = 12, padding: int = 10):  # Optional parameters
        """
        Sets the title of the plot
        :param title: First title line of the plot
        :param title_session: Session object for automatic generation of the second title line (default: None)
        :param fontsize: Font size of the title (default: 12)
        :param padding: Padding of the title (default: 10)
        :return:
        """

        if title_session is not None:
            title = f'{title_session.event.EventName} {title_session.event.year}: {title_session.name}\n{title}'
        else:
            title = title
        self.ax.set_title(title, fontsize=fontsize, pad=padding)

    def set_axis_labels(self, x_label: str, y_label: str):
        """
        Sets the labels of the x and y axes
        :param x_label: Label for the x-axis
        :param y_label: Label for the y-axis
        :return:
        """

        self.ax.set(xlabel=x_label, ylabel=y_label)

    def create_plot_line(self, x_data: tuple, y_data: tuple, label: str, color: str,
                         exclude_data: list = None, marker: str = '.'):  # Optional parameter
        """
        Creates a data line on the plot
        :param x_data: Datapoints for the x-axis
        :param y_data: Datapoints for the y-axis
        :param label: Data line label in the legend
        :param color: Data line color
        :param exclude_data: Datapoints to exclude from the plot (default: None)
        :param marker: Marker for individual datapoints (default: '.')
        :return:
        """

        if exclude_data is None:
            exclude_data = []

        data_dict = {"x_data": x_data, "y_data": y_data}
        data_df = pandas.DataFrame(data_dict)
        data_df.loc[data_df['x_data'].isin(exclude_data), 'y_data'] = np.nan

        self.ax.plot(data_df['x_data'], data_df['y_data'], label=label, color=color, marker=marker, zorder=1)

    def mark_x_axis(self, lap: int, color: str, label: str, alpha: float = 0.3, linewidth: int = 6):
        """
        Marks a vertical line (area) on the plot
        :param lap: Lap number of the area to mark
        :param color: Color of the highlighted area
        :param label: Label for the highlighted area in the legend
        :param alpha: Transparency of the highlighted area (default: 0.3)
        :param linewidth: Width (x-axis) of the highlighted area (default: 6)
        :return:
        """

        if label == "":
            self.ax.axvline(x=lap, color=color, alpha=alpha, linewidth=linewidth, zorder=2)
        else:
            self.ax.axvline(x=lap, color=color, alpha=alpha, linewidth=linewidth, label=label, zorder=2)

    def plot(self):
        """
        Displays the plot
        :return:
        """

        if self.legend:
            self.ax.legend()
        plt.show()
