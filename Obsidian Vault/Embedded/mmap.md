header ile : #include <sys/mman.h>

void * mmap (void*address, size_t length, int protect, int flags, int filedes,  off_t offset);


### **address**:
This argument gives a preferred starting address for the mapping. If another mapping does not exist there, then the kernel will pick a nearby page boundary and create the mapping; otherwise, the kernel picks a new address. If this argument is NULL, then the kernel can place the mapping anywhere it sees fit.

### **length:**
This is the number of bytes which to be mapped.

### protect:
This argument is used to control what kind of access is permitted. This argument may be logical ‘OR’ of the following flags **_PROT_READ | PROT_WRITE | PROT_EXEC | PROT_NONE._**  The access types of read, write and execute are the permissions on the content.

### flags:
This argument is used to control the nature of the map.
- **_MAP_SHARED:_** This flag is used to share the mapping with all other processes, which are mapped to this object. Changes made to the mapping region will be written back to the file.
- **_MAP_PRIVATE:_** When this flag is used, the mapping will not be seen by any other processes, and the changes made will not be written to the file.
- **_MAP_ANONYMOUS / MAP_ANON:_** This flag is used to create an anonymous mapping. Anonymous mapping means the mapping is not connected to any files. This mapping is used as the basic primitive to extend the heap.
- **_MAP_FIXED:_** When this flag is used, the system has to be forced to use the exact mapping address specified in the _address_ If this is not possible, then the mapping will be failed.

### filedes:
This is the file descriptor

### offset:
This is offset from where the file mapping started. In simple terms, the mapping connects to **_(offset)_** to **_(offset+length-1)_** bytes for the file open on **_filedes_** descriptor.
![[Pasted image 20240418132407.png]]
