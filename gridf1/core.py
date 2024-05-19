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

