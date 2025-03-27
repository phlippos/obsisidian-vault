(secure copy) command in Linux system is used to copy file(s) between servers in a secure way.The SCP command or secure copy allows the secure transferring of files between the local host and the remote host or between two remote hosts. It uses the same authentication and security as it is used in the [Secure Shell (SSH) protocol](https://www.geeksforgeeks.org/introduction-to-sshsecure-shell-keys/). SCP is known for its simplicity, security, and pre-installed availability.

scp [options] from to


| Options | Description                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------ |
| -P      | ****port:**** Specifies the port to connect on the remote host.                                  |
| -p      | Preserves modification times, access times, and modes from the original file.                    |
| -q      | Disables the progress meter.                                                                     |
| -r      | Recursively copy entire directories.                                                             |
| -s      | Name of program to use for the encrypted connection. The program must understand ssh(1) options. |
|         |                                                                                                  |
