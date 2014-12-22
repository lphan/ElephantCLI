from active_worker.task import task
from task_types import TaskTypes as tt

_task_full_name = "lphan_addition_task"
_task_caption = "it adds numbers"
_task_author = "lphan"
_task_description = "first test basic addition"
_task_categories = ['test']  # list of category strings (ex. ['test'])
_task_compatible_queues = ['all']  # ***list of compatible queue strings.


@task(accepts=(tt.LongType, tt.LongType), returns=tt.LongType)
def lphan_addition_task(left, right):
    # *** task code
    return left + right

if __name__ == '__main__':
    print lphan_addition_task(1, 1)
