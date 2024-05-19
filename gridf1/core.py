import datetime
import fastf1 as ff1
import fastf1.plotting


def create_session(race, session='Race', year='latest', cache_dir='cache'):
    # Enable the cache
    ff1.Cache.enable_cache(cache_dir)
    # Enable plotting settings
    ff1.plotting.setup_mpl()
    # Get the session
    if year == 'latest':
        year = datetime.datetime.now().year
    session = ff1.get_session(year, race, session)
    session.load()
    return session


class Driver:
    def __init__(self, abbr, session):
        self.abbr = abbr
        self.name = self.convert_name()
        self.color = self.get_color()
        self.laps = self.get_driver_laps(session)

    def convert_name(self):  # TODO: Maybe extract this method from class
        return ff1.plotting.DRIVER_TRANSLATE.get(self.abbr).title()

    def get_color(self):  # TODO: Maybe extract this method from class
        return ff1.plotting.driver_color(self.abbr)

    def get_driver_laps(self, session):  # TODO: Maybe extract this method from class
        return session.laps.pick_driver(self.abbr)
