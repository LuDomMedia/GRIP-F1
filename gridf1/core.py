import datetime
import fastf1 as ff1
import fastf1.core
import fastf1.plotting


def create_session(race: str, session: str = 'Race', year: str = 'latest', cache_dir: str = 'cache') -> fastf1.core.Session:
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
    def __init__(self, abbr: str, session: fastf1.core.Session):
        self.abbr = abbr.upper()
        self.name = self.convert_name()
        self.color = self.get_color()
        self.laps = self.get_driver_laps(session)

    def convert_name(self) -> str:  # TODO: Maybe extract this method from class
        return ff1.plotting.DRIVER_TRANSLATE.get(self.abbr).title()

    def get_color(self) -> str:  # TODO: Maybe extract this method from class
        return ff1.plotting.driver_color(self.abbr)

    def get_driver_laps(self, session) -> fastf1.core.Laps:  # TODO: Maybe extract this method from class
        return session.laps.pick_driver(self.abbr)
