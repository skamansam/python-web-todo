import os
import psycopg2

class ORModel(object):
    db_connection = None
    db_cursor = None
    table_name = None
    row_id = None

    @classmethod
    def init_db(cls):
      file = open('setup.sql', 'r')
      db_create_string = file.read()
      print("Connecting to DB using the string: \n{}".format(
          os.environ["DATABASE"]))
      conn = psycopg2.connect(os.environ["DATABASE"])
      cursor = conn.cursor()
      cursor.execute(db_create_string)
      cursor.close()
      conn.close()

    def __init__(self):
      try:
        self.db_connection = psycopg2.connect(os.environ["DATABASE"])
        self.db_cursor = self.db_connection.cursor()
        self.table_name = self.__class__.__name__.lower() + 's'
        # conn = psycopg2.connect("dbname='python-todo' user='pythontodo' host='localhost' password='dbpass'")
      except:
        print("I am unable to connect to the database")

    def _close(self):
      self.db_cursor.close()
      self.db_connection.close()

    def all(self):
      items = self.db_cursor.execute("select * from {}".format(self.table_name))
      self._close()
      return items

    def find_by_id(self, id):
      self.row_id = id
      item = self.db_cursor.execute("select * from {} where id = {}".format(self.table_name, id))[0]
      self._close()
      return item
