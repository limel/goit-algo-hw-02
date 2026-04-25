import random
import time
from task1 import Queue
from task2 import is_palindrome


def run_task1():
    queue = Queue()
    print("Script started. Press Ctrl+C to stop.\n")
    try:
        while True:
            for _ in range(random.randint(1, 5)):
                queue.generate_request()

            queue.process_request()
            print(f"      Queue size: {queue.qsize()}\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nScript stopped. Processing remaining {queue.qsize()} request(s)...\n")
        while not queue.empty():
            queue.process_request()
            time.sleep(0.5)
        print("\nAll requests processed.")


def run_task2():
    print("Palindrome checker. Type 'exit' to quit.\n")
    while True:
        string = input("Enter a string: ")
        if string.lower() == "exit":
            break
        result = is_palindrome(string)
        print(f"  '{string}' is {'a palindrome' if result else 'not a palindrome'}\n")


if __name__ == "__main__":
    print("Select a task:")
    print("  1 — Service center (queue)")
    print("  2 — Palindrome checker (deque)")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        run_task1()
    elif choice == "2":
        run_task2()
    else:
        print("Invalid choice.")
