from flask import Flask, request, render_template
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Assurez-vous d'avoir un fichier index.html dans un dossier templates

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']  # Récupération de l'URL à partir du formulaire
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    download_path = video.download('/chemin/de/destination')
    return f'Vidéo téléchargée : {download_path}'

if __name__ == '__main__':
    app.run(debug=True)
