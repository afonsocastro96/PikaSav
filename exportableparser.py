import re


def validate_input(exportable):
    regex = '^([\w -\'.,()?!/:;\[\]]{1,10}( \([\w -\'.,()?!/:;\[\]]{1,10}\))?( \((M|F)\))?( @ [\w -]{1,20})?[ ]*\n' \
            'Ability: ([\w ]{1,20})?[ ]*\n(Level: \d{1,3}[ ]*\n)?(Shiny: (Yes|No)[ ]*\n)?(Happiness: \d{1,3}[ ]*\n)?' \
            '(EVs: (\d{1,3} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}(\d{1,3} (HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?' \
            '((Adamant|Bashful|Bold|Brave|Calm|Careful|Docile|Gentle|Hardy|Hasty|Impish|Jolly|Lax|Lonely|Mild|Modest|' \
            'Naive|Naughty|Quiet|Quirky|Rash|Relaxed|Sassy|Serious|Timid) Nature[ ]*\n)?' \
            '(IVs: (\d{1,2} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}(\d{1,3} (HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?' \
            '(- [\w \[\]-]{4,20}[ ]*\n?){1,4}[\n]*){1,6}$'

    match = re.match(regex, exportable, 0)
    return match


def get_lines(p):
    tp = p
    lines = []
    while len(tp) > 0:
        t = tp.find('\n')
        if t == -1:
            break
        lines.append(tp[:t])
        tp = tp[t + 1:]
    return lines


def get_pokemons(lines):
    pokemons = []
    pokemon = []
    for i in range(len(lines)):
        if lines[i] == '':
            if len(pokemon) != 0:
                pokemons.append(pokemon)
            pokemon = []
        else:
            pokemon.append(lines[i])
    return pokemons


def parse_first_line(line):
    p1 = line.find('(')
    p2 = line.find('(', p1 + 1)
    i = line.find('@')
    first_line = {}

    if p1 != -1 and p2 != -1:
        f1 = line.find(')')
        first_line['Pokemon'] = line[p1 + 1:f1]
        first_line['Nickname'] = line[:p1 - 1]
        first_line['Gender'] = line[p2 + 1]

    elif p1 != -1:
        f1 = line.find(')')
        if f1 == (p1 + 2):
            first_line['Gender'] = line[p1 + 1]
            first_line['Pokemon'] = line[:p1 - 1]
            first_line['Nickname'] = ''
        else:
            first_line['Pokemon'] = line[p1 + 1:f1]
            first_line['Nickname'] = line[:p1 - 1]
            first_line['Gender'] = ''

    else:
        first_line['Gender'] = ''
        first_line['Nickname'] = ''
        if i != -1:
            first_line['Pokemon'] = line[:i - 1]
        else:
            first_line['Pokemon'] = line

    if i != -1:
        first_line['Item'] = line[i + 2:-2]
    else:
        first_line['Item'] = ''

    return first_line


def parse_stats(evs, values_type):
    ret = {}
    keys = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
    value = ''
    for key in keys:
        i = evs.find(key)
        if i != -1:
            if values_type == 'EVs':
                i -= 4
            else:
                i -= 3
            while evs[i].isdigit():
                value += evs[i]
                i += 1
            ret[key] = value
            value = ''
        else:
            ret[key] = ''
    return ret


def parse_pokemon(pokemon):
    moves = []
    line = 1

    ret = parse_first_line(pokemon[0])
    for i in range(len(pokemon) - 4, len(pokemon)):
        moves.append(pokemon[i][2:-2])
    ret['Moves'] = moves

    keys = ['Ability', 'Level', 'Shiny', 'Happiness']

    for key in keys:
        if pokemon[line].find(key) != -1:
            ret[key[:]] = pokemon[line][len(key) + 2:-2]
            line += 1
        else:
            ret[key] = ''

    e = pokemon[line].find('EVs')
    if e != -1:
        info = pokemon[line]
        ret['EVs'] = parse_stats(info, 'EVs')
        line += 1
    else:
        ret['EVs'] = {}
        ret['EVs']['HP'] = ''
        ret['EVs']['Atk'] = ''
        ret['EVs']['Def'] = ''
        ret['EVs']['SpA'] = ''
        ret['EVs']['SpD'] = ''
        ret['EVs']['Spe'] = ''

    nature = pokemon[line].find('Nature')
    if nature != -1:
        ret['Nature'] = pokemon[line][:nature - 1]
        line += 1
    else:
        ret['Nature'] = ''

    e = pokemon[line].find('IVs')
    if e != -1:
        info = pokemon[line]
        ret['IVs'] = parse_stats(info, 'IVs')
        line += 1
    else:
        ret['IVs'] = {}
        ret['IVs']['HP'] = ''
        ret['IVs']['Atk'] = ''
        ret['IVs']['Def'] = ''
        ret['IVs']['SpA'] = ''
        ret['IVs']['SpD'] = ''
        ret['IVs']['Spe'] = ''

    return ret


def parse_exportable(exportable):
    exportable += '\n\n'
    if validate_input(exportable):
        ret = []
        for pokemon in get_pokemons(get_lines(exportable)):
            ret.append(parse_pokemon(pokemon))
        return ret
    return False
