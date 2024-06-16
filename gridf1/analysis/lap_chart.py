import fastf1.core
from matplotlib import pyplot as plt

def create_lap_chart(session: fastf1.core.Session, lap: fastf1.core.Lap, *additional_laps: fastf1.core.Lap) -> None:

