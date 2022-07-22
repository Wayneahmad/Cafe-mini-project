from file_manager import *



# UNIT TESTING UNIVERSAL INPUTS FUNCTIONS

def test_get_inputs():
    def mock_input(value):
        return "wayne"
    
    def get_inputs(values, input):
        name = input(f"\nAdd {values[1]}: ").title()
        value = input(f"Set {values[2]}: ")
        return name, value
    
    values = ("", "Hardick", "marshall" )
  
    expected = ("Wayne", "wayne")
    result = get_inputs(values, mock_input)

    assert expected == result
    print("TEST HAS PASSED!")
test_get_inputs()