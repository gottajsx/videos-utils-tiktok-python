import subprocess
import json
import os
import config

def get_video_width(video_path):
    try:
        # Commande FFmpeg pour obtenir les métadonnées de la vidéo en format JSON
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width',
            '-of', 'json',
            video_path
        ]
        
        # Exécute la commande et capture la sortie
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Parse la sortie JSON
        video_info = json.loads(result.stdout)
        
        # Récupère la largeur
        width = video_info['streams'][0]['width']
        
        return width
    
    except Exception as e:
        print(f"Erreur lors de la récupération de la largeur de la vidéo: {e}")
        return None

# Exemple d'utilisation
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    video_file = os.path.join(current_dir, config.INPUT_VIDEO_DIRECTORY, 'video2.mp4')
    width = get_video_width(video_file)
    print(f"La largeur de la vidéo est: {width} pixels")