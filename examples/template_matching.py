import time
from cv2 import cv2

from vision_gaming.process import show_screen, resize, convert_color, binary_threshold
from vision_gaming.identify import tesseract, match_template, match_template_multiple, match_number
from vision_gaming.vision_system import VisionSystem as VS
from vision_gaming.job import Job


# job data
screen_rect = (200, 800, 250, 850)
prc = [convert_color(cv2.COLOR_BGR2GRAY),
       show_screen('screen'),
       binary_threshold(200, 255)]

templates = [cv2.imread('templates/{}.jpg'.format(i), 0) for i in range(0, 10)]
iden = match_number(templates, range(0, 10))

# creating a Job
j = Job(screen_rect=screen_rect, process=prc, identify=iden)

# creating VisionSystem
system = VS()

# registering a Job
system.register_job('job1', j)

# running VisionSystem
system.run()

while True:
    print('returned: {}'.format(system.get_results().get('job1', None)))
    time.sleep(1)
