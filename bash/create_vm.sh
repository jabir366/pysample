#!/bin/sh

# ./create_vm.sh test_2019-09-19-1 Ubuntu_64 4024 20240 /tmp/preseed-ubuntu-18.04.2-server-amd64.iso
# VBoxManage startvm vm1 -type headless
# VBoxManage unregistervm vm1 --delete


VM_NAME=$1
OS_TYPE=$2
MEMORY_SIZE=$3
HDD_SIZE=$4
VRDEPORT=$5
DVD_PATH=$6

HDD_PATH=.VirtualBox/Machines/$VM_NAME/$VM_NAME.vdi


VBoxManage createvm -name $VM_NAME -ostype $OS_TYPE --register
VBoxManage modifyvm $VM_NAME \
    --memory $MEMORY_SIZE \
    --cpus 4 \
    --vram 12 \
    --ioapic on \
    --boot1 dvd --boot2 disk \
    --usb off \
    --usbehci off \
    --usbxhci off \
    --pae off \
    --nic1 intnet --intnet1 "lan" \
    --nic2 intnet --intnet2 "wan0" \
    --nic3 intnet --intnet2 "wan1" \
    --nic4 intnet --intnet2 "wan2" \
    --nic5 intnet --intnet2 "wan3" \
    --nic6 nat \
    --natpf1 "guestssh,tcp,,2222,,22"

VBoxManage modifyvm $VM_NAME \
    --vrde on \
#    --vrdeauthtype external \
#    --vrdeaddress 0.0.0.0 \
#    --vrdeproperty "Security/Method=negotiate"
#    --vrdeport $VRDEPORT



VBoxManage createvdi --filename $HDD_PATH --size $HDD_SIZE

VBoxManage storagectl $VM_NAME --name "IDE Controller" --add ide
VBoxManage storagectl $VM_NAME --name "SATA Controller" --add sata

VBoxManage storageattach $VM_NAME --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium $DVD_PATH
VBoxManage storageattach $VM_NAME --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $HDD_PATH

VBoxManage startvm  $VM_NAME --type headless

