import cherrypy
import os
import os.path


@cherrypy.expose
class c4API(object):
    def GET(self):
        print("called")
        return "<h1>Test</h1>"  # <gameboard html> or a status code signifying no change

    def PUT(self, x, y):
        # Update game
        return "nothing"

    def POST(self):
        # Delete the current game
        # Create a new one
        return "nothing"


class Root(object):
    api = c4API()

    @cherrypy.expose
    def index(self):
        return open('index.html')


def error_page_default(status, message, traceback, version):
    return """<div style="text-align:center;" ><img src="/static/suspicious.jpeg"><div><div style="text-align:center;">Bad Kitty</div>"""


if __name__ == '__main__':
    folderRoot = os.path.abspath(os.getcwd())
    conf = {
        'global': {
            'server.socket_port': 25545,
            'server.socket_host': '192.168.32.5',
            'error_page.default': error_page_default,
            'log.access_file': './logs/normal.log',
        },
        '/': {
            'tools.staticdir.root': folderRoot
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
