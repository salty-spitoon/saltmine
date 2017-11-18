import pytest
from saltmine import miner

''''@pytest.fixture
def miner():
    from saltmine import miner
    return miner('2017', '470610', from_file='oauth.json')
'''

def test_connect():
    with pytest.raises(ValueError):
        worker = miner('2099', '470610', from_file='oauth.json')

    with pytest.raises(ValueError):
        worker = miner('2017', '999999999', from_file='oauth.json')

    with pytest.raises(IOError):
        worker = miner('2017', '470610', from_file='badfile.json')

    worker = miner('2017', '470610', from_file='oauth.json')
    assert worker