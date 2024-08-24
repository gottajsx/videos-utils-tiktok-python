from moviepy.editor import VideoFileClip
import os 
import config

def crop_to_tiktok_format(input_path, output_path):
    # Charger la vidéo
    clip = VideoFileClip(input_path)
    
    # Format TikTok (9:16, soit 1080x1920)
    tiktok_width, tiktok_height = 1080, 1920
    tiktok_aspect_ratio = tiktok_width / tiktok_height
    
    # Calculer le rapport d'aspect de la vidéo originale
    original_aspect_ratio = clip.size[0] / clip.size[1]
    
    if original_aspect_ratio > tiktok_aspect_ratio:
        # La vidéo est plus large que le format TikTok, on crope en largeur
        new_width = int(clip.size[1] * tiktok_aspect_ratio)
        x1 = (clip.size[0] - new_width) // 2
        y1 = 0
        x2 = x1 + new_width
        y2 = clip.size[1]
    else:
        # La vidéo est plus haute que le format TikTok, on crope en hauteur
        new_height = int(clip.size[0] / tiktok_aspect_ratio)
        x1 = 0
        y1 = (clip.size[1] - new_height) // 2
        x2 = clip.size[0]
        y2 = y1 + new_height
    
    # Recadrer la vidéo pour l'adapter au format TikTok
    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
    
    # Redimensionner la vidéo croppée pour qu'elle corresponde exactement au format TikTok
    final_clip = cropped_clip.resize(newsize=(tiktok_width, tiktok_height))
    
    # Sauvegarder la vidéo recadrée
    final_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

# Exemple d'utilisation
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_video_path = os.path.join(current_dir, config.INPUT_VIDEO_DIRECTORY, 'video1.mp4')
    output_video_path = os.path.join(current_dir, config.OUTPUT_VIDEO_DIRECTORY, 'video1_to_tiktok.mp4')

    crop_to_tiktok_format(input_video_path, output_video_path)


