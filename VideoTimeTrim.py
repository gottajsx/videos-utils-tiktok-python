from moviepy.editor import VideoFileClip

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

# Chemins vers les fichiers vidéo
input_video_path = 'chemin/vers/ton/video.mp4'
output_video_path = 'chemin/vers/ton/video_cut.mp4'

# Temps de début (t1) et de fin (t2) en secondes
t1 = 30  # par exemple, couper à partir de 30 secondes
t2 = 60  # par exemple, jusqu'à 60 secondes

cut_video(input_video_path, output_video_path, t1, t2)