# the file sound/effects/__init__.py could contain the following code:
__all__ = ["echo", "surround", "reverse"]

# Consider this code:
import sound.effects.echo
import sound.effects.surround
from sound.effects import *