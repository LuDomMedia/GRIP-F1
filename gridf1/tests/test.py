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
gridf1.analysis.lap_time_chart.create_lap_time_chart(session, ham, nor)
