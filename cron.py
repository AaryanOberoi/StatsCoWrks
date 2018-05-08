from crontab import CronTab

cron = CronTab(user='aaryan')  
job = cron.new(command='python example1.py')  
job.minute.every(10)

cron.write()  