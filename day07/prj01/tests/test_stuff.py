import pytest



class Stuff:
    def prep(self):
        self.foo = 1
        self.bar = 2


@pytest.fixture
def get_prepped_stuff():
    mystuff = Stuff()
    mystuff.prep()
    return mystuff

def test_foo_updates(get_prepped_stuff):
    mystuff = get_prepped_stuff
    assert 1 == mystuff.foo
    mystuff.foo = 300
    assert 300 == mystuff.foo
    

def test_bar_updates(get_prepped_stuff):
    mystuff = get_prepped_stuff
    assert 2== mystuff.bar
    mystuff.bar = 300
    assert 300 == mystuff.bar
