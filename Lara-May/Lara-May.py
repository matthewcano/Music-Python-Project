#if socket is in use use $ lsof -i 50000(port #)
#and kill the pid with $ kill (pid)
#run with command line :
#/Users/matthewcano/cs3320-env/bin/python /Users/matthewcano/PycharmProjects/Lara-May/Lara-May.py runserver --debug --reload

import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('homepage.html')

@app.route('/songs')
def songs():
    return flask.render_template('songs.html')

@app.route('/bio')
def bio():
    return flask.render_template('bio.html')

@app.route('/photos')
def photos():
    return flask.render_template('photos.html')

@app.route('/events')
def events():
    return flask.render_template('events.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html')

@app.route('/downloads')
def downloads():
    return flask.render_template('downloads.html')

if __name__ == '__main__':
   app.run()
