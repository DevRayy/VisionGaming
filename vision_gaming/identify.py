from cv2 import cv2
import pytesseract
from PIL import Image


def debug_identifier(message):
    def debug_identifier_wrapped(input):
        print(message)
        return message
    return debug_identifier_wrapped


def tesseract(exe_path, data_dir, lang='eng'):
    pytesseract.pytesseract.tesseract_cmd = exe_path
    def tesseract_wrapped(input):
        return pytesseract.image_to_string(Image.fromarray(input), lang=lang, config=data_dir)
    return tesseract_wrapped


def match_template(template_image, method=cv2.TM_CCOEFF, show_result=False):
    def match_template_wrapped(input):
        res = cv2.matchTemplate(input, template_image, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if show_result:
            w, h = template_image.shape[::-1]
            top_left = min_loc if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] else max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(input, top_left, bottom_right, 255, 2)
            cv2.imshow('Template identification', input)
        return max_val, max_loc
    return match_template_wrapped
