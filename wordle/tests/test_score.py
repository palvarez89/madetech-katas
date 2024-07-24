from main import calculate_score


def test_score_no_matching():
    target = "ropes"
    guess = "child"
    expected = "00000"
    score = calculate_score(target, guess)
    assert score == expected


def test_score_matching_correct_positions():
    target = "alert"
    guess = "alarm"
    expected = "22020"
    score = calculate_score(target, guess)
    assert score == expected


def test_score_char_in_wrong_position():
    target = "stair"
    guess = "chore"
    expected = "00010"
    score = calculate_score(target, guess)
    assert score == expected


def test_score_mix_match_and_wrong_position():
    target = "hairy"
    guess = "charm"
    expected = "01120"
    score = calculate_score(target, guess)
    assert score == expected


def test_score_multiple_in_wrong_position():
    target = "reads"
    guess = "elect"
    expected = "10000"
    score = calculate_score(target, guess)
    assert score == expected
