# Python

## Programming(Problem Solving)

Business Problem တွေကို Solving လုပ်ပေးတာကို Programming လို့ခေါ်တယ်။

## Programming Language

Computer နဲ့ လူတွေကြားမှာ သုံးသော Language တစ်ခုဖြစ်ပါတယ်။ Computer သည် Electronic Device ဖြစ်ပါတယ်။ Computer သည် Binary
ကိုပဲ နားလည်တယ်။

| Programming Process | workflow                   |
|---------------------|----------------------------|
| hardware            |                            |
| Machine Language    | binary(10101010101010)     |
| Assembly            | textual(add a,b)           |
| C++                 | a + b (or) cout<<"Hello"   |
| Python              | print('Hello From Python') |

## Assembly Language

Assembly Language သည် machine code အပေါ်မှာပဲ ရှိတယ်။ Machine Code ကို Assembly Language (Textual) နဲ့ပြတာကို Assembly
Code လို့ခေါ်တယ်။

## Abstration

Complex details တွေကို hide လုပ်ပြီးတော့ လွယ်ကူတဲ့ interface ကနေ သုံးလို့ရတယ်။ Complex ဖြစ်နေတဲ့ identies တွေကို hide
လုပ်ပြီးတော့ အရာအဖြစ် အစားထိုးတာကို abstration လုပ်တယ်လို့ ခေါ်ပါတယ်။ Assembly Language သည် Machine Language နဲ့ ရေးတဲ့
binary တွေကို hide လုပ်ပြီးတော့ textual နဲ့ရေးနိုင်တာကို abstration လို့ခေါ်ပါတယ်။ Complex ဖြစ်နေတဲ့အရာကို Complex
ဖြစ်နေတဲ့အတိုင်းမသုံးပဲနဲ့ ပိုလွယ်ကူအရာအဖြစ် ထိန်းချုပ်လိုက်တာကို abstration လို့ခေါ်ပါတယ်။

Assembly &rarr; Translator &rarr; Machine Language

## Translator

Programming Language တစ်ခုကနေ နောက် Language တစ်ခု ပြောင်းတာကို **Translator** လို့ခေါ်ပါတယ်။ Translator သည်လည်း Program
တစ်ခုဖြစ်ပါတယ်။ ဘာ Program လဲဆိုရင် Programming Language တစ်ခုကနေ နောက်ထပ် Language တစ်ခုကို ပြောင်းပေးတဲ့ Programm (or)
Software ဖြစ်ပါတယ်။ **Translator** သည် abstration ကို သုံးပြီးတော့ **Assembly** to **Machine Language**
ကိုပြောင်းပေးတယ်။

1. Compiler
2. Interpreter
3. Virtual Machine
4. Transpiler
5. JIT/AOT Compiler

## Programming Language(Elements)

| Language   | How to Work                  |
|------------|------------------------------|
| Syntax     | Grammar                      |
| Semantics  | Behind the scenes            |
| Pragmatics | Short, Stout and Right usage |

## Compiler

C++ &rarr; Assembly (Intermediate Code) &rarr; Machine Code (native code)

Get **Source Code**

Transform **Intermediate Code**

Transform **Intermediate Code to Native Code**

## Assembler

Assembly ကို compile လုပ်ပေးသော compiler ကို Assembler လို့ခေါ်တယ်။

## Interpreter

Python Interpreter သည် **Intermediate Code** ကို in memory မှာ ထုတ်တယ် အဲ့ code ကို cpu ပေါ်မှာ Run တယ်။ Interpreter သည်
**Source code** ကို **runtime** မှာ **Byte Code** ကိုပြောင်းပါတယ်။ Interpreter သည် Source code ကို line by line execute
လုပ်တာ မဟုတ်ပါဘူး Byte code ကိုပဲ line by line execute လုပ်ပါတယ်။ Interpreter တွေသည် compiler တွေထက် နှေးပါတယ်။

Source code &rarr; Byte Code (in memory) &rarr; Directly execute byte code

## Byte Code

Byte Code can be executed VM or Interpreter. Byte code is running on memory. Byte code ထုတ်တဲ့အချိန်မှာ Stack ကို
သုံးပြီး execute လုပ်တာဖြစ်တဲ့အတွက်ကြောင့် Stack base interpreter လို့ခေါ်ပါတယ်။

a + b + c

| push a |
|:------:|
| push b |
| push c |
|  mult  |
|  add   |

### Stack Based VM

&rarr; a = b + c \* d; (b=2, c=3, d=5)

### Push

Push လုပ်တဲ့အချိန်မှာ ပထမဆုံးစတဲ့ value ကို lowest level stack မှာ စ၍ push လုပ်ပါတယ်။

| Push on stack | Value |
|:-------------:|:-----:|
|    Push d     |   5   |
|    Push c     |   3   |
|    Push b     |   2   |

