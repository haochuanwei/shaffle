import shaffle


def test_uniform():
    for obj in [0, "1", ("2", "3")]:
        for method in ["sha1", "md5", "sha256"]:
            number = shaffle.uniform(obj, method=method)
            assert 0.0 <= number <= 1.0
