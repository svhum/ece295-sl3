'''make sure matplotlib is properlly installed. Following link may help: https://www.tutorialspoint.com/how-to-install-matplotlib-in-python'''
import matplotlib.pyplot as plt 
import pyvisa as visa
import numpy as n
import time, csv
rm = visa.ResourceManager(r'C:\WINDOWS\system32\visa64.dll')
print(rm)
print(rm.list_resources('TCPIP0::?*'))

try:
    '''Connect to the instruments'''
    meter =  rm.open_resource('TCPIP0::192.168.0.252::5025::SOCKET')
 

    ''' Set up the digital multimeter IO configuration'''
    meter.timeout = 20000

    # Define string terminations
    meter.write_termination = '\n'
    meter.read_termination = '\n'

    # Set string terminations
    print('\nVISA termination string (write) set to newline: ASCII ',
          ord(meter.write_termination))
    print('VISA termination string (read) set to newline: ASCII ',
          ord(meter.read_termination))

    # Get the ID info of the digital multimeter 
    print('meter ID string:\n  ', meter.query('*IDN?'), flush=True)

    # Code goes here
    #meter.write('CONF:VOLT:AC') #AC voltage measurement configuration
    '''change digital multimeter's triggering system from "idle" to "wait for trigger", then trigger and send out the measurement'''
    #meter.write('READ?') #way 1
    #meter.write('INIT')  #way 2
    #meter.write('FETC?')
    
    #meter.write('MEAS:VOLT:AC?') #set AC voltage measurement

    #print(meter.query('MEAS:VOLT:AC?'))
    #values = meter.query_ascii_values('MEAS:VOLT:AC?')
    #print("Average voltage: ", sum(values) / len(values)) #output average voltage 
     
    meter.write('CONF:VOLT: DC')
    #print(meter.query('READ?'))

    num_times = 20
    times = n.linspace(1,num_times,num_times)
    temperature = [0]*num_times

    time_idx = 0
    for i in times:

      temperature[time_idx] = float(meter.query('MEAS:VOLT:DC?'))*100-273
      print(temperature[time_idx])
      time.sleep(0.25)
      time_idx = time_idx+1

    plt.plot(times,temperature, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()



except(KeyboardInterrupt):
    print('Keyboard Interrupted execution!')




    '''OutputTable = n.empty([99,2])
    inputSamples = 0
    StopTime = 10000
    testStartTime = time.time() 

    while testStartTime < StopTime:
      meter.write('MEAS:VOLT:AC?')
      [volt] = meter.query('MEAS:VOLT:AC?')
      print([volt])
'''
    
except(KeyboardInterrupt):
    print('Keyboard Interrupted execution!')
