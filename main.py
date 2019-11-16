# !/usr/bin/python
# -*- coding:utf-8 -*-
import subprocess, time, sys
import datetime
from mail import send
import arg

TIME = 3600
CMD = "run.py"
PERIOD = arg.PERIOD
ITER = arg.ITER

class Auto_Run():
    def __init__(self, sleep_time, cmd):
        if sys.version_info < (3, 6):
            print("only support python 3.6 and later version")
            sys.exit(1111)
        self.sleep_time = sleep_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()
        self.p = None
        self.run()

        try:
            while 1:
                time.sleep(sleep_time * 20)
                self.poll = self.p.poll()
                if self.p.poll() is None:
                    print("restarting......")
                    self.p.kill()
                    self.run()

                else:
                    print("starting......")
                    self.run()
        except KeyboardInterrupt:
            print("exit???")

    def run(self):
        if self.ext == ".py":
            # use now running python version, think multiple python installed and now use python3.6 to run
            python_path = sys.executable
            #print("use the absolute path of python to run", python_path)
            print('\n[{}] [Sys]     Started!\n'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) )
            with open(r'./stat/daliy_total.txt','w') as f:
                f.write('0')
            self.p = subprocess.Popen([python_path, '%s' % self.cmd], stdin=sys.stdin, stdout=sys.stdout,
                                      stderr=sys.stderr, shell=False)
            for i in range (ITER):
                
                time.sleep(PERIOD * 60)
                with open(r'./stat/daliy_total.txt','r') as f:
                    amount = f.readline()
                print('\n[{}] [Sys]     Running for {} mins --Got {} lotteries\n'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str((i+1) * PERIOD), amount))
            
            with open(r'./stat/log_total.txt','a') as f:
                    f.write('[{}] Got {} lotteries in total'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount))
            
            if arg.mail == 1:                    
                send()
            self.p.kill()
            
        else:
            pass

app = Auto_Run(TIME, CMD)