### Multiply

Multiply operation လုပ်တဲ့ အချိန်မှာ top level stack မှာရှိတဲ့ value နှစ်ခုကို pop လုပ်ပြီးတော့မှ multiply လုပ်တယ်။
multiply လုပ်ပြီးတဲ့အချိန်မှာ value ကို stack ပေါ်မှာ ပြန်တင်ပေးပါတယ်။

| Multiply on stack | Value |
|:-----------------:|:------|
|       Mult        | 15    |
|      Push b       | 2     |

### Add

Add operation သည်လည်း multiply လုပ်တဲ့ operation နဲ့ အတူတူပါပဲ။ value နှစ်ကို pop လုပ်ပြီးတော့မှ Add လုပ်တယ်။ Add
လုပ်ပြီးတဲ့အချိန်မှ value ကို stack ပေါ်ပြန်တင်ပေးပါတယ်။

| Add on stack | Value |
|:------------:|:------|
|     Add      | 17    |

### Store A

| Store |    |
|-------|----|
| a     | 17 |

## Java/C# Approach?

Java Compiler &rarr; byte code &rarr; Mac &rarr; JVM on Mac

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&rarr; Window &rarr; JVM on Window

## Performance

1. Compiler
2. Based VM
3. Interpreter

## VM

Byte code &rarr;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Interpret

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Byte code to native code &rarr; JVM
Compiler

## Hotspot Compilation

Classes တွေမှာ သုံးကြိမ်လေးကြိမ်ထပ် သုံးတဲ့ code တွေကို compile လုပ်တဲ့အချိန် မှာ hotspot compilation ဖြစ်လာပါတယ်။

## JIT

Just in Time Compilation သည် byte code ကနေ native code ကို ပြောင်းလိုက်တာကို JIT လို့ခေါ်ပါတယ်။
JIT သည် byte code ရဲ့ တစ်စိတ်တစ်ပိုင်းကိုပဲ native code ပြောင်းတာဖြစ်ပါတယ်။

## AOT

Byte Code ကို မ run ခင်မှာ native code ပြောင်းလိုက်တာကို AOT လို့ခေါ်ပါတယ်။ AOT ကတော့ Byte code အကုန်လုံးကို native code
အဖြစ်ပြောင်းလိုက်ပါတယ်။

## Transpiler

High Level Language (higher abstraction) &rarr; High Level Language (lower abstraction)

TypeScript &rarr; Babel Transpiler &rarr; JavaScript (Transpilation approach)

JS ECMA 6 &rarr; Babel Transpiler &rarr; JS ECMA 5

## Lexical Analysis

Character String ကနေပြီးတော့ သက်ဆိုင်ရာ အသေးဆုံး unit တွေ ခွဲခြားလိုက်တာကို lexical analysis လို့ခေါ်ပါတယ်။

int a = 10;

| int |
|:---:|
|  a  |
|  =  |
| 10  |
|  ;  |

## Syntax Analysis

Grammar rule တွေအတိုင်း syntax မှန်မမှန် စစ်တာကို Syntax Analysis လို့ခေါ်ပါတယ်။

