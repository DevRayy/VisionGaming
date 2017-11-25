from vision_gaming.vision_system import VisionSystem as VS
from vision_gaming.job import Job

def prc(input):
    print('prc_fcn')

def iden(input):
    print('iden')
    return 5

system = VS()
j = Job(screen_rect=None, process=[prc], identify=iden)
system.register_job('job1', j)
system.run()

while True:
    print('returned: {}'.format(system.get_results()['job1']))
