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

def averageRuntime(logfile):
  return 0