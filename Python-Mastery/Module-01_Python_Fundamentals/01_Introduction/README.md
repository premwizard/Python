# Lesson 01: Python Introduction & CPython Execution Architecture

> **Understand what happens under the hood when Python executes your code—from source code parsing to CPython bytecode compilation, PVM execution, and the Global Interpreter Lock (GIL).**

---

## 📌 Lesson Overview

Many developers treat Python as a simple black box: you write `.py` text, press run, and magic happens. In this lesson, we demystify Python's execution model. We explore the CPython interpreter reference implementation, trace the multi-stage transformation from source code into an Abstract Syntax Tree (AST), disassemble code into CPython bytecode, and inspect Python Virtual Machine (PVM) stack execution.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
1. Explain the architectural difference between Compiled vs. Interpreted languages and where CPython fits.
2. Trace the step-by-step lifecycle of Python execution: Source Code -> Lexing & Parsing -> AST -> Bytecode (`.pyc`) -> PVM Execution.
3. Use Python's built-in `dis` module to disassemble Python functions into bytecode instructions.
4. Understand CPython's stack-based Virtual Machine and thread safety via the Global Interpreter Lock (GIL).
5. Inspect interpreter configuration, platform details, and bytecode versions programmatically using `sys` and `platform`.

---

## 🔑 Prerequisites

- Basic command-line terminal operations (`cd`, `python` / `python3`).
- VS Code installed with the Python extension.

---

## ⏱️ Estimated Time

- **Theory (`notes.md`)**: 25 Minutes
- **Examples (`examples.py`)**: 15 Minutes
- **Practice & Experiments (`practice.py`)**: 20 Minutes
- **Exercises & Verification (`exercises.py` & `solutions.py`)**: 30 Minutes
- **Total**: ~90 Minutes

---

## 🧠 Concepts Covered

- **CPython Reference Implementation**: C-based core runtime vs PyPy, Jython, IronPython.
- **Source Code Parsing**: Lexing (tokenization), parsing, and Abstract Syntax Tree (AST) construction.
- **Bytecode & Memory Representation**: `.pyc` files, `__pycache__`, and code objects (`co_code`, `co_consts`, `co_names`).
- **Python Virtual Machine (PVM)**: Stack-based evaluation loop (`ceval.c`).
- **Global Interpreter Lock (GIL)**: What it is, why it exists in CPython, and its impact on multi-threading vs multi-processing.

---

## 🌍 Real-World Engineering Usage

- **Performance Optimization**: Understanding bytecode helps engineers write faster, more efficient loops and avoid opcode overhead.
- **Debugging & Profiling**: Disassembling code allows low-level performance profiling and understanding bytecode-level bottlenecks.
- **Security & Obfuscation**: Reverse-engineering `.pyc` bytecode files and analyzing Python security vulnerabilities.
- **System Architecture**: Making informed architectural decisions when choosing between multi-threading (I/O-bound) vs multi-processing (CPU-bound) due to GIL constraints.

---

## ✅ Learning Outcomes

After completing this lesson, you will be able to speak confidently in technical interviews about Python execution, inspect opcode streams using `dis.dis()`, and write code with full awareness of how CPython handles instruction execution.
