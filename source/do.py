#!/usr/bin/python3

from task import TaskItem, Tasks
from cxn import get_cxn
from datetime import date, timedelta
import sys

def help():
    default = "do"
    all = 'do all'
    add = 'do add "[task]" [days]'
    delete = 'do delete [id]'
    edit = 'do edit [id] ["task"]'
    days = 'do days [id] [days]'
    completed = 'do complete [id]'
    incomplete = 'do incomplete [id]'
    
    statement = """{:<25}: displays list of incomplete tasks
{:<25}: displays all incomplete and complete tasks
{:<25}: how to add a task to the list
{:<25}: delete task of given id
{:<25}: edit task of given id
{:<25}: reset days of task with given id
{:<25}: mark task of id as completed
{:<25}: mark task of id as inccomplete""".format(
                                            default,
                                            all,
                                            add,
                                            delete,
                                            edit,
                                            days,
                                            completed,
                                            incomplete
                                        )

    print(statement)

def main():
    # parse arguments
    args = sys.argv

    cxn = get_cxn()
    cursor = cxn.cursor()

    if len(args) == 1:
        cxn = get_cxn()
        cursor = cxn.cursor()
        query = """
                select id, task, finish_by, completed
                from tasks 
                where completed = false
                order by finish_by;
                """
        cursor.execute(query)
        rows = cursor.fetchall()

        # initialize tasks list
        tasks = Tasks(rows)
        tasks.display()

    elif len(args) == 2 and args[1] == 'all':
        query = """
                select id, task, finish_by, completed
                from tasks 
                order by finish_by;
                """
        cursor.execute(query)
        rows = cursor.fetchall()

        # initialize tasks list
        tasks = Tasks(rows)
        tasks.display()
    
    elif args[1] == 'add':
        days = args[3]
        task = args[2]

        query = """
                insert into 
                tasks (task, finish_by, completed) 
                values ('{}', date_add(current_date, interval {} day), 0);
                """.format(
                    task,
                    days
                )

        cursor.execute(query)
        cxn.commit()
    
    elif args[1] == 'delete':
        id = args[2]

        query = """
                delete from tasks
                where id = {};
                """.format(
                    id
                )

        cursor.execute(query)
        cxn.commit()

    elif args[1] == 'edit':
        id = args[2]
        task = args[3]

        query = """
                update tasks
                set task = '{}'
                where id = {};
                """.format(
                    task,
                    id
                )

        cursor.execute(query)
        cxn.commit()

    elif args[1] == 'days':
        id = args[2]
        days = args[3]

        query = """
                update tasks
                set finish_by = date_add(current_date, interval {} day)
                where id = {};
                """.format(
                    days,
                    id
                )

        cursor.execute(query)
        cxn.commit()

    elif args[1] == 'complete':
        id = args[2]

        query = """
                update tasks
                set complete = true
                where id = {};
                """.format(
                    days,
                    id
                )

        cursor.execute(query)
        cxn.commit()

    elif args[1] == 'incomplete':
        id = args[2]

        query = """
                update tasks
                set complete = false
                where id = {};
                """.format(
                    days,
                    id
                )

        cursor.execute(query)
        cxn.commit()
    
    elif args[1] == 'help':
        help()

    cxn.close()

if __name__ == '__main__':
    main()