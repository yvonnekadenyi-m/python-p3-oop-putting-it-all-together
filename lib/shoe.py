
#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    @property
    def size(self):
        """Get the shoe size."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the shoe size with validation."""
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        """Simulate repairing the shoe."""
        print("Your shoe is as good as new!")
        self.condition = "New"
    
    @property
    def condition(self):
        """Get the condition of the shoe."""
        return self._condition if hasattr(self, '_condition') else None
    
    @condition.setter
    def condition(self, value):
        """Set the condition of the shoe."""
        self._condition = value