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
        print(cherrypy.request.cookie['color'].value)
        _instance.place(cherrypy.request.cookie['color'].value, int(x), int(y))

    def POST(self):
        # Delete the current game
        # Create a new one
        pass


@cherrypy.expose
class registerAPI(object):
    def PUT(self, color):
        cherrypy.response.cookie['color'] = color
        # return ''


class Root(object):
    c4 = c4API()
    register = registerAPI()

    def __init__(self) -> None:
        super().__init__()
        index = document(title='Jank Connect4')
        index.head.add(link(href="/static/style.css", rel='stylesheet'))
        index.head.add(
            script(src="https://code.jquery.com/jquery-3.6.0.min.js"))
        index.head.add(script(src="/static/behavior.js"))

        index += h1("Jank connect 4", id="Title")
        index += div(button("Red", onclick="register('red')"),
                     span(" or "),
                     button("Black", onclick="register('black')"), id="Content")
        index += button("refresh", onclick="refresh()",
                        id="refresh", style='display: none;')

        self.rendered = index.render()

    @cherrypy.expose
    def index(self):
        return self.rendered


def error_page_default(status, message, traceback, version):
    return ''  # """<div style="text-align:center;" ><img src="/static/suspicious.jpeg"><div>"""


if __name__ == '__main__':
    folderRoot = os.path.abspath(os.getcwd())
    conf = {
        'global': {
            'server.socket_port': 8080,
            'server.socket_host': '192.168.32.5',
            'error_page.default': error_page_default,
            # 'log.access_file': './logs/normal.log',
        },
        '/': {
            'tools.staticdir.root': folderRoot
        },
        '/c4': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
        '/register': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(Root(), '/', conf)
