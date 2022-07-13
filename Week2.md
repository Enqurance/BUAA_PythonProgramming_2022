# Week2

## Things from last week

### A.Namespace

​		In conclusion, we got 3 types of name space.

- Built-in namespace: Python's built-in namespace, it can be accessed by any module. It stores built-in functions and exceptions.
- Global namespace: Created when the module is loaded and executed executed, it records the variables and constants defined in the module, including functions and classes defined in the module.
- Local Namespace: This namespace is owned by each function and class.

​		Let's have a look at a simple case: 

```python
def add():
		x = x + 1
x = 10
add()
```

​		This code occurs error. As we know, `x` is primarily a global variable. If you want to modify a global variable in a custom function, python will create a local variable the same name as the global variable. However, when `x` is created as a local variable, complier find in the right side of `=`, such a local variable called `x` is not declared. Exception is thrown here.

## Object Oriented Programming

​		In python, we have OO programming as well.

### A.Class and Objects

```Python
class ClassName:
  	def __init__(self[...])		# Initializer, built-in method #
  	def methodName(self[...])		# Customized mothed #
  	def __def__(delf):		# Destory resourse, built-in method #
```

​		Let's have a look on a sample:

```Python
class Box:
  	# Functions start with `__` mean their visibilities are private #
    # Functions start with `_` mean their visibilities are protected #
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
 
    def getVolume(self):
        return self.width * self.height * self.depth
 
b = Box(10, 20, 30)
print(b.getVolume())
```

​		`__init__()` has four arguments, but we only filled in three when creating an object of  the class. The `self` argument is assigned automatically by your interpreter. 

### B.Class Variable and Instance Variable

​		Class variable "belongs to" a class, and can be visited by all instances of the class. Instance variable belongs to an instance and is visited privately.

​		There are some detials in this area, you can search them online.

### C.Visibility

​		Visibility is similar with Java's

## Libiaries

### Numpy

​		Numpy is a commonly used libiary in python. You can import it in this way:

```Python
import numpy as np
```

​		Array is  a special type in `numpy`. You can create a array in various ways.

```python
a = [1, 2, 3, 4]
b = (5, 6, 7, 8)
c = np.array(a, b)
```

​		In addition to one-dimensional vectors, we can also create matrix with `array()`.

### Interpolation and Fitting Problem

​		In the process of manufacturing practice or scientific experiments, it is usually necessary to understand the inherent laws between variables. So the key point is to find a appropriate function.

​		How to find the function? We have two ways to do that:

- Interpolation. When the sample is small and accurate, this method is mostly used. This  method requires your function to approximate the sample point. Figure below shows interpolation.Both P(x) and F(x) are acceptable since they add pass through all the points of the sample.

  ![7991657506059_.pic](/Users/enqurance/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/8595b9ac6731cc4fd34dd896c9aacf68/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/7991657506059_.pic.jpg)

- Fitting. When the scale of data is pretty large, or a certain error exists between the measured value and real value, or we need to predict a value out of the sample range, fitting method is generally used. Fitting emphasizes minimum variance. In scientific researches, the smaller variances are, the better the models are.

  ![8001657506148_.pic](/Users/enqurance/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/8595b9ac6731cc4fd34dd896c9aacf68/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/8001657506148_.pic.jpg)

## GUI

### Tkinter

​		`tkinter` is a local library of python which can help us build easy GUI. It includes some built-in functions that are able to run easy GUI. You can import it with:

```Python
import tkinter
```

​		Tkinter also has some simple widgets for us to use.

```Python
# create four radiobuttons with for loop
buttons = ["Prefect", "Good", "Soso", "Bad"]
for i in buttons:
    R = tkinter.Radiobutton(root, text=i)
    R.pack(anchor=tkinter.W, padx=20)
    
# create a textbox for user to input
root = tkinter.Tk()
l1 = tkinter.Label(root, text = 'Input a number:')
l1.pack()
e1 = tkinter.Entry(root)
e1.pack()
b1 = tkinter.Button(root,text = 'OK')
b1.pack()
root.mainloop()
```

​		Apart from those text type widgets, there are also some picture type widgets.

```Python
tkinter.Label(root,text = 'error',compound = 'bottom',bitmap ='error').pack()
```

