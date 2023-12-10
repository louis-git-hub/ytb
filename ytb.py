from flask import Flask, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download('/path/to/download')

    # Après le téléchargement, envoyez le fichier au client
    return send_file('/path/to/download/video.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False, port=5001)  # Désactiver le mode debug et changer le port
