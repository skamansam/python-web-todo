import tornado.ioloop
import tornado.web


class ListsHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'lists': [
          {
            'title': 'List One',
            'id': 1,
            'color': '#ff0000'
          },{
              'title': 'List One',
              'id': 2,
              'color': '#ff0000'
          }
        ]}
        self.write(response)
