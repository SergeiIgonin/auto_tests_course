"""
Проверка ожидаемого результата и фактического(переменные для примера)
"""
#expected_result = Input.text
#actual_result = Output.text
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
    f"expected {expected_result}, got {actual_result}"

"""
Проверка присутствия искомой части текста в полном тексте
"""
def test_substring(full_string, substring):
    assert substring in full_string, \
    f"expected '{substring}' to be substring of '{full_string}'"

#Пример:    
x = 'My Name is Julia'
if 'Name' in x:
    print('Substring found')
