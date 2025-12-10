#!/usr/bin/env python3

class Book:
    pass
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set the page count with validation."""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        """Simulate turning a page."""
        print("Flipping the page...wow, you read fast!")
    
        