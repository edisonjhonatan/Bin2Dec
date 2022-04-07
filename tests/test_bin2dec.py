import pytest
from src.bin2dec import Bin2Dec

def test_create_object_of_type_bin2_dec():
    """
    Test creating object of type Bin2Dec
    """
    converter = Bin2Dec(101)
    
    assert isinstance(converter, Bin2Dec)

def test_get_number():
    """
    Test getting number
    """
    converter = Bin2Dec(101)

    assert converter.get_number() == 101

def test_input_with_invalid_characters():
    """
    The number entered must be a binary number; number composed only of 0's and 1's.
    """
    with pytest.raises(ValueError):
        
        Bin2Dec('abcde')

def test_input_must_allow_only_binary_number():
    """
    The number entered must be a binary number; number composed only of 0's and 1's.
    """
    with pytest.raises(ValueError):
        
        Bin2Dec(12345)

def test_input_cannot_be_more_than_eight_digits():
    """
    As proposed by the problem described in the README, the binary number entered must not have more than 08 digits.
    """
    with pytest.raises(ValueError):
        
        Bin2Dec(111100001111)

def test_convert_binary_to_decimal():
    """
    After typing the binary number, its respective decimal number must be returned.
    """
    converter = Bin2Dec(101)
    
    assert converter.convert_binary_to_decimal() == 5