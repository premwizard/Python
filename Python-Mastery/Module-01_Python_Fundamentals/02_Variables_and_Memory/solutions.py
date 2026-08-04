"""
Lesson 02: Variables & Memory References in CPython
====================================================
Reference Solutions & Verification Suite.

Execute this script to verify solutions:
    python solutions.py
"""

import sys
from typing import Any, Dict, List, Set, Tuple


# ==============================================================================
# LEVEL 1: EASY - SOLUTIONS
# ==============================================================================

def get_hex_address(obj: Any) -> str:
    """
    Solution 1.1 (Easy):
    Uses `hex(id(obj))` to obtain hexadecimal memory address representation.
    """
    return hex(id(obj))


def is_same_object(a: Any, b: Any) -> bool:
    """
    Solution 1.2 (Easy):
    Uses the identity operator `is` (equivalent to `id(a) == id(b)`).
    """
    return a is b


# ==============================================================================
# LEVEL 2: MEDIUM - SOLUTIONS
# ==============================================================================

def get_adjusted_ref_count(obj: Any) -> int:
    """
    Solution 2.1 (Medium):
    Calculates net reference count in caller scope by subtracting 2 from `sys.getrefcount(obj)`.
    Offset breakdown:
    - 1 for `sys.getrefcount` parameter.
    - 1 for `get_adjusted_ref_count` wrapper parameter.
    """
    return sys.getrefcount(obj) - 2


# ==============================================================================
# LEVEL 3: HARD - SOLUTIONS
# ==============================================================================

def find_cached_integers_in_range(start: int, stop: int) -> List[int]:
    """
    Solution 3.1 (Hard):
    Iterates through [start, stop] inclusive, dynamically converting each number 
    from string to int twice (`int(str(i))`) to avoid compiler constant pooling, 
    and returns numbers where `v1 is v2` is True.
    """
    cached_nums = []
    for num in range(start, stop + 1):
        val1 = int(str(num))
        val2 = int(str(num))
        if val1 is val2:
            cached_nums.append(num)
    return cached_nums


# ==============================================================================
# LEVEL 4: CHALLENGE - SOLUTIONS
# ==============================================================================

def group_variables_by_memory_address(variables: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Solution 4.1 (Challenge):
    Groups variable names by their object's hexadecimal RAM address `hex(id(obj))`.
    """
    grouped: Dict[str, List[str]] = {}
    
    for var_name, obj in variables.items():
        addr = hex(id(obj))
        if addr not in grouped:
            grouped[addr] = []
        grouped[addr].append(var_name)

    return grouped


# ==============================================================================
# AUTOMATED VERIFICATION SUITE
# ==============================================================================

def run_tests() -> None:
    print("=" * 70)
    print(" LESSON 02: EXERCISES VERIFICATION SUITE")
    print("=" * 70)

    # Test 1.1
    val = 100
    addr_str = get_hex_address(val)
    assert addr_str.startswith("0x"), "Test 1.1 Failed: Address must start with 0x"
    print("[OK] Solution 1.1 (get_hex_address) Passed!")

    # Test 1.2
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    lst3 = lst1
    assert is_same_object(lst1, lst3) is True, "Test 1.2 Failed: Aliases must share identity"
    assert is_same_object(lst1, lst2) is False, "Test 1.2 Failed: Separate lists must not share identity"
    print("[OK] Solution 1.2 (is_same_object) Passed!")

    # Test 2.1
    test_obj = {"a": 1}
    count = get_adjusted_ref_count(test_obj)
    assert count == 1, f"Test 2.1 Failed: Expected caller refcount 1, got {count}"
    
    alias_ref = test_obj
    count_aliased = get_adjusted_ref_count(test_obj)
    assert count_aliased == 2, f"Test 2.1 Failed: Expected aliased refcount 2, got {count_aliased}"
    print("[OK] Solution 2.1 (get_adjusted_ref_count) Passed!")

    # Test 3.1
    cached = find_cached_integers_in_range(-10, 10)
    expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert cached == expected, f"Test 3.1 Failed: Small int cache range mismatch. Got {cached}"
    print("[OK] Solution 3.1 (find_cached_integers_in_range) Passed!")

    # Test 4.1
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    groups = group_variables_by_memory_address({"x": x, "y": y, "z": z})
    assert len(groups) == 2, f"Test 4.1 Failed: Expected 2 distinct memory groups, got {len(groups)}"
    x_addr = hex(id(x))
    assert sorted(groups[x_addr]) == ["x", "y"], "Test 4.1 Failed: Aliased variables not grouped"
    print("[OK] Solution 4.1 (group_variables_by_memory_address) Passed!")

    print("\n" + "=" * 70)
    print(" ALL LESSON 02 EXERCISES VERIFIED SUCCESSFULLY! (100% PASS)")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
