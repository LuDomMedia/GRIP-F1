from matplotlib import pyplot as plt


def create_time_series_plot(lap_times, x_label, y_label, title, virtual_safety_car_laps, safety_car_laps,
                            session_title=False, legend=False):
    fig, ax = plt.subplots()
    for driver, data in lap_times.items():
        ax.plot(data[0], data[1], label=driver, marker='.', color=data[2])
    ax.set(xlabel=x_label, ylabel=y_label)
    if session_title:
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
