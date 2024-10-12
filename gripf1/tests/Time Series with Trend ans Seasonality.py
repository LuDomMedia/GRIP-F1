import gripf1
import numpy as np

start_value = 1  # Startwert der Sinuswelle
trend_modifier = 0.25  # Trend in der Form trend = x * trend_modifier
seasonality_modifier = 1  # Saisonalität in der Form seasonality = sin(x) * seasonality_modifier

x = np.arange(0.0, 25.0, 0.1)  # Generiert Werte von 0 bis 25 in 0.1er-Schritten
y = np.sin(x) * seasonality_modifier + start_value + (x * trend_modifier)  # Sinuswelle mit Saisonalität und ansteigendem Trend

tsplot = gripf1.plotting.time_series_plot.TimeSeriesPlot('Zeit', 'Daten der Beispielfunktion',
                                                         'Beispiel Zeitreihe: Trend=0.25x, Saisonalität=sin(x)')

tsplot.create_plot_line(x, y, 'Beispieldaten', 'blue', marker='')
tsplot.ax.grid()
tsplot.plot()
