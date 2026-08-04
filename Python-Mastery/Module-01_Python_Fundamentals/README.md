# Module 01: Python Fundamentals

> **Build an Unshakable Foundation in Python Syntax, CPython Execution Mechanics, and Memory References.**

---

## 📌 Module Overview

Welcome to **Module 01: Python Fundamentals**. This module opens the hood of the Python programming language to reveal how source code transitions from human-readable text into bytecode, how the CPython Virtual Machine executes instructions, and how Python handles variables, dynamic typing, and memory references.

Rather than treating Python as a simple scripting wrapper, this module establishes a deep engineering mental model of CPython primitives, memory addresses (`id()`), name binding mechanics, and PEP 8 standards.

---

## 🎯 Module Objectives

By completing Module 01, you will:
1. Understand the internal execution pipeline: Source Code -> Lexing/Parsing -> AST -> Bytecode Compilation -> CPython PVM Execution.
2. Master object references, reference counting, and CPython `PyObject` internal header structures.
3. Differentiate between static binding, dynamic typing, and rebinding vs in-place mutation.
4. Apply PEP 8 naming standards, identifier scoping, and clean docstring conventions across all codebases.
5. Navigate Python primitive and non-primitive type hierarchies with confidence.

---

## 🔑 Module Prerequisites

- No prior Python experience required!
- A working installation of Python 3.11+ and VS Code.
- basic terminal / command-line familiarity.

---

## ⏱️ Estimated Completion Time

- **Total Module Duration**: 6 - 8 Hours (including exercises and code experimentation)

---

## 🗺️ Lesson Checklist

- [x] **[01_Introduction](./01_Introduction/README.md)**: CPython Architecture, Source Code Execution, Bytecode, PVM & GIL Overview
- [x] **[02_Variables_and_Memory](./02_Variables_and_Memory/README.md)**: Object References, Reference Counting, CPython `PyObject` Layout & `id()`
- [ ] **[03_Variable_Assignment_Dynamic_Typing](./03_Variable_Assignment_Dynamic_Typing/README.md)**: Binding Mechanics, Rebinding vs Mutation, Duck Typing
- [ ] **[04_Naming_Rules_and_PEP8](./04_Naming_Rules_and_PEP8/README.md)**: PEP 8 Naming Standards, Identifiers, Keywords & Scope Rules
- [ ] **[05_Data_Types_Overview](./05_Data_Types_Overview/README.md)**: Type Hierarchy, Primitive vs Non-Primitive Types, Type Conversions

---

## 💡 How to Approach This Module

1. Go into `01_Introduction/` and read `README.md` first.
2. Study `notes.md` carefully—pay attention to the memory diagrams and CPython architecture notes.
3. Run `examples.py` (`python3 examples.py`) and inspect the disassembler bytecode outputs.
4. Work through `practice.py` to observe dynamic behaviors.
5. Solve the graded problems in `exercises.py`.
6. Verify your solutions against `solutions.py`.
7. Move on to Lesson 02!
