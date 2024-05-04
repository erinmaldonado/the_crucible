# Assuming the same get_args function as defined earlier.

def test_default_name():
    args = get_args([])
    assert args.name == "World"

def test_custom_name():
    args = get_args(['--name', 'Bob'])
    assert args.name == 'Bob'
