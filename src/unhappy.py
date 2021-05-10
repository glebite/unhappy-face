#!/usr/bin/env python3
"""unhappy.py - base class for displaying unhappy face
"""


NORMALGAME = 6


class Unhappy(object):
    """
    """
    def __init__(self, n_pieces=NORMALGAME):
        """__init__ -
        """
        self.n_pieces = n_pieces
        self.to_draw = 0

    def draw(self):
        """draw - base unhappy face
        """
        pass

    def __str__(self):
        return f'%={self.to_draw/self.n_pieces}'

    def __repr__(self):
        return f'Unhappy(n_pieces={self.n_pieces})'


def main():
    """
    """
    pass


if __name__ == "__main__":
    main()
