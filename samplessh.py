import subprocess
import sys

HOST="mettle@192.168.3.145"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"

key="ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAQDhljlCUcG4Vjysf6PSek+4GFq54wT1y1ZEMBbE8ZTmuH53gDsgSOC4hVCMszWPfvuPA97ISJuZHiibX4oWQwr/RvNfrmOjH+XxeN2ucuDqg9qwhKH7X8DapKVM3nvCuX/g3IxNGWg/y2VeeqGhlHX9L7pdPz+vfenZjwEDYpF3Oa1JvbkB1FJbLhAw3moChyMDS/pTFtsb8i61OPdBBnQS/bTvbYl8a07qHKHXK4HQfy6gtlr8PTpt0iT6pv2BTY9G1k0P66GZ5j8/XhvJobgg6ODtHFjwI8W1VEBTlcOwoxtA4kORCPpac1wkM3TNLLtZO8qRQ1dmkhT0cJIN54T1jabir@hercules"

#:print "ssh -i "+key +" %s" % HOST, COMMAND"
ssh = subprocess.Popen(["ssh -i "+key +" %s" % HOST, COMMAND],
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
print 'completed'
