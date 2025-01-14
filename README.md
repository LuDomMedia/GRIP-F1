# **GRIP-F1** 
[![Maintained yes Badge](https://img.shields.io/badge/Maintained%3F-yes-green?style=for-the-badge)](#)
[![Repository License Badge](https://img.shields.io/github/license/LuDomMedia/GRIP-F1?style=for-the-badge)](#)
[![Repository Release Badge](https://img.shields.io/github/release/LuDomMedia/GRIP-F1?style=for-the-badge)](https://github.com/LuDomMedia/GRIP-F1/releases/latest)
[![Python Badge](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![pypi Badge](https://img.shields.io/badge/pypi-coming_soon-purple?style=for-the-badge)](#)
<hr />
The Graphical Racing Insights Package - Formula 1 (GRIP-F1 for short) is a python package for analyzing and visualizing Formula 1 timing & telemetry data and results.

GRIP-F1 relies heavily on other packages and projects to achieve its functionality. A complete list can be found under [Dependencies](#dependencies).

> [!WARNING]
> GRIP-F1 was created as part of a final project and is only being developed and tested occasionally at present. I am working on making GRIP-F1 as stable and accurate as possible, but I cannot guarantee anything.

## **Features**
- Simplified integration of **[FastF1](https://github.com/theOehrly/Fast-F1)**:  the package can be initialized with just one line of code
- **Driver** class containing all important attributes and methods related to drivers
- **TimeSeriesPlot** class enabling the simple creation of time series diagrams. This class can be used directly, but also serves as foundation for all ready-to-use time series diagrams below
  - **LapTimeChart** class for plotting lap times of specified drivers over the course of a race (or any other session)
  - **SpeedChart** class for plotting the speed of specified drivers during a single lap

## **Installation**
For now the only way to use GRIP-F1 is to `download or clone this repository` and work directly in the source code. But a simpler installation method is currently being worked on.

You will need additional packages to use GRIP-F1. These can be downloaded from pip with the following command (only FastF1 needs to be installed as all other packages are installed with it automatically):
```commandline
pip install fastf1
```

There are some examples of how GRIP-F1 can be used in the `tests` folder. Detailed instructions will follow in the future.

> [!IMPORTANT]
> - It is highly recommended that you work within this `tests/private` folder if you've cloned the repository as this folder is excluded from GitHub and therefore nothing will be overwritten by future updates.
> - It is important to open the folder containing all files from GRIP-F1 as a project in your IDE to avoid problems with importing and referencing GRIP-F1.
> - Due to limitations of the APIs, some analyses can only be performed from 2018 onwards.

## **Dependencies**
GRIP-F1 depends on a variety of different cool open souurce projects and uses the following packages to function correctly:
- **[FastF1](https://github.com/theOehrly/Fast-F1)** (Access to F1 data)
- **[matplotlib](https://github.com/matplotlib/matplotlib)** (Data visualisation)
- **[pandas](https://github.com/pandas-dev/pandas)** (Structurizing data)
- **[NumPy](https://github.com/numpy/numpy)** (Calculations)
- **[Ergast](https://ergast.com/mrd)** (Archive for historical F1 data)

## **Notice**
GRIP-F1 and all of its related components are unofficial and in no way affiliated with Formula 1.
F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V.
