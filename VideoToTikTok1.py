from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize
import os

def convert_to_tiktok_format(input_path, output_path):
    # Charger la vidéo
    clip = VideoFileClip(input_path)
    
    # Format TikTok (9:16, soit 1080x1920)
    tiktok_width, tiktok_height = 1080, 1920
    tiktok_aspect_ratio = tiktok_width / tiktok_height
    
    # Calculer le rapport d'aspect de la vidéo originale
    original_aspect_ratio = clip.size[0] / clip.size[1]
    
    # Redimensionner la vidéo tout en conservant le rapport d'aspect
    if original_aspect_ratio > tiktok_aspect_ratio:
        # La vidéo est plus large que le format TikTok, ajuster la largeur
        new_width = tiktok_width
        new_height = int(tiktok_width / original_aspect_ratio)
    else:
        # La vidéo est plus haute que le format TikTok, ajuster la hauteur
        new_height = tiktok_height
        new_width = int(tiktok_height * original_aspect_ratio)
    
    resized_clip = resize(clip, (new_width, new_height))
    
    # Ajouter du padding (des bandes noires) pour correspondre au format TikTok
    final_clip = resized_clip.margin(
        left=(tiktok_width - new_width) // 2,
        right=(tiktok_width - new_width) // 2,
        top=(tiktok_height - new_height) // 2,
        bottom=(tiktok_height - new_height) // 2,
        color=(0, 0, 0)  # Couleur des bandes noires
    )
    
    # Sauvegarder la vidéo au format TikTok
    final_clip.write_videofile(output_path, codec="libx264")

# Exemple d'utilisation
current_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(current_dir, 'tmp', 'video1.mp4')
output_video_path = os.path.join(current_dir, 'tmp', 'video1_to_tiktok.mp4')

convert_to_tiktok_format(input_video_path, output_video_path)