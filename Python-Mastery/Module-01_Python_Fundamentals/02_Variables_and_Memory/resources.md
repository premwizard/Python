# Lesson 02: Further Reading & Curated Resources

> **Curated books, official documentation, articles, and video lectures to deepen your understanding of CPython memory management, `PyObject` headers, and object references.**

---

## 📖 Official Python Documentation

- **[CPython C-API: Object Structures](https://docs.python.org/3/c-api/structures.html)**  
  Official reference for `PyObject`, `PyVarObject`, `ob_refcnt`, and `ob_type`.
- **[Python `gc` Module (Garbage Collector Interface)](https://docs.python.org/3/library/gc.html)**  
  Documentation for inspecting cyclic garbage collection tracks and generational thresholds.
- **[Built-in `id()` Function](https://docs.python.org/3/library/functions.html#id)**  
  Official specification of `id()` guarantee and memory address return values.
- **[Built-in `is` vs `==` Operators](https://docs.python.org/3/reference/expressions.html#is)**  
  Comparisons specification in the Python Language Reference.

---

## 📚 Recommended Books

1. **Fluent Python (2nd Edition)** — *Luciano Ramalho* (O'Reilly Media)  
   *Chapter 6: Object References, Mutability, and Recycling.*
2. **CPython Internals** — *Anthony Shaw* (Real Python Publishing)  
   *Chapter 4: Memory Management and Object Allocation in CPython.*
3. **Python In a Nutshell (4th Edition)** — *Alex Martelli et al.* (O'Reilly Media)  
   *Chapter 3: Python Language Basics: Objects, References, and Types.*

---

## 🎥 Video Lectures & Talks

- **[Python Memory Management & Garbage Collection](https://www.youtube.com/watch?v=F6u5rhz6iF4)** — *PyCon Talk*  
  Visual breakdown of heap memory allocation, reference counting, and cyclic GC passes.
- **[The Mystery of `is` vs `==` in Python](https://www.youtube.com/watch?v=in2Pqqxbgaw)** — *Real Python*  
  Clear explanation of object identity versus object value comparison.
- **[How Python Manages Memory](https://www.youtube.com/watch?v=arxWaw-EI54)** — *Ned Batchelder*  
  Famous PyCon talk on how names point to objects in Python memory.

---

## 📰 Articles & Deep Dives

- **[Memory Management in Python](https://realpython.com/python-memory-management/)** — *Real Python*
- **[CPython Garbage Collection Internals](https://devguide.python.org/internals/garbage-collector/)** — *Python Developer's Guide*
- **[Why Python's `is` Operator Can Be Dangerous](https://switowski.com/blog/is-vs-equal/)** — *Sebastian Witowski*

---

## 🧠 Interactive Practice Tools

- **[Python Tutor (Memory Visualizer)](https://pythontutor.com/)**: Visualize stack frame pointers pointing to heap objects in real-time.
