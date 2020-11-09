from flask import Flask, render_template
from DataMusic import MusicList
from Similarity import similar

app = Flask(__name__)

MusicList = MusicList()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/music')
def music():
    return render_template('music.html', ml=MusicList)

@app.route('/song/<string:title>/')
def song(title):
    sim = similar(title)
    return render_template('song.html', t1=title, m=MusicList, s1=sim)




if __name__ == '__main__':
    app.run(debug=True)
