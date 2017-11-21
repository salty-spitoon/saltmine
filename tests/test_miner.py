import pytest
import warnings
from saltmine import miner

''''@pytest.fixture
def miner():
    from saltmine import miner
    return miner('2017', u'470610', from_file='oauth.json')
'''


def test_connect():

    with warnings.catch_warnings(record=True) as w: # Note: this will not output warnings to log file

        warnings.simplefilter('always')

        worker = miner.Miner(1999, u'470610', from_file='oauth.json')
        assert len(w) == 1
        assert 'Invalid year' in str(w[-1].message)

        worker = miner.Miner(2099, u'470610', from_file='oauth.json')
        assert len(w) == 2
        assert 'Invalid year' in str(w[-1].message)

        worker = miner.Miner(2017, u'123abc', from_file='oauth.json')
        assert len(w) == 3
        assert 'Invalid league ID' in str(w[-1].message)

#    This test case will be implemented when hooks into Yahoo are available.
#    with pytest.raises(ValueError):
#        worker = miner.Miner(2017, u'999999999', from_file='/Users/smythcc/Documents/dev/saltmine/oauth.json')

    with pytest.raises(IOError):
        worker = miner.Miner(2017, u'470610')

    with pytest.raises(IOError):
        worker = miner.Miner(2017, u'470610', from_file='file_doesnt_exist.json')

#    Handle bad authorizations?
#    with pytest.raises(miner.AuthenticationError):
#        worker = miner.Miner(2017, u'470610', from_file='badauth.json')

    worker = miner.Miner(2017, u'470610', from_file='oauth.json')
    assert worker
