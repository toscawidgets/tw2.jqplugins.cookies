
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery core imports
from tw2.jquery.base import jQueryJSLink, jQueryPluginLinkMixin
from tw2.jquery.version import JSLinkMixin

# import from *this* package
from tw2.jqplugins.cookies import defaults

### Links, etc...
class jQueryCookiesMixin(jQueryPluginLinkMixin):
    dirname = defaults._cookies_dirname_
    basename='jquery.cookies'
    modname = 'tw2.jqplugins.cookies'

class jQueryCookiesJSLink(twc.JSLink, jQueryCookiesMixin):
    subdir = 'js'

### Resources
jquery_cookies_js = jQueryCookiesJSLink()
