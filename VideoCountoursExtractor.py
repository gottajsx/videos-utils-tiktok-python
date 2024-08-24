import cv2
import numpy as np 
from moviepy.editor import VideoFileClip
import os

def process_frame(frame):
    # Convertir en niveaux de gris
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un filtre de détection des contours
    edges = cv2.Canny(gray_frame, threshold1=100, threshold2=200)
    
    # Augmenter l'épaisseur des contours (dilate)
    edges = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)
    
    # Convertir le résultat en une image RGB (nécessaire pour moviepy)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    
    return edges_rgb

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    processed_clip = clip.fl_image(process_frame)
    processed_clip.write_videofile(output_path, codec='libx264')

# Exemple d'utilisation
current_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(current_dir, 'tmp', 'video1.mp4')
output_video_path = os.path.join(current_dir, 'tmp', 'video1_out.mp4')

process_video(input_video_path, output_video_path)