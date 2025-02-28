from datetime import datetime
import time

start = datetime.now()
time.sleep(2)

now = datetime.now()

diff = now - start

print(diff, type(diff), diff.total_seconds(), int(diff.total_seconds()))