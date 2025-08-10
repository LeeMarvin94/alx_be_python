# book_class.py

class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Using !r ensures proper quoting/escaping for strings while matching the expected format.
        return f"Book({self.title!r}, {self.author!r}, {self.year})"

    def __del__(self):
        """Destructor that announces when a Book is being deleted."""
        # flush=True helps ensure the message appears promptly before interpreter shutdown.
        try:
            print(f"Deleting {self.title}", flush=True)
        except Exception:
            # Be silent if stdout is unavailable during interpreter teardown.
            pass

