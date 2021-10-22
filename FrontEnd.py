import cherrypy
import os
import os.path

from src.Connect4 import Connect4
from dominate.tags import *
from dominate.document import document

_instance = Connect4()


@cherrypy.expose
class c4API(object):
    def GET(self):
        return _instance.display()

    def PUT(self, x, y):
        _instance.place('cookie value', int(x), int(y))

    def POST(self):
        # Delete the current game
        # Create a new one
        pass


class Root(object):
    api = c4API()

    def __init__(self) -> None:
        super().__init__()
        index = document(title='CJank Connect4')
        index.head.add(link(href="/static/style.css", rel='stylesheet'))
        index.head.add(
            script(src="https://code.jquery.com/jquery-3.6.0.min.js"))
        index.head.add(script(src="/static/behavior.js"))

        index += h1("Janky connect 4", id="Title")
        index += div(id="Content")
        index += button("Refresh", onclick="refresh()")

        self.rendered = index.render()

    @cherrypy.expose
    def index(self):
        return self.rendered

    @cherrypy.expose
    def PUT(self, color):
        cherrypy.session['color'] = color


def error_page_default(status, message, traceback, version):
    return ''  # """<div style="text-align:center;" ><img src="/static/suspicious.jpeg"><div>"""


if __name__ == '__main__':
    folderRoot = os.path.abspath(os.getcwd())
    conf = {
        'global': {
            'server.socket_port': 25545,
            'server.socket_host': '192.168.32.5',
            'error_page.default': error_page_default,
            # 'log.access_file': './logs/normal.log',
        },
        '/': {
            'tools.staticdir.root': folderRoot,
            'tools.sessions.on': True
        },
        '/api': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(Root(), '/', conf)
