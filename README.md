# shaffle
SHA-ffle: Map hash-ables to pseudo-random floats.

## Usage

[Hashlib functions](https://docs.python.org/3/library/hashlib.html)

```python
from shaffle import uniform

# will always get pseudo-uniform numbers between 0 and 1
uniform('hello world!')
uniform('any-object-with-repr')

# can use any hashing function supported by hashlib
uniform(123, method='sha256')
```
