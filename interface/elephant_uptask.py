from up.crosscorrelogram_task.crosscorrelogram_task import crosscorrelogram_task as cr
from up.elephant_cv_task.elephant_cv_task import elephant_cv_task as el


__author__ = 'lphan'


class Elephant_sub(object):
    '''Sub Interface to call up-functions locally
    '''
    def __init__(self):
        pass

    @staticmethod
    def elephant_up_cc(inputdata, number_of_jobs, job_id):
        cr(inputdata, number_of_jobs, job_id)

    @staticmethod
    def elephant_up_cv():
        el()
