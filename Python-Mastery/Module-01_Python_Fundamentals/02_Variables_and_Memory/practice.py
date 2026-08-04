"""
Lesson 02: Variables & Memory References in CPython
====================================================
Interactive Practice & Hands-On Experiments Laboratory.

Run this script directly:
    python practice.py

Follow the instructions in each section, uncomment/modify values, and observe 
how memory addresses, identity comparisons, and reference counts respond.
"""

import sys


def Experiment_1_Small_Integer_Cache_Boundary_Explorer() -> None:
    """
    EXPERIMENT 1: SMALL INTEGER CACHE BOUNDARY TESTER
    
    Task for Learner:
    1. Test integer values around the boundary limits of CPython's cache: -5 and 256.
    2. Change `test_val` to -6, -5, 0, 256, 257 and observe if `var1 is var2` returns True!
    """
    print("\n--- EXPERIMENT 1: SMALL INTEGER CACHE BOUNDARY TESTER ---")

    # LEARNER TASK: Change test_val to different numbers (-6, -5, 100, 256, 257)
    test_values = [-6, -5, 256, 257]

    for val in test_values:
        v1 = int(str(val))
        v2 = int(str(val))
        is_cached = v1 is v2
        print(f"Testing Value {val:4d} | v1 is v2: {str(is_cached):5s} | Address v1: {id(v1)} | Address v2: {id(v2)}")


def Experiment_2_Reference_Counter_Tracker() -> None:
    """
    EXPERIMENT 2: TRACKING REFERENCE COUNT LIFECYCLES
    
    Task for Learner:
    Observe how `sys.getrefcount()` increments when variables reference an object,
    and decrements when references are reassigned or deleted.
    """
    print("\n--- EXPERIMENT 2: REFERENCE COUNT LIFECYCLE TRACKER ---")

    # Step 1: Create a dictionary object
    my_data = {"key": "value"}
    
    def get_actual_refcount(obj):
        # Subtract 1 for sys.getrefcount's temporary parameter reference
        return sys.getrefcount(obj) - 1

    print(f"1. Base object created              | Ref Count: {get_actual_refcount(my_data)}")

    # Step 2: Bind two alias variables
    ref_a = my_data
    ref_b = my_data
    print(f"2. Bound ref_a and ref_b            | Ref Count: {get_actual_refcount(my_data)}")

    # Step 3: Put into a list container
    container = [my_data, my_data]
    print(f"3. Placed twice into list container | Ref Count: {get_actual_refcount(my_data)}")

    # Step 4: Clear list container
    container.clear()
    print(f"4. Cleared list container           | Ref Count: {get_actual_refcount(my_data)}")

    # Step 5: Delete references
    del ref_a
    del ref_b
    print(f"5. Deleted ref_a and ref_b          | Ref Count: {get_actual_refcount(my_data)}")


def Experiment_3_Immutable_VS_Mutable_Empty_Singletons() -> None:
    """
    EXPERIMENT 3: EMPTY CONTAINER SINGLETONS (TUPLE VS LIST VS DICT)
    
    Task for Learner:
    1. Observe whether empty tuples `()`, empty lists `[]`, and empty dicts `{}` 
       reuse memory singleton instances!
    """
    print("\n--- EXPERIMENT 3: EMPTY CONTAINER SINGLETON COMPARISON ---")

    t1, t2 = (), ()
    l1, l2 = [], []
    d1, d2 = {}, {}

    print(f"Empty Tuples ()  -> t1 is t2: {t1 is t2} (Tuples are immutable -> Singleton cached!)")
    print(f"Empty Lists []   -> l1 is l2: {l1 is l2} (Lists are mutable   -> Separate RAM allocations)")
    print(f"Empty Dicts {{}}   -> d1 is d2: {d1 is d2} (Dicts are mutable   -> Separate RAM allocations)")


if __name__ == "__main__":
    print("=" * 70)
    print(" LESSON 02: HANDS-ON LAB EXPERIMENTS")
    print("=" * 70)
    Experiment_1_Small_Integer_Cache_Boundary_Explorer()
    Experiment_2_Reference_Counter_Tracker()
    Experiment_3_Immutable_VS_Mutable_Empty_Singletons()
    print("\n" + "=" * 70)
    print(" LAB EXPERIMENTS COMPLETE - TRY MODIFYING VALUES IN PRACTICE.PY!")
    print("=" * 70)
