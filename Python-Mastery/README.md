# 🐍 Python Mastery Workspace

> **A Comprehensive, University-Grade Interactive Python Curriculum & Long-Term Reference**  
> *From CPython Architecture & Fundamentals to Production Engineering, AsyncIO, Metaprogramming & System Design.*

---

## 📌 Project Overview

Welcome to the **Python Mastery Workspace**. This repository is engineered to serve as a complete, self-contained, interactive Python learning system and lifetime reference. Whether you are revising core concepts before top-tier engineering interviews, building production web/AI systems, or diving deep into CPython internals, this workspace provides executable code, textbook-depth documentation, hands-on practice labs, and graded exercise sets.

Every lesson in this workspace is **independent**, **fully executable**, **PEP 8 compliant**, and structured to take you from foundational understanding to deep advanced mastery.

---

## 🎯 Learning Philosophy

1. **No Magic Allowed**: Never settle for knowing *how* to write code—understand *why* it works and *how* Python executes it internally at the CPython memory level.
2. **Executable First**: Code cannot be learned by reading passive text. Every concept features runnable code (`examples.py`), interactive lab experiments (`practice.py`), and graded problem sets (`exercises.py`).
3. **Strict Pythonic Standards**: Adhere strictly to **PEP 8**, type annotations, clean docstrings, and clean modular code design from Day 1.
4. **Zero Blind Spots**: Complete coverage of edge cases, performance trade-offs, security implications, and real-world production engineering practices.

---

## 🗺️ Master Curriculum Roadmap & Progress Tracker

**Overall Course Completion**: `[ 2 / 50 Lessons Complete ]` (4%)

```
[████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 4% Completed
```

### Module 01: Python Fundamentals `[ 2 / 5 ]`
- [x] **01_Introduction**: CPython Architecture, Source Code Execution, Bytecode, PVM & GIL Overview
- [x] **02_Variables_and_Memory**: Object References, Reference Counting, CPython `PyObject` Layout & `id()`
- [ ] **03_Variable_Assignment_Dynamic_Typing**: Binding Mechanics, Rebinding vs Mutation, Duck Typing
- [ ] **04_Naming_Rules_and_PEP8**: PEP 8 Naming Standards, Identifiers, Keywords & Scope Rules
- [ ] **05_Data_Types_Overview**: Type Hierarchy, Primitive vs Non-Primitive Types, Type Conversions

---

### Module 02: Control Flow & Logical Execution `[ 0 / 5 ]`
- [ ] **01_Conditional_Statements**: `if-elif-else` Execution Trees & Short-Circuit Evaluation
- [ ] **02_Pattern_Matching**: Structural Pattern Matching (`match-case`), Guards & Destructuring
- [ ] **03_Loops_and_Iteration**: `for` and `while` Loops, `break`, `continue`, `else` Clause Mechanics
- [ ] **04_Iterators_and_Protocols**: `__iter__` and `__next__`, `iter()` and `next()` Internal Protocols
- [ ] **05_Control_Flow_Mini_Project**: Command-Line Interactive Calculator & Logical Workflow Engine

---

### Module 03: Functions & Modular Software Design `[ 0 / 5 ]`
- [ ] **01_Function_Basics**: Function Definitions, Execution Frames, Call Stack & Return Values
- [ ] **02_Parameters_and_Arguments**: Positional, Keyword, `*args`, `**kwargs`, Positional-Only (`/`) & Keyword-Only (`*`)
- [ ] **03_Scope_and_LEGB**: Local, Enclosing, Global, Built-in Scopes, `global` and `nonlocal` Keywords
- [ ] **04_First_Class_Functions_Closures**: Higher-Order Functions, Function Attributes, Lexical Closures & Cell Objects
- [ ] **05_Modules_and_Packages**: `import` System, `sys.path`, `__init__.py`, Namespace Packages & Circular Imports

---

