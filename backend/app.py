import flask, sqlite3
from flask_cors import CORS
import db_helper
import llm_helper
from constants import DB_PATH, MODEL
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    filename='logfile.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

app = flask.Flask(__name__)
CORS(app)

try:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    logger.info(f"Successfully connected to database at {DB_PATH}")
except Exception as e:
    logger.error(f"Failed to connect to database: {str(e)}")
    raise


@app.route('/')
def index():
    logger.info("Accessed root endpoint")
    return 'Hello, World!'


@app.route('/books', methods=['GET'])
def get_books():
    logger.info("Fetching all books")
    try:
        books = db_helper.get_books(conn)
        logger.info(f"Successfully retrieved {len(books)} books")
        return flask.jsonify(books)
    except Exception as e:
        logger.error(f"Error fetching books: {str(e)}")
        return flask.jsonify({"error": "Failed to fetch books"}), 500


@app.route('/books/search', methods=['POST'])
def search_books():
    data = flask.request.json
    search_term = data.get('search', '')
    logger.info(f"Searching books with term: {search_term}")
    
    try:
        books = db_helper.search_books(conn, search_term)
        logger.info(f"Search returned {len(books)} results")
        return flask.jsonify(books)
    except Exception as e:
        logger.error(f"Error searching books: {str(e)}")
        return flask.jsonify({"error": "Failed to search books"}), 500


@app.route('/llm/invoke', methods=['POST'])
def invoke_llm():
    data = flask.request.json
    query = data.get('query', '')
    logger.info(f"LLM invocation request with query: {query}")
    
    try:
        result = llm_helper.invoke(query, 3)
        logger.info("LLM invocation successful")
        return flask.jsonify(result)
    except Exception as e:
        logger.error(f"Error in LLM invocation: {str(e)}")
        return flask.jsonify({"error": "Failed to process LLM request"}), 500


if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True)