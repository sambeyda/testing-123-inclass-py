





from app.my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # note the function name is prefixed with "test_"
    result = enlarge(3) 
    assert result == 9