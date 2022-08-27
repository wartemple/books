# 栈

## 概念介绍
使用数组或者链表进行实现，满足后进先出，先进后出的规则。
即插入和删除被限制。

## 常用操作
- 弹出栈顶元素
- 入栈
- 获取栈长度
## 常用的应用

- ### 表达式求值
判断流程：
1. 申请两个栈，数字栈num_stack,字符栈symbols_stack
2. 遍历表达式
3. 数入num_stack, 运算字符入symbols_stack
3.1 运算符入栈时判断：
3.1.1 运算符入栈比较栈顶元素的优先级，优先级大：入栈。优先级小或等于：弹出栈顶元素，将num_stack前两个栈元素进行运算，运算结果入num_stack。
```python3
regex = '3+(2*9)'
symbols_level = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,
    ')': 0,
}

def math(regex):
    num_stack= Stack(20)
    symbols_stack = Stack(20)
    for i in regex:
        if i.isdigit():
            num_stack.append(i)
        elif:
            exec()
```
- ### 括号匹配
- ### 浏览器的返回