# Eng Py Programming

## 1.Introduction to Python

**Static language and dynamic language:**

​		In static language, the most important trait is that, you must declare the data type before compile the program, or there will be exceptions. However, in dynamic language you don't have to declare that bofore.

**Interpreted language and compiled language:**

​		Program which is coded in compiled language compile only once, and there is an intermediate process if complitation and linking.Interpreted language is executed while interupting.

## 2.Environment And Basic Cognition

### **A.Two modes to run code**

**Interactive mode:**

​		You can get feedback immediately, but you can't save anything.This mode is only suitable for simple programming.

**Script mode:**

​		Just like normal programming, you code on a text editor and then run the code.This type is the most used.

### B.Reversed words

​		Some words are occupied in Python, which means there not for private use.Please pay attenetion to them.

### **C.Basic program structure**

**Identifier:**

​		Identifier is the name used to identify variables, functions, classes, modules and other objects. It is a combination of character digits and underscore.Rules are as follow:

- Must start with a letter or underscore
- Except for the first character, it contain any combination of letters, numbers and so on.
- ......

​		When you name a identifier, please pay attention to the name rules. Resonable identifier names can make your program more understandable. There are two main type of naming style, and they both based on the logical breakpoint of your identifier:

- Underscore style: Each logical breakpoint in the name is marked with and under score and similiar or same name should be avoided.
- camelScore: Just like the style's is named, each logical break point in the name is marked with a capital letter.

### **D.Simple Statement**

​		Statements which are very simple.You only need one line to code them. Such as **Input**, **Output**, **Assignment** and so on.

​		Pay attendtion to the following tips: 

- When you use `input()`, you get a `str` type variable as a feedback
- When you need to transform the type of a variable, pay attention to some restrictions
- In python, when you need to write a **code block**, you must aligned the lines vertically

### E.Module

​		Module is a **simply file** with the `.py` extension containing code which includes functions, classes variables and so on.

- **Built_in module:**This comes with IDLE, loaded automatically and provides common functions
- **Custom module:**Programmers can create and maintain module by themselves

​		You can use `import` to include module.

### F.Package

​		Package is physically a **file** which can contain many files.A python package must contain `__init__.py`.Conceptually it is a namespace.

​		Why we use mofule and passages? If the program is simple, of course we can use one file to code. However, when the structure of our program is being more and more complicated, using package and modules can make your program more readable.

### G.Annotation

​		Use `#` in a single line and use `'''` in many lines.

### H.Input Tips

#### How to enter multiple data in one line and separate each data with a space?

​		**Method 1:** When there is less data, you can use split to extract.

```python
a,b,c = input.split()
```

​		In the case above, you input string will be divided into three string elements with space.

​		**Method 2:** If there are a lot of variables awaiting for input, you can also use function `split()` and store the return value into a special python type `list`

```python
input_list = input().split()
```

​		You can get the elements by using their indexes.

#### How to enter multiple data in one line and convert them into certain type?

​		**Method1: **You can use map.

```python
x,y = map(int, input().split)
```

​		**Method2:** The same as above, you can store your input int a list.

```
num_list = map(int, input().split)
```

##  3.Variables and Data Types

### A.Variables

​		Python **must** use the basic assignment symbol `=` to create a variable. When you use `=`, the left element must be a variable while the right element's type is flexible. Again, you cannot declare a variable without assigning it.

#### **I.Meaning of variables**

​		Variables are references to memory contents.Each variable got an id.Remember id is not equal to address, however you can take is as a address.

```Python
a = 10
b = a
print(id(a))
print(id(b))
a = 20
print(id(a))
print(id(b))
```

 		Variable is only reference.This trait is similar to Java.

#### II.The sizes of variables

​		In python, the size of the variable.

#### III.Naming of variable

​		You'd better follow the following suggestions to make your variables more readable:

- Must start with a letter or underscore
- Can contain any conbition of letters, numbers or underscores except the first characters
- Do not be too abstractive

### B.Data and Types

​		Types include `integer`, `float`, `complex` and so on.

- Integer: 123, -123, 0b1(binary), 0o7(octonary), 0xa(hexadecimal)
- floating: 2.7, 3e+2(scientific notation)
- Boolean:True, False

#### I.Immutable Types

