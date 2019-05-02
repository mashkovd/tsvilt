import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.insert(0, 'C:/Users/user/PycharmProjects/flask+dash/venv/Lib/site-packages')
sys.path.insert(0, BASE_DIR)



from app.app import server as application