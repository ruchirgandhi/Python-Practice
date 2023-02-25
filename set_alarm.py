import time
import pyaudio


print("made by python.hub")


def myAlarm():
    try:
          myTime=list(map(int,input('enter the time in the m/sec').split()))
          if len(myTime)==3:
              total_sounds= myTime[0]*60*60+myTime[1]*60+myTime[2]
              time.sleep(total_sounds)
              frequency=2500
              duration=1000
              pyaudio.Beep(frequency , duration )
          else:
             print('please write the correct format as mentioned\n')
             myAlarm()
    except Exception as e:
        print('this is the exception',e,'please enter correct details')
        myAlarm()
    myAlarm()


myAlarm()