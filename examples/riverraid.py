import time
from cv2 import cv2

from vision_gaming.process import show_screen, resize, convert_color, binary_threshold
from vision_gaming.identify import tesseract, match_template, match_template_multiple, match_number
from vision_gaming.vision_system import VisionSystem as VS
from vision_gaming.job import Job
def fuel_guage():
    def fuel_guage_wrapped(screen):
        try:
            line = [p for p in screen[10]]
            first_idx = line.index(255)
            last_idx = len(line) - 1 - line[::-1].index(255)
            thickness = last_idx - first_idx
            percentage = int(100*first_idx / (len(line) - thickness))
            return percentage
        except:
            return None
    return fuel_guage_wrapped

# job data
screen_rect1 = (245, 570, 710, 880)
prc1 = [show_screen('screen'),
        convert_color(cv2.COLOR_BGR2GRAY)]

fuel_template = cv2.imread('templates/fuel.PNG', 1)
fuel_template = cv2.cvtColor(fuel_template, cv2.COLOR_BGR2GRAY)
iden1 = match_template_multiple(fuel_template, 0.8)
j1 = Job(screen_rect=screen_rect1, process=prc1, identify=iden1)

screen_rect2 = (420, 835, 535, 860)
prc2 = [show_screen('screen'),
        convert_color(cv2.COLOR_BGR2GRAY),
        binary_threshold(200, 255),
        show_screen('binarized')]
iden2 = fuel_guage()
j2 = Job(screen_rect=screen_rect2, process=prc2, identify=iden2)

# creating VisionSystem
system = VS(wait=0.2)

# registering a Job
system.register_job('job1', j1)
system.register_job('job2', j2)

# running VisionSystem
system.run()

while True:
    print('fuel positions: {}'.format(system.get_results().get('job1', None)))
    print('fuel left:: {}'.format(system.get_results().get('job2', None)))
    time.sleep(0.5)
