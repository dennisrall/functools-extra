def test_readme():
    from operator import itemgetter

    from functools_extra import pipe

    def add_one(x: int) -> int:
        return x + 1

    assert pipe(range(3), list, itemgetter(2), add_one) == 3  # noqa: PLR2004
