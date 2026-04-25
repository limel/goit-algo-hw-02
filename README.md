# GoIT Algo HW-02 Andrii Nazarenko

## Structure

```
goit-algo-hw-02/
├── main.py          # entry point with task selection menu
├── task1/
│   ├── __init__.py
│   └── task1.py     # Task 1 — service center queue
└── task2/
    ├── __init__.py
    └── task2.py     # Task 2 — palindrome checker
```

## Run

```bash
python main.py
```

You will be prompted to choose a task:

```
Select a task:
  1 — Service center (queue)
  2 — Palindrome checker (deque)
```

---

## Task 1 — Service Center

Simulates a service center that generates and processes requests using a FIFO queue.

**Implementation:** `Queue` extends `queue.Queue` from the standard library with two methods:

- `generate_request()` — creates a request with a unique UUID-based ID and adds it to the queue
- `process_request()` — removes and processes the next request, or reports that the queue is empty

Each cycle generates 1–5 random requests and processes one. On `Ctrl+C` the program drains all remaining requests before exiting.

**Example output:**

```
  [+] Generated:  Request-a1b2c3d4
  [+] Generated:  Request-e5f6a7b8
  [-] Processing: Request-a1b2c3d4
      Queue size: 1
```

---

## Task 2 — Palindrome Checker

Determines whether a string is a palindrome using a `deque`.

**Implementation:** `is_palindrome(string)` normalizes the input (lowercase, alphanumeric only), loads characters into a `deque`, then repeatedly compares characters from both ends (`popleft` vs `pop`) until 0 or 1 characters remain.

**Examples:**

| Input                            | Result           |
| -------------------------------- | ---------------- |
| `racecar`                        | palindrome       |
| `A man, a plan, a canal: Panama` | palindrome       |
| `hello`                          | not a palindrome |
