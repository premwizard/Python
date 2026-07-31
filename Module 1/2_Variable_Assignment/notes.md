# Lesson 1.2 – Variable Assignment

## What is Assignment?

Assignment is the process of binding a variable name to an object.

Syntax

```python
variable = value
```

Example

```python
name = "Prem"
```

Python creates the object and then makes the variable refer to that object.

---

## Reassignment

Variables can point to different objects later.

Example

```python
age = 22
age = 23
```

Now the variable refers to the object 23 instead of 22.

---

## Multiple Assignment

Multiple variables can be assigned in one line.

Example

```python
name, age, cgpa = "Prem", 22, 8.17
```

---

## Chain Assignment

The same value can be assigned to multiple variables.

Example

```python
x = y = z = 500
```

All three variables refer to the same object.

---

## Variable Swapping

Traditional method

```python
temp = a
a = b
b = temp
```

Pythonic method

```python
a, b = b, a
```

Python swaps the values without using a temporary variable.

---

## Sequence Unpacking

Values from a list or tuple can be assigned directly to variables.

Example

```python
colors = ["Red", "Green", "Blue"]

red, green, blue = colors
```

---

## Common Mistakes

### Wrong

```python
print("salary")
```

Prints the word salary.

### Correct

```python
print(salary)
```

Prints the value stored in the variable.

---

## Best Practices

- Use meaningful variable names.
- Follow snake_case naming.
- Keep names descriptive.
- Avoid single-letter variable names unless needed.

Example

```python
student_name
student_age
student_course
```

---

## Interview Questions

Q. What does the assignment operator do?

Answer:
It binds a variable name to an object.

---

Q. Does assignment copy an object?

Answer:
No.
Assignment creates another reference to the same object.

---

Q. What is unpacking?

Answer:
Assigning values from an iterable to multiple variables.

---

## Summary

- Variables are references.
- Assignment binds variables to objects.
- Variables can be reassigned.
- Python supports multiple assignment.
- Python supports unpacking.
- Python supports swapping without temp variables.