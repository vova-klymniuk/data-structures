## Stack:
```
    Stack is a linear data structure that follows a particalar order in which the 
    operations are performed. The order is LIFO (Last in first out). Entering and 
    retrieving data is possible from only one end. The entering and retrieving 
    of data is also called push and pop operation in a stack. There are different
    operations possible in a stack like reversing a stack using recursion, Sorting, Deleting the
    middle element of a stack etc.
                                                                   Push             
                                                                 //|  
                                                                 /
            Stack           |   |   |   |   |   |   |           /
                            |   |   |   |   |   |   | ----------
    Insertion and Deletion  |   |   |   |   |   |   |       Last in, first out
       happen on same end   |   |   |   |   |   |   |
                            |   |   |   |   |   |   |
                            |   |   |   |   |   |   | ----------
                                                    |           \
                                                    v            \
                                                   Top            \
                                                                  \/
                                                                   Pop
```

## Characteristics of a Stack:
Stack has various different characteristics which are as follows:
```
 - Stack is used in many different algorithms like Tower of Hanoi, tree traversal, recursion, etc.
 - Stack is implemented through an array or linked list.
 - It follows the Last In first Out operation i.e, an element that is inserted first will pop in last amd vice versa.
 - The insertion and deletion are performed at one end i.e., from the top of the stack.
 - In stack, if the allocated space for the stack is full and still anyone attempts to
   add more elements, it will lead to stack overflow.
```

## Application of Stack:
Different application of Stack are as follows:
```
    - The stack data structure is used in the evaluation and conversion of arithmetic expressions.
    - Stack is used in Recursion
    - It is used for parenthesis checking.
    - While reversing a string, the stack is used as well.
    - Stack is used in memory management.
    - It is also used for processing function calls.
    - The stack is used to convert expressions from inflix to postfix ( Infix: (A + B), Postfix: AB+, Prefix: +AB )
    - The stack is used to perform undo as well as redo operations in word processors.
    - The stack is used in vertual machines like JVM.
    - The stack is used in the media players. Usefill to play the next and previous song.
    - The stack is used in recursion operations.
```

## Real-Life Application os Stack:
```
    - Real life example of a stack is the layer of eating plates arranged one above the other.
      When you remove a plate from the pile, you can take the plate to the top
      of the pile. But this is exactly the plate that was added most recently to the pile.
      If you want the plate at the bottom of the pile, you mustg remove all the plates on
      top of it to reach it.
    - Browsers use stack data structures to keep track of previously visited sites.
    - Call log in mobile also uses stack data structure.
```


## Basic Operations on Stack
In order to make manipulations in a stack, there are certain operations provided to us.

- push() to insert an element into the stack
- pop() to remove an element from the stack
- top() Returns the top element of the stack.
- isEmpty() returns true if stack is empty else false.
- size() returns the size of stack.

```
     __
    /  \
        v   Push item
             ________
            |________|              ______
                                   /       \
                         ________          \/   Pop item
            Top ----->  |________|       ________  
                         ________       |________|
                        |________|
                         ________
                        |________|
                         ________
                        |________|
                         ________
                        |________|
                         ________
                        |________|
                         ________
                        |________|
                         ________
                        |________|
```

```
Push:
    Adds an item to the stack. If the stack is full, then it is said to be an Overflow confition.
     
Pop:
    Removes an item from the stack. The items are popped in the reversed order
    in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.

Top:
    Returns the top element of the stack.

isEmpty:
    Returns true of the stack is empty, else false.

Complexity Analysis:
    - Time Complexity

___________________________
| Operations | Complexity |
---------------------------
| push()     | 0(1)       |
---------------------------
| pop()      | 0(1)       |
---------------------------
| isEmpty()  | 0(1)       |
---------------------------
| size()     | 0(1)       |
---------------------------
```

## Types of stacks:
```
    - Register Stack: This type of stack is also a memory element present in the memory unit and can handle a small amount of data only. 
                      The height of the register stack is always limited as the size of the register stack is very small compared to the memory.

    - Memory Stack: This type of stack can handle a large amount of memory data. 
                    The height of the memory stack is flexible as it occupies a large amount of memory data. 
```

## Applications of the stack:
```
    - Стеки также используются для реализации операции отмены/повтора в текстовом редакторе.
    - Стек также помогает в реализации вызова функций на компьютерах. Последняя вызванная функция всегда завершается первой.
    - Обращение строк также является еще одним применением стека. Здесь один за другим каждый символ вставляется в стек. Таким образом, первый символ строки находится в нижней части стека, а последний элемент строки — в верхней части стека. После выполнения операций извлечения из стека мы получаем строку в обратном порядке.
    - В управлении памятью любой современный компьютер использует стек в качестве основного средства управления для текущих целей. Каждая программа, работающая в компьютерной системе, имеет собственное распределение памяти.
    - В графических алгоритмах, таких как топологическая сортировка и сильно связанные компоненты
    - Возврат является одним из методов разработки алгоритмов. Некоторыми примерами возврата являются задача коня-тур, проблема N-ферзя, поиск пути в лабиринте и игровые шахматы или шашки во всех этих задачах, в которые мы каким-то образом погружаемся, если этот способ неэффективен, мы возвращаемся к предыдущему состояние и пойти по какому-то другому пути. Чтобы вернуться из текущего состояния, нам нужно сохранить предыдущее состояние, для этого нам нужен стек.
    - Используется во многих алгоритмах, таких как Ханойская башня, обход дерева, задачи с запасами и задачи с гистограммами.
    - Вперед и назад функции в веб-браузерах
    - Функции повтора-отмены во многих местах, таких как редакторы, фотошоп.
    - Преобразование инфикса в постфикс/префикс    
```