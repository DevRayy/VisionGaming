import threading

import time


class VisionSystem:

    def __init__(self, wait=None):
        self.jobs = {}
        self.results = {}
        self.th = None
        self.wait = wait

    def register_job(self, name, job):
        self.jobs[name] = job

    def deregister_job(self, name):
        del self.jobs[name]

    def loop(self):
        while True:
            self.results = {name: job.do() for name, job in self.jobs.items()}
            if self.wait is not None:
                time.sleep(self.wait)

    def run(self):
        self.th = threading.Thread(target=self.loop)
        self.th.start()

    def get_results(self):
        return self.results