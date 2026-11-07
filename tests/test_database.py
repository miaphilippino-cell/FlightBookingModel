from database.repository import Repository # type: ignore


def test_repository():

    repository = Repository()

    assert repository is not None