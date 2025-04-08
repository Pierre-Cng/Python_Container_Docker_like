import os
import ctypes

# Constants for namespace flags
CLONE_NEWNS = 0x00020000
CLONE_NEWUTS = 0x04000000
CLONE_NEWPID = 0x20000000

# Function to check for errors in system calls
def check_result(result, func, args):
    if result == -1:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))

# Load libc and get the necessary functions
libc = ctypes.CDLL(None, use_errno=True)
libc.clone.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
libc.clone.restype = ctypes.c_int
libc.unshare.argtypes = (ctypes.c_int,)
libc.unshare.restype = ctypes.c_int
libc.sethostname.argtypes = (ctypes.c_char_p, ctypes.c_size_t)
libc.sethostname.restype = ctypes.c_int

def create_namespace(flags):
    stack = ctypes.c_ubyte(0x10000)  # Allocate a small stack for the new process
    stack_top = ctypes.cast(ctypes.byref(stack) + ctypes.sizeof(stack), ctypes.c_void_p)

    pid = libc.clone(None, stack_top, flags, None)
    check_result(pid, libc.clone, (None, stack_top, flags, None))

    return pid

def set_hostname(hostname):
    libc.sethostname(hostname.encode(), len(hostname))

if __name__ == "__main__":
    print("Original Hostname:", os.uname().nodename)

    # Create a new UTS (hostname) namespace
    create_namespace(CLONE_NEWUTS)

    # Set the hostname in the new namespace
    new_hostname = "my-new-hostname"
    set_hostname(new_hostname)

    print("New Hostname in Namespace:", os.uname().nodename)
