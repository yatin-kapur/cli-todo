# TODO

## Setup
1. Run this command to create `todo` database and make the `tasks` table.

```
$ mysql < initialize_db.sql
```

2. Add cronjob to update task dates after date ticks over, you might have to change permissions allowed to your cron depending on OS.

```
0 0 * * * /usr/local/bin/mysql todo < [mypathtoproject]todo/update_date.sql
```

3. This scripts copies the `todo` file into `/usr/local/bin` so it can be used as a cli command.

```
$ chmod u+x update.sh; bash update.sh
```

## How to Use
Just run `todo --help`, it's super easy to work with

![example](example.png)

## Pending
Test Suite.