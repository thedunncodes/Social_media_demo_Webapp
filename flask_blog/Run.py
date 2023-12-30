# NOTE: '.' in the importation code lines mean current directory.
#       therefore in our case 'flaskblog' since it's our package dir. 

from flaskblog import app
# style="padding:20px;font-size:20px;border:2px solid grey;border-radius:5px;"

if __name__ == '__main__':
    app.run(debug=True)