lst = [1,2,3,4,5 &nbsp; ❌

lst = [1,2,3,4,5] &nbsp; ✅

## Type System

1. Static Typed
2. Dynamic Typed

## Variable

Variable သည် memory အပေါ်မှာ cell တစ်ခုမှာ address အနေနဲ့ သိမ်းထားတာဖြစ်ပါတယ်။ variable သည် value ကို memory အပေါ်မှာ
သိမ်းလို့ရတယ် ပြန်ယူသုံးလို့ရတယ် ပြောင်းလို့ရတယ်။ Variable can store any type of value.

Variable &rarr;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store Value &rarr;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Have Type

## Static Typed

Variable have type and cannot change type.

## Dynamic Typed

variable can store any type. value have type.

## Strongly Type

Invalid type operation တွေကို လုပ်ခွင့်မပေးဘူးဆိုရင် Strong Type လို့ခေါ်ပါတယ်။ မတူညီတဲ့ Type ကို operation လုပ်တဲ့အခါ
လုပ်ခွင့်မပေးတာကို ဆိုလိုတာပါ။

## Weakly Type

Invalid type operation တွေကို လုပ်ခွင့်ပေးတာကို Weakly Type လို့ခေါ်ပါတယ်။

## Types of Data

1. Integers (Number)
2. Float (3.4)
3. Boolean (Ture & False)
4. String ('Hello')
5. Complex
6. Bytes
7. Bytearray

## Grammar of Assignment

\<variable> = \<expression>

```python
price = 1.5
quantity = 2
total = price * quantity
print('Total is ', total)
```

### Read and write

Variable တွေသည် assignment operator တွေရဲ့ right မှာရှိရင် read လုပ်တာဖြစ်ပါတယ်။ left မှာရှိရင် write လုပ်တာဖြစ်ပါတယ်။

### Expression

value တစ်ခုကို ပြန်ထုတ်ပေးနိုင်ရင် expression ဖြစ်ပါတယ်။

Types of Expression

1. simple expression
2. complex expression

#### 1. Simple Expression

```python
price = 1.5
quantity = 2
```

#### 2. Complex Expression

```python
price = 1.5
quantity = 2
total = price * quantity
```

### Variable Naming Conventions

- class Camel Case
- Other lowercase \_
- Constant All Capital

#### Must start with letter or underscore

##### Start With Letter

```python
var_name = "Hello World"
print(var_name)
```

##### Start With Underscore

```python
_var_name = "Hello World"
print(_var_name)
```

#### Cannot start with a digit

```python
# 2_var_name = "Hello World"  # error
# print(2_var_name)  # error
```

#### Can have up to 256 total characters

#### Can include letters, digits, underscores, dollar signs

```python
_var_name3 = "Hello World"
print(_var_name3)
```

#### Cannot contain spaces

```python
varname = "Hello World"  # error
print(varname)  # error
```

#### Cannot contain math symbols (+, -, /, \*, %, parentheses)

#### Camel Case

```python
varName = "Hello World"
print(varName)
```

#### Case Sensitivity

## Comment

Documentation purposes

```python
# print('hello world')
```

## Arithmetic Operators

Arithmetic should only apply to number type.

### Binary Operator

- \+ Add
- \- Subtract
- \* Multiply
- / Divide
- // Interger Divide
- \*\* Power
- % Remainder
- ( ) Grouping

```python
a = 10
b = 3

print('Sum ', a + b)  # 13
print("Subtract ", a - b)  # 7
print("Mult ", a * b)  # 30
print("Div ", a / b)  # 3.3333333333333335 # floating point division
print("Interger Division ", a // b)  # 3  # integer division
print("Power ", a ** b)  # 1000
print("Remainder ", a % b)  # 1
```

Operand အရေအတွက် ၂ ခု လိုက်ရတဲ့ အတွက် binary operator လို့ခေါ်တာဖြစ်ပါတယ်။

|  +   | Operation |
|:----:|:---------:|
| a, b |  Operand  |

### Unary Operator

```python
c = -10
print('-c ', +-c)  # 10
```

## Order

```python
a = 10
b = 3
c = 4

print('a + b * c ', a + b * c)  # 22
```

## Integer

### Integer in Literal

#### What is literal?

literal is immediately value.

```python
num_in_dec = 23  # literal
print(num_in_dec)
```

### Integer in Binary

only can use 0 or 1

```python
num_in_binary = 0B11
print("Num in binary 11 ", num_in_binary)  # 3
```

### Integer in Octal

only can use 0 to 17

```python
num_in_octal = 0O17
print('Num in octal ', num_in_octal)  # 15
```

### Integer in Hexa

```python
num_in_hexa = 0X10
print('Num in hexa ', num_in_hexa)  # 16
```

#### Check Hexa

hex() သည် language ကပေးထားသော api လေးတွေဖြစ်ပါတယ်။ language မှာပါလာပြီးသာ function တွေဖြစ်ပါတယ်။

```python
print('32 in hexa ', hex(32))  # 0x20
```

#### Check Octal

```python
print('32 in octal ', oct(32))  # 0o40
```

#### Check Binary

```python
print('32 in binary ', bin(32))  # 0b100000
```

#### Calculation hexa and octal

```python
x = 0x20
y = 0o40
print("x + y ", x + y)  # 64
```

## Floating Point

float is not exactly.

```python
my_float = 23.
print('my float', my_float)  # 23.0
print('my float type', type(my_float))  # <class 'float'>
```

### Floating point scientific notation

```python
my_float = 1.1e2
print('my float', my_float)  # 110.0
```

```python
print('0.3 - 0.2', 0.3 - 0.2)  # 0.09999999999999998
```

### Zero

[Different zero](https://www.facebook.com/thet.khine.587/posts/pfbid0nH8fV5jh5a7pLvSbEx8v32Gk3mh5UDwP31K4QtL4s5sodq5dEHdGzCrvF7Gaz3ial)

## Boolean

1. True ( calculation in number 1 )
2. False ( calculation in number 0 )

```python
flag = True
print('flag is ', flag)

flag = False
print('flag is ', flag)

x = 10
print('x + flat ', x + flag)
```

## String

String is immutable.

- ' ' ( Single Quotes )

```python
my_str = 'Hello'
print("my_str ", my_str)
```

- " " ( Double Quotes )

```python
my_str = "Hello"
print("my_str ", my_str)
```

- """ """ ( Triple Quotes for **_Multi Line String_** )

```python
my_str = """This is multiline string
Another Line
"""
print("my_str ", my_str)

"""This is comment
comment second
"""
```

### Escape Sequence ( \ )

```python
my_str = 'Hello "How are you" I\'m fine'
print("my_str ", my_str)
```

## Type Casting

type တစ်ခုခုကနေပြီးတော့ နောက်ထပ် type တစ်ခုခုကိုပြောင်းတာကို type casting လို့ခေါ်ပါတယ်။

### int()

Default အားဖြင့် Base 10 ကိုပဲ Type Convert လုပ်လို့ရပါတယ်။

```python
my_str = '123'
my_num = 10

print("my_str + my_num", int(my_str) + my_num)  # 133
print("int(' 1000 ')", int(' 1000 '))  # 1000
# print("int(' 10.1 ')", int(' 10.1 ')) # invalid literal
# print("int('0x10')", int('0x10')) # invalid literal
print("int(True)", int(True))  # 1
print("int(False)", int(False))  # 0
print("int()", int())  # 0

```

### float()

```python
print("float(' 1000 ')", float(' 1000 '))  # 1000.0
print("float(' 10.1 ')", float(' 10.1 '))  # 10.1
# print("int('0x10')", float('0x10'))  # invalid literal
print("float(True)", float(True))  # 1.0
print("float(False)", float(False))  # 0.0
print("float()", float())  # 0.0
```

### bool()

Falsely Value

1. False
2. 0
3. ""
4. []
5. ()

```python
print("bool(0) ", bool(0))  # False
print("bool(1) ", bool(1))  # True
print("bool(0.0) ", bool(0.0))  # False
print("bool(1.0) ", bool(1.0))  # True
print("bool('False')", bool("False"))  # True
print("bool('')", bool(''))  # False
print("bool([])", bool([]))  # False
print("bool(())", bool(()))  # False
```

## ID

ID is unique identifier.

```python
x = 500
y = 500


def hello():
    k = 500
    print("id of k ", hex(id(k)))


hello()  # 0x101832ea8
print("Id of x ", hex(id(x)))  # 0x101832ea8
print("Id of y ", hex(id(y)))  # 0x101832ea8
```

same memory location ရှိနေလားကို စစ်ချင်ရင် id နဲ့ မစစ်ပဲနဲ့ `is` နဲ့ စစ်သင့်တယ်။ id are not same in python2.

```python
x = 1500
y = 1500
print("x is y ", x is y)


def hello():
    k = 1500
    print("id of k ", id(k))


hello()  # 4333236688
print("Id of x ", id(x))  # 4333236688
print("Id of y ", id(y))  # 4333236688
```

- python3

```bash
x is y  True
id of k  4310561232
Id of x  4310561232
Id of y  4310561232
```

- python2

```bash
('x is y ', True)
('id of k ', 140194292463392)
('Id of x ', 140194292463344)
('Id of y ', 140194292463344)
```

### bytes()

bytes must be in range 0 to 256. Bytes သည် ပြောင်းလဲခြင်း(mutate) လုပ်လို့မရပါဘူး။

```python
x = [0, 10, 25, 30]
my_bytes = bytes(x)

print("my_bytes", my_bytes)  # b'\x00\n\x19\x1e'
print("type my_bytes", type(my_bytes))  # <class 'bytes'>
print("my_bytes[1]", my_bytes[1])  # 10
```

### bytearray()

byte array is immutable.

```python
x = [0, 10, 25, 30]
my_bytes = bytearray(x)

print("my_bytes", my_bytes)  # bytearray(b'\x00\n\x19\x1e')
print("type my_bytes", type(my_bytes))  # <class 'bytearray'>
print("my_bytes[1]", my_bytes[1])  # 10

my_bytes[0] = 100
print("my_bytes", my_bytes)  # bytearray(b'd\n\x19\x1e')
print("my_bytes", my_bytes[0])  # 100
```

## List `[]`

- List is **collection of values**.
- List ကို index or အခန်းနံပါတ်တွေနဲ့ ပြန်ခေါ်သုံးလို့ရပါတယ်။
- List are **heterogeneous**.(Types တွေ အများကြီးပါလို့ရတယ်)
- List are **Linear Data Structure**
- List is mutable

```python
ages = [10, 20, 28, 45]

print("Ages ", ages)
print("Ages[0] ", ages[0])
print("Ages[3] ", ages[3])
print("Sum ", sum(ages))
print("Average ", sum(ages) / len(ages))
```

## Tuple `()`

- Tuple is immutable
- Tuple can only readable.

```python
ages = (10, 20)

print("Ages ", ages)
print("Ages[0] ", ages[0])
print("Ages[1] ", ages[1])
print("len ages ", len(ages))
print("type of ", type(ages))
# ages[0] = 18

mg_mg = ("Mg Mg", 18, "UCSY")
print("mg mg", mg_mg[0])
```