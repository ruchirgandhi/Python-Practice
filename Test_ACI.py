import pexpect
try:
  import pxssh
except:
  from pexpect import pxssh

import re
import os
import subprocess
import threading
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")



#to enable sms/text service
import smtplib
from email.mime.text import MIMEText


# Username/Password
USERNAME = 'admin'
PASSWORD = 'ins3965!'


# Expect Prompts
SWITCH_DEFAULT_PASSWORD_PROMPT = r'(?i)password'
SWITCH_DEFAULT_PROMPT = r'#'

apicIpAddr = ['scale123-apic1.insieme.local', 'ifav41-ifc1.insieme.local']


class ParallelApicCheck(threading.Thread):
    def run(self):
        doApicLogin(self.ApicAddr)


def sendEmail(subject, body, recipients):
        msg = MIMEText("""%s""" %body)
        msg['Subject'] = subject
        msg['From'] = 'sarokum3@cisco.com'
        msg['To'] = ','.join(recipients)
        server = smtplib.SMTP('mail.cisco.com')
        server.sendmail('sarokum3@cisco.com', recipients, msg.as_string())


def doApicLogin(apicIpAddr, USERNAME='admin', PASSWORD='ins3965!'):
            resultFlag = False
            cflag = True
            ssh = pexpect.spawn('ssh -a -o UserKnownHostsFile=/dev/null \
                            -o StrictHostKeyChecking=no -o PubkeyAuthentication=no \
                            -o PreferredAuthentications=keyboard-interactive,password ' + \
                            USERNAME + '@' + apicIpAddr)
            ssh.expect(SWITCH_DEFAULT_PASSWORD_PROMPT, timeout=20)
            ssh.sendline(PASSWORD)
            index = ssh.expect([SWITCH_DEFAULT_PROMPT, 'password', pexpect.TIMEOUT])
            if(index==0):
                print "Login successful: %s" % apicIpAddr
                pexpectlogFile = '/home/sarokum3/pexpectlog_%s' % apicIpAddr

                if os.path.exists(pexpectlogFile):
                    os.remove(pexpectlogFile)
                logfile = file(pexpectlogFile, "w")
                ssh.logfile_read = logfile
                ssh.sendline('dmesg -T | grep kill\n')
                ssh.expect(SWITCH_DEFAULT_PROMPT, timeout=180)
                ssh.sendline('exit')
                ssh.expect(pexpect.EOF)

                pattern = 'oom_kill_process.*'
                fout =  open(pexpectlogFile, 'r')
                foutput = fout.read().split('\n')
                foutput.remove('')
                print(foutput[-2])
                pattern1 = '\[(.*)\].*'
                x = re.match(pattern1, foutput[-2])
                if x is not None:
                    out = datetime.strptime(x.group(1), "%a %b %d %H:%M:%S %Y").strftime("%d/%m/%Y %H:%M:%S")
                    if os.path.exists('/home/sarokum3/issue_track.txt'):
                        with open('/home/sarokum3/issue_track.txt', 'r') as fh:
                            line = fh.readline()
                        if line == out:
                            cflag = False
                    with open('/home/sarokum3/issue_track.txt', 'w') as fh:
                        fh.write(out)
                    for i in foutput:
                        if re.search(pattern, i):
                            resultFlag = True

                if resultFlag and cflag:
                     #send email to interested folks:
                     subject = '[AUTO-ALERT] OOM killer process seen ,please check the apic and take appropriate action!!!'
                     body = 'OOM Killer process in '+apicIpAddr
                     recipients = ['sarokum3@cisco.com']
                     sendEmail(subject, body, recipients)
                ssh.close()
            if(index==1):
                print "***** Authentication failed: %s *****" % apicIpAddr

#doApicLogin('scale123-apic1.insieme.local')
for apicAddr in apicIpAddr:
    t = ParallelApicCheck()
    t.ApicAddr = apicAddr
    t.start()
