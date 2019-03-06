from agent import _init_
import unittest

class unittests(unittest.TestCase):
  def test_is_bootstrapping(self):
      self.assertEqual(is_bootstrapping(),True)
# Don't understand who make test for can_read_cert() 
# def test_can_read_cert(self):
#      self.assertTrue()
  def test_get_primary_ip(self):
      self.assertTrue(get_primary_ip()!=None)
	  isipresult=False
	  resulttest = get_primary_ip().split('.')
      if len(resulttest) != 4: isipresult=False
      try: all(0<=int(p)<256 for p in resulttest)
	  isipresult=True
      except ValueError: isipresult=False
	  self.assertTrue(isipresult)
  def test_get_certificate_expiration_date(self):
      try:
      newDate = datetime.datetime(get_certificate_expiration_date())
      correctDate = True
      except ValueError:
      correctDate = False
      self.assertTrue(correctDate)
  def test_time_for_certificate_renewal(self):
      self.assertTrue(time_for_certificate_renewal())
  def test_generate_device_id(self):
      self.assertTrue(generate_device_id()!=None)
  def test_get_device_id(self):
      self.assertTrue(get_device_id()!=None)
  def test_generate_cert(self):
      bootstrapping = is_bootstrapping()
      if bootstrapping:
      gcval = generate_cert(get_device_id())
	  if isinstance(gcval, list)==False:
	  gcval = None
	  else:
	  gcval = None
      self.assertTrue(gcval!=None)
  def test_get_ca_cert(self):
      self.assertTrue(get_ca_cert()!=None)
  def test_get_open_ports(self):
      self.assertTrue(get_open_ports()!=None)
	  
if __name__ == '__main__':
    unittest.main()