from agent import _init_
import unittest

class unittests(unittest.TestCase):
  def test_is_bootstrapping(self):
  #test def is_bootstrapping() for return True
      self.assertTrue(is_bootstrapping())
# Don't understand who make test for can_read_cert() 
# def test_can_read_cert(self):
#      self.assertTrue()
  def test_get_primary_ip(self):
  #test def get_primary_ip() checking for an explicit return value and for matching the result against the pattern of the ip-address
      self.assertTrue(get_primary_ip()!=None)
	  isipresult=False
	  resulttest = get_primary_ip().split('.')
      if len(resulttest) != 4: isipresult=False
      try: all(0<=int(p)<256 for p in resulttest)
	  isipresult=True
      except ValueError: isipresult=False
	  self.assertTrue(isipresult)
  def test_get_certificate_expiration_date(self):
  #test def get_certificate_expiration_date() whether the returned result is a date
      try:
      newDate = datetime.datetime(get_certificate_expiration_date())
      correctDate = True
      except ValueError:
      correctDate = False
      self.assertTrue(correctDate)
  def test_time_for_certificate_renewal(self):
  #test def time_for_certificate_renewal() for return True
      self.assertTrue(time_for_certificate_renewal())
  def test_generate_device_id(self):
  #test def generate_device_id() checking for an explicit return value
      self.assertTrue(generate_device_id()!=None)
  def test_get_device_id(self):
  #test def get_device_id() checking for an explicit return value
      self.assertTrue(get_device_id()!=None)
  def test_generate_cert(self):
  #test def generate_cert() whether the return result is an array
  	gcval=None; bootstrapping=is_bootstrapping()
	
	if bootstrapping:device_id=generate_device_id()
	else:deviceid = get_device_id()

	gcval=generate_cert(deviceid)
	
	if not isinstance(gcval, list):gcval=None
	  
      self.assertTrue(gcval!=None)
  def test_get_ca_cert(self):
  #test def get_ca_cert() checking for an explicit return value
      self.assertTrue(get_ca_cert()!=None)
  def test_get_open_ports(self):
  #test def get_open_ports() checking for an explicit return value
      self.assertTrue(get_open_ports()!=None)
	  
if __name__ == '__main__':
    unittest.main()
