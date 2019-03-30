import unittest

target = __import__("averageRuntime")

class averageRuntimeTest(unittest.TestCase):

  testFileDir = 'samples/'

  def testEmptyFile(self):
    result = target.averageRuntime(self.testFileDir + 'empty.txt')
    self.assertEqual(result, 0)

  # 1m
  # 98m
  # 75m
  # 940m
  # 77m
  # == ==
  # 238.2
  #
  def testInterleavedFile(self):
    result = target.averageRuntime(self.testFileDir + 'interleavedJobs.txt')
    self.assertEqual(result, 238.2)

  def testSingleJob(self):
    result = target.averageRuntime(self.testFileDir + 'singleJob.txt')
    self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
