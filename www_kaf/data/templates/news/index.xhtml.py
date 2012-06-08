# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1339169190.6177
_enable_loop = True
_template_filename = '/home/finder/cursework/www_kaf/www_kaf/templates/news/index.xhtml'
_template_uri = 'news/index.xhtml'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html>\n\t<head>\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\t<title>\u0421\u0430\u0439\u0442 \u043a\u0430\u0444\u0435\u0434\u0440\u044b \u041c\u0423\u0421</title>\n\t<link rel="stylesheet" href="style.css" type="text/css" />\n\t<link rel="shortcut icon" href="http://s017.radikal.ru/i418/1205/76/a870db0b4f73.jpg" type="image/jpg">\n\t</head>\n\t<body style="background-color: #F8F8E6">\n\t\t<!--header-->\n\t\t<div id="header"p><img src="images/urfu.jpg" alt="Header" width="100%"></div>\n\t\t<!--title content-->\n\t\t<div id = "content_top">\n\t\t\t<ul id="content_top">\n\t\t\t\t<li><a href="index.html">\u041d\u043e\u0432\u043e\u0441\u0442\u0438</a></li>\n\t\t\t\t<li><a href="aboutk.html">\u041e \u043a\u0430\u0444\u0435\u0434\u0440\u0435</a></li>\n\t\t\t\t<li><a href="schedule.html">\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435</a></li>\n\t\t\t\t<li><a href="forum.html">\u0424\u043e\u0440\u0443\u043c</a></li>\n\t\t\t\t<li><a href="abouts.html">\u041e \u0441\u0430\u0439\u0442\u0435</a></li>\n\t\t\t\t<li><a href="map.html">\u041a\u0430\u0440\u0442\u0430 \u0441\u0430\u0439\u0442\u0430</a></li>\n\t\t\t\t<li><a href="search.html">\u041f\u043e\u0438\u0441\u043a</a></li>\n\t\t\t</ul>\n\t\t</div>\n\t\t<!--body content-->\n\t\t<div id="content_body">\n\t\t<h2>\u041d\u043e\u0432\u043e\u0441\u0442\u0438</h2>\n\t\t<hr></hr>\n\t\t<h3>\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439</h3>\n\t\t<ul>\n\t\t    <li>')
        # SOURCE LINE 31
        __M_writer(escape(c.name))
        __M_writer(u'</li>\n\t\t</ul>\n\t\t</div>\n\t\t<!--footer-->\n\t\t<div id="footer">\n\t\t<hr></hr>\n\t\t<a href="mailto:vasiliy.sushko@mail.ru?subject=\u0412\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0441\u0430\u0439\u0442\u0443 \u043a\u0430\u0444\u0435\u0434\u0440\u044b" target="_blank">Sushko Vasiliy [USU]</a>\n\t\t</div>\n\t\t\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


