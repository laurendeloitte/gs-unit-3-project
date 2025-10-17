from lib.most_often import MostOften

#These tests check the MostOften class step by step

#The class should keep the list we give it at the start

def test_init_stores_starting_list():
    most_often = MostOften([1, 2, 3])
    assert most_often.starting_list == [1, 2, 3]

#Adding a new number should appear at the end

def test_function_to_appendix_to_existing_list():
    most_often = MostOften([1, 2, 3])
    most_often.add_new(4)
    assert most_often.starting_list == [1, 2, 3, 4]

#2 appears most often, so it should be returned

def test_to_see_most_common_num():
    most_often = MostOften([1, 2, 2, 2, 2, 3, 4, 5])
    assert most_often.get_most_often() == 2

#1 and 2 appear twice, so there is no clear winner as they are tied
def test_to_see_there_is_no_clear_winner_if_tie():
    most_often = MostOften([1, 1 , 2, 2, 3])
    assert most_often.get_most_often() == "no clear winner"

#No clear winner if there is an empty string    
def test_to_see_no_clear_winner_if_empty():
    most_often = MostOften("")
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_handles_strings():
    # Works with text items, not just numbers
    most_often = MostOften(["apple", "apple", "banana"])
    assert most_often.get_most_often() == "apple"


def test_add_new_can_change_winner_from_other_item():
    # Adding items can flip the winner
    most_often = MostOften([1, 1, 2])
    most_often.add_new(2)
    most_often.add_new(2)
    assert most_often.get_most_often() == 2


def test_get_most_often_no_winner_when_all_unique():
    # All items appear once, so theres no clear winner
    most_often = MostOften([7, 8, 9, 10])
    assert most_often.get_most_often() == "no clear winner"


def test_get_most_often_no_winner_after_add_creates_tie():
    # After adding, top counts tie, so theres no clear winner
    most_often = MostOften([3, 3, 2])
    most_often.add_new(2)
    assert most_often.get_most_often() == "no clear winner"


def test_add_new_accepts_strings():
    # Adding a string appends to the list
    most_often = MostOften(["a"])
    most_often.add_new("b")
    assert most_often.starting_list == ["a", "b"]


def test_get_most_often_with_negative_numbers():
    # Negative numbers are counted like any other value
    most_often = MostOften([-1, -1, 0, -2])
    assert most_often.get_most_often() == -1
