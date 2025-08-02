#!/usr/bin/python3
"""
Module containing a Rectangle class with static comparison method.
"""
class Rectangle:
    """
    A Rectangle class that defines a rectangle with width, height properties,
    area and perimeter calculations, string representation, destructor,
    instance counter, customizable print symbol, and static comparison
    method.
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.
        Args:
            width: The width of the rectangle (default: 0)
            height: The height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        """
        Get the width of the rectangle.
        Returns:
            int: The width of the rectangle
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.
        Args:
            value: The new width value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """
        Get the height of the rectangle.
        Returns:
            int: The height of the rectangle
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.
        Args:
            value: The new height value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle (2 * (width + height))
                 Returns 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    def __str__(self):
        """
        Return a string representation of the rectangle using the print
        symbol.
        Returns:
            str: String representation of the rectangle
                 Returns empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])
    def __repr__(self):
        """
        Return a string representation that can recreate the rectangle
        instance.
        Returns:
            str: String representation that can be used with eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        """
        Destructor method that prints a message when the rectangle is
        deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with larger or equal area.
        Args:
            rect_1: First rectangle to compare
            rect_2: Second rectangle to compare
        Returns:
            Rectangle: The rectangle with larger or equal area
                      Returns rect_1 if areas are equal
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

