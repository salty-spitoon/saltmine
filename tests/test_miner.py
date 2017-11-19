import pytest
from saltmine import miner

''''@pytest.fixture
def miner():
    from saltmine import miner
    return miner('2017', '470610', from_file='oauth.json')
'''


def test_connect():
    with pytest.raises(ValueError):
        worker = miner.Miner(None, '470610', from_file='oauth.json')

    with pytest.raises(ValueError):
        worker = miner.Miner(1999, '470610', from_file='oauth.json')

    with pytest.raises(ValueError):
        worker = miner.Miner(2099, '470610', from_file='oauth.json')

    with pytest.raises(ValueError):
        worker = miner.Miner(2017, None, from_file='oauth.json')

#    This test case will be implemented when hooks into Yahoo are available.
#    with pytest.raises(ValueError):
#        worker = miner.Miner(2017, '999999999', from_file='/Users/smythcc/Documents/dev/saltmine/oauth.json')

    with pytest.raises(IOError):
        worker = miner.Miner(2017, '470610')

    with pytest.raises(IOError):
        worker = miner.Miner(2017, '470610', from_file='file_doesnt_exist.json')

#    Handle bad authorizations?
#    with pytest.raises(miner.AuthenticationError):
#        worker = miner.Miner(2017, '470610', from_file='badauth.json')

    worker = miner.Miner(2017, '470610', from_file='oauth.json')
    assert worker
