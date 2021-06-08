from madlib_cli import __version__
from madlib_cli.madlib_cli import read_template, parse_template, merge

def test_version():
    assert __version__ == '0.1.0'

def test_read():
    actual = read_template('./assets/make_me_a_video_game_2.txt')
    expected = open('./assets/make_me_a_video_game_2.txt', 'r').read()
    assert expected == actual

def test_parse_template():
    actual = read_template('./assets/make_me_a_video_game_2.txt')
    expected = ['0', '1', '2', '3', '4', '5', '6', '7']
    assert expected == actual

def test_merge():
    actual = merge('Make Me A Video Game!\n I am {0} and {1} {2} have {3}{4}s {5} sister and plan to steal her {6} {7}!', ['suhib', 'lovely', 'taha', 'beautiful', 'pet', 'amazing', 'small', 'dogs'])
    expected = 'Make Me A Video Game!\n I am suhib and lovely taha have beautiful pets amazing sister and plan to steal her small dogs!'
    assert expected == actual

def test_parse():
    actual = parse_template('./assets/make_me_a_video_game_2.txt')
    expected = ['0', '1', '2', '3', '4', '5', '6', '7']
    assert actual == expected