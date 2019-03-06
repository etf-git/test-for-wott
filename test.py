from agent import _init_
import unittest
from unittest import mock
  try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class unittests(unittest.TestCase):
  def test_is_bootstrapping(self):
  #test def is_bootstrapping() for return True
      self.assertTrue(is_bootstrapping())
	  
  def test_can_read_cert(self):
  #test def can_read_cert() check for correct function, no exit
	  capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput
      can_read_cert()
      sys.stdout = sys.__stdout__
	  printtest=capturedOutput.getvalue()
	  if(printtest!='Permission denied when trying to read the certificate file.' and printtest!='Permission denied when trying to read the key file.'):resulttest=True
	  else:resulttest=False
	  
      self.assertTrue(resulttest)
	  
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
	  
  def test_send_ping(self):
  #test def send_ping() check for correct function
      capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput
      send_ping()
      sys.stdout = sys.__stdout__
	  printtest=capturedOutput.getvalue()
      self.assertTrue(printtest!='Ping failed.')
	  
  def test_say_hello(self):
  #test def say_hello() check for correct work function and return value and test value is JSON
  	  funcreturn=say_hello()
	  self.assertTrue(funcreturn!=None)
	  capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput
      say_hello()
      sys.stdout = sys.__stdout__
	  printtest=capturedOutput.getvalue()
      self.assertTrue(printtest!='Hello failed.')
      try:
      json_insert = json.loads(myjson)
	  json_test=True
      except ValueError as e: json_test=False

	  self.assertTrue(json_test)

  def test_sign_cert(self): 
  #test def sign_cert() check for correct work function and return value and test value is JSON
      self.assertTrue(get_open_ports()!=None)
  	  bootstrapping=is_bootstrapping()
  	  if bootstrapping:device_id=generate_device_id()
  	  else:deviceid = get_device_id()

  	  gen_key=generate_cert(deviceid); rsign_cert=sign_cert(gen_key['csr'], device_id)
  	  self.assertTrue(rsign_cert!=None)
  	  try:
      json_insert = json.loads(rsign_cert)
	  json_test=True
      except ValueError as e: json_test=False
	  
	  self.assertTrue(json_test)
	  
  def test_renew_cert(self): 
  #test def renew_cert() check for correct work function and return value and test value is JSON
      self.assertTrue(get_open_ports()!=None)
  	  bootstrapping=is_bootstrapping()
  	  if bootstrapping:device_id=generate_device_id()
  	  else:deviceid = get_device_id()

  	  gen_key=generate_cert(deviceid); rsign_cert=renew_cert(gen_key['csr'], device_id)
  	  self.assertTrue(rsign_cert!=None)
  	  try:
      json_insert = json.loads(rsign_cert)
	  json_test=True
      except ValueError as e: json_test=False
	  
	  self.assertTrue(json_test)
	  
if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
