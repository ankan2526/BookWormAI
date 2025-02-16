import flask, sqlite3
from flask_cors import CORS
from db_helper import DB_Helper
from llm_helper import LLM_Helper
from constants import DB_PATH, MODEL


app = flask.Flask(__name__)
CORS(app)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
db_helper = DB_Helper()
llm_helper = LLM_Helper(MODEL)



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


@app.route('/llm/invoke', methods=['POST'])
def invoke_llm():
    data = flask.request.json
    result = llm_helper.invoke(data['query'])
    return flask.jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)