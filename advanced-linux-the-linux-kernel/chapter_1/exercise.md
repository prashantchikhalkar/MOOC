Linux Kernel Fundamentals: Chapter 1, Surveying the Linux Kernel

1. What kernel version is your Linux system running?
-> uname -r
4.4.0-111-generic

2. What is the size of the kernel file that corresponds to the kernel your system is running?
-> du -h /boot/vmlinuz-4.4.0-111-generic
6.7M    /boot/vmlinuz-4.4.0-111-generic

3. How much RAM is available to your running kernel? Note: It may or may not be the amount of 
physical RAM on your system.
-> cat /proc/meminfo | grep MemTotal
MemTotal:       16336352 kB

4. The command strace will display the system calls that a process makes as it runs. Using the man 
command, determine what option for strace will show a summary, with a count, of the number of 
times a process called each system call. Using that option, what system call is called the most by the 
command date?
-> strace -c date
Thu Oct  3 04:14:42 IST 2019
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         3           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0         4           open
  0.00    0.000000           0         6           close
  0.00    0.000000           0         6           fstat
  0.00    0.000000           0         1           lseek
  0.00    0.000000           0         9           mmap
  0.00    0.000000           0         4           mprotect
  0.00    0.000000           0         3           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         3         3 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           arch_prctl
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                    45         3 total

5. Can you determine, using strace, what system call is used to change the directory? 
-> strace cd /tmp

6. Run a sleep 100 with & (to put it in the background). What files does its process have open?
-> /$ sleep 100 &
[1] 27667
/$ jobs
[1]+  Running                 sleep 100 &
/$ cd /proc/27667/fd
/proc/27667/fd$ ll
total 0
dr-xr-xr-x 9 pchikhal users  0 Oct  3 05:10 ..
dr-x------ 2 pchikhal users  0 Oct  3 05:10 .
lrwx------ 1 pchikhal users 64 Oct  3 05:10 2 -> /dev/pts/2
lrwx------ 1 pchikhal users 64 Oct  3 05:10 1 -> /dev/pts/2
lrwx------ 1 pchikhal users 64 Oct  3 05:10 0 -> /dev/pts/2
:/proc/27667/fd$ tty
/dev/pts/2
/proc/27667/fd$

7. Does your system have a PCI Ethernet device? 
-> lspci | grep -i ethernet
00:19.0 Ethernet controller: Intel Corporation Ethernet Connection I218-LM (rev 04)

8. Is the kernel variable ip_forward (under /proc/sys/…) set to 1 or 0 on your system?
-> sudo find . -name ip_forward
[sudo] password for pchikhal:
./sys/net/ipv4/ip_forward
$ cat ./sys/net/ipv4/ip_forward
0

9. According to /sys/block, do you have a block device (disk) sda? If so, do you have device files for 
partitions of sda? How many? Using strace, does the command fdisk -l (run it as root), open any 
files under /sys/dev/block?
-> sudo strace fdisk -l |& grep -i /proc/
open("/proc/partitions", O_RDONLY)      = 3
/sys/block/sda$ cat /proc/partitions
major minor  #blocks  name

   8        0  250059096 sda
   8        1  233377792 sda1
   8        2          1 sda2
   8        5   16678912 sda5

10. Using dmesg and grep, do you see the kernel reporting the kernel command line? If not, can you 
determine if the boot messages from the kernel were lost? Does your system have a log file that 
recorded the boot messages? You can grep for BOOT_IMAGE under /var/log to look.
-> dmesg | grep -i 'COMMAND LINE'
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-111-generic root=UUID=b30b901d-a5b0-4abc-bc0c-b4c81c23f6e3 ro quiet splash vt.handoff=7
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-111-generic root=UUID=b30b901d-a5b0-4abc-bc0c-b4c81c23f6e3 ro quiet splash vt.handoff=7

11. What other device files are character devices and share the same major number with /dev/null?
-> ll /dev/null
crw-rw-rw- 1 root root 1, 3 Sep 17 00:36 /dev/null

ll /dev/ | grep ^c | grep " 1,"
crw-rw-rw-   1 root root      1,   8 Sep 17 00:36 random
crw-r-----   1 root kmem      1,   4 Sep 17 00:36 port
crw-rw-rw-   1 root root      1,   3 Sep 17 00:36 null
crw-r-----   1 root kmem      1,   1 Sep 17 00:36 mem
crw-r--r--   1 root root      1,  11 Sep 17 00:36 kmsg
crw-rw-rw-   1 root root      1,   7 Sep 17 00:36 full
crw-rw-rw-   1 root root      1,   5 Sep 17 00:36 zero
crw-rw-rw-   1 root root      1,   9 Sep 17 00:36 urandom


12. What other device files are character devices and share the same major number with /dev/null?
-> "
