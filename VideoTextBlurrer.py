import cv2
import pytesseract
import numpy as np
from moviepy.editor import VideoFileClip
import os
import shutil

# Assure-toi d'avoir installé Tesseract OCR sur ton système
# https://github.com/tesseract-ocr/tesseract

# Trouver le chemin vers l'exécutable Tesseract
tesseract_cmd_path = shutil.which('tesseract')

if tesseract_cmd_path is None:
    raise FileNotFoundError("Tesseract-OCR n'est pas installé ou non trouvé dans le PATH")

# Configurer pytesseract pour utiliser le chemin trouvé
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

def blur_text_areas(frame):
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utiliser pytesseract pour détecter les boîtes englobantes des textes
    boxes = pytesseract.image_to_boxes(gray)

    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

        # Appliquer un flou sur la région contenant du texte
        roi = frame[frame.shape[0] - h:frame.shape[0] - y, x:w]
        roi = cv2.GaussianBlur(roi, (15, 15), 0)
        frame[frame.shape[0] - h:frame.shape[0] - y, x:w] = roi

    return frame

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    processed_clip = clip.fl_image(blur_text_areas)
    processed_clip.write_videofile(output_path, codec='libx264')

# Chemins de la vidéo d'entrée et de sortie
current_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(current_dir, 'tmp', 'video1.mp4')
output_video_path = os.path.join(current_dir, 'tmp', 'video1_blur.mp4')

# Traiter la vidéo
process_video(input_video_path, output_video_path)