​		String, Integer and boolean are all immutable types in python.If a variable is refer to a string in the memory and you are changing is value superficially, it create a new space in memory to store the new value and redirect the origin variable to the new memory address.That is similar to Java.

#### II.Numeric operations

- Roundoff error may occur cause storage of float number in computer is not as accurate as we excepted

- You can convert a varibale one type to another type under certain restrictions.However, some can be accurate, others may lead to errors.Those errors mostly happen when you try to operate a float number

- When comparing float numbers, `==`, `!=`,`>=`, `<=` sometime cannot function as we excepted.We shall use `eps` sometimes.When comparing two float variables name x and y, there are replacement as follow:

  | Original |     Replacement     |
  | :------: | :-----------------: |
  |    ==    |  abs(x - y) < eps   |
  |    !=    | !(abs(x - y) < eps) |
  |    >=    |    x - y > -eps     |
  |    <=    |     x - y < eps     |

  You can use a number axis to analyze the priciple of them.Please recall a classic case: how to Judge the number of roots of a quadratic equation with one variable? You can use eps and quadratic formula.

  When choosing the value of eps, what might be a proper value? The principle is that the value you pick must be neither too big or small and can judge correctly.

- Radix conversion.We can use functions like `bin()`, `hex()` to convert a variable's radix

- Chain assignment in python is fro left to right, the same of our reading direction

- All objects in python can be. treated as boolean values, however, treated != equivalent

- Short-circuiting in logical operations: we can combine expressions with logical operators such as `&` and `|`.Since in some cases, the results can be calculated before the whole expressions is exectued, the python program is clever enough to save the profermance by circuting those expressions.

#### III.Non-numeric operations

​		In python there is no type "character", instead the so called characters are all string. Index of a string can help us visit its element easily.The index begins from 0 cause it shows the offset.

- In some case, we have to judge certain type of strings, starting or end with certain number or something else. We have some built-in functions to do that like `startswith()` and `endswith()`.
- In python, you can use index is silce a string in a fexilible way. In built-in operations `[]`, we got three value: `[x:y:z]`. If `x` and `y` are positive, we start to count from index 0 to the end of the string. In another way they can also be negative, which means we are counting it from the end of the string to the beginning of the string. In normal cases, we start from `x` and end at `y` and the  default value of `z` is 1. When `z` is set to -1 manually, we count from the opposite direction.
- Conversion from various types (int, float ect.) to string is allowed, but on the contrary it may not succeed.
- Operators and separators in python. Operators contain `+-*/>><<`  and so on.Seperators contain `{}[]()` and so on.

## 4.Structure

#### A.Sequence type

​		It's most important trait is that it can be arranged in order.

#### B.Set

​		Set is a collection of unordered data elements. In python, different types of data can be put into one set. Set is used when you don't need to order your data and the scale of the data is pretty large.

#### C.Map

​		In a map, each key is mapped to a value.

#### D.List

​		List is easy for user to insert and delete, but it might cost some time when finding. In python, there is a special built-in type named list. We use `[]` to create a empty list

```python
L = []
```

​		Since we have a list, we can operate it with some built-in functions like `sppend()`, `extend()`, `remove()` and so on. Different from C, list in python has encapsulated some strong functions. Like you can use index to visit the elements in a list.

#### E.Line assignment, Shallow copy and Deep copy

​		The concept of shallow copy and deep copy also exist in python. Normal assignment  is shallow copy of course. However their might be a recognition may be wrong. Copy with function `copy()` seems to be a deep copy on the surface. However when there exist a heritage in a list like below:

```python
d = [4, 5]
e = [1, 2, 3, d]
f = e.copy()
print(e)
print(f)
e.append(6)
print(e)
print(f)
d.append(6)
print(e)
print(f)
```

​		In this case, output is as follow:

```Python
[1, 2, 3, [4, 5]]
[1, 2, 3, [4, 5]]
[1, 2, 3, [4, 5], 6]
[1, 2, 3, [4, 5]]
[1, 2, 3, [4, 5, 7], 6]
[1, 2, 3, [4, 5, 7]]
```

​		We successfully realised deep copy in the first layer, however failed in the second layer. This may be frustrating, but we still got a way to ge, that is `copy.deepcopy()`.

## 5.Function