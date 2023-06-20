To access files stored on Teams/OneDrive, the path needs to contain a username (providing relative paths are not being used)

To do this dynamically, use getuser in the getpass library. Inject the result into a filepath string

```python
from getpass import getuser

path = f'C:/Users/{getuser()}/Jisc/...'
```
NB: Python 3.6 introduced "f strings" allowing variables to be inserted directly into strings by wrapping them in curly brackets. Previously this was ```'some text'+variable+'more text'```
