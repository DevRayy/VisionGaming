import time
from cv2 import cv2

from vision_gaming.process import show_screen, resize, convert_color, binary_threshold
from vision_gaming.identify import tesseract, match_template, match_template_multiple
from vision_gaming.vision_system import VisionSystem as VS
from vision_gaming.job import Job


# job data
screen_rect = (1, 600, 400, 1000)
prc = [convert_color(cv2.COLOR_BGR2RGB),
       show_screen('original'),
       convert_color(cv2.COLOR_RGB2GRAY),
       binary_threshold(200, 255)]
template = cv2.imread('4.jpg', 0)
iden = match_template_multiple(template, show_result=True)

# creating a Job
j = Job(screen_rect=screen_rect, process=prc, identify=iden)

# creating VisionSystem
system = VS(wait=0.1)

# registering a Job
system.register_job('job1', j)

# running VisionSystem
system.run()

while True:
    print('returned: {}'.format(system.get_results().get('job1', None)))
    time.sleep(1)
