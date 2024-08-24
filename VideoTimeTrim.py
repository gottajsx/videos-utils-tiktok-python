from moviepy.editor import VideoFileClip
import config
import os

def cut_video(input_path, output_path, t1, t2):
    # Charger la vidéo
    clip = VideoFileClip(input_path)
    
    # Vérifier que les temps sont dans les limites de la vidéo
    if t1 < 0 or t2 > clip.duration or t1 >= t2:
        raise ValueError("Les temps t1 et t2 doivent être valides et t1 doit être inférieur à t2.")
    
    # Couper la vidéo entre t1 et t2
    cropped_clip = clip.subclip(t1, t2)
    
    # Écrire le fichier de sortie
    cropped_clip.write_videofile(output_path, codec='libx264')

if __name__ == '__main__':
    # Chemins vers les fichiers vidéo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_video_path = os.path.join(current_dir, config.INPUT_VIDEO_DIRECTORY, 'video2.mp4')
    output_video_path = os.path.join(current_dir, config.OUTPUT_VIDEO_DIRECTORY, 'video2_trim.mp4')

    # Temps de début (t1) et de fin (t2) en secondes
    t1 = 10  # par exemple, couper à partir de 30 secondes
    t2 = 20  # par exemple, jusqu'à 60 secondes

    cut_video(input_video_path, output_video_path, t1, t2)