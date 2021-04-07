cooling_range =  { 'PASSIVE_COOLING'     : {'lowerLimit': 0,'upperLimit':35},
                   'HI_ACTIVE_COOLING'   : {'lowerLimit': 0,'upperLimit':45},
                   'MED_ACTIVE_COOLING'  : {'lowerLimit': 0,'upperLimit':40} }

alert_messages_for_breach_code = { 'TOO_LOW'  : 'Temperature is too low', 
                                   'TOO_HIGH' : 'Temperature is too high', 
                                   'NORMAL'   : 'Temperature is normal' }
                                
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = cooling_range[coolingType]['lowerLimit']
  upperLimit = cooling_range[coolingType]['upperLimit']
  return infer_breach(temperatureInC, lowerLimit, upperLimit)

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')                             
  return f'{header}, {breachType}'

def send_to_console(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')                             
  return f'{header}, {breachType}'

def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  print(alert_messages_for_breach_code[breachType]) 
  return alert_messages_for_breach_code[breachType]                               

alert_target_function_mapping = { "TO_CONTROLLER": send_to_controller, "TO_EMAIL" : send_to_email, "TO_CONSOLE" : send_to_console }

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar, temperatureInC)
  return alert_target_function_mapping[alertTarget](breachType)
