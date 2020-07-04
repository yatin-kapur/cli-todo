update tasks
set finish_by = current_date
where finish_by < current_date
and completed = false;
