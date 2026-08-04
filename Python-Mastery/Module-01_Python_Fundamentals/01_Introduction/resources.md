# Lesson 01: Further Reading & Curated Resources

> **Curated books, official documentation, articles, and video lectures to deepen your understanding of CPython execution architecture.**

---

## 📖 Official Python Documentation

- **[Python Execution Model](https://docs.python.org/3/reference/executionmodel.html)**  
  Official reference manual covering structure of a program, naming and binding, and exception handling.
- **[Disassembler for Python Bytecode (`dis`)](https://docs.python.org/3/library/dis.html)**  
  Complete opcode documentation and API details for inspecting CPython bytecodes.
- **[Python Data Model](https://docs.python.org/3/reference/datamodel.html)**  
  Defines objects, values, types, code objects (`PyCodeObject`), and frame objects (`PyFrameObject`).
- **[Python `sys` Module](https://docs.python.org/3/library/sys.html)**  
  Access interpreter variables and system interactions.

---

## 📚 Recommended Books

1. **CPython Internals** — *Anthony Shaw* (Real Python Publishing)  
   *The definitive guide to CPython 3 source code architecture, lexer, parser, compiler, and evaluation loop.*
2. **Fluent Python (2nd Edition)** — *Luciano Ramalho* (O'Reilly Media)  
   *Chapter 1 & Chapter 22: In-depth exploration of Python data structures and metaprogramming internals.*
3. **High Performance Python (2nd Edition)** — *Micha Gorelick & Ian Ozsvald* (O'Reilly Media)  
   *Under-the-hood analysis of Python execution overhead, bytecode profiling, and memory allocation.*

---

## 🎥 Video Lectures & Talks

- **[Inside the CPython Interpreter](https://www.youtube.com/watch?v=HVUTjQzESeo)** — *Larry Hastings (PyCon)*  
  A legendary walk-through of `ceval.c`, the PVM evaluation stack, and opcode execution.
- **[Understanding Python Bytecode](https://www.youtube.com/watch?v=cSSpnq392lU)** — *James Powell*  
  Deep dive into standard library disassembly, frame object manipulation, and bytecode injection.
- **[The GIL and Its Effects on Python Multithreading](https://www.youtube.com/watch?v=Obt-vMVdM8s)** — *Real Python*  
  Visual demonstration of Global Interpreter Lock lock contention and thread switching mechanics.

---

## 📰 Articles & Deep Dives

- **[Your Guide to the CPython Source Code](https://realpython.com/cpython-source-code-guide/)** — *Real Python*
- **[Python Bytecode: What It Is and How to Use It](https://opensource.com/article/18/4/introduction-python-bytecode)** — *Opensource.com*
- **[Understanding Python ASTs](https://greentreesnakes.readthedocs.io/en/latest/)** — *Green Tree Snakes Documentation*

---

## 🧠 Interactive Practice Websites

- **[Python Compiler Explorer (Godbolt)](https://godbolt.org/)**: Select Python to view bytecode disassemblies side-by-side with source code.
- **[Python Tutor (Visualizer)](https://pythontutor.com/)**: Visualize execution step-by-step, stack frames, and object references in your browser.
