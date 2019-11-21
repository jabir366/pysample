#!/bin/bash
TS=`date "+%s"`

set +x
create_vm() {
    VMNAME=$1_${TS}
    vboxmanage clonevm ubuntu1804_2019-11-12-1573546596 \
           --name ${VMNAME} \
           --register \
           --options link \
           --snapshot ubuntu_base_snapshot

    VBoxManage modifyvm ${VMNAME} --memory 4096 --vram 2 --cpus 2
    VBoxManage modifyvm ${VMNAME} --ioapic on
    VBoxManage modifyvm ${VMNAME} --boot1 disk --boot2 none --boot3 none --boot4 none
    VBoxManage modifyvm ${VMNAME} --cpus 2
    VBoxManage modifyvm ${VMNAME} --audio none
    VBoxManage modifyvm ${VMNAME} --usb off
    VBoxManage modifyvm ${VMNAME} --usbehci off
    VBoxManage modifyvm ${VMNAME} --usbxhci off
    VBoxManage modifyvm ${VMNAME} --nic1 bridged --bridgeadapter1 enp1s0f1
    VBoxManage modifyvm ${VMNAME} --nic2 intnet
    VBoxManage modifyvm ${VMNAME} --intnet2 $2
    VBoxManage modifyvm ${VMNAME} --nic3 intnet
    VBoxManage modifyvm ${VMNAME} --intnet3 $3
    VBoxManage modifyvm ${VMNAME} --nic4 intnet
    VBoxManage modifyvm ${VMNAME} --intnet4 $4
    VBoxManage modifyvm ${VMNAME} --nic5 intnet
    VBoxManage modifyvm ${VMNAME} --intnet5 $5
    VBoxManage modifyvm ${VMNAME} --nic6 intnet
    VBoxManage modifyvm ${VMNAME} --intnet5 $6
    VBoxManage modifyvm ${VMNAME} --nic7 intnet
    VBoxManage modifyvm ${VMNAME} --intnet5 $7
    VBoxManage modifyvm ${VMNAME} --vrde on --vrdeport $8
    # VBoxManage startvm  ${VMNAME} --type headless
}

create_vm tg tg_dut1_1 tg_dut1_2 tg_dut2_1 tg_dut2_2 tg_tg1 tg_tg1 5000
#create_vm dut1 tg_dut1_1 tg_dut1_2 dut1_dut2_1 dut1_dut2_2 5001
#create_vm dut2 tg_dut2_1 tg_dut2_2 dut1_dut2_1 dut1_dut2_2 5002

