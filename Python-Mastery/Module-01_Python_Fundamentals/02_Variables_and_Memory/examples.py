"""
Lesson 02: Variables & Memory References in CPython
====================================================
Executable examples demonstrating Python object references, memory addresses, 
identity vs equality, small integer caching, and reference counts.

Execute this script using:
    python examples.py
"""

import sys


def Section_1_Memory_Addresses_And_Variables() -> None:
    """
    Demonstrates that variables are pointers/name tags to objects in heap memory.
    The built-in id() function returns the memory address of the object.
    """
    print("=" * 70)
    print(" SECTION 1: MEMORY ADDRESSES & VARIABLE NAME BINDING")
    print("=" * 70)

    # 1. Create an integer object in heap RAM
    x = 1000
    print(f"[+] Value of x            : {x}")
    print(f"[+] Memory Address (id)   : {id(x)}")
    print(f"[+] Hexadecimal Address   : {hex(id(x))}")

    # 2. Assigning y = x does NOT copy the value! It copies the POINTER address.
    y = x
    print(f"\n[+] Value of y (after y=x): {y}")
    print(f"[+] Memory Address of y   : {id(y)}")
    print(f"[+] Do x and y share RAM? : {id(x) == id(y)}")  # True

    # 3. Rebinding x to a new integer creates a NEW object at a NEW address
    x = 2000
    print(f"\n[+] Value of x (rebound)  : {x}")
    print(f"[+] New Address of x      : {id(x)}")
    print(f"[+] Value of y (unchanged): {y}")
    print(f"[+] Address of y          : {id(y)}")
    print(f"[+] Do x and y share RAM? : {id(x) == id(y)}")  # False
    print()


def Section_2_Identity_VS_Equality() -> None:
    """
    Demonstrates the fundamental distinction between:
    - Identity (`is`): Checks if two variables point to the exact same RAM address.
    - Equality (`==`): Checks if two variables point to objects with equal values.
    """
    print("=" * 70)
    print(" SECTION 2: OBJECT IDENTITY (`is`) VS VALUE EQUALITY (`==`)")
    print("=" * 70)

    # Create two separate list objects with identical contents
    list1 = [10, 20, 30]
    list2 = [10, 20, 30]
    list3 = list1  # Alias pointing to list1

    print(f"list1 Address: {hex(id(list1))} -> Contents: {list1}")
    print(f"list2 Address: {hex(id(list2))} -> Contents: {list2}")
    print(f"list3 Address: {hex(id(list3))} -> Contents: {list3}\n")

    # Value Equality Comparison (==)
    print(f"[+] list1 == list2 : {list1 == list2}")  # True (Same elements)
    print(f"[+] list1 == list3 : {list1 == list3}")  # True (Same elements)

    # Memory Identity Comparison (is)
    print(f"[+] list1 is list2 : {list1 is list2}")  # False (Different RAM objects)
    print(f"[+] list1 is list3 : {list1 is list3}")  # True  (Same RAM object)
    print()


def Section_3_Small_Integer_Caching() -> None:
    """
    Demonstrates CPython's Small Integer Cache optimization.
    CPython pre-allocates singleton integer objects for numbers -5 through 256.
    
    Note: Dynamic creation (int("500")) avoids module-level constant pooling.
    """
    print("=" * 70)
    print(" SECTION 3: CPYTHON SMALL INTEGER CACHING (-5 TO 256)")
    print("=" * 70)

    # Dynamic creation within cached range [-5, 256]
    small_a = int("100")
    small_b = int("100")
    print(f"small_a = int('100'), small_b = int('100')")
    print(f"  id(small_a) : {id(small_a)}")
    print(f"  id(small_b) : {id(small_b)}")
    print(f"  small_a is small_b : {small_a is small_b}")  # True (Small int singleton!)

    # Dynamic creation outside cached range
    large_a = int("500")
    large_b = int("500")
    print(f"\nlarge_a = int('500'), large_b = int('500')")
    print(f"  id(large_a) : {id(large_a)}")
    print(f"  id(large_b) : {id(large_b)}")
    print(f"  large_a is large_b : {large_a is large_b}")  # False (Distinct objects!)
    print()


def Section_4_Reference_Counting_Inspection() -> None:
    """
    Demonstrates inspecting an object's ob_refcnt using sys.getrefcount().
    Note: sys.getrefcount(obj) temporarily adds +1 to the count!
    """
    print("=" * 70)
    print(" SECTION 4: REFERENCE COUNTING (`sys.getrefcount`)")
    print("=" * 70)

    # Create a fresh object
    target_object = [1, 2, 3, 4, 5]
    print(f"[+] Initial Reference Count : {sys.getrefcount(target_object) - 1}")

    # Create second reference (alias)
    ref2 = target_object
    print(f"[+] After ref2 = target     : {sys.getrefcount(target_object) - 1}")

    # Create third reference in a list
    ref3_list = [target_object]
    print(f"[+] After adding to list    : {sys.getrefcount(target_object) - 1}")

    # Delete second reference
    del ref2
    print(f"[+] After del ref2          : {sys.getrefcount(target_object) - 1}")
    print()


def Section_5_Pointer_Aliasing_And_Mutation() -> None:
    """
    Demonstrates how pointer aliasing affects mutable objects versus immutable ones.
    Modifying a mutable object via one reference affects all alias references!
    """
    print("=" * 70)
    print(" SECTION 5: POINTER ALIASING & MUTABLE OBJECT MODIFICATION")
    print("=" * 70)

    # Mutable Object (List) Aliasing
    original_list = ["apple", "banana"]
    aliased_list = original_list

    print(f"Before Mutation:")
    print(f"  original_list: {original_list}")
    print(f"  aliased_list : {aliased_list}")

    # Mutate the list in-place
    aliased_list.append("cherry")

    print(f"\nAfter aliased_list.append('cherry'):")
    print(f"  original_list: {original_list}")  # Notice original is mutated too!
    print(f"  aliased_list : {aliased_list}")
    print(f"  Do they share identity? {original_list is aliased_list}")
    print()


if __name__ == "__main__":
    print("\nPYTHON MASTERY: LESSON 02 - EXECUTABLE EXAMPLES\n")
    Section_1_Memory_Addresses_And_Variables()
    Section_2_Identity_VS_Equality()
    Section_3_Small_Integer_Caching()
    Section_4_Reference_Counting_Inspection()
    Section_5_Pointer_Aliasing_And_Mutation()
    print("=" * 70)
    print(" EXAMPLES COMPLETE - ALL DEMONSTRATIONS EXECUTED SUCCESSFULLY")
    print("=" * 70)
