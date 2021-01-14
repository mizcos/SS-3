# 未服用時
import datetime

t = datetime.datetime.now()+datetime.timedelta(minutes=10)
print(t)

snooze = str(t.hour)+':'
if t.minute<10:
    snooze = snooze+'0'
snooze = snooze+str(t.minute)

print(snooze)

currentTime = datetime.datetime.now()
if currentTime == snooze or currentTime == snooze: #食事時刻すべて
    import alarm_test
    # すでに鳴らしている場合の対処も必要？
