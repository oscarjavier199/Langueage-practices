from name_function import get_formatted_name

def test_first_last_name():
    '''Do names like 'janis joplin' work? '''
    
    formatted_name = get_formatted_name('oscar', 'perez')
    assert formatted_name == 'Oscar Perez'


def test_first_last_middle_name():
    '''Do names like 'Albus wulfric Dumbledor' work? '''
    
    formatted_name = get_formatted_name('albus','dumbledor', 'wulfric')
    assert formatted_name == 'Albus Wulfric Dumbledor'

