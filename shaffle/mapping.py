import hashlib
from functools import lru_cache


@lru_cache(maxsize=32)
def get_consts(method):
    """
    Create hash object and its integer upper bound.
    """
    hasher = getattr(hashlib, method)
    max_plus_one = 2 ** (hasher().digest_size * 8)
    return hasher, max_plus_one


def uniform(obj, method="sha1"):
    """
    Create a 0-to-1 float from a hashable object.
    """
    hasher, max_plus_one = get_consts(method)
    seed = repr(obj).encode("utf-8")

    hash_digest = hasher(seed).digest()
    hash_int = int.from_bytes(hash_digest, "big")
    return hash_int / max_plus_one
