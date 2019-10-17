# print("hello")
def test_hello():
    print("\ntesting the words hello and goodbye")
    assert "hello" > "goodbye"
def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    print("\nsetting up module")

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print("\nteardown module")
def test_add():
    assert 1 == 2-1

# def setup_method(self, method):
#     print("\nmethod")
#
#
# def teardown_method(self, method):
#     """ teardown any state that was previously setup with a setup_method
#     call.
#     """
#     print("\nmethod")

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    print("\nsetup function")

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    print("\nteardown function")
