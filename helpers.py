from collections import OrderedDict
from dfa import DFA, ACCEPT, CONTINUE, TRAP
from colorama import Fore, Style

def new_dfa_from_patterns(patterns: list[str]) -> DFA:
    dfa = DFA()
    for pattern in patterns:
        dfa.insert(pattern)
    return dfa


def match_paragraph(dfa: DFA, paragraph: str) -> list[tuple[int, int, str]]:
    match_infos = []

    start = 0
    end = None
    match = ''

    for i, char in enumerate(paragraph):
        status, is_start = dfa.step_and_check(char)
        if status == ACCEPT:
            end = i
            match += char
            match_infos.append((start, end, match))
            match = ''
        elif is_start:
            start = i
            match = char
        elif status == CONTINUE:
            match += char
        elif status == TRAP:
            match = ''

    return match_infos


def display_match_infos(paragraph: str, match_infos: list[tuple[int, int, int]]):
    # step 1: create bolded paragraph
    def bold_paragraph() -> str:
        bolded_paragraph = ''
        if len(match_infos) == 0:
            bolded_paragraph = paragraph
        else:
            next_match_i = 0
            
            for i, char in enumerate(paragraph):
                if i == match_infos[next_match_i][0]:
                    bolded_paragraph += Fore.RED
                    bolded_paragraph += Style.BRIGHT
                bolded_paragraph += char
                if i == match_infos[next_match_i][1]:
                    bolded_paragraph += Style.RESET_ALL
                    if next_match_i < len(match_infos) - 1:
                        next_match_i += 1
        return bolded_paragraph


    def aggregate_matches():
        matches = OrderedDict()
        for match in match_infos:
            position = (match[0], match[1])
            if match[2] in matches:
                matches[match[2]].append(position)
            else:
                matches[match[2]] = [position]
        return matches

    
    def annotate_paragraph(matches: OrderedDict) -> str:
        counter = 0
        match_to_index = {}
        for i in matches.keys():
            match_to_index[i] = counter
            counter += 1

        annotated_paragraph = ''
        if len(match_infos) == 0:
            annotated_paragraph = paragraph
        else:
            next_match_i = 0
            
            for i, char in enumerate(paragraph):
                if i == match_infos[next_match_i][0]:
                    annotated_paragraph += Fore.RED
                    annotated_paragraph += Style.BRIGHT
                annotated_paragraph += char
                if i == match_infos[next_match_i][1]:
                    annotated_paragraph += Fore.BLUE
                    annotated_paragraph += f'({match_to_index[match_infos[next_match_i][2]] + 1})'
                    annotated_paragraph += Style.RESET_ALL
                    if next_match_i < len(match_infos) - 1:
                        next_match_i += 1
        return annotated_paragraph

    print('MATCHES:')
    print('{:<4} {:<30} {:<25} {:<70}\n'.format('No', 'Pattern', 'Number of occurences', 'Positions found'))
    aggregated = aggregate_matches()
    i = 0
    for k, v in aggregated.items():
        i += 1
        print('{:<4} {:<30} {:<25} {:<70}'.format(i, k, str(len(v)), ", ".join(map(lambda x: str(x), v))))
 
    print('\n'*5)
    print('PARAGRAPH:')
    print(bold_paragraph())
    print()
    annotated = annotate_paragraph(aggregated)
    print('\n'*5)
    print('ANNOTATED PARAGRAPH:')
    print(annotated)