//each process has a unique process ID(pid).

//PIDs are 16-bit numbers.

// Every process has a parent process (except the ""init"" process)

//process on a linux system as arranged(organize somthing) in a tree, with the init process at its root

//The parent process ID, or ppid, is simply the process ID of the process's parent.

  

//process ID in C or C++ program, always use the pid_t typedef (<sys/types.h>)

//getpid() -> to obtain the pid

//getppid() -> to obtain the pid of the parent process


**Viewing Active Processes**

>The **ps** command displays the processes that are running on your system.
>
>-e option instructs ps to display all processes running on the system.
>
 -o pid,ppid,command option tells ps what information to show about each process
>
>p pidlist
              Select by process ID.  Identical to -p and --pid.

       -p pidlist
              Select by PID.  This selects the processes whose process ID
              numbers appear in pidlist.  Identical to p and --pid.

       --pid pidlist
              Select by process ID.  Identical to -p and p.

       --ppid pidlist
              Select by parent process ID.  This selects the processes with a
              parent process ID in pidlist.  That is, it selects processes
              that are children of those listed in pidlist.


**Killing a Process**

>kill a running process with the kill command.
>The kill command works by sending the process a SIGTERM, or termination,signal.


**Fork and exec**

>fork, that makes a child process that is an exact copy of its parent process.
>When a program calls fork, a duplicate process, called the child process, is created.The parent process continues executing the program from the point that fork was called. The child process, too, executes the same program from the same place.
>
>The return value in the child process is zero.



 