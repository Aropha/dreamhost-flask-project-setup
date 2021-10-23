
import sys, os
# INTERP = os.path.join(os.environ['HOME'], 'ai.aropha.com', 'venv', 'bin', 'python3')
INTERP = os.path.expanduser("~/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
sys.path.append('~/ai.aropha.com/app')
from app.app import app as application

if __name__ == '__main__':
    application.run(debug=False)





# ###### App Config ######

# import sys, os

# # Switch to the virtualenv if we're not already there
# INTERP = os.path.expanduser("~/env/wsgi/bin/python")
# if sys.executable != INTERP: 
#     os.execl(INTERP, INTERP, *sys.argv)
# sys.path.append(os.getcwd())

# sys.path.append('~/<DOMAIN PATH>/app')
# from app.app import app as application

# if __name__ == '__main__':
#     application.run(debug=False)