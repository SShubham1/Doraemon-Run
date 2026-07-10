
# Doraemon Run: Score Injection Writeup (Python/Pygame)

I decided to try and hack one of my old Pygame projects that I made during class 9. My goal was to manipulate the live game score in memory.

## 1. The Cheat Engine Failure

First, I tried to use **Cheat Engine** but got `0` addresses when I tried to scan based on score changes.

![Cheat Engine Scanning Failure](cheat_engine.png)

**The Reason:** Unlike C/C++, Python doesn't use fixed memory pointers to change the value of a variable. Instead, when a variable's value changes, Python creates an entirely new object in memory and points the variable label to it. The garbage collector then cleans up the old address. This makes traditional memory scanners like Cheat Engine practically useless for interpreted Python games.

---

## 2. The GDB Exploitation

Since Python (CPython) itself is written in C, I decided to use the native Linux debugger (`gdb`) to hook directly into the Python interpreter's C-API and inject my payload.

### Step 2.1: Finding the Process
First, I located the Process ID (PID) of the running game.

```bash
┌──(venv)─(shubham㉿kali)-[~/Documents/Doraemon-Run]
└─$ ps -aux | grep Doraemon                                                                 
shubham   243382  56.3  1.4 702648 109968 pts/3    Sl+  23:28   0:02 python3 Doraemon Run.py
shubham   243651   0.0  0.0   6560  2488 pts/4    S+   23:29   0:00 grep --color=auto Doraemon

```

### Step 2.2: Attaching and Injecting via GDB

I attached GDB to the target PID `243382`. To avoid crashing the game with a `SIGSEGV` (Segmentation Fault), I had to properly manage the **GIL (Global Interpreter Lock)** before injecting arbitrary Python code.

```gdb
┌──(venv)─(shubham㉿kali)-[~/Documents/Doraemon-Run]
└─$ sudo gdb -p 243382  
GNU gdb (Debian 17.2-1+b1) 17.2
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
Attaching to process 243382
[New LWP 243397]
[New LWP 243396]
[New LWP 243393]
[New LWP 243392]
[New LWP 243387]
[New LWP 243386]
[New LWP 243385]
[New LWP 243383]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007f5629584ffe in ?? () from /usr/lib/x86_64-linux-gnu/libc.so.6

# 1. Acquire the Global Interpreter Lock (GIL) to freeze Python's state safely
(gdb) call (int)PyGILState_Ensure()
$1 = 1

# 2. Inject the custom payload using CPython's API
(gdb) call (void)PyRun_SimpleString("import sys; sys.modules['__main__'].score += 999999")

# 3. Release the GIL using the return value from step 1
(gdb) call (void)PyGILState_Release($1)

# 4. Detach from the process and resume the game
(gdb) detach 
Detaching from program: /usr/bin/python3.13, process 243382
[Inferior 1 (process 243382) detached]
(gdb) quit

```

---

## 3. The Result

Looks like our score injection was completely successful! The game resumed perfectly without crashing, and the memory state was manipulated exactly as intended.
