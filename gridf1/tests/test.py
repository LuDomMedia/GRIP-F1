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
#gridf1.analysis.lap_time_chart.create_lap_time_chart(session, ham, nor)
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
'''
for index, lap in ham.laps.iterrows():
    print(lap.get_telemetry().head(3))
    break
'''

#print(ham.laps.pick_fastest().get_telemetry().head(3))

Ham_SC = gridf1.analysis.speed_chart.SpeedChart(session, ham, 0, legend=True)
#Ham_SC.add_driver(nor, 1)
#Ham_SC.set_title("Speed Analysis", session)
Ham_SC.plot()

#Ham_LTC = gridf1.analysis.lap_time_chart.LapTimeChart(session, ham, legend=True, mark_sc=True, mark_vsc=True, mark_yellow_flag=True)
#Ham_LTC.add_driver(nor)
#Ham_LTC.set_title("Lap Time Progression", session)
#Ham_LTC.plot()