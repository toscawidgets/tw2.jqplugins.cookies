import tw2.core as twc

def request_local_tst():
    global _request_local, _request_id
#    if _request_id is None:
#        raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()


def test_jquery_resource():
    from tw2.jqplugins.cookies import jquery_cookies_js
    the_link = '/resources/tw2.jqplugins.cookies/static/jquery/cookies/js/jquery.cookies.js'
    assert(jquery_cookies_js.req().link == the_link)
