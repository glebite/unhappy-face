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
    """Unhappy - class to manage the display of the game pieces.
    """
    def __init__(self, n_pieces=NORMALGAME):
        """__init__ -start this one up

        :param:     n_pieces - number of pieces to make up the face.
        :return:    n/a
        :exception: n/a
        """
        if n_pieces <= 0:
            raise ValueError
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

    def incr(self):
        """incr - method to increment the to_draw value
        """
        self.to_draw += 1

    def clear(self):
        """clear - reset/erace the characters
        """
        self.to_draw = 0


def main():
    """
    """
    u = Unhappy()
    for pieces in range(NORMALGAME):
        u.to_draw = pieces
        u.draw()


if __name__ == "__main__":
    main()
