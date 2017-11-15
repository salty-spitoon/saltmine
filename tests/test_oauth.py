from yahoo_oauth import OAuth2

def get_token(consumer_key, consumer_secret, **kwargs):
    token = OAuth2(consumer_key, consumer_secret, **kwargs)
    return token

def test_token(capsys):
    with capsys.disabled(): # must do this to allow reading from stdin
        tmpToken = get_token(None, None, from_file='oauth.json')
    assert tmpToken.token_is_valid()