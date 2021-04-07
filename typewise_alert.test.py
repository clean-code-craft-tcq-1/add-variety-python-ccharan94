import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    #Check Breaches
    self.assertTrue(typewise_alert.infer_breach(10, 20, 60) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(30, 20, 60) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(50, 20, 60) == 'NORMAL')
   
   #Check Alerts
   def test_check_and_alert(self): 
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 60) == 'Temperature is too high')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 60) == '65261, TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 60) == 'Temperature is too low')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 60) == '65261, TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 60) == 'Temperature is normal')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 60) == '65261, NORMAL')
    
if __name__ == '__main__':
  unittest.main()
