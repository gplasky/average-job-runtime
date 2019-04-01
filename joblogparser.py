# Parse the log file
# Find the average runtime of all of the operations
# 
# 2018-01-01T00:00 - Operation ABC Start
# 2018-01-01T00:01 - Operation ABC End
# 2018-01-01T01:02 - Operation XYZ Start
# 2018-01-01T01:05 - Operation CDE Start
# 2018-01-01T02:20 - Operation CDE End
# 2018-01-01T02:50 - Operation XYZ End
# 2018-01-01T06:10 - Operation BCD Start
# 2018-01-01T06:20 - Operation ABC Start
# 2018-01-01T10:50 - Operation FGH End
# 2018-01-01T10:59 - Operation ABC Start
# 2018-01-01T12:16 - Operation ABC End
# 2018-01-01T22:00 - Operation BCD End

import re
from datetime import datetime

class JobLogParser():

  def __init__(self, logfile):
    self.logfile = logfile

  def averageRuntime(self):
    with open(self.logfile, 'r') as f:
      jobEvents = f.read().splitlines()

    if not jobEvents:
      return 0

    startedJobs = dict()
    runtimes = []

    # Job regex
    j = re.compile(
        '(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}) - Operation (?P<job>\w+) (?P<status>Start|End)')

    for event in jobEvents:
      m = j.search(event)
      if m:
        currentJob = m.group('job')
        currentTimestamp = datetime.strptime(
            m.group('timestamp'), '%Y-%m-%dT%H:%M')
        currentStatus = m.group('status')

        #print('timestamp: {}, job: {}, status: {}'.format(
        #    m.group('timestamp'), m.group('job'), m.group('status')))

        # Job has already started
        if currentJob in startedJobs and currentStatus == 'End':
          timedelta = currentTimestamp - startedJobs[currentJob]
          total_minutes = timedelta.total_seconds() / 60
          runtimes.append(total_minutes)
          continue

        if currentStatus == 'Start':
          startedJobs[currentJob] = currentTimestamp

        # We ignore 'End' events with no corresponding start

    #print runtimes
    if (len(runtimes) == 0):
      return 0
    else:
      print runtimes
      return (sum(runtimes) / len(runtimes))

if __name__ == "__main__":
    jlp = JobLogParser('test/samples/interleavedJobs.txt')
    print(jlp.averageRuntime())
