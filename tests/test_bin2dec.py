import pytest
from src.bin2dec import Bin2Dec

def test_create_object_of_type_bin2_dec():
	converter = Bin2Dec(101)

	assert isinstance(converter, Bin2Dec)

def test_get_number():
	converter = Bin2Dec(101)

	assert converter.get_number() == 101

def test_input_with_invalid_characters():
    with pytest.raises(ValueError):
        
        converter = Bin2Dec('abcde')

def test_input_must_allow_only_binary_number():
    with pytest.raises(ValueError):
        
        converter = Bin2Dec(12345)

def test_input_cannot_be_more_than_eight_digits():
    with pytest.raises(ValueError):
        
        converter = Bin2Dec(111100001111)

def test_convert_binary_to_decimal():
    converter = Bin2Dec(101)
    
    assert converter.convert_binary_to_decimal() == 5