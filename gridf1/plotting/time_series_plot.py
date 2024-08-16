import fastf1.core
import pandas
import numpy as np
from matplotlib import pyplot as plt


# DEPRECATED
'''
def create_time_series_plot(x_data, y_data, x_label, y_label, data_label, title, session_title=False, color="m",
                            legend=False):
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data, label=data_label, marker='.', color=color)
    ax.set(xlabel=x_label, ylabel=y_label)
    if session_title:
        title = f'{session_title.event.EventName} {session_title.event.year}: {session_title.name}\n{title}'
    ax.set_title(title, fontsize=12, pad=10)
    if legend:
        ax.legend()
    plt.show()
'''


# DEPRECATED
'''
def create_time_series_plot(lap_times: dict, x_label: str, y_label: str, title: str, virtual_safety_car_laps: list,
                            safety_car_laps: list, session_title: fastf1.core.Session = None, legend: bool = False) -> None:
    fig, ax = plt.subplots()
    for driver, data in lap_times.items():
        ax.plot(data[0], data[1], label=driver, marker='.', color=data[2])
    ax.set(xlabel=x_label, ylabel=y_label)
    if session_title is not None:
        title = f'{session_title.event.EventName} {session_title.event.year}: {session_title.name}\n{title}'
    ax.set_title(title, fontsize=12, pad=10)

    if virtual_safety_car_laps:
        ax.axvline(x=virtual_safety_car_laps[0], color='#ffa500', alpha=0.2, linewidth=6, label='Virtual Safety Car')  # Handle first lap separately with label
        for lap in virtual_safety_car_laps[1:]:  # Skip first lap as it is already plotted
            ax.axvline(x=lap, color='#ffa500', alpha=0.2, linewidth=6)

    if safety_car_laps:
        ax.axvline(x=safety_car_laps[0], color='#ff6a00', alpha=0.2, linewidth=6, label='Safety Car')  # Handle first lap separately with label
        for lap in safety_car_laps[1:]:  # Skip first lap as it is already plotted
            ax.axvline(x=lap, color='#ff6a00', alpha=0.2, linewidth=6)

    if legend:
        ax.legend()
    plt.show()
'''


# DEPRECATED
'''
def create_time_series_plot(data_series_collection: list, x_label: str, y_label: str, title: str, marked_laps: list,  #TODO: Title must be put together in other function before calling this
                            legend: bool = False) -> None:
    fig, ax = plt.subplots()


    #dict: data_series_collection = [data_series_1, data_series_2, ...]
    #dict: data_series = [x_data:, y_data:, label:, color:, marker:]


    for data_series in data_series_collection:
        ax.plot(data_series.get("x_data"), data_series.get("y_data"), label=data_series.get("label"),
                color=data_series.get("color"), marker=data_series.get("marker"))
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title, fontsize=12, pad=10)

    if marked_laps:
        # TODO: Handle marked laps (create ext. function)
        ax = handle_marked_laps(ax, marked_laps)

    if legend:
        ax.legend()
    plt.show()
'''


# DEPRECATED
'''
def handle_marked_laps(ax: plt.Axes, marked_laps: list) -> plt.Axes:
    
    # list: marked_laps = [{type: "Virtual Safety Car", color: "#ffa500", laps: [1, 2, 3]}, {type: "Safety Car", color: "#ff6a00", laps: [1, 2, 3]}]
    

    for lap_type in marked_laps:
        ax.axvline(x=lap_type.get("laps")[0], color=lap_type.get("color"), alpha=0.2, linewidth=6, label=lap_type.get("type"))
        for lap in lap_type[1:]:
            ax.axvline(x=lap, color=lap_type.get("color"), alpha=0.2, linewidth=6)
    return ax
'''


class TimeSeriesPlot:
    def __init__(self, x_label: str, y_label: str, title: str,
                 title_session: fastf1.core.Session = None, legend: bool = False):  # Optional parameters
        self.legend = legend
        self.fig, self.ax = plt.subplots()
        self.set_title(title, title_session)
        self.set_axis_labels(x_label, y_label)

    def set_title(self, title: str, title_session: fastf1.core.Session = None, fontsize: int = 12, padding: int = 10):
        if title_session is not None:
            title = f'{title_session.event.EventName} {title_session.event.year}: {title_session.name}\n{title}'
        else:
            title = title
        self.ax.set_title(title, fontsize=fontsize, pad=padding)

    def set_axis_labels(self, x_label: str, y_label: str):
        self.ax.set(xlabel=x_label, ylabel=y_label)

    def create_plot_line(self, x_data: tuple, y_data: tuple, label: str, color: str, exclude_data: list = None,
                         marker: str = '.'):
        if exclude_data is None:
            exclude_data = []

        data_dict = {"x_data": x_data, "y_data": y_data}
        data_df = pandas.DataFrame(data_dict)
        data_df.loc[data_df['x_data'].isin(exclude_data), 'y_data'] = np.nan

        self.ax.plot(data_df['x_data'], data_df['y_data'], label=label, color=color, marker=marker, zorder=1)

    def mark_x_axis(self, lap: int, color: str, label: str, alpha: float = 0.3, linewidth: int = 6):
        if label == "":
            self.ax.axvline(x=lap, color=color, alpha=alpha, linewidth=linewidth, zorder=2)
        else:
            self.ax.axvline(x=lap, color=color, alpha=alpha, linewidth=linewidth, label=label, zorder=2)

    def plot(self):
        if self.legend:
            self.ax.legend()
        plt.show()
