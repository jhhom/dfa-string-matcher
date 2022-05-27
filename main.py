import json
from colorama import init as colorama_init
from helpers import new_dfa_from_patterns, match_paragraph, display_match_infos


if __name__ == '__main__':
    colorama_init()

    patterns = json.load(open('patterns.json', 'r'))
    dfa = new_dfa_from_patterns(patterns)
    input_text = open('input.txt', 'r').read()

    match_infos = match_paragraph(dfa, input_text)
    display_match_infos(input_text, match_infos)
    