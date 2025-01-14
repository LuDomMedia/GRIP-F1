import fastf1.core
import pandas
import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator


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
    set_limit(axis: str, lower_limit: float | pandas.Timedelta = None, upper_limit: float | pandas.Timedelta = None):
        Sets the limits of a single axis
    set_limits(lower_limit_x: float | pandas.Timedelta = None, upper_limit_x: float | pandas.Timedelta = None, lower_limit_y: float | pandas.Timedelta = None, upper_limit_y: float | pandas.Timedelta = None):
        Sets the limits of the x and y axes
    plot():
        Displays the plot
    save_to_file(file_name: str, directory: str = 'output', file_type: str = 'png', transparency: bool = False, dpi: float = 100):
        Saves the plot to a file

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

    def add_grid_lines(self,
                       minor_x_ticks: float = 0, minor_y_ticks: float = 0):  # Optional parameters
        """
        Adds grid lines to the plot
        :return:
        """

        # Set x-axis ticks  every 2 laps
        if minor_x_ticks > 0:
            self.ax.xaxis.set_minor_locator(MultipleLocator(minor_x_ticks))

        # Set y-axis ticks every 0.5 seconds
        if minor_y_ticks > 0:
            self.ax.yaxis.set_minor_locator(MultipleLocator(minor_y_ticks))

        # Display grid lines
        plt.grid(which='minor', alpha=0.2)
        plt.grid(which='major', alpha=0.5)

    def set_limit(self, axis: str,
                  lower_limit: float | pandas.Timedelta = None, upper_limit: float | pandas.Timedelta = None): # Optional parameters
        """
        Sets the limits of a single axis
        :param axis: Axis to set the limits for
        :param lower_limit: Lower limit of the axis (default: None)
        :param upper_limit: Upper limit of the axis (default: None)
        :return:
        """

        if axis == 'x':
            self.ax.set_xlim([lower_limit, upper_limit])
        elif axis == 'y':
            self.ax.set_ylim([lower_limit, upper_limit])
        else:
            raise ValueError("Invalid axis. Use 'x' or 'y'.")

    def set_limits(self, lower_limit_x: float | pandas.Timedelta = None, upper_limit_x: float | pandas.Timedelta = None, # Optional parameters
                   lower_limit_y: float | pandas.Timedelta = None, upper_limit_y: float | pandas.Timedelta = None): # Optional parameters
        """
        Sets the limits of the x and y axes
        :param lower_limit_x: Lower limit of the x-axis (default: None)
        :param upper_limit_x: Upper limit of the x-axis (default: None)
        :param lower_limit_y: Lower limit of the y-axis (default: None)
        :param upper_limit_y: Upper limit of the y-axis (default: None)
        :return:
        """

        self.set_limit('x', lower_limit_x, upper_limit_x)
        self.set_limit('y', lower_limit_y, upper_limit_y)

    def plot(self):
        """
        Displays the plot
        :return:
        """

        if self.legend:
            self.ax.legend()

        plt.show()

    def save_to_file(self, file_name: str,
                     directory: str = 'output', file_type: str = 'png', transparency: bool = False, dpi: float = 100):  # Optional parameters
        """
        Saves the plot to a file
        :param file_name: Name of the file
        :param directory: Directory to save the file (default: 'output')
        :param file_type: File type of the file (default: 'png')
        :param transparency: Transparency of the file (default: False)
        :param dpi: Resolution of the file in Dots per Inch (default: 100)
        :return:
        """
        file_path = f'{directory}/{file_name}.{file_type}'

        if not os.path.exists(directory):
            os.mkdir(directory)
            print(f'Created new output folder: {directory}')

        if self.legend:
            self.ax.legend()

        plt.savefig(file_path, transparent=transparency, dpi=dpi)
