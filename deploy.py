
# coding: utf-8

# In[ ]:


import paramiko
import time

def deploy(path_to_ssh_key_private_key, server_address, prefix):
    print "Connecting to box"
    print ""
    k = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "connecting"
    c.connect(hostname = server_address, username = "testtest", pkey = k ) # change back username 
    print "connected"

    c.exec_command("rm -rf sprint1; git clone https://github.com/chrispaulca/sprint1.git")
    print "Pull from Sprint1 successful"
    time.sleep(10)
    print "Script fully executed ... exiting"
    c.exec_command("""(crontab -l ; echo "*/5 * * * * python '/home/testtest/sprint1/execute.py' '%s'")| crontab -'"""%prefix) 
    c.close()
    
deploy('/Users/siavashmortezavi/data/comp/deeplearningkey/smortezavi.pem','ec2-54-218-42-161.us-west-2.compute.amazonaws.com','anchor')

