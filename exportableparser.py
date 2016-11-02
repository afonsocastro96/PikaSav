import re


def validate_input(exportable):
    regex = '^([\w \-\'.,()?!/:;\[\]]{1,10}( \([\w \-\'.,()?!/:;\[\]]{1,10}\))?( \((M|F)\))?( @ [\w \-.]{1,20})?[ ]*\n'\
            'Ability: ([\w ]{1,20})?[ ]*\n(Level: \d{1,3}[ ]*\n)?(Shiny: (Yes|No)[ ]*\n)?(Happiness: \d{1,3}[ ]*\n)?' \
            '(EVs: (\d{1,3} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}(\d{1,3} (HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?' \
            '((Adamant|Bashful|Bold|Brave|Calm|Careful|Docile|Gentle|Hardy|Hasty|Impish|Jolly|Lax|Lonely|Mild|Modest|' \
            'Naive|Naughty|Quiet|Quirky|Rash|Relaxed|Sassy|Serious|Timid) Nature[ ]*\n)?' \
            '(IVs: (\d{1,2} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}(\d{1,3} (HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?' \
            '(- [\w \[\]-]{3,25}[ ]*\n?){1,4}[\n]*){1,6}$'

    multiple_teams_regex = '^(((=== .{1,100} ===)\n*)([\w \-\'.,()?!/:;\[\]]{1,10}( \([\w \-\'.,()?!/:;\[\]]{1,10}\))?'\
                           '( \((M|F)\))?( @ [\w \-.]{1,20})?[ ]*\nAbility: ([\w ]{1,20})?[ ]*\n' \
                           '(Level: \d{1,3}[ ]*\n)?(Shiny: (Yes|No)[ ]*\n)?(Happiness: \d{1,3}[ ]*\n)?' \
                           '(EVs: (\d{1,3} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}' \
                           '(\d{1,3} (HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?((Adamant|Bashful|Bold|Brave|Calm|Careful|' \
                           'Docile|Gentle|Hardy|Hasty|Impish|Jolly|Lax|Lonely|Mild|Modest|Naive|Naughty|Quiet|Quirky|' \
                           'Rash|Relaxed|Sassy|Serious|Timid) Nature[ ]*\n)?' \
                           '(IVs: (\d{1,2} (HP|Atk|Def|SpA|SpD|Spe) \/ ){0,5}(\d{1,3} ' \
                           '(HP|Atk|Def|SpA|SpD|Spe))[ ]*\n)?(- [\w \[\]-]{3,25}[ ]*\n?){1,4}[\n]*){1,6}){2,21}$'

    match = re.match(regex, exportable, 0)
    if not match:
        match = re.match(multiple_teams_regex, exportable, 0)
        if match:
            return 'multiple_teams'
        return False
    return 'single_team'


def create_exportable(pokemons):
    exportable = ''
    for pokemon in pokemons:
        pkmn_exportable = pokemon['Nickname'] + ' (' + pokemon['Pokemon'] + ') '
        if pokemon['Gender'] != 'L':
            pkmn_exportable += '(' + pokemon['Gender'] + ') '
        if pokemon['Item'] != '':
            pkmn_exportable += '@ ' + pokemon['Item']
        pkmn_exportable += '\nAbility: ' + pokemon['Ability'] + '\n'
        if pokemon['Level'] != 100:
            pkmn_exportable += 'Level: ' + str(pokemon['Level']) + '\n'
        if pokemon['Shiny'] == 'Yes':
            pkmn_exportable += 'Shiny: Yes\n'
        if pokemon['Happiness'] != 255:
            pkmn_exportable += 'Happiness: ' + str(pokemon['Happiness']) + '\n'
        pkmn_exportable += 'EVs: ' + str(pokemon['EVs'][0]) + ' HP / ' + str(pokemon['EVs'][1]) + ' Atk / ' +\
                           str(pokemon['EVs'][2]) + ' Def / ' + str(pokemon['EVs'][3]) + ' SpA / ' +\
                           str(pokemon['EVs'][4]) + ' SpD / ' + str(pokemon['EVs'][5]) + ' Spe\n'
        if pokemon['Nature'] != '':
            pkmn_exportable += pokemon['Nature'] + ' Nature\n'
        pkmn_exportable += 'IVs: ' + str(pokemon['IVs'][0]) + ' HP / ' + str(pokemon['IVs'][1]) + ' Atk / ' +\
                           str(pokemon['IVs'][2]) + ' Def / ' + str(pokemon['IVs'][3]) + ' SpA / ' +\
                           str(pokemon['IVs'][4]) + ' SpD / ' + str(pokemon['IVs'][5]) + ' Spe\n'

        for move in pokemon['Moves']:
            pkmn_exportable += '- ' + move + '\n'

        pkmn_exportable += '\n'
        exportable += pkmn_exportable
    exportable += '\n'
    return exportable


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
            first_line['Pokemon'] = line.replace(' ', '')

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
            for _ in range(4):
                if evs[i].isdigit():
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
        if pokemon[i][0] == '-':
            move = pokemon[i][2:]
            move = move[::-1]
            while move[0] == ' ':
                move = move.replace(' ', '', 1)
            move = move[::-1]
            moves.append(move)
    while len(moves) != 4:
        moves.append('')
    ret['Moves'] = moves

    keys = ['Ability', 'Level', 'Shiny', 'Happiness']

    for key in keys:
        if pokemon[line].find(key) != -1:
            string = pokemon[line][len(key) + 2:]
            string = string[::-1]
            while string[0] == ' ':
                string = string.replace(' ', '', 1)
            string = string[::-1]
            ret[key[:]] = string
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


def empty_evs(evs):
    stats = ['HP', 'Atk', 'Def', 'SpA', 'Spe']
    for i in range(len(stats)):
        if evs[stats[i]] != '':
            return False
    else:
        return True


def get_teams(lines):
    teams = []
    name = ''
    pokemons = []
    for line in lines:
        if '===' in line:
            if name != '':
                teams.append({'name': name, 'pokemons': list(pokemons)})
                pokemons = []
            beg = line.find('=')+4
            name = line[beg:line.find('=', beg)-1]
        else:
            pokemons.append(line)
    teams.append({'name': name, 'pokemons': list(pokemons)})
    return teams


def parse_exportable(exportable):
    exportable += '\n\n'
    v = validate_input(exportable)
    team = []
    ret = {}
    if v == 'single_team':
        for pokemon in get_pokemons(get_lines(exportable)):
            team.append(parse_pokemon(pokemon))
        ret['untitled'] = team
        return ret
    elif v == 'multiple_teams':
        teams = get_teams(get_lines(exportable))
        for t in teams:
            for pokemon in get_pokemons(t['pokemons']):
                team.append(parse_pokemon(pokemon))
            ret[t['name']] = team
            team = []
        return ret
    return False
