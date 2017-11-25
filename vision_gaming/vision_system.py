import threading


class VisionSystem:

    def __init__(self):
        self.jobs = {}
        self.results = {}
        self.th = None

    def register_job(self, name, job):
        self.jobs[name] = job

    def deregister_job(self, name):
        del self.jobs[name]

    def loop(self):
        while True:
            self.results = {name: job.do() for name, job in self.jobs.items()}

    def run(self):
        self.th = threading.Thread(target=self.loop)
        self.th.start()

    def get_results(self):
        return self.results