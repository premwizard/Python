"""
Lesson 01: Python Introduction & CPython Execution Architecture
================================================================
Graded Practice Exercises.

Instructions:
-------------
Implement the functions below according to their specifications.
Do NOT modify function signatures or docstrings.
Run this file or test your solutions against `solutions.py`.

Level 1: Easy
Level 2: Medium
Level 3: Hard
Level 4: Challenge
"""

from typing import Any, Dict, List, Tuple


# ==============================================================================
# LEVEL 1: EASY
# ==============================================================================

def extract_code_constants(func: Any) -> Tuple[Any, ...]:
    """
    Exercise 1.1 (Easy):
    Extract and return the tuple of literal constants (`co_consts`) from the 
    code object of the provided function `func`.

    Args:
        func: Any Python function object.

    Returns:
        Tuple[Any, ...]: The `co_consts` tuple from `func.__code__`.

    Example:
        >>> def test(): return 42
        >>> extract_code_constants(test)
        (None, 42)
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


def get_cpython_info() -> Dict[str, str]:
    """
    Exercise 1.2 (Easy):
    Return a dictionary containing the following CPython environment details:
    - "implementation": Python implementation name (e.g. 'CPython')
    - "version_major": Major version number as a string (e.g. '3')
    - "version_minor": Minor version number as a string (e.g. '11')
    - "byte_order": System byte order (e.g. 'little' or 'big')

    Returns:
        Dict[str, str]: Dictionary of system metadata keys and values.
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 2: MEDIUM
# ==============================================================================

def count_opcodes_by_name(func: Any, opcode_name: str) -> int:
    """
    Exercise 2.1 (Medium):
    Given a Python function `func` and an opcode instruction name (e.g., 'LOAD_FAST' 
    or 'LOAD_CONST'), use the `dis.get_instructions()` generator to count how 
    many times that specific opcode appears in `func`'s compiled bytecode instructions.

    Args:
        func: The target function to disassemble.
        opcode_name: The string name of the opcode to count.

    Returns:
        int: The total count of matching opcode instructions.

    Example:
        >>> def add(a, b): return a + b
        >>> count_opcodes_by_name(add, 'LOAD_FAST')
        2
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 3: HARD
# ==============================================================================

def analyze_function_complexity(func: Any) -> Dict[str, Any]:
    """
    Exercise 3.1 (Hard):
    Analyze the compiled bytecode of a given function and return a dictionary 
    containing bytecode metrics:
    - "total_instructions": Total number of bytecode instructions (int).
    - "unique_opcodes": Sorted list of unique opcode names present (List[str]).
    - "max_stack_depth": Maximum evaluation stack depth (`co_stacksize`) (int).
    - "local_variable_count": Total number of local variables (`co_nlocals`) (int).

    Args:
        func: The function object to analyze.

    Returns:
        Dict[str, Any]: Analysis summary dictionary.
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 4: CHALLENGE
# ==============================================================================

def compare_bytecode_instruction_counts(func1: Any, func2: Any) -> Dict[str, Any]:
    """
    Exercise 4.1 (Challenge):
    Compare two functions `func1` and `func2` to determine which one compiles 
    to FEWER bytecode instructions.

    Returns a dictionary:
    - "func1_count": Instruction count for func1 (int).
    - "func2_count": Instruction count for func2 (int).
    - "more_efficient": Name of the function (`__name__`) with FEWER instructions. 
                       If equal, return "EQUAL".

    Args:
        func1: First target function.
        func2: Second target function.

    Returns:
        Dict[str, Any]: Comparison results dictionary.
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


if __name__ == "__main__":
    print("=" * 70)
    print(" LESSON 01: GRADED EXERCISES")
    print(" Solve the exercises above and test solutions in solutions.py")
    print("=" * 70)
