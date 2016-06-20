import TString as ts

def test_two_words():
    assert ts.find_prefix("aab","aac") == "aa"
    print(".",end='')

def test_three_words():
    assert ts.find_prefix3("aab","aac","aad") == "aa"
    print(".",end='')

def test_list_of_words():
    assert ts.find_prefix_list(["aab","aac","aad","aaa","aar","aab"]) == "aa"
    print(".",end='')

def test_extract_decimal():
    pass
