from datetime import datetime

now = datetime.now()

time_now = ("{0}-{1}-{2} {3}:{4}:{5}"
            .format(now.day, now.month, now.year,
                    now.hour, now.minute, now.second))

print("{0}\n{1}".format(now, time_now))
