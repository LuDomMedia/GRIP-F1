import gridf1
import pandas as pd


session = gridf1.core.create_session("Miami", "Race")
ham = gridf1.core.Driver("HAM", session)
nor = gridf1.core.Driver("NOR", session)

'''
ver = gridf1.driver.Driver("VER", session)
lec = gridf1.driver.Driver("LEC", session)
alo = gridf1.driver.Driver("ALO", session)
gas = gridf1.driver.Driver("GAS", session)
rus = gridf1.driver.Driver("RUS", session)

'''


#Ham_SC = gridf1.analysis.speed_chart.SpeedChart(session, ham, 0, legend=True)
#Ham_SC.add_lap(nor, 1)
#Ham_SC.set_title("Speed Analysis", session)
#Ham_SC.plot()

Ham_LTC = gridf1.analysis.lap_time_chart.LapTimeChart(session, ham, legend=True, mark_sc=True, mark_vsc=True, mark_yellow_flag=True)
Ham_LTC.add_driver(nor)
Ham_LTC.set_title("Lap Time Progression", session)
Ham_LTC.plot()
