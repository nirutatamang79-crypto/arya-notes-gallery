# 💻 Object-Oriented Programming (C++) — Solutions & Concept Guide

> Detailed solutions and C++ code examples for IOE Engineering OOP examinations.

---

## 📑 Table of Contents
1. [Chapter 1: Principles of Object-Oriented Programming](#chapter-1-principles-of-object-oriented-programming)
2. [Chapter 2: Classes, Objects, & Operator Overloading](#chapter-2-classes-objects--operator-overloading)
3. [Chapter 3: Inheritance & Polymorphism](#chapter-3-inheritance--polymorphism)
4. [Chapter 4: Virtual Functions & Abstract Classes](#chapter-4-virtual-functions--abstract-classes)
5. [Chapter 5: Templates & Exception Handling](#chapter-5-templates--exception-handling)
6. [Chapter 6: File I/O Streams](#chapter-6-file-io-streams)

---

## Chapter 1: Principles of Object-Oriented Programming

### Q1. Contrast Procedural Programming (C) with Object-Oriented Programming (C++).

| Parameter | Procedural Programming (POP) | Object-Oriented Programming (OOP) |
|---|---|---|
| **Approach** | Top-down approach | Bottom-up approach |
| **Focus** | Focuses on functions and algorithms | Focuses on data and security |
| **Data Hiding** | No data hiding; data is global and vulnerable | High security through encapsulation/private access |
| **Reusability** | Code reuse limited to function calls | Reusability through inheritance & polymorphism |
| **Overloading** | Operator & function overloading not supported | Supported (Function & Operator Overloading) |

---

## Chapter 2: Classes, Objects, & Operator Overloading

### Q2. Write a C++ program to overload the `+` operator to add two `Complex` numbers.

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
    float real;
    float imag;

public:
    // Default and Parameterized Constructor
    Complex(float r = 0, float i = 0) : real(r), imag(i) {}

    // Overload + operator
    Complex operator+(const Complex& obj) const {
        return Complex(real + obj.real, imag + obj.imag);
    }

    void display() const {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    Complex c1(3.5, 2.5), c2(1.5, 4.5);
    Complex c3 = c1 + c2; // Calls c1.operator+(c2)

    cout << "Sum: ";
    c3.display(); // Output: 5 + 7i
    return 0;
}
```

---

## Chapter 3: Inheritance & Polymorphism

### Q3. Explain Ambiguity in Multiple Inheritance and how to resolve it using Virtual Base Class.

#### Solution & Code Example:
When a derived class inherits from two base classes that both derive from a single root base class (the Diamond Problem), multiple instances of the root base class exist in the grandchild class.

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    int val = 100;
};

// Use virtual inheritance to resolve diamond problem ambiguity
class DerivedA : virtual public Base {};
class DerivedB : virtual public Base {};

class FinalChild : public DerivedA, public DerivedB {};

int main() {
    FinalChild obj;
    cout << "Value: " << obj.val << endl; // Unambiguous reference!
    return 0;
}
```

---

## Chapter 4: Virtual Functions & Abstract Classes

### Q4. What is a Pure Virtual Function and an Abstract Class? Show with code.

- **Pure Virtual Function**: A function declared in a base class that has no definition and is set to `= 0`.
- **Abstract Class**: A class containing at least one pure virtual function. It cannot be instantiated directly.

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
    // Pure Virtual Function
    virtual void draw() = 0; 
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Circle!" << endl;
    }
};

int main() {
    // Shape s; // ERROR: Cannot instantiate abstract class
    Shape* ptr = new Circle();
    ptr->draw(); // Runtime Polymorphism
    delete ptr;
    return 0;
}
```

---

## Chapter 5: Templates & Exception Handling

### Q5. Write a Function Template to find the maximum of two values of any data type.

```cpp
#include <iostream>
using namespace std;

template <typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << "Max Int: " << getMax(10, 20) << endl;
    cout << "Max Double: " << getMax(5.67, 3.14) << endl;
    cout << "Max Char: " << getMax('A', 'Z') << endl;
    return 0;
}
```
