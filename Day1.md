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

###  3.Variables

#### A.Variables

​		Python **must** use the basic assignment symbol `=` to create a variable. When you use `=`, the left element must be a variable while the right element's type is flexible.

#### **B.Meaning of variables**

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

#### C.The sizes of variables

​		In python, the size of the variable.