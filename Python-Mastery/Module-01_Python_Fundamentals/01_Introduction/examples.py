"""
Lesson 01: Python Introduction & CPython Execution Architecture
================================================================
This file contains executable Python code demonstrating runtime environment 
inspection, CPython bytecode compilation, code objects, and disassembly.

Execute this script using:
    python examples.py
"""

import dis
import platform
import sys


def Section_1_Interpreter_Environment_Inspection() -> None:
    """
    Demonstrates programmatic inspection of the CPython runtime environment.
    Python exposes interpreter internals through the `sys` and `platform` modules.
    """
    print("=" * 70)
    print(" SECTION 1: INTERPRETER & SYSTEM ENVIRONMENT INSPECTION")
    print("=" * 70)

    # 1. Python Version Information
    # sys.version returns a detailed string of Python version and compiler build flags.
    print(f"[+] Python Version      : {sys.version}")
    print(f"[+] Python Version Info : {sys.version_info}")
    
    # 2. CPython Implementation Check
    # platform.python_implementation() returns 'CPython', 'PyPy', 'Jython', etc.
    print(f"[+] Implementation      : {platform.python_implementation()}")
    print(f"[+] CPython Compiler    : {platform.python_compiler()}")

    # 3. Interpreter Executable Path
    # sys.executable shows the absolute path to the binary running this process.
    print(f"[+] Executable Location : {sys.executable}")

    # 4. Byte Order & Platform Architecture
    # Byte order indicates endianness (little endian on x86/ARM systems).
    print(f"[+] System Byte Order   : {sys.byteorder}")
    print(f"[+] Platform OS         : {platform.system()} ({platform.machine()})")
    print()

    # Expected Output Overview:
    # Shows running Python version (3.11+), CPython build info, OS architecture, etc.


def Section_2_Exploring_Code_Objects() -> None:
    """
    Demonstrates inspecting a compiled Python function's Code Object (PyCodeObject).
    CPython compiles functions into code objects containing raw bytecode, constants, 
    variable names, and stack depth specifications before execution.
    """
    print("=" * 70)
    print(" SECTION 2: CODE OBJECT (`PyCodeObject`) INSPECTION")
    print("=" * 70)

    def calculate_total(price: float, tax_rate: float) -> float:
        """Calculate total price including tax."""
        discount = 5.0
        final_price = (price - discount) * (1.0 + tax_rate)
        return final_price

    # Retrieve the code object attached to the function via `__code__` attribute
    code_obj = calculate_total.__code__

    print(f"[+] Function Name       : {calculate_total.__name__}")
    print(f"[+] Code Object Type    : {type(code_obj)}")
    
    # co_code: Raw sequence of bytecode instructions (bytes)
    print(f"[+] Raw Bytecode Bytes  : {code_obj.co_code}")

    # co_consts: Tuple containing literal constants used in the function
    # Note: Includes docstring at index 0 and float literals (5.0, 1.0)
    print(f"[+] Constants (co_consts): {code_obj.co_consts}")

    # co_varnames: Tuple containing names of local variables (including arguments)
    print(f"[+] Local Variables     : {code_obj.co_varnames}")

    # co_argcount: Number of positional arguments expected
    print(f"[+] Argument Count      : {code_obj.co_argcount}")

    # co_stacksize: Max stack depth required by PVM to evaluate this function
    print(f"[+] Max Stack Depth     : {code_obj.co_stacksize}")
    print()


def Section_3_Disassembling_Bytecode_With_Dis() -> None:
    """
    Demonstrates using the built-in `dis` disassembler module to disassemble 
    Python code into human-readable PVM bytecode instructions.
    """
    print("=" * 70)
    print(" SECTION 3: DISASSEMBLING BYTECODE WITH `dis.dis()`")
    print("=" * 70)

    def multiply_and_add(x: int, y: int) -> int:
        z = x * y
        result = z + 100
        return result

    print("Source Function Code:")
    print("    def multiply_and_add(x, y):")
    print("        z = x * y")
    print("        result = z + 100")
    print("        return result\n")

    print("Disassembled Bytecode Opcodes:")
    print("-" * 50)
    
    # dis.dis() prints the disassembled opcodes to standard stdout.
    dis.dis(multiply_and_add)
    
    print("-" * 50)
    print("Instruction Breakdown:")
    print(" 1. LOAD_FAST 0 (x)   -> Pushes argument 'x' onto stack.")
    print(" 2. LOAD_FAST 1 (y)   -> Pushes argument 'y' onto stack.")
    print(" 3. BINARY_MULTIPLY   -> Pops top 2 items, multiplies, pushes product.")
    print(" 4. STORE_FAST 2 (z)  -> Pops product and assigns to local variable 'z'.")
    print(" 5. LOAD_FAST 2 (z)   -> Pushes 'z' onto stack.")
    print(" 6. LOAD_CONST        -> Pushes constant integer 100 onto stack.")
    print(" 7. BINARY_ADD        -> Pops top 2 items, adds them, pushes sum.")
    print(" 8. STORE_FAST 3      -> Pops sum and stores in 'result'.")
    print(" 9. RETURN_VALUE      -> Returns top of stack to caller.\n")


def Section_4_Global_VS_Local_Variable_Bytecode_Performance() -> None:
    """
    Demonstrates the bytecode difference between accessing global variables 
    versus local variables.
    
    Why functions run faster than global script code:
    - Local variables use LOAD_FAST (fast array indexed lookup in C array).
    - Global variables use LOAD_GLOBAL (slower hash-map dict lookup in globals()).
    """
    print("=" * 70)
    print(" SECTION 4: GLOBAL VS LOCAL VARIABLE LOOKUP BYTECODE DIFFERENCE")
    print("=" * 70)

    # Function using local variable
    def local_lookup() -> int:
        val = 42
        return val

    # Function using global variable
    def global_lookup() -> int:
        return GLOBAL_VAL

    print("[1] Bytecode for Local Variable Access (`LOAD_FAST`):")
    dis.dis(local_lookup)
    print()

    print("[2] Bytecode for Global Variable Access (`LOAD_GLOBAL`):")
    dis.dis(global_lookup)
    print()


# Global variable used by Section 4
GLOBAL_VAL = 42


if __name__ == "__main__":
    print("\nPYTHON MASTERY: LESSON 01 - EXECUTABLE EXAMPLES\n")
    Section_1_Interpreter_Environment_Inspection()
    Section_2_Exploring_Code_Objects()
    Section_3_Disassembling_Bytecode_With_Dis()
    Section_4_Global_VS_Local_Variable_Bytecode_Performance()
    print("=" * 70)
    print(" EXAMPLES COMPLETE - ALL DEMONSTRATIONS EXECUTED SUCCESSFULLY")
    print("=" * 70)
