#!/usr/bin/env python3
"""
Example code for Code Art Studio demonstrations
"""

def fibonacci(n):
    """Calculate fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def bubble_sort(arr):
    """Simple bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers"""
        self.result = a + b
        self.history.append(f"{a} + {b} = {self.result}")
        return self.result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        self.result = a - b
        self.history.append(f"{a} - {b} = {self.result}")
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        self.result = a * b
        self.history.append(f"{a} * {b} = {self.result}")
        return self.result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        self.history.append(f"{a} / {b} = {self.result}")
        return self.result
    
    def get_history(self):
        """Get calculation history"""
        return self.history


class LinkedList:
    """Simple linked list implementation"""
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add element to end"""
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        """Display the list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


def binary_search(arr, target):
    """Binary search implementation"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Main execution
if __name__ == "__main__":
    # Test fibonacci
    print("Fibonacci sequence:")
    for i in range(10):
        print(f"  fib({i}) = {fibonacci(i)}")
    
    # Test calculator
    calc = Calculator()
    print("\nCalculator operations:")
    print(f"  5 + 3 = {calc.add(5, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  6 * 7 = {calc.multiply(6, 7)}")
    print(f"  20 / 4 = {calc.divide(20, 4)}")
    
    # Test linked list
    ll = LinkedList()
    for i in range(5):
        ll.append(i * 10)
    print(f"\nLinked List: {ll.display()}")
    
    # Test binary search
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(sorted_arr, target)
    print(f"\nBinary search for {target}: found at index {result}")
