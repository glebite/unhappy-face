#!/usr/bin/env python3
"""unhappy.py - base class for displaying unhappy face
"""

FACEPIECES = [
    'top-outline',
    'bottom-outline',
    'left-eye',
    'right-eye',
    'nose',
    'unhappy-smile']
NORMALGAME = len(FACEPIECES)


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
        for piece in range(self.to_draw):
            print(f'{FACEPIECES[piece]}')

    def __str__(self):
        return f'%={self.to_draw/self.n_pieces}'

    def __repr__(self):
        return f'Unhappy(n_pieces={self.n_pieces})'


def main():
    """
    """
    u = Unhappy()
    for pieces in range(NORMALGAME):
        u.to_draw = pieces
        u.draw()


if __name__ == "__main__":
    main()
