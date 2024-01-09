#!/usr/bin/env python3


class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    def __init__(self, name="Guido", job="Sales"):
        self.name = name
        self.job = job
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()
    
    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job not in self.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job
    
    name = property(get_name, set_name)
    job = property(get_job, set_job)

guido = Person("Guido", "Sales")

print(guido.name)
print(guido.job)