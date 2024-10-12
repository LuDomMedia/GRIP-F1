import datetime
import fastf1 as ff1
import fastf1.core
import fastf1.plotting


def create_session(race: str, session: str = 'Race',
                   year: str = 'latest', cache_dir: str = 'cache') -> fastf1.core.Session:  # Optional parameters
    """
    Creates a fastf1 Session object and loads the data. When the year is 'latest', the current year is used.
    :param race: String to specify the Race Weekend
    :param session: String to specify the Session
    :param year: String to specify the year (default: 'latest')
    :param cache_dir: String to specify the cache directory
    :return: fastf1.core.Session
    """

    # Enable the cache and setup matplotlib
    ff1.Cache.enable_cache(cache_dir)
    ff1.plotting.setup_mpl()

    # Get the session
    if year == 'latest':
        year = datetime.datetime.now().year
    session = ff1.get_session(year, race, session)
    session.load()

    return session


class Driver:
    """
        A class used to represent a driver in the FastF1 data

        ...

        Attributes
        ----------
        abbr
            Three character abbreviation of the driver
        session
            Session object to get the data from
        name
            Full name of the driver. Retrieved from the convert_name function
        color
            Color of the driver. Retrieved from the get_color function
        laps
            Laps object of the driver and current session

        Methods
        -------
        convert_name()
            Converts the abbreviation to the full name
        get_color()
            Retrieves the color of the driver
        get_driver_laps()
            Retrieves the laps of the driver out of the current session

    """

    def __init__(self, abbr: str, session: fastf1.core.Session):
        self.abbr = abbr.upper()
        self.name = self.convert_name()
        self.color = self.get_color()
        self.laps = self.get_driver_laps(session)

    def convert_name(self) -> str:
        """
        Converts the abbreviation to the full name
        :return: str
        """
        return ff1.plotting.DRIVER_TRANSLATE.get(self.abbr).title()

    def get_color(self) -> str:
        """
        Retrieves the color of the driver
        :return: str
        """
        return ff1.plotting.driver_color(self.abbr)

    def get_driver_laps(self, session) -> fastf1.core.Laps:
        """
        Retrieves the laps of the driver out of the current session
        :param session: Session object to get the data from
        :return: fastf1.core.Laps
        """
        return session.laps.pick_driver(self.abbr)