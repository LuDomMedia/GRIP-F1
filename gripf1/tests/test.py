import gripf1


session = gripf1.core.create_session("Monaco", "Race")
ham = gripf1.core.Driver("HAM", session)
nor = gripf1.core.Driver("NOR", session)

'''
ver = gripf1.driver.Driver("VER", session)
lec = gripf1.driver.Driver("LEC", session)
alo = gripf1.driver.Driver("ALO", session)
gas = gripf1.driver.Driver("GAS", session)
rus = gripf1.driver.Driver("RUS", session)

'''


# Ham_SC = gripf1.analysis.speed_chart.SpeedChart(session, nor, 4, legend=True)
# Ham_SC.add_lap(ham, 4)
# Ham_SC.set_title("Speed Analysis", session)
# Ham_SC.plot()

Ham_LTC = gripf1.analysis.lap_time_chart.LapTimeChart(session, ham, legend=False, excluded_laps=[1])
# Ham_LTC.add_driver(nor)
# Ham_LTC.set_title("Lap Time Progression", session)
Ham_LTC.plot()
