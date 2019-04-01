import unittest
from joblogparser import JobLogParser

class TestEmpty(unittest.TestCase):

  def setUp(self):
    self.jlp = JobLogParser('samples/empty.txt')

  def test_empty_file(self):
    result = self.jlp.averageRuntime()
    self.assertEqual(result, 0)

class TestInterleaved(unittest.TestCase):

  def setUp(self):
    self.jlp = JobLogParser('samples/interleavedJobs.txt')

  def test_interleaved_file(self):
    result = self.jlp.averageRuntime()
    self.assertEqual(result, 242.2)

class TestSingle(unittest.TestCase):

  def setUp(self):
    self.jlp = JobLogParser('samples/singleJob.txt')
  
  def test_single_job(self):
    result = self.jlp.averageRuntime()
    self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
