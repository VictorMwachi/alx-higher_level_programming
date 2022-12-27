#!/usr/bin/python3
"""
module contains class square that
inherits from class rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines our square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """custom string defination of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
