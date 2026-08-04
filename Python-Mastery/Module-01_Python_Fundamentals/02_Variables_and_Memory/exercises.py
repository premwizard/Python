"""
Lesson 02: Variables & Memory References in CPython
====================================================
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

from typing import Any, Dict, List, Set, Tuple


# ==============================================================================
# LEVEL 1: EASY
# ==============================================================================

def get_hex_address(obj: Any) -> str:
    """
    Exercise 1.1 (Easy):
    Return the memory address of `obj` formatted as a hexadecimal string 
    prefixed with '0x'.

    Args:
        obj: Any Python object.

    Returns:
        str: Hexadecimal memory address representation (e.g., '0x7f9a102040').

    Example:
        >>> obj = 42
        >>> get_hex_address(obj).startswith("0x")
        True
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


def is_same_object(a: Any, b: Any) -> bool:
    """
    Exercise 1.2 (Easy):
    Return `True` if objects `a` and `b` reference the exact same memory address, 
    otherwise return `False`.

    Args:
        a: First Python object.
        b: Second Python object.

    Returns:
        bool: True if `a is b`, False otherwise.
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 2: MEDIUM
# ==============================================================================

def get_adjusted_ref_count(obj: Any) -> int:
    """
    Exercise 2.1 (Medium):
    Return the exact reference count of `obj` by removing the temporary 
    reference overhead added by `sys.getrefcount()`.

    Args:
        obj: Any Python object.

    Returns:
        int: Net reference count pointing to `obj`.
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 3: HARD
# ==============================================================================

def find_cached_integers_in_range(start: int, stop: int) -> List[int]:
    """
    Exercise 3.1 (Hard):
    Given a range [start, stop] inclusive, test every integer by dynamically 
    constructing two separate integer objects (`int(str(num))`) and checking if 
    they share memory identity (`is`). 

    Return a list of all integer values in the range that are cached by CPython.

    Args:
        start (int): Starting integer bound.
        stop (int): Ending integer bound (inclusive).

    Returns:
        List[int]: List of cached integer values.

    Example:
        >>> find_cached_integers_in_range(-10, 5)
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


# ==============================================================================
# LEVEL 4: CHALLENGE
# ==============================================================================

def group_variables_by_memory_address(variables: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Exercise 4.1 (Challenge):
    Given a dictionary mapping variable names (strings) to Python objects, 
    group variable names together if they share the exact same memory address (`id()`).

    Returns a dictionary mapping the hexadecimal memory address (string) 
    to a list of variable names (List[str]) referencing that memory address.

    Args:
        variables (Dict[str, Any]): Mapping of variable names to objects.

    Returns:
        Dict[str, List[str]]: Grouped dictionary where keys are hex memory addresses.

    Example:
        >>> x = [1, 2]
        >>> y = x
        >>> z = [1, 2]
        >>> result = group_variables_by_memory_address({"x": x, "y": y, "z": z})
        >>> len(result)
        2
    """
    # TODO: Implement this function
    raise NotImplementedError("Student implementation required.")


if __name__ == "__main__":
    print("=" * 70)
    print(" LESSON 02: GRADED EXERCISES")
    print(" Solve the exercises above and test solutions in solutions.py")
    print("=" * 70)