### Module 04: Data Structures In-Depth `[ 0 / 5 ]`
- [ ] **01_Strings_and_Formatting**: Immutable Strings, PyASCII Object Layout, String Interning, `f-strings` & Formatting
- [ ] **02_Lists_Dynamic_Arrays**: CPython List Implementation, Dynamic Resizing Amortized Complexity, Slicing Operations
- [ ] **03_Tuples_Immutability**: Memory Layout, Tuple Optimizations, Namedtuples & Unpacking
- [ ] **04_Dictionaries_Hash_Tables**: CPython Open-Addressing Compact Dictionaries, Hash Collisions, Key Immutability
- [ ] **05_Sets_Collections**: Set Hash Tables, Mathematical Operations, `collections` (`deque`, `Counter`, `defaultdict`)

---

### Module 05: Object-Oriented Programming (OOP) `[ 0 / 5 ]`
- [ ] **01_Classes_and_Objects**: Type vs Instance, `__init__`, `self` Reference, Instance Attributes
- [ ] **02_Class_and_Static_Methods**: `@classmethod`, `@staticmethod`, Class Attributes vs Instance Attributes
- [ ] **03_Encapsulation_Properties**: Access Modifiers, Name Mangling (`__var`), `@property` Getters/Setters
- [ ] **04_Inheritance_and_MRO**: Single/Multiple Inheritance, C3 Linearization Algorithm, `super()` Mechanics
- [ ] **05_Dunder_Methods_Polymorphism**: Operator Overloading (`__str__`, `__repr__`, `__eq__`, `__add__`), Abstract Base Classes (`abc`)

---

### Module 06: Advanced Python Mechanics `[ 0 / 5 ]`
- [ ] **01_Decorators_Metaprogramming**: Function & Class Decorators, `@wraps`, Parameterized Decorators, `__call__`
- [ ] **02_Generators_Coroutines**: Generator Expressions, `yield` vs `yield from`, Memory Efficiency, Coroutine Foundations
- [ ] **03_Context_Managers**: `with` Statement, `__enter__` / `__exit__` Protocol, `@contextmanager` Utility
- [ ] **04_Descriptors_Properties**: Descriptor Protocol (`__get__`, `__set__`, `__delete__`), Data vs Non-Data Descriptors
- [ ] **05_Dataclasses_Enums**: `@dataclass`, Immutability (`frozen`), `field()` Customization, `Enum` & `IntEnum`

---

### Module 07: File Systems, Networking & Databases `[ 0 / 5 ]`
- [ ] **01_File_IO_Streams**: Context-Safe File Handling, Binary vs Text Streams, Encodings (UTF-8) & Buffer Management
- [ ] **02_Data_Serialization**: JSON, CSV, Struct Protocol, `pickle` Security Risks & Best Practices
- [ ] **03_Socket_Networking**: TCP/UDP Sockets, Client-Server Architectures, Non-blocking I/O
- [ ] **04_Database_Integration**: SQLite3 Interface, Parameterized Queries (SQL Injection Prevention), Connection Pools
- [ ] **05_ORM_Fundamentals**: SQLAlchemy Core/ORM Models, Schema Migrations & Transaction Management

---

### Module 08: Testing, Debugging & Performance Optimization `[ 0 / 5 ]`
- [ ] **01_Unit_Testing**: `unittest` Framework, `pytest`, Assertions, Test Fixtures, Mocking & Patching
- [ ] **02_Debugging_Techniques**: `pdb`, `breakpoint()`, Stack Trace Inspection, Logging (`logging` module)
- [ ] **03_Profiling_Memory**: `cProfile`, `pstats`, `tracemalloc`, Memory Leak Detection & Object Tracking
- [ ] **04_Benchmarking_Optimization**: `timeit` Module, Algorithmic Complexity Optimization, `__slots__` Usage
- [ ] **05_Static_Analysis**: Type Checking with `mypy`, Linting with `flake8`/`ruff`, Code Formatting with `black`

---

### Module 09: Modern Python Ecosystem & Concurrency `[ 0 / 5 ]`
- [ ] **01_Virtual_Environments**: `venv`, Dependency Isolation, `pip`, `pip-tools`, `poetry` & Project Packaging
- [ ] **02_Multithreading**: `threading` Module, GIL Limitations, I/O-Bound Parallelism, Thread Pools (`ThreadPoolExecutor`)
- [ ] **03_Multiprocessing**: `multiprocessing` Module, CPU-Bound Parallelism, Process Pools, IPC (Queues, Pipes, Shared Memory)
- [ ] **04_Asyncio_Event_Loop**: `async`/`await`, Event Loop Mechanics, Coroutines, Tasks, Futures, `aiohttp` Basics
- [ ] **05_Dockerization_Deployment**: Dockerfiles for Python Apps, Multi-stage Builds, Microservice Containerization

