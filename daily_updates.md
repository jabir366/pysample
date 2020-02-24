#Daily Updates

==========  Mon Dec  2 10:29:11 IST 2019 ========== 
* closing a GNU screen split    C-z Q
* clearing top of git stash 
     `git stash drop `
     `git stash drop stash@{n}`
* clearing all stashed items
     git stash clear
* bind a pci device to a driver 
 ` /opt/trex-core-2.61/scripts$ sudo ./dpdk_nic_bind.py -b ixgbe 05:00.0 05:00.1`
* identify ports of a pci device  
  `/opt/trex-core-2.61/scripts$ sudo ./dpdk_setup_ports.py -s`

==========  Wed Dec  4 15:07:51 IST 2019 ========== 
* adding acl via vpp_api_test  
   `acl_add_replace -1 ipv4 permit src 192.168.255.1/32`  
   `acl_interface_set_acl_list sw_if_index 1 input 0 output`
* insert a line from another line in vim
  :nt. where n is the line numer

==========  Mon Dec  9 20:49:43 IST 2019 ========== 
* create a tracking branch of remote branch in git   
   `git checkout -t -b <loacl branchname> <remote branchname>`
 
========== Mon Dec 16 18:37:40 IST 2019 ==========

* in case ssh-add shows error    
          eval `ssh-agent -s`

========== Fri Dec 20 12:13:26 IST 2019 ========== 
* mount a drive in rw mode  
             `sudo mkdir /mnt/newmedia`
             `sudo mount /dev/sdb1 /mnt/newmedia -rw`  

========== Sat Dec 21 15:02:23 IST 2019 ========== 

* to see a python dict log in json format in bash  
            `echo "{'name': 'GigabitEthernet3/0/0', 'fname': None}"|tr \' \" | sed 's/None/null/g' |jq . `

========== Wed Jan 15 12:30:05 IST 2020 ========== 
* tmux set vim keybindings in copy mode
            `set-window-option -g mode-keys vi`
* copying a text in tmux
     if we are in vim mode , enter copy mode and press space
     else enter Control-space to select text
     press enter to copy
     to paste press C-b 

========== Mon Feb  3 12:19:59 IST 2020 ========== 
* taking pcaps in VPP
	vpp# pcap tx trace status
	vpp# pcap tx trace on max 35 intfc GigabitEthernet0/8/0 file vppTest.pcap
	vpp# vppctl pcap tx trace off


========== Tue Feb  4 17:23:37 IST 2020 ========== 
* reducing escape delay in vim inside tmux
      add this line in .tmux.conf 
		set -s escape-time 0

