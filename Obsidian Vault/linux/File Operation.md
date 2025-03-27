to open a file : open(path, flag(read,write,create ...),mode    #include <[fcntl.h](https://pubs.opengroup.org/onlinepubs/007904875/basedefs/fcntl.h.html)>

<sys/stat.h>
>O_RDONLY : Open for reading only.

>O_WRONLY : Open for writing only.

>O_RDWR : Open for reading and writing. The result is undefined if this flag is applied to a FIFO.

>O_APPEND : to write to the end of file
>O_TRUNC : to truncate the opened file, if it previously existed. Data written
to the file descriptor will replace previous contents of the file.
>O_CREAT to create a new file. If the filename that you provide to open
does not exist, a new file will be created, provided that the directory containing
it exists and that the process has permission to create files in that directory. If the
file already exists, it is opened instead.
O_EXCL with O_CREAT to force creation of a new file. If the file already
exists, the open call will fail.

include <sys/types.h>
//mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH;


>int read(int fileDescriptor, void *buffer, size_t bytesToRead)
>It can be accessed by using the `unistd.h` library provided by C.
>**`buffer`****:** This pointer points to a buffer where data that is read will bestored.
>**`bytesToRead`****:** Here, we provide an unsigned integer variable that specifies the maximum number of bytes we want to read from the file.
>To avoid buffer overflow, the max value of the `bytesToRead` variable should not exceed the size of the `buffer` variable.


>int write(int fileDescriptor, void *buffer, size_t bytesToWrite)
>by the `unistd.h` library in C
>`bytesToWrite`: Here, we provide an unsigned integer variable that specifies the maximum number of bytes we want to write from the buffer to the file.


>Moving around a file
>A file descriptor remembers its position in a file. As you read from or write to the file
descriptor, its position advances corresponding to the number of bytes you read or
write. Sometimes, however, you’ll need to move around a file without reading or writ-
ing data.The lseek call enables you to reposition a file descriptor in a file.

1. If the third argument is SEEK_SET, lseek interprets the second argument as a
	position, in bytes, from the start of the file.
2. If the third argument is SEEK_CUR, lseek interprets the second argument as an
	offset, which may be positive or negative, from the current position.
3. If the third argument is SEEK_END, lseek interprets the second argument as an
	offset from the end of the file. A positive value indicates a position beyond the
	end of the file.

>off_t position = lseek (file_descriptor, 0, SEEK_CUR)
