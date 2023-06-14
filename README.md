# Python

## Programming(Problem Solving)

Business Problem တွေကို Solving လုပ်ပေးတာကို Programming လို့ခေါ်တယ်။

## Programming Language

Computer နဲ့ လူတွေကြားမှာ သုံးသော Language တစ်ခုဖြစ်ပါတယ်။ Computer သည် Electronic Device ဖြစ်ပါတယ်။ Computer သည် Binary
ကိုပဲ နားလည်တယ်။

| Programming Process | workflow                   |
| ------------------- | -------------------------- |
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
| ---------- | ---------------------------- |
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
| :----: |
| push b |
| push c |
|  mult  |
|  add   |

### Stack Based VM

&rarr; a = b + c \* d; (b=2, c=3, d=5)

### &rarr; Push

Push လုပ်တဲ့အချိန်မှာ ပထမဆုံးစတဲ့ value ကို lowest level stack မှာ စ၍ push လုပ်ပါတယ်။

| Push on stack | Value |
| :-----------: | :---: |
|    Push d     |   5   |
|    Push c     |   3   |
|    Push b     |   2   |

### &rarr; Multiply

Multiply operation လုပ်တဲ့ အချိန်မှာ top level stack မှာရှိတဲ့ value နှစ်ခုကို pop လုပ်ပြီးတော့မှ multiply လုပ်တယ်။
multiply လုပ်ပြီးတဲ့အချိန်မှာ value ကို stack ပေါ်မှာ ပြန်တင်ပေးပါတယ်။

| Multiply on stack | Value |
| :---------------: | :---- |
|       Mult        | 15    |
|      Push b       | 2     |

### &rarr; Add

Add operation သည်လည်း multiply လုပ်တဲ့ operation နဲ့ အတူတူပါပဲ။ value နှစ်ကို pop လုပ်ပြီးတော့မှ Add လုပ်တယ်။ Add
လုပ်ပြီးတဲ့အချိန်မှ value ကို stack ပေါ်ပြန်တင်ပေးပါတယ်။

| Add on stack | Value |
| :----------: | :---- |
|     Add      | 17    |

### &rarr; Store A

| Store |     |
| ----- | --- |
| a     | 17  |

## Java/C# Approach?

Java Compiler &rarr; byte code &rarr; Mac &rarr; JVM on Mac

$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ &rarr; Window &rarr; JVM on Window

## Performance

1. Compiler
2. Based VM
3. Interpreter

## VM

Byte code &rarr;

$~~~~~~~~~~~~~~~~~$ Interpret

$~~~~~~~~~~~~~~~~~$ Byte code to native code &rarr; JVM Compiler

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
| :-: |
|  a  |
|  =  |
| 10  |
|  ;  |

## Syntax Analysis

Grammar rule တွေအတိုင်း syntax မှန်မမှန် စစ်တာကို Syntax Analysis လို့ခေါ်ပါတယ်။

lst = [1,2,3,4,5 $~~~$ ❌

lst = [1,2,3,4,5] $~~$ ✅

## Type System

1. Static Typed
2. Dynamic Typed

## Variable

Variable သည် memory အပေါ်မှာ cell တစ်ခုမှာ address အနေနဲ့ သိမ်းထားတာဖြစ်ပါတယ်။ variable သည် value ကို memory အပေါ်မှာ
သိမ်းလို့ရတယ် ပြန်ယူသုံးလို့ရတယ် ပြောင်းလို့ရတယ်။ Variable can store any type of value.

Variable &rarr;

$~~~~~~$ Store Value &rarr;

$~~~~~~~~~~~~~~~~~~~$ Have Type

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
total = price * quantity
```

## Variable Naming Conventions

### Must start with letter or underscore

#### Start With Letter

```python
var_name = "Hello World"
print(var_name)
```

#### Start With Underscore

```python
_var_name = "Hello World"
print(_var_name)
```

### Cannot start with a digit

```python
2_var_name = "Hello World" # error
print(2_var_name) # error
```

### Can have up to 256 total characters

### Can include letters, digits, underscores, dollar signs

```python
_var_name3 = "Hello World"
print(_var_name3)
```

### Cannot contain spaces

```python
var name = "Hello World" #error
print(var name) #error
```

### Cannot contain math symbols (+, -, /, \*, %, parentheses)
