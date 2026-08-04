"""
Lesson 01: Python Introduction & CPython Execution Architecture
================================================================
Reference Solutions & Verification Suite.

Execute this script to verify solutions:
    python solutions.py
"""

import dis
import platform
import sys
from typing import Any, Dict, List, Tuple


# ==============================================================================
# LEVEL 1: EASY - SOLUTIONS
# ==============================================================================

def extract_code_constants(func: Any) -> Tuple[Any, ...]:
    """
    Solution 1.1 (Easy):
    Extracts `co_consts` tuple directly from `func.__code__`.
    """
    if not hasattr(func, "__code__"):
        raise TypeError("Object provided does not possess a `__code__` attribute.")
    return func.__code__.co_consts


def get_cpython_info() -> Dict[str, str]:
    """
    Solution 1.2 (Easy):
    Queries `sys` and `platform` modules for runtime CPython environment info.
    """
    return {
        "implementation": platform.python_implementation(),
        "version_major": str(sys.version_info.major),
        "version_minor": str(sys.version_info.minor),
        "byte_order": sys.byteorder,
    }


# ==============================================================================
# LEVEL 2: MEDIUM - SOLUTIONS
# ==============================================================================

def count_opcodes_by_name(func: Any, opcode_name: str) -> int:
    """
    Solution 2.1 (Medium):
    Uses `dis.get_instructions(func)` to iterate over instruction objects 
    and match `instr.opname` against `opcode_name`.
    """
    instructions = dis.get_instructions(func)
    count = 0
    for instr in instructions:
        if instr.opname == opcode_name:
            count += 1
    return count


# ==============================================================================
# LEVEL 3: HARD - SOLUTIONS
# ==============================================================================

def analyze_function_complexity(func: Any) -> Dict[str, Any]:
    """
    Solution 3.1 (Hard):
    Extracts bytecode instructions via `dis.get_instructions` and reads code object 
    metadata (`co_stacksize`, `co_nlocals`).
    """
    instructions = list(dis.get_instructions(func))
    total_instructions = len(instructions)
    unique_opcodes = sorted(list({instr.opname for instr in instructions}))
    
    code_obj = func.__code__
    max_stack_depth = code_obj.co_stacksize
    local_variable_count = code_obj.co_nlocals

    return {
        "total_instructions": total_instructions,
        "unique_opcodes": unique_opcodes,
        "max_stack_depth": max_stack_depth,
        "local_variable_count": local_variable_count,
    }


# ==============================================================================
# LEVEL 4: CHALLENGE - SOLUTIONS
# ==============================================================================

def compare_bytecode_instruction_counts(func1: Any, func2: Any) -> Dict[str, Any]:
    """
    Solution 4.1 (Challenge):
    Compares the total instruction length of two functions and determines 
    which compiles to fewer bytecode opcodes.
    """
    count1 = len(list(dis.get_instructions(func1)))
    count2 = len(list(dis.get_instructions(func2)))

    if count1 < count2:
        more_efficient = func1.__name__
    elif count2 < count1:
        more_efficient = func2.__name__
    else:
        more_efficient = "EQUAL"

    return {
        "func1_count": count1,
        "func2_count": count2,
        "more_efficient": more_efficient,
    }


# ==============================================================================
# AUTOMATED VERIFICATION SUITE
# ==============================================================================

def run_tests() -> None:
    print("=" * 70)
    print(" LESSON 01: EXERCISES VERIFICATION SUITE")
    print("=" * 70)

    # Test Sample Functions
    def sample_add(a: int, b: int) -> int:
        res = a + b
        return res

    def sample_fast_add(a: int, b: int) -> int:
        return a + b

    # Test 1.1
    consts = extract_code_constants(sample_add)
    assert isinstance(consts, tuple), "Test 1.1 Failed: Output must be a tuple"
    print("[OK] Solution 1.1 (extract_code_constants) Passed!")

    # Test 1.2
    info = get_cpython_info()
    assert info["implementation"] == "CPython", "Test 1.2 Failed: Implementation mismatch"
    assert "version_major" in info and "version_minor" in info
    print("[OK] Solution 1.2 (get_cpython_info) Passed!")

    # Test 2.1
    load_fast_count = count_opcodes_by_name(sample_add, "LOAD_FAST")
    assert load_fast_count >= 2, "Test 2.1 Failed: LOAD_FAST count mismatch"
    print("[OK] Solution 2.1 (count_opcodes_by_name) Passed!")

    # Test 3.1
    metrics = analyze_function_complexity(sample_add)
    assert "total_instructions" in metrics and "unique_opcodes" in metrics
    assert metrics["local_variable_count"] >= 3  # a, b, res
    print("[OK] Solution 3.1 (analyze_function_complexity) Passed!")

    # Test 4.1
    comp = compare_bytecode_instruction_counts(sample_fast_add, sample_add)
    assert comp["func1_count"] < comp["func2_count"]
    assert comp["more_efficient"] == "sample_fast_add"
    print("[OK] Solution 4.1 (compare_bytecode_instruction_counts) Passed!")

    print("\n" + "=" * 70)
    print(" ALL LESSON 01 EXERCISES VERIFIED SUCCESSFULLY! (100% PASS)")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
