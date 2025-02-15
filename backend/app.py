import flask, sqlite3
from db_helper import DB_Helper
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)

conn = sqlite3.connect(r'/Users/ankanmahapatra/Desktop/genAI/BookWormAI/books.db', check_same_thread=False)
db_helper = DB_Helper()



@app.route('/')
def index():
    return 'Hello, World!'



@app.route('/books', methods=['GET'])
def get_books():
    books = db_helper.get_books(conn)
    return flask.jsonify(books)


@app.route('/books/search', methods=['POST'])
def search_books():
    data = flask.request.json
    books = db_helper.search_books(conn, data['search'])
    return flask.jsonify(books)



if __name__ == '__main__':
    app.run(debug=True)