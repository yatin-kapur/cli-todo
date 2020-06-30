from collections import OrderedDict
from datetime import date

class Tasks:
    def __init__(self, rows):
        self.rows = rows
        self.tasks = self.initialize_items()

    def initialize_items(self):
        tasks = OrderedDict()
        n = len(self.rows)
        for i, row in enumerate(self.rows):
            t = TaskItem(row)
            tasks[t.id] = t

        return tasks

    def display(self):
        # keep track of previous day for output formatting
        prev_day = -1
        print("ID | Days | Task")

        for id, task in self.tasks.items():
            if prev_day != task.days:
                print()
                prev_day = task.days

            print(task.show())

class TaskItem:
    def __init__(self, data):
        self.id = data[0]
        self.task = data[1]
        self.finish_by = data[2]
        self.days = (self.finish_by - date.today()).days
        self.completed = data[3]
        self.output = self.show()

    def show(self):
        output = "{:>2} | {:>4} | {}".format(
            self.id, 
            self.days,
            self.task
        )

        if self.completed:
            output = ''.join([u'\u0336{}'.format(c) for c in output])

        return output