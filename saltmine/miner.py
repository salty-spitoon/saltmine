from yahoo_oauth import OAuth2
import os
import logging, warnings
import json

base_uri = 'https://fantasysports.yahooapis.com/fantasy/v2/'

logger = logging.getLogger(__name__)


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
    league_id : str
        The assigned identifier for the league, as assigned by the provider
    from_file : str
        Path to or name of a file containing OAuth token information

    """

    def __init__(self, league_id, from_file=None):    # future iterations may take OAuth key and secrets directly

        logger.info('Creating Miner...')

        if not league_id.isnumeric():
            warnings.warn('Invalid league ID')
        self.league_id = league_id

        if (from_file is None) or (not os.path.isfile(from_file)):
            raise IOError('Bad or no file name given')
        else:
            self.from_file = from_file
            self.token = OAuth2(None, None, from_file=self.from_file)

    def get(self, query):
        """GET method for Miner.

        Makes request to API using Miner's token and the passed query.

        Parameters
        ----------
        query : str
            The query to pass to provider

        """

        uri = base_uri+ query + '?format=json'
        response = self.token.session.get(uri)

        if response.status_code != 200:
            logger.info('Service returned status code %s', response.status_code)
            return None

        result = json.loads(str(response.content,'utf-8'))

        return result
