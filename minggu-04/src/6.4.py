sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

# Users of the package can import individual modules from the package, for example:
import sound.effects.echo

# This loads the submodule sound.effects.echo. It must be referenced with its full name.
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# An alternative way of importing the submodule is:
from sound.effects import echo

# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:
echo.echofilter(input, output, delay=0.7, atten=4)

# Yet another variation is to import the desired function or variable directly:
from sound.effects.echo import echofilter

# Again, this loads the submodule echo, but this makes its function echofilter() directly available:
echofilter(input, output, delay=0.7, atten=4)