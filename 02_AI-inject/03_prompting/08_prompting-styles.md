<div align="center">

# 🎯 Prompting Styles Guide

</div>

---

<div align="center">

# 📚 1. Alpaca Format

</div>

**Origin:** Stanford University | **Type:** Structured Instruction Format  
**Used By:** Alpaca, Vicuna, LLaMA-derivatives, WizardLM

### 🔧 Structure

The Alpaca format uses **three distinct sections** separated by markdown headers:

```text
### Instruction:
[Your clear, specific instruction or task]

### Input:
[Optional: Additional context, data, or constraints]

### Response:
[Model's generated output]
```

### 💡 Practical Examples

**Example 1: Simple Task**
```text
### Instruction:
Write a Python function to calculate factorial.

### Input:
The function should handle numbers up to 1000.

### Response:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
```

**Example 2: Code Debugging**
```text
### Instruction:
Debug the following Python code and explain the issue.

### Input:
def add_numbers(a, b):
    return a + b + c

### Response:
Error: Variable 'c' is not defined. The function only accepts 
parameters 'a' and 'b', but tries to use 'c' in the return statement.

Fixed code:
def add_numbers(a, b):
    return a + b
```

**Example 3: No Input Needed**
```text
### Instruction:
Explain the concept of recursion in programming.

### Response:
Recursion is a programming technique where a function calls itself 
to solve a problem by breaking it down into smaller subproblems...
```
---

<div align="center">

# 💬 2. ChatML (Chat Markup Language) Format

</div>

**Origin:** OpenAI | **Type:** Conversational Role-Based Format  
**Used By:** GPT-3.5, GPT-4, Claude, Gemini, ChatGPT API

### 🔧 Structure

ChatML uses **special tokens** and **role identifiers** for multi-turn conversations:

```text
<|im_start|>system
[System-level instructions and behavior definition]<|im_end|>
<|im_start|>user
[User's message or question]<|im_end|>
<|im_start|>assistant
[AI assistant's response]<|im_end|>
```

### 💡 Practical Examples

**Example 1: Python API Format**

```python
messages = [
    {
        "role": "system", 
        "content": "You are a helpful Python coding assistant specialized in data science."
    },
    {
        "role": "user", 
        "content": "Explain list comprehension with an example."
    },
    {
        "role": "assistant", 
        "content": "List comprehension is a concise way to create lists in Python.\n\nExample:\nsquares = [x**2 for x in range(10)]\n# Creates: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
    }
]
```

**Example 2: Multi-turn Conversation**
```python
conversation = [
    {"role": "system", "content": "You are a patient teacher explaining JavaScript."},
    {"role": "user", "content": "What's the difference between let and const?"},
    {"role": "assistant", "content": "'let' allows reassignment, 'const' creates a constant reference that cannot be reassigned."},
    {"role": "user", "content": "Can I modify a const array?"},
    {"role": "assistant", "content": "Yes! 'const' prevents reassignment, but array methods like push() still work because you're modifying the content, not reassigning the reference."}
]

```
---

<div align="center">

# 📝 3. Instruction Format

</div>

**Type:** Simple Direct Format  
**Used By:** Text completion APIs, simple prompts, CLI tools

### 🔧 Structure

The simplest format - **just write what you want:**

```text
[Your clear instruction or question]
```

Or with **optional context:**

```text
[Role/Context description]

[Task description]
[Additional constraints or details]
```

### 💡 Practical Examples

**Example 1: Simple Direct Request**
```text
Write a JavaScript function to reverse a string.
```

**Example 2: With Context**
```text
You are an expert Python developer specializing in Django.

Task: Create a model for a blog post with title, content, author, and timestamp.
```

**Example 3: Detailed Instruction**
```text
Explain the difference between async/await and Promises in JavaScript. 
Include code examples showing when to use each approach.
Assume the reader has basic JS knowledge but hasn't used async patterns before.

```
### 🎯 When to Use

- ✅ Quick one-off queries
- ✅ Simple API calls or CLI interactions
- ✅ Prototyping and experimentation
- ✅ Text completion tasks
- ✅ When you don't need conversation history
- ✅ Scripting and automation
- ✅ Single-turn Q&A

---

**💡 Remember:** The best format is the one that works for your specific use case. Don't be afraid to mix and match or adapt these formats to your needs!

---

<div align="center">

# 🏆 ChatML is the Most Dominant and Widely Used Format Today!

**Used by all major AI providers: OpenAI, Anthropic, Google, Microsoft, and most modern LLM APIs**

</div>