from queue import Queue as BaseQueue
import uuid


class Queue(BaseQueue):
    def __init__(self):
        super().__init__()

    def generate_request(self) -> None:
        request = f"Request-{uuid.uuid4().hex[:8]}"
        self.put(request)
        print(f"  [+] Generated:  {request}")

    def process_request(self) -> None:
        if not self.empty():
            request = self.get()
            print(f"  [-] Processing: {request}")
        else:
            print("  [!] Queue is empty, nothing to process")
