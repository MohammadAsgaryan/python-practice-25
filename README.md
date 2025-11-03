# Python Error Handling & Unit Testing

This project demonstrates how to properly handle errors in Python using `try` and `except`, 
and how to write unit tests to ensure functions behave correctly even when unexpected input is given.

---

## ✅ Features

✔ Safe division function with ZeroDivisionError and TypeError handling  
✔ Convert-to-int function with ValueError and TypeError handling  
✔ Full unit test coverage using Python `unittest`  
✔ Beginner-friendly and clean code structure  

---

## 📂 Project Structure


project/
│
├── main.py # Functions with error handling
├── tests.py # Unit test for verification
└── README.md # Documentation



---

## ✅ Functions

### `safe_divide(a, b)`
Returns the result of a / b.  
Handles:
- Division by zero
- Invalid input types

### `convert_to_int(value)`
Converts input to integer.
Returns `None` if conversion fails.

---

## ✅ Running the tests

In terminal:

python tests.py


You should see:

......

Ran 6 tests in 0.000s

OK



---

## ✅ Why Unit Testing Matters?

Unit testing makes sure:

- Code does not break when input is invalid
- Errors are handled properly
- Functions behave consistently
- Future code changes do not introduce bugs

---

✅ This project is great for learning:
- Python error handling
- Clean code
- Professional unit testing
- Real-world defensive programming