---

### Module 10: Capstone Projects & Technical Interview Mastery `[ 0 / 5 ]`
- [ ] **01_Project_Expense_Tracker**: CLI-Based Modular Financial Management System
- [ ] **02_Project_REST_API**: Fast-API Microservice with Pydantic Validation & SQLite Database
- [ ] **03_Project_RAG_System**: Local AI Document Q&A Pipeline (Vector Storage + LLM Integration)
- [ ] **04_Python_Algorithmic_Patterns**: Two Pointers, Sliding Window, Graph Traversals, Dynamic Programming in Pythonic Idioms
- [ ] **05_Interview_Mastery**: 100 Systemic Python Interview Questions, Edge Cases & CPython Tricks

---

## 🛠️ Workspace Folder & Lesson Architecture

Each lesson folder maintains a uniform, robust 7-file structure:

```
Lesson-Folder/
├── README.md        --> Lesson meta, objectives, prerequisites, estimated time, learning outcomes.
├── notes.md         --> Textbook-grade theory, CPython internals, memory diagrams, Pythonic vs non-Pythonic code.
├── examples.py      --> Executable code with exhaustive inline comments explaining WHAT, WHY, and HOW.
├── practice.py      --> Hands-on lab environment with step-by-step experimentation tasks.
├── exercises.py     --> Graded practice problems (Easy, Medium, Hard, Challenge) without solutions.
├── solutions.py     --> Production-grade, Pythonic solutions with detailed explanations.
└── resources.md     --> Curated official documentation, books, videos, and articles for further learning.
```

---

## 🚀 How to Use This Workspace

1. **Clone / Open Workspace**: Open the `Python-Mastery/` folder in VS Code.
2. **Follow Module Sequence**: Begin with `Module-01_Python_Fundamentals` and proceed sequentially.
3. **Read `README.md` & `notes.md`**: Understand the theoretical foundations and internal mechanics.
4. **Execute `examples.py`**: Run `python3 examples.py` in your terminal to see live execution and inspect outputs.
5. **Experiment in `practice.py`**: Complete the guided coding experiments.
6. **Solve `exercises.py`**: Attempt the problem set independently before looking at `solutions.py`.
7. **Verify via `solutions.py`**: Compare your implementation with the Pythonic reference solution.

---

## 📋 System Requirements & Environment Setup

- **Python Version**: Python 3.11+ (Python 3.12+ recommended)
- **Recommended VS Code Extensions**:
  - `ms-python.python` (Official Python Extension)
  - `ms-python.vscode-pylance` (Pylance Language Server & Type Checking)
  - `charliermarsh.ruff` (Ultra-fast Python Linter)
  - `bierner.markdown-preview-github-styles` (GitHub Markdown Preview)

### Useful VS Code Shortcuts
- **Run Python File**: `Ctrl + F5` (Windows/Linux) or `Cmd + Shift + F5` (Mac)
- **Toggle Terminal**: `Ctrl + ~`
- **Markdown Preview**: `Ctrl + K, V`
- **Format Code (Black/Ruff)**: `Shift + Alt + F`

---

## 📝 Git Commit Conventions

When adding or updating lessons, adhere to Conventional Commits:

- `feat(m01-l01): complete lesson 01 introduction & execution flow`
- `feat(m01-l02): complete lesson 02 variables and memory references`
- `docs(m02-l03): add notes and diagrams for python iteration protocol`
- `test(m08-l01): add pytest fixtures practice exercise`
- `refactor(m05-l04): optimize MRO demonstration in examples.py`

---

## 📚 Recommended Master Resources

- **Official Documentation**: [Python 3 Documentation](https://docs.python.org/3/)
- **CPython Internals**: *Python In-Depth* / *CPython Internals* by Anthony Shaw
- **Advanced Python Reference**: *Fluent Python (2nd Edition)* by Luciano Ramalho
- **Python Design Patterns**: *Architecture Patterns with Python* by Harry Percival & Bob Gregory

---

*Maintained with ❤️ for ambitious Python Engineers & Software Architects.*
