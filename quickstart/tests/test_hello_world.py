from quickstart.assets import hello_world

def test_processed_file() -> None:
    assert hello_world.hello_world().iloc[0, 0] == "Hello, World!"  