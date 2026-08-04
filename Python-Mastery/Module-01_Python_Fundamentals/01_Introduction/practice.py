"""
Lesson 01: Python Introduction & CPython Execution Architecture
================================================================
Interactive Practice & Hands-On Experiments Laboratory.

Run this script directly:
    python practice.py

Follow the instructions in each section, uncomment/modify values, and observe 
how CPython opcode execution and code object structures respond.
"""

import dis
import timeit

# Global variable for Experiment 2 benchmark
GLOBAL_COUNTER = 0


def Experiment_1_Code_Object_Mutation_Observation() -> None:
    """
    EXPERIMENT 1: CONSTANT FOLDING & CODE OBJECT CONSTANTS
    
    Task for Learner:
    1. Look at function `get_seconds_per_day()` below.
    2. Run this script and observe `co_consts`.
    3. Notice how CPython automatically folds `24 * 60 * 60` into a single constant `86400` during compilation!
       This compiler optimization is called CONSTANT FOLDING.
    """
    print("\n--- EXPERIMENT 1: CONSTANT FOLDING IN CPYTHON ---")

    def get_seconds_per_day() -> int:
        # CPython evaluates literal expression 24 * 60 * 60 at compile time into 86400
        return 24 * 60 * 60

    print("Function Source: return 24 * 60 * 60")
    print(f"Compiled Constants (`co_consts`): {get_seconds_per_day.__code__.co_consts}")
    
    print("\nDisassembled Bytecode:")
    dis.dis(get_seconds_per_day)


def Experiment_2_Local_Vs_Global_Scope_Speed_Benchmark() -> None:
    """
    EXPERIMENT 2: BENCHMARKING LOCAL VS GLOBAL VARIABLE ACCESS
    
    Task for Learner:
    1. Observe the two benchmark functions below.
    2. `run_global_benchmark()` performs 1,000,000 iterations modifying a global variable.
    3. `run_local_benchmark()` performs 1,000,000 iterations inside local function scope.
    4. Run the script and compare execution times!
    """
    print("\n--- EXPERIMENT 2: SCOPE PERFORMANCE BENCHMARK ---")

    def run_global_benchmark():
        global GLOBAL_COUNTER
        for _ in range(1_000_000):
            GLOBAL_COUNTER += 1

    def run_local_benchmark():
        local_counter = 0
        for _ in range(1_000_000):
            local_counter += 1

    time_global = timeit.timeit(run_global_benchmark, number=5)
    time_local = timeit.timeit(run_local_benchmark, number=5)

    print(f"[+] Global Scope Lookup Time (5 runs x 1M iter) : {time_global:.4f} seconds")
    print(f"[+] Local Scope Lookup Time  (5 runs x 1M iter) : {time_local:.4f} seconds")
    
    speedup = ((time_global - time_local) / time_global) * 100
    print(f"[>] Local Variable Access is ~{speedup:.2f}% faster due to LOAD_FAST / STORE_FAST opcodes!")


def Experiment_3_Custom_Opcode_Inspector() -> None:
    """
    EXPERIMENT 3: INSPECTING OPCODES FOR CUSTOM EXPRESSIONS
    
    Task for Learner:
    Try editing `sample_expression` below to test different Python expressions 
    (e.g., ternary operators, string formatting, arithmetic) 
    and observe how CPython translates them into stack instructions.
    """
    print("\n--- EXPERIMENT 3: CUSTOM OPCODE INSPECTOR ---")

    def sample_expression(a: int, b: int) -> bool:
        # LEARNER TASK: Modify this expression and re-run!
        # Try: return a if a > b else b
        # Try: return f"Sum is {a + b}"
        return (a > 10) and (b < 20)

    print("Inspecting bytecode for function: `sample_expression`")
    dis.dis(sample_expression)


if __name__ == "__main__":
    print("=" * 70)
    print(" LESSON 01: HANDS-ON LAB EXPERIMENTS")
    print("=" * 70)
    Experiment_1_Code_Object_Mutation_Observation()
    Experiment_2_Local_Vs_Global_Scope_Speed_Benchmark()
    Experiment_3_Custom_Opcode_Inspector()
    print("\n" + "=" * 70)
    print(" LAB EXPERIMENTS COMPLETE - TRY EDITING VALUES IN PRACTICE.PY!")
    print("=" * 70)
