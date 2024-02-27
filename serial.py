"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start=0):
        """Makes a new generator starting at a defined number or default start is 0"""
        self.start = self.next = start 
    
    def __repr__(self):
        """Representation"""
        return f"<SerialGenerator start={self.start} next={self.next}"
    
    def generate(self):
        """Returns the next sequential serial number"""
        self.next += 1 
        return self.next - 1 
    
    def reset(self):
        "Re-starts the generator using the defined start number"
        self.next = self.start