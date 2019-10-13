import urllib3
from twisted.internet import task, reactor
from datetime import datetime

timeout = 60.0 # Sixty seconds

def internet_on():
    try:
       http = urllib3.PoolManager()      
       r = http.request('GET', 'http://httpbin.org/robots.txt',timeout=30)
       if(r.status == 200):
          print('true')
       else:
          f = open("DLINK_Log.txt","a+")
          f.write("Internet off at " + str(datetime.now() + "\r\n"))
          f.close()
          print('Internet disconnected: ' + str(datetime.now()))
    except:
        f = open("DLINK_Log.txt","a+")
        f.write("Internet off at " + str(datetime.now())+ "\r\n")
        f.close()
        print('Internet disconnected: ' + str(datetime.now()))

f = open("DLINK_Log.txt","a+")
f.write("Log started at " + str(datetime.now())+ "\r\n")
f.close()
l = task.LoopingCall(internet_on)
l.start(timeout) # call every sixty seconds

reactor.run()

#internet_on()