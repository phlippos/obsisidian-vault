In C++, `std::shared_ptr` and `std::make_shared` are part of the Standard Library and are used for memory management, particularly for shared ownership of dynamically allocated objects. Here’s an overview of both concepts, their usage, and advantages.

**Definition**: `std::shared_ptr` is a smart pointer that retains shared ownership of an object through a pointer. Multiple `shared_ptr` instances can manage the same object, and the object will be destroyed when the last `shared_ptr` managing it is destroyed or reset.


**Reference Counting**: `shared_ptr` uses reference counting to keep track of how many `shared_ptr`s are pointing to the same object. When a new `shared_ptr` is created that points to the same object, the reference count is incremented. When a `shared_ptr` is destroyed, the reference count is decremented. When the reference count reaches zero, the managed object is deleted.

**Usage**: It is useful in scenarios where you need to share ownership of an object among multiple parts of your program without worrying about memory leaks.

```cpp
#include <iostream>
#include <memory> // For std::shared_ptr

class MyClass {
public:
    MyClass() { std::cout << "MyClass constructor\n"; }
    ~MyClass() { std::cout << "MyClass destructor\n"; }
    void display() { std::cout << "Hello from MyClass\n"; }
};

int main() {
    std::shared_ptr<MyClass> ptr1 = std::make_shared<MyClass>(); // Create a shared_ptr
    {
        std::shared_ptr<MyClass> ptr2 = ptr1; // Share ownership
        ptr2->display();
        std::cout << "Reference count: " << ptr1.use_count() << std::endl; // Output: 2
    } // ptr2 goes out of scope, but the object is not deleted yet

    std::cout << "Reference count after ptr2 goes out of scope: " << ptr1.use_count() << std::endl; // Output: 1
    ptr1->display(); // Still valid
    return 0;
}


```


### `std::make_shared`
**Definition**: `std::make_shared` is a function that allocates memory for an object and returns a `std::shared_ptr` pointing to it. It combines the allocation of the object and the `shared_ptr` into a single allocation, which can improve performance and memory usage.

**Advantages**:

- **Performance**: It performs a single allocation for both the control block (which holds the reference count) and the object itself, reducing overhead compared to creating a `shared_ptr` with `new`.
- **Safety**: It prevents the possibility of memory leaks that can occur if you allocate memory using `new` but forget to wrap it in a `shared_ptr`.