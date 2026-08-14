# Notes of Python

Pattern example
```python
import packagexyz

class Circle:
    def __init__(self, radius):
        self.PI_6DEC = 3.141592
        self.radius = radius
    
    def circumference(self):
        return 2 * self.PI_6DEC * self.radius
    
    def get_area(self):
        return self.PI_6DEC * self.radius * self.radius


given_radius = 10
circle = Circle(given_radius)
circle_area = circle.get_area()
```

```python
/directory-name/file_name.py
```
