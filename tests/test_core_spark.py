from src.core_spark.core import watch


def test_watch_keeps_first():
    rows = [{"id": "a"}, {"id": "a"}, {"id": "b"}]
    assert watch(rows) == [{"id": "a"}, {"id": "b"}]
