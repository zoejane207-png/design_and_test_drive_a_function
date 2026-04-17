from lib.check_todo import *

def test_check_todo_returns_true_with_only_correct_todo():
    result = check_todo("#TODO")
    assert result == True

def test_check_todo_returns_true_with_todo_and_word():
    result = check_todo("#TODO walk")
    assert result == True

def test_check_todo_returns_false_for_empty_string():
    result = check_todo("")
    assert result == False

def test_check_todo_returns_false_when_todo_not_included():
    result = check_todo("go to the grocery store")
    assert result == False

def test_check_todo_returns_false_with_lowercase_todo():
    result = check_todo("#todo go to the grocery store")
    assert result == False

def test_check_todo_returns_false_when_no_hashtag():
    result = check_todo("TODO go to the grocery store")
    assert result == False