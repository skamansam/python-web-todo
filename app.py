import tornado.ioloop
import tornado.options
import uuid
import tornado.web
import os.path

from handlers.main import MainHandler  
from handlers.lists import ListsHandler

from models.ormodel import ORModel

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("database_url", default="", help="the db connection string", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/lists*.json", ListsHandler),
         ]
        settings = dict(
            cookie_secret="51ea7622d2c144799c4fbfcbd311fa7a1404fbc134dd400e9a9910d89fbad08471af493139b9427bab9bc481020e62003399b79475804beabb95ca772d2d258d",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        super(Application, self).__init__(handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    ORModel.init_db()
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
