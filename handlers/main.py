import tornado.ioloop
import tornado.web
from models.lists import List

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = List().all()
        self.render("index.html", title="Tornado To Do", items=items)
