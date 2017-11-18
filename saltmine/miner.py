from yahoo_oauth import OAuth2
import os

ids = [57, 49, 79, 101, 124, 153, 175, 199, 222, 242, 257, 273, 999, 331, 348, 359, 371]


class AuthenticationError(Exception):
    """Custom exception for handling authentication errors.

    Parameters
    ----------
    message : str
        Text to be thrown with exception.

    """
    def __init__(self, message):
        super().__init__(message)


class Miner(object):
    """Primary worker class for saltmine.

    Fetches a valid OAuth token and handles requests to APIs.

    Parameters
    ----------
    year : int
        The calendar year to request data from
    league_id : str
        The assigned identifier for the league, as assigned by the provider
    from_file : str
        Path to or name of a file containing OAuth token information

    """

    def __init__(self, year, league_id, from_file=None):    # future iterations may take OAuth key and secrets directly

        if (year < 2001) or (year > 2017):
            raise ValueError('Year not valid')
        self.year = ids[year - 2001]

        if (league_id is None) or (not league_id.isnumeric()):
            raise ValueError('League ID not valid')
        self.league_id = league_id

        if (from_file is None) or (not os.path.isfile(from_file)):
            raise IOError('Bad or no file name given')
        else:
            self.from_file = from_file
            self.token = OAuth2(None, None, from_file=self.from_file)
