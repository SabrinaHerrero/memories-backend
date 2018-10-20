from app import app
from api import api

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=60)
   api.run(debug=True, host='0.0.0.0', port=80)
