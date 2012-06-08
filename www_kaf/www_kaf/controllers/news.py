import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from www_kaf.lib.base import BaseController, render

log = logging.getLogger(__name__)

class NewsController(BaseController):
    
    def index(self):
	c.name = "News 1"
        return render('news/index.xhtml')
