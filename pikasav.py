"""
Created on 07/04/2011

@author: Ritchie
"""
from Tkinter import *
from Tix import *
from tkFileDialog import *
from tkMessageBox import *
from random import randint

from parse import parse

from rbsav import RBSav
from gssav import GSSav
from crsav import CRSav
from rssav import RSSav
from exportableparser import *
import math
import os

items_rb = ['~0',
            'Master Ball',
            'Ultra Ball',
            'Great Ball',
            'Poke Ball',
            'Town Map',
            'Bicycle',
            '?????',
            'Safari Ball',
            'Pokedex',
            'Moon Stone',
            'Antidote',
            'Burn Heal',
            'Ice Heal',
            'Awakening',
            'Parlyz Heal',
            'Full Restore',
            'Max Potion',
            'Hyper Potion',
            'Super Potion',
            'Potion',
            'Boulderbadge',
            'Cascadebadge',
            'Thunderbadge',
            'Rainbowbadge',
            'Soulbadge',
            'Marshbadge',
            'Volcanobadge',
            'Earthbadge',
            'Escape Rope',
            'Repel',
            'Old Amber',
            'Fire Stone',
            'Thunderstone',
            'Water Stone',
            'HP Up',
            'Protein',
            'Iron',
            'Carbos',
            'Calcium',
            'Rare Candy',
            'Dome Fossil',
            'Helix Fossil',
            'Secret Key',
            '????? (44)',
            'Bike Voucher',
            'X Accuracy',
            'Leaf Stone',
            'Card Key',
            'Nugget',
            'PP Up',
            'Poke Doll',
            'Full Heal',
            'Revive',
            'Max Revive',
            'Guard Spec',
            'Super Repel',
            'Max Repel',
            'Dire Hit',
            'Coin',
            'Fresh Water',
            'Soda Pop',
            'Lemonade',
            'S.S.Ticket',
            'Gold Teeth',
            'X Attack',
            'X Defend',
            'X Speed',
            'X Special',
            'Coin Case',
            'Oak Parcel',
            'Itemfinder',
            'Silph Scope',
            'Poke Flute',
            'Lift Key',
            'Exp.All',
            'Old Rod',
            'Good Rod',
            'Super Rod',
            'Pp Up',
            'Ether',
            'Max Ether',
            'Elixer',
            'Max Elixer',
            '~84',
            '~85',
            '~86',
            '~87',
            '~88',
            '~89',
            '~90',
            '~91',
            '~92',
            '~93',
            '~94',
            '~95',
            '~96',
            '~97',
            '~98',
            '~99',
            '~100',
            '~101',
            '~102',
            '~103',
            '~104',
            '~105',
            '~106',
            '~107',
            '~108',
            '~109',
            '~110',
            '~111',
            '~112',
            '~113',
            '~163',
            '~115',
            '~116',
            '~117',
            '~118',
            '~119',
            '~120',
            '~121',
            '~122',
            '~123',
            '~124',
            '~125',
            '~126',
            '~127',
            '~128',
            '~129',
            '~130',
            '~131',
            '~132',
            '~133',
            '~134',
            '~135',
            '~136',
            '~137',
            '~138',
            '~139',
            '~140',
            '~141',
            '~142',
            '~143',
            '~144',
            '~145',
            '~146',
            '~147',
            '~148',
            '~149',
            '~150',
            '~151',
            '~152',
            '~153',
            '~154',
            '~155',
            '~156',
            '~163',
            '~158',
            '~159',
            '~160',
            '~161',
            '~162',
            '~163',
            '~164',
            '~165',
            '~166',
            '~167',
            '~168',
            '~169',
            '~170',
            '~171',
            '~172',
            '~173',
            '~174',
            '~175',
            '~176',
            '~177',
            '~178',
            '~179',
            '~180',
            '~181',
            '~182',
            '~183',
            '~184',
            '~185',
            '~186',
            '~187',
            '~188',
            '~189',
            '~190',
            '~191',
            '~192',
            '~193',
            '~194',
            '~195',
            'HM01',
            'HM02',
            'HM03',
            'HM04',
            'HM05',
            'TM01',
            'TM02',
            'TM03',
            'TM04',
            'TM05',
            'TM06',
            'TM07',
            'TM08',
            'TM09',
            'TM10',
            'TM11',
            'TM12',
            'TM13',
            'TM14',
            'TM15',
            'TM16',
            'TM17',
            'TM18',
            'TM19',
            'TM20',
            'TM21',
            'TM22',
            'TM23',
            'TM24',
            'TM25',
            'TM26',
            'TM27',
            'TM28',
            'TM29',
            'TM30',
            'TM31',
            'TM32',
            'TM33',
            'TM34',
            'TM35',
            'TM36',
            'TM37',
            'TM38',
            'TM39',
            'TM40',
            'TM41',
            'TM42',
            'TM43',
            'TM44',
            'TM45',
            'TM46',
            'TM47',
            'TM48',
            'TM49',
            'TM50',
            'TM51',
            'TM52',
            'TM53',
            'TM54',
            '-- Cancel -- (255)']
pokemon_rb = [' (0)',
              'Rhydon',
              'Kangaskhan',
              'Nidoranm',
              'Clefairy',
              'Spearow',
              'Voltorb',
              'Nidoking',
              'Slowbro',
              'Ivysaur',
              'Exeggutor',
              'Lickitung',
              'Exeggcute',
              'Grimer',
              'Gengar',
              'Nidoranh',
              'Nidoqueen',
              'Cubone',
              'Rhyhorn',
              'Lapras',
              'Arcanine',
              'Mew',
              'Gyarados',
              'Shellder',
              'Tentacool',
              'Gastly',
              'Scyther',
              'Staryu',
              'Blastoise',
              'Pinsir',
              'Tangela',
              'Missingno (31)',
              'Missingno (32)',
              'Growlithe',
              'Onix',
              'Fearow',
              'Pidgey',
              'Slowpoke',
              'Kadabra',
              'Graveler',
              'Chansey',
              'Machoke',
              'Mr. Mime',
              'Hitmonlee',
              'Hitmonchan',
              'Arbok',
              'Parasect',
              'Psyduck',
              'Drowzee',
              'Golem',
              'Missingno (50)',
              'Magmar',
              'Missingno (52)',
              'Electabuzz',
              'Magneton',
              'Koffing',
              'Missingno (56)',
              'Mankey',
              'Seel',
              'Diglett',
              'Tauros',
              'Missingno (61)',
              'Missingno (62)',
              'Missingno (63)',
              "Farfetch'd",
              'Venonat',
              'Dragonite',
              'Missingno (67)',
              'Missingno (68)',
              'Missingno (69)',
              'Doduo',
              'Poliwag',
              'Jynx',
              'Moltres',
              'Articuno',
              'Zapdos',
              'Ditto',
              'Meowth',
              'Krabby',
              'Missingno (79)',
              'Missingno (80)',
              'Missingno (81)',
              'Vulpix',
              'Ninetales',
              'Pikachu',
              'Raichu',
              'Missingno',
              'Missingno',
              'Dratini',
              'Dragonair',
              'Kabuto',
              'Kabutops',
              'Horsea',
              'Seadra',
              'Missingno',
              'Missingno',
              'Sandshrew',
              'Sandslash',
              'Omanyte',
              'Omastar',
              'Jigglypuff',
              'Wigglytuff',
              'Eevee',
              'Flareon',
              'Jolteon',
              'Vaporeon',
              'Machop',
              'Zubat',
              'Ekans',
              'Paras',
              'Poliwhirl',
              'Poliwrath',
              'Weedle',
              'Kakuna',
              'Beedrill',
              'Missingno (115)',
              'Dodrio',
              'Primeape',
              'Dugtrio',
              'Venomoth',
              'Dewgong',
              'Missingno (121)',
              'Missingno (122)',
              'Caterpie',
              'Metapod',
              'Butterfree',
              'Machamp',
              'Missingno (127)',
              'Golduck',
              'Hypno',
              'Golbat',
              'Mewtwo',
              'Snorlax',
              'Magikarp',
              'Missingno (134)',
              'Missingno (135)',
              'Muk',
              'Missingno (137)',
              'Kingler',
              'Cloyster',
              'Missingno (140)',
              'Electrode',
              'Clefable',
              'Weezing',
              'Persian',
              'Marowak',
              'Missingno (146)',
              'Haunter',
              'Abra',
              'Alakazam',
              'Pidgeotto',
              'Pidgeot',
              'Starmie',
              'Bulbasaur',
              'Venusaur',
              'Tentacruel',
              'Missingno (156)',
              'Goldeen',
              'Seaking',
              'Missingno (159)',
              'Missingno (160)',
              'Missingno (161)',
              'Missingno (162)',
              'Ponyta',
              'Rapidash',
              'Rattata',
              'Raticate',
              'Nidorino',
              'Nidorina',
              'Geodude',
              'Porygon',
              'Aerodactyl',
              'Missingno (172)',
              'Magnemite',
              'Missingno (174)',
              'Missingno (175)',
              'Charmander',
              'Squirtle',
              'Charmeleon',
              'Wartortle',
              'Charizard (180)',
              'Missingno (181)',
              'Missingno (182)',
              'Missingno (183)',
              'Missingno (184)',
              'Oddish',
              'Gloom',
              'Vileplume',
              'Bellsprout',
              'Weepinbell',
              'Victreebel',
              '~191',
              '~192',
              '~193',
              '~194',
              '~195',
              '~196',
              '~197',
              '~198',
              '~199',
              '~200',
              '~201',
              '~202',
              '~203',
              '~204',
              '~205',
              '~206',
              '~207',
              '~208',
              '~209',
              '~210',
              '~211',
              '~212',
              '~213',
              '~214',
              '~215',
              '~216',
              '~217',
              '~218',
              '~219',
              '~220',
              '~221',
              '~222',
              '~223',
              '~224',
              '~225',
              '~226',
              '~227',
              '~228',
              '~229',
              '~230',
              '~231',
              '~232',
              '~233',
              '~234',
              '~235',
              '~236',
              '~237',
              '~238',
              '~239',
              '~240',
              '~241',
              '~242',
              '~243',
              '~244',
              '~245',
              '~246',
              '~247',
              '~248',
              '~249',
              '~250',
              '~251',
              '~252',
              '~253',
              '~254',
              '-- No Pokemon -- (255)']
pokemon_lower_rb = ['',
                    'rhydon',
                    'kangaskhan',
                    'nidoranm',
                    'clefairy',
                    'spearow',
                    'voltorb',
                    'nidoking',
                    'slowbro',
                    'ivysaur',
                    'exeggutor',
                    'lickitung',
                    'exeggcute',
                    'grimer',
                    'gengar',
                    'nidoranh',
                    'nidoqueen',
                    'cubone',
                    'rhyhorn',
                    'lapras',
                    'arcanine',
                    'mew',
                    'gyarados',
                    'shellder',
                    'tentacool',
                    'gastly',
                    'scyther',
                    'staryu',
                    'blastoise',
                    'pinsir',
                    'tangela',
                    'missingno.',
                    'missingno.',
                    'growlithe',
                    'onix',
                    'fearow',
                    'pidgey',
                    'slowpoke',
                    'kadabra',
                    'graveler',
                    'chansey',
                    'machoke',
                    'mr.mime',
                    'hitmonlee',
                    'hitmonchan',
                    'arbok',
                    'parasect',
                    'psyduck',
                    'drowzee',
                    'golem',
                    'missingno.',
                    'magmar',
                    'missingno.',
                    'electabuzz',
                    'magneton',
                    'koffing',
                    'missingno.',
                    'mankey',
                    'seel',
                    'diglett',
                    'tauros',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    "farfetch'd",
                    'venonat',
                    'dragonite',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'doduo',
                    'poliwag',
                    'jynx',
                    'moltres',
                    'articuno',
                    'zapdos',
                    'ditto',
                    'meowth',
                    'krabby',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'vulpix',
                    'ninetales',
                    'pikachu',
                    'raichu',
                    'missingno.',
                    'missingno.',
                    'dratini',
                    'dragonair',
                    'kabuto',
                    'kabutops',
                    'horsea',
                    'seadra',
                    'missingno.',
                    'missingno.',
                    'sandshrew',
                    'sandslash',
                    'omanyte',
                    'omastar',
                    'jigglypuff',
                    'wigglytuff',
                    'eevee',
                    'flareon',
                    'jolteon',
                    'vaporeon',
                    'machop',
                    'zubat',
                    'ekans',
                    'paras',
                    'poliwhirl',
                    'poliwrath',
                    'weedle',
                    'kakuna',
                    'beedrill',
                    'missingno.',
                    'dodrio',
                    'primeape',
                    'dugtrio',
                    'venomoth',
                    'dewgong',
                    'missingno.',
                    'missingno.',
                    'caterpie',
                    'metapod',
                    'butterfree',
                    'machamp',
                    'missingno.',
                    'golduck',
                    'hypno',
                    'golbat',
                    'mewtwo',
                    'snorlax',
                    'magikarp',
                    'missingno.',
                    'missingno.',
                    'muk',
                    'missingno.',
                    'kingler',
                    'cloyster',
                    'missingno.',
                    'electrode',
                    'clefable',
                    'weezing',
                    'persian',
                    'marowak',
                    'missingno.',
                    'haunter',
                    'abra',
                    'alakazam',
                    'pidgeotto',
                    'pidgeot',
                    'starmie',
                    'bulbasaur',
                    'venusaur',
                    'tentacruel',
                    'missingno.',
                    'goldeen',
                    'seaking',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'ponyta',
                    'rapidash',
                    'rattata',
                    'raticate',
                    'nidorino',
                    'nidorina',
                    'geodude',
                    'porygon',
                    'aerodactyl',
                    'missingno.',
                    'magnemite',
                    'missingno.',
                    'missingno.',
                    'charmander',
                    'squirtle',
                    'charmeleon',
                    'wartortle',
                    'charizard',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'missingno.',
                    'oddish',
                    'gloom',
                    'vileplume',
                    'bellsprout',
                    'weepinbell',
                    'victreebel',
                    '191',
                    '192',
                    '193',
                    '194',
                    '195',
                    '196',
                    '197',
                    '198',
                    '199',
                    '200',
                    '201',
                    '202',
                    '203',
                    '204',
                    '205',
                    '206',
                    '207',
                    '208',
                    '209',
                    '210',
                    '211',
                    '212',
                    '213',
                    '214',
                    '215',
                    '216',
                    '217',
                    '218',
                    '219',
                    '220',
                    '221',
                    '222',
                    '223',
                    '224',
                    '225',
                    '226',
                    '227',
                    '228',
                    '229',
                    '230',
                    '231',
                    '232',
                    '233',
                    '234',
                    '235',
                    '236',
                    '237',
                    '238',
                    '239',
                    '240',
                    '241',
                    '242',
                    '243',
                    '244',
                    '245',
                    '246',
                    '247',
                    '248',
                    '249',
                    '250',
                    '251',
                    '252',
                    '253',
                    '254',
                    '']
pokedex_rb = ['#000 Missingno',
              '#001 Bulbasaur',
              '#002 Ivysaur',
              '#003 Venusaur',
              '#004 Charmander',
              '#005 Charmeleon',
              '#006 Charizard',
              '#007 Squirtle',
              '#008 Wartortle',
              '#009 Blastoise',
              '#010 Caterpie',
              '#011 Metapod',
              '#012 Butterfree',
              '#013 Weedle',
              '#014 Kakuna',
              '#015 Beedrill',
              '#016 Pidgey',
              '#017 Pidgeotto',
              '#018 Pidgeot',
              '#019 Rattata',
              '#020 Raticate',
              '#021 Spearow',
              '#022 Fearow',
              '#023 Ekans',
              '#024 Arbok',
              '#025 Pikachu',
              '#026 Raichu',
              '#027 Sandshrew',
              '#028 Sandslash',
              '#029 Nidoranh',
              '#030 Nidorina',
              '#031 Nidoqueen',
              '#032 Nidoranm',
              '#033 Nidorino',
              '#034 Nidoking',
              '#035 Clefairy',
              '#036 Clefable',
              '#037 Vulpix',
              '#038 Ninetales',
              '#039 Jigglypuff',
              '#040 Wigglytuff',
              '#041 Zubat',
              '#042 Golbat',
              '#043 Oddish',
              '#044 Gloom',
              '#045 Vileplume',
              '#046 Paras',
              '#047 Parasect',
              '#048 Venonat',
              '#049 Venomoth',
              '#050 Diglett',
              '#051 Dugtrio',
              '#052 Meowth',
              '#053 Persian',
              '#054 Psyduck',
              '#055 Golduck',
              '#056 Mankey',
              '#057 Primeape',
              '#058 Growlithe',
              '#059 Arcanine',
              '#060 Poliwag',
              '#061 Poliwhirl',
              '#062 Poliwrath',
              '#063 Abra',
              '#064 Kadabra',
              '#065 Alakazam',
              '#066 Machop',
              '#067 Machoke',
              '#068 Machamp',
              '#069 Bellsprout',
              '#070 Weepinbell',
              '#071 Victreebel',
              '#072 Tentacool',
              '#073 Tentacruel',
              '#074 Geodude',
              '#075 Graveler',
              '#076 Golem',
              '#077 Ponyta',
              '#078 Rapidash',
              '#079 Slowpoke',
              '#080 Slowbro',
              '#081 Magnemite',
              '#082 Magneton',
              "#083 Farfetch'd",
              '#084 Doduo',
              '#085 Dodrio',
              '#086 Seel',
              '#087 Dewgong',
              '#088 Grimer',
              '#089 Muk',
              '#090 Shellder',
              '#091 Cloyster',
              '#092 Gastly',
              '#093 Haunter',
              '#094 Gengar',
              '#095 Onix',
              '#096 Drowzee',
              '#097 Hypno',
              '#098 Krabby',
              '#099 Kingler',
              '#100 Voltorb',
              '#101 Electrode',
              '#102 Exeggcute',
              '#103 Exeggutor',
              '#104 Cubone',
              '#105 Marowak',
              '#106 Hitmonlee',
              '#107 Hitmonchan',
              '#108 Lickitung',
              '#109 Koffing',
              '#110 Weezing',
              '#111 Rhyhorn',
              '#112 Rhydon',
              '#113 Chansey',
              '#163 Tangela',
              '#115 Kangaskhan',
              '#116 Horsea',
              '#117 Seadra',
              '#118 Goldeen',
              '#119 Seaking',
              '#120 Staryu',
              '#121 Starmie',
              '#122 Mr. Mime',
              '#123 Scyther',
              '#124 Jynx',
              '#125 Electabuzz',
              '#126 Magmar',
              '#127 Pinsir',
              '#128 Tauros',
              '#129 Magikarp',
              '#130 Gyarados',
              '#131 Lapras',
              '#132 Ditto',
              '#133 Eevee',
              '#134 Vaporeon',
              '#135 Jolteon',
              '#136 Flareon',
              '#137 Porygon',
              '#138 Omanyte',
              '#139 Omastar',
              '#140 Kabuto',
              '#141 Kabutops',
              '#142 Aerodactyl',
              '#143 Snorlax',
              '#144 Articuno',
              '#145 Zapdos',
              '#146 Moltres',
              '#147 Dratini',
              '#148 Dragonair',
              '#149 Dragonite',
              '#150 Mewtwo',
              '#151 Mew',
              '#152',
              '#153',
              '#154',
              '#155',
              '#156',
              '#163',
              '#158',
              '#159',
              '#160',
              '#161',
              '#162',
              '#163',
              '#164',
              '#165',
              '#166',
              '#167',
              '#168',
              '#169',
              '#170',
              '#171',
              '#172',
              '#173',
              '#174',
              '#175',
              '#176',
              '#177',
              '#178',
              '#179',
              '#180',
              '#181',
              '#182',
              '#183',
              '#184',
              '#185',
              '#186',
              '#187',
              '#188',
              '#189',
              '#190',
              '#191',
              '#192',
              '#193',
              '#194',
              '#195',
              '#196',
              '#197',
              '#198',
              '#199',
              '#200',
              '#201',
              '#202',
              '#203',
              '#204',
              '#205',
              '#206',
              '#207',
              '#208',
              '#209',
              '#210',
              '#211',
              '#212',
              '#213',
              '#214',
              '#215',
              '#216',
              '#217',
              '#218',
              '#219',
              '#220',
              '#221',
              '#222',
              '#223',
              '#224',
              '#225',
              '#226',
              '#227',
              '#228',
              '#229',
              '#230',
              '#231',
              '#232',
              '#233',
              '#234',
              '#235',
              '#236',
              '#237',
              '#238',
              '#239',
              '#240',
              '#241',
              '#242',
              '#243',
              '#244',
              '#245',
              '#246',
              '#247',
              '#248',
              '#249',
              '#250',
              '#251',
              '#252',
              '#253',
              '#254',
              '#255']
moves_rb = ['-- No Move -- (0)',
            'Pound',
            'Karate Chop',
            'Doubleslap',
            'Comet Punch',
            'Mega Punch',
            'Pay Day',
            'Fire Punch',
            'Ice Punch',
            'Thunderpunch',
            'Scratch',
            'Vicegrip',
            'Guillotine',
            'Razor Wind',
            'Swords Dance',
            'Cut',
            'Gust',
            'Wing Attack',
            'Whirlwind',
            'Fly',
            'Bind',
            'Slam',
            'Vine Whip',
            'Stomp',
            'Double Kick',
            'Mega Kick',
            'Jump Kick',
            'Rolling Kick',
            'Sand-attack',
            'Headbutt',
            'Horn Attack',
            'Fury Attack',
            'Horn Drill',
            'Tackle',
            'Body Slam',
            'Wrap',
            'Take Down',
            'Thrash',
            'Double-edge',
            'Tail Whip',
            'Poison Sting',
            'Twineedle',
            'Pin Missile',
            'Leer',
            'Bite',
            'Growl',
            'Roar',
            'Sing',
            'Supersonic',
            'Sonicboom',
            'Disable',
            'Acid',
            'Ember',
            'Flamethrower',
            'Mist',
            'Water Gun',
            'Hydro Pump',
            'Surf',
            'Ice Beam',
            'Blizzard',
            'Psybeam',
            'Bubblebeam',
            'Aurora Beam',
            'Hyper Beam',
            'Peck',
            'Drill Peck',
            'Submission',
            'Low Kick',
            'Counter',
            'Seismic Toss',
            'Strength',
            'Absorb',
            'Mega Drain',
            'Leech Seed',
            'Growth',
            'Razor Leaf',
            'Solarbeam',
            'Poisonpowder',
            'Stun Spore',
            'Sleep Powder',
            'Petal Dance',
            'String Shot',
            'Dragon Rage',
            'Fire Spin',
            'Thundershock',
            'Thunderbolt',
            'Thunder Wave',
            'Thunder',
            'Rock Throw',
            'Earthquake',
            'Fissure',
            'Dig',
            'Toxic',
            'Confusion',
            'Psychic',
            'Hypnosis',
            'Meditate',
            'Agility',
            'Quick Attack',
            'Rage',
            'Teleport',
            'Night Shade',
            'Mimic',
            'Screech',
            'Double Team',
            'Recover',
            'Harden',
            'Minimize',
            'Smokescreen',
            'Confuse Ray',
            'Withdraw',
            'Defense Curl',
            'Barrier',
            'Light Screen',
            'Haze',
            'Reflect',
            'Focus Energy',
            'Bide',
            'Metronome',
            'Mirror Move',
            'Selfdestruct',
            'Egg Bomb',
            'Lick',
            'Smog',
            'Sludge',
            'Bone Club',
            'Fire Blast',
            'Waterfall',
            'Clamp',
            'Swift',
            'Skull Bash',
            'Spike Cannon',
            'Constrict',
            'Amnesia',
            'Kinesis',
            'Softboiled',
            'Hi Jump Kick',
            'Glare',
            'Dream Eater',
            'Poison Gas',
            'Barrage',
            'Leech Life',
            'Lovely Kiss',
            'Sky Attack',
            'Transform',
            'Bubble',
            'Dizzy Punch',
            'Spore',
            'Flash',
            'Psywave',
            'Splash',
            'Acid Armor',
            'Crabhammer',
            'Explosion',
            'Fury Swipes',
            'Bonemerang',
            'Rest',
            'Rock Slide',
            'Hyper Fang',
            'Sharpen',
            'Conversion',
            'Tri Attack',
            'Super Fang',
            'Slash',
            'Substitute',
            'Struggle',
            '~166',
            '~167',
            '~168',
            '~169',
            '~170',
            '~171',
            '~172',
            '~173',
            '~174',
            '~175',
            '~176',
            '~177',
            '~178',
            '~179',
            '~180',
            '~181',
            '~182',
            '~183',
            '~184',
            '~185',
            '~186',
            '~187',
            '~188',
            '~189',
            '~190',
            '~191',
            '~192',
            '~193',
            '~194',
            '~195',
            '~196',
            '~197',
            '~198',
            '~199',
            '~200',
            '~201',
            '~202',
            '~203',
            '~204',
            '~205',
            '~206',
            '~207',
            '~208',
            '~209',
            '~210',
            '~211',
            '~212',
            '~213',
            '~214',
            '~215',
            '~216',
            '~217',
            '~218',
            '~219',
            '~220',
            '~221',
            '~222',
            '~223',
            '~224',
            '~225',
            '~226',
            '~227',
            '~228',
            '~229',
            '~230',
            '~231',
            '~232',
            '~233',
            '~234',
            '~235',
            '~236',
            '~237',
            '~238',
            '~239',
            '~240',
            '~241',
            '~242',
            '~243',
            '~244',
            '~245',
            '~246',
            '~247',
            '~248',
            '~249',
            '~250',
            '~251',
            '~252',
            '~253',
            '~254',
            '~255']
types_rb = ['Normal',
            'Fighting',
            'Flying',
            'Poison',
            'Ground',
            'Rock',
            'Bird',
            'Bug',
            'Ghost',
            '~9',
            '~10',
            '~11',
            '~12',
            '~13',
            '~14',
            '~15',
            '~16',
            '~17',
            '~18',
            '~19',
            'Fire',
            'Water',
            'Grass',
            'Electric',
            'Psychic',
            'Ice',
            'Dragon',
            '~27',
            '~28',
            '~29',
            '~30',
            '~31',
            '~32',
            '~33',
            '~34',
            '~35',
            '~36',
            '~37',
            '~38',
            '~39',
            '~40',
            '~41',
            '~42',
            '~43',
            '~44',
            '~45',
            '~46',
            '~47',
            '~48',
            '~49',
            '~50',
            '~51',
            '~52',
            '~53',
            '~54',
            '~55',
            '~56',
            '~57',
            '~58',
            '~59',
            '~60',
            '~61',
            '~62',
            '~63',
            '~64',
            '~65',
            '~66',
            '~67',
            '~68',
            '~69',
            '~70',
            '~71',
            '~72',
            '~73',
            '~74',
            '~75',
            '~76',
            '~77',
            '~78',
            '~79',
            '~80',
            '~81',
            '~82',
            '~83',
            '~84',
            '~85',
            '~86',
            '~87',
            '~88',
            '~89',
            '~90',
            '~91',
            '~92',
            '~93',
            '~94',
            '~95',
            '~96',
            '~97',
            '~98',
            '~99',
            '~100',
            '~101',
            '~102',
            '~103',
            '~104',
            '~105',
            '~106',
            '~107',
            '~108',
            '~109',
            '~110',
            '~111',
            '~112',
            '~113',
            '~163',
            '~115',
            '~116',
            '~117',
            '~118',
            '~119',
            '~120',
            '~121',
            '~122',
            '~123',
            '~124',
            '~125',
            '~126',
            '~127',
            '~128',
            '~129',
            '~130',
            '~131',
            '~132',
            '~133',
            '~134',
            '~135',
            '~136',
            '~137',
            '~138',
            '~139',
            '~140',
            '~141',
            '~142',
            '~143',
            '~144',
            '~145',
            '~146',
            '~147',
            '~148',
            '~149',
            '~150',
            '~151',
            '~152',
            '~153',
            '~154',
            '~155',
            '~156',
            '~163',
            '~158',
            '~159',
            '~160',
            '~161',
            '~162',
            '~163',
            '~164',
            '~165',
            '~166',
            '~167',
            '~168',
            '~169',
            '~170',
            '~171',
            '~172',
            '~173',
            '~174',
            '~175',
            '~176',
            '~177',
            '~178',
            '~179',
            '~180',
            '~181',
            '~182',
            '~183',
            '~184',
            '~185',
            '~186',
            '~187',
            '~188',
            '~189',
            '~190',
            '~191',
            '~192',
            '~193',
            '~194',
            '~195',
            '~196',
            '~197',
            '~198',
            '~199',
            '~200',
            '~201',
            '~202',
            '~203',
            '~204',
            '~205',
            '~206',
            '~207',
            '~208',
            '~209',
            '~210',
            '~211',
            '~212',
            '~213',
            '~214',
            '~215',
            '~216',
            '~217',
            '~218',
            '~219',
            '~220',
            '~221',
            '~222',
            '~223',
            '~224',
            '~225',
            '~226',
            '~227',
            '~228',
            '~229',
            '~230',
            '~231',
            '~232',
            '~233',
            '~234',
            '~235',
            '~236',
            '~237',
            '~238',
            '~239',
            '~240',
            '~241',
            '~242',
            '~243',
            '~244',
            '~245',
            '~246',
            '~247',
            '~248',
            '~249',
            '~250',
            '~251',
            '~252',
            '~253',
            '~254',
            '~255']
items_gs = ['~0',
            'Master Ball',
            'Ultra Ball',
            'Brightpowder',
            'Great Ball',
            'Pok\xc3\xa9 Ball',
            'Teru-sama (6)',
            'Bicycle',
            'Moon Stone',
            'Antidote',
            'Burn Heal',
            'Ice Heal',
            'Awakening',
            'Parlyz Heal',
            'Full Restore',
            'Max Potion',
            'Hyper Potion',
            'Super Potion',
            'Potion',
            'Escape Rope',
            'Repel',
            'Max Elixer',
            'Fire Stone',
            'Thunderstone',
            'Water Stone',
            'Teru-sama (25)',
            'HP Up',
            'Protein',
            'Iron',
            'Carbos',
            'Lucky Punch',
            'Calcium',
            'Rare Candy',
            'X Accuracy',
            'Leaf Stone',
            'Metal Powder',
            'Nugget',
            'Pok\xc3\xa9 Doll',
            'Full Heal',
            'Revive',
            'Max Revive',
            'Guard Spec.',
            'Super Repel',
            'Max Repel',
            'Dire Hit',
            'Teru-sama (45)',
            'Fresh Water',
            'Soda Pop',
            'Lemonade',
            'X Attack',
            'Teru-sama (50)',
            'X Defend',
            'X Speed',
            'X Special',
            'Coin Case',
            'Itemfinder',
            'Teru-sama (56)',
            'Exp.share',
            'Old Rod',
            'Good Rod',
            'Silver Leaf',
            'Super Rod',
            'PP Up',
            'Ether',
            'Max Ether',
            'Elixer',
            'Red Scale',
            'Secretpotion',
            'S.s.ticket',
            'Mystery Egg',
            'Teru-sama (70)',
            'Silver Wing',
            'Moomoo Milk',
            'Quick Claw',
            'Psncureberry',
            'Gold Leaf',
            'Soft Sand',
            'Sharp Beak',
            'Przcureberry',
            'Burnt Berry',
            'Ice Berry',
            'Poison Barb',
            "King's Rock",
            'Bitter Berry',
            'Mint Berry',
            'Red Apricorn',
            'Tinymushroom',
            'Big Mushroom',
            'Silverpowder',
            'Blu Apricorn',
            'Teru-sama (90)',
            'Amulet Coin',
            'Ylw Apricorn',
            'Grn Apricorn',
            'Cleanse Tag',
            'Mystic Water',
            'Twistedspoon',
            'Wht Apricorn',
            'Blackbelt',
            'Blk Apricorn',
            'Teru-sama',
            'Pnk Apricorn',
            'Blackglasses',
            'Slowpoketail',
            'Pink Bow',
            'Stick',
            'Smoke Ball',
            'Nevermeltice',
            'Magnet',
            'Miracleberry',
            'Pearl',
            'Big Pearl',
            'Everstone',
            'Spell Tag',
            'Ragecandybar',
            'Teru-sama (115)',
            'Teru-sama (116)',
            'Miracle Seed',
            'Thick Club',
            'Focus Band',
            'Teru-sama (120)',
            'Energypowder',
            'Energy Root',
            'Heal Powder',
            'Revival Herb',
            'Hard Stone',
            'Lucky Egg',
            'Card Key',
            'Machine Part',
            'Teru-sama (129)',
            'Lost Item',
            'Stardust',
            'Star Piece',
            'Basement Key',
            'Pass',
            'Teru-sama (135)',
            'Teru-sama (136)',
            'Teru-sama (137)',
            'Charcoal',
            'Berry Juice',
            'Scope Lens',
            'Teru-sama (141)',
            'Teru-sama (142)',
            'Metal Coat',
            'Dragon Fang',
            'Teru-sama (145)',
            'Leftovers',
            'Teru-sama (147)',
            'Teru-sama (148)',
            'Teru-sama (149)',
            'Mysteryberry',
            'Dragon Scale',
            'Berserk Gene',
            'Teru-sama (153)',
            'Teru-sama (154)',
            'Teru-sama (155)',
            'Sacred Ash',
            'Heavy Ball',
            'Flower Mail',
            'Level Ball',
            'Lure Ball',
            'Fast Ball',
            'Teru-sama (162)',
            'Light Ball',
            'Friend Ball',
            'Moon Ball',
            'Love Ball',
            'Normal Box',
            'Gorgeous Box',
            'Sun Stone',
            'Polkadot Bow',
            'Teru-sama (171)',
            'Up-grade',
            'Berry',
            'Gold Berry',
            'Squirtbottle',
            'Teru-sama (176)',
            'Park Ball',
            'Rainbow Wing',
            'Teru-sama (179)',
            'Brick Piece',
            'Surf Mail',
            'Litebluemail',
            'Portraitmail',
            'Lovely Mail',
            'Eon Mail',
            'Morph Mail',
            'Bluesky Mail',
            'Music Mail',
            'Mirage Mail',
            'Teru-sama (190)',
            'TM01',
            'TM02',
            'TM03',
            'TM04',
            'Teru-sama (195)',
            'TM05',
            'TM06',
            'TM07',
            'TM08',
            'TM09',
            'TM10',
            'TM11',
            'TM12',
            'TM13',
            'TM14',
            'TM15',
            'TM16',
            'TM17',
            'TM18',
            'TM19',
            'TM20',
            'TM21',
            'TM22',
            'TM23',
            'TM24',
            'TM25',
            'TM26',
            'TM27',
            'TM28',
            'Teru-sama (220)',
            'TM29',
            'TM30',
            'TM31',
            'TM32',
            'TM33',
            'TM34',
            'TM35',
            'TM36',
            'TM37',
            'TM38',
            'TM39',
            'TM40',
            'TM41',
            'TM42',
            'TM43',
            'TM44',
            'TM45',
            'TM46',
            'TM47',
            'TM48',
            'TM49',
            'TM50',
            'HM01',
            'HM02',
            'HM03',
            'HM04',
            'HM05',
            'HM06',
            'HM07',
            'Teru-sama (250)',
            'Teru-sama (251)',
            'Teru-sama (252)',
            'Teru-sama (253)',
            'Teru-sama (254)',
            '-- Cancel -- (255)']
pokemon_gs = ['0',
              'Bulbasaur',
              'Ivysaur',
              'Venusaur',
              'Charmander',
              'Charmeleon',
              'Charizard',
              'Squirtle',
              'Wartortle',
              'Blastoise',
              'Caterpie',
              'Metapod',
              'Butterfree',
              'Weedle',
              'Kakuna',
              'Beedrill',
              'Pidgey',
              'Pidgeotto',
              'Pidgeot',
              'Rattata',
              'Raticate',
              'Spearow',
              'Fearow',
              'Ekans',
              'Arbok',
              'Pikachu',
              'Raichu',
              'Sandshrew',
              'Sandslash',
              'Nidoranh',
              'Nidorina',
              'Nidoqueen',
              'Nidoranm',
              'Nidorino',
              'Nidoking',
              'Clefairy',
              'Clefable',
              'Vulpix',
              'Ninetales',
              'Jigglypuff',
              'Wigglytuff',
              'Zubat',
              'Golbat',
              'Oddish',
              'Gloom',
              'Vileplume',
              'Paras',
              'Parasect',
              'Venonat',
              'Venomoth',
              'Diglett',
              'Dugtrio',
              'Meowth',
              'Persian',
              'Psyduck',
              'Golduck',
              'Mankey',
              'Primeape',
              'Growlithe',
              'Arcanine',
              'Poliwag',
              'Poliwhirl',
              'Poliwrath',
              'Abra',
              'Kadabra',
              'Alakazam',
              'Machop',
              'Machoke',
              'Machamp',
              'Bellsprout',
              'Weepinbell',
              'Victreebel',
              'Tentacool',
              'Tentacruel',
              'Geodude',
              'Graveler',
              'Golem',
              'Ponyta',
              'Rapidash',
              'Slowpoke',
              'Slowbro',
              'Magnemite',
              'Magneton',
              "Farfetch'd",
              'Doduo',
              'Dodrio',
              'Seel',
              'Dewgong',
              'Grimer',
              'Muk',
              'Shellder',
              'Cloyster',
              'Gastly',
              'Haunter',
              'Gengar',
              'Onix',
              'Drowzee',
              'Hypno',
              'Krabby',
              'Kingler',
              'Voltorb',
              'Electrode',
              'Exeggcute',
              'Exeggutor',
              'Cubone',
              'Marowak',
              'Hitmonlee',
              'Hitmonchan',
              'Lickitung',
              'Koffing',
              'Weezing',
              'Rhyhorn',
              'Rhydon',
              'Chansey',
              'Tangela',
              'Kangaskhan',
              'Horsea',
              'Seadra',
              'Goldeen',
              'Seaking',
              'Staryu',
              'Starmie',
              'Mr. Mime',
              'Scyther',
              'Jynx',
              'Electabuzz',
              'Magmar',
              'Pinsir',
              'Tauros',
              'Magikarp',
              'Gyarados',
              'Lapras',
              'Ditto',
              'Eevee',
              'Vaporeon',
              'Jolteon',
              'Flareon',
              'Porygon',
              'Omanyte',
              'Omastar',
              'Kabuto',
              'Kabutops',
              'Aerodactyl',
              'Snorlax',
              'Articuno',
              'Zapdos',
              'Moltres',
              'Dratini',
              'Dragonair',
              'Dragonite',
              'Mewtwo',
              'Mew',
              'Chikorita',
              'Bayleef',
              'Meganium',
              'Cyndaquil',
              'Quilava',
              'Typhlosion',
              'Totodile',
              'Croconaw',
              'Feraligatr',
              'Sentret',
              'Furret',
              'Hoothoot',
              'Noctowl',
              'Ledyba',
              'Ledian',
              'Spinarak',
              'Ariados',
              'Crobat',
              'Chinchou',
              'Lanturn',
              'Pichu',
              'Cleffa',
              'Igglybuff',
              'Togepi',
              'Togetic',
              'Natu',
              'Xatu',
              'Mareep',
              'Flaaffy',
              'Ampharos',
              'Bellossom',
              'Marill',
              'Azumarill',
              'Sudowoodo',
              'Politoed',
              'Hoppip',
              'Skiploom',
              'Jumpluff',
              'Aipom',
              'Sunkern',
              'Sunflora',
              'Yanma',
              'Wooper',
              'Quagsire',
              'Espeon',
              'Umbreon',
              'Murkrow',
              'Slowking',
              'Misdreavus',
              'Unown',
              'Wobbuffet',
              'Girafarig',
              'Pineco',
              'Forretress',
              'Dunsparce',
              'Gligar',
              'Steelix',
              'Snubbull',
              'Granbull',
              'Qwilfish',
              'Scizor',
              'Shuckle',
              'Heracross',
              'Sneasel',
              'Teddiursa',
              'Ursaring',
              'Slugma',
              'Magcargo',
              'Swinub',
              'Piloswine',
              'Corsola',
              'Remoraid',
              'Octillery',
              'Delibird',
              'Mantine',
              'Skarmory',
              'Houndour',
              'Houndoom',
              'Kingdra',
              'Phanpy',
              'Donphan',
              'Porygon2',
              'Stantler',
              'Smeargle',
              'Tyrogue',
              'Hitmontop',
              'Smoochum',
              'Elekid',
              'Magby',
              'Miltank',
              'Blissey',
              'Raikou',
              'Entei',
              'Suicune',
              'Larvitar',
              'Pupitar',
              'Tyranitar',
              'Lugia',
              'Ho-oh',
              'Celebi',
              '????? (252)',
              'Egg (253)',
              '????? (254)',
              '-- No Pokemon -- (255)']
pokemon_lower_gs = ['er',
                    'bulbasaur',
                    'ivysaur',
                    'venusaur',
                    'charmander',
                    'charmeleon',
                    'charizard',
                    'squirtle',
                    'wartortle',
                    'blastoise',
                    'caterpie',
                    'metapod',
                    'butterfree',
                    'weedle',
                    'kakuna',
                    'beedrill',
                    'pidgey',
                    'pidgeotto',
                    'pidgeot',
                    'rattata',
                    'raticate',
                    'spearow',
                    'fearow',
                    'ekans',
                    'arbok',
                    'pikachu',
                    'raichu',
                    'sandshrew',
                    'sandslash',
                    'nidoranh',
                    'nidorina',
                    'nidoqueen',
                    'nidoranm',
                    'nidorino',
                    'nidoking',
                    'clefairy',
                    'clefable',
                    'vulpix',
                    'ninetales',
                    'jigglypuff',
                    'wigglytuff',
                    'zubat',
                    'golbat',
                    'oddish',
                    'gloom',
                    'vileplume',
                    'paras',
                    'parasect',
                    'venonat',
                    'venomoth',
                    'diglett',
                    'dugtrio',
                    'meowth',
                    'persian',
                    'psyduck',
                    'golduck',
                    'mankey',
                    'primeape',
                    'growlithe',
                    'arcanine',
                    'poliwag',
                    'poliwhirl',
                    'poliwrath',
                    'abra',
                    'kadabra',
                    'alakazam',
                    'machop',
                    'machoke',
                    'machamp',
                    'bellsprout',
                    'weepinbell',
                    'victreebel',
                    'tentacool',
                    'tentacruel',
                    'geodude',
                    'graveler',
                    'golem',
                    'ponyta',
                    'rapidash',
                    'slowpoke',
                    'slowbro',
                    'magnemite',
                    'magneton',
                    "farfetch'd",
                    'doduo',
                    'dodrio',
                    'seel',
                    'dewgong',
                    'grimer',
                    'muk',
                    'shellder',
                    'cloyster',
                    'gastly',
                    'haunter',
                    'gengar',
                    'onix',
                    'drowzee',
                    'hypno',
                    'krabby',
                    'kingler',
                    'voltorb',
                    'electrode',
                    'exeggcute',
                    'exeggutor',
                    'cubone',
                    'marowak',
                    'hitmonlee',
                    'hitmonchan',
                    'lickitung',
                    'koffing',
                    'weezing',
                    'rhyhorn',
                    'rhydon',
                    'chansey',
                    'tangela',
                    'kangaskhan',
                    'horsea',
                    'seadra',
                    'goldeen',
                    'seaking',
                    'staryu',
                    'starmie',
                    'mr. mime',
                    'scyther',
                    'jynx',
                    'electabuzz',
                    'magmar',
                    'pinsir',
                    'tauros',
                    'magikarp',
                    'gyarados',
                    'lapras',
                    'ditto',
                    'eevee',
                    'vaporeon',
                    'jolteon',
                    'flareon',
                    'porygon',
                    'omanyte',
                    'omastar',
                    'kabuto',
                    'kabutops',
                    'aerodactyl',
                    'snorlax',
                    'articuno',
                    'zapdos',
                    'moltres',
                    'dratini',
                    'dragonair',
                    'dragonite',
                    'mewtwo',
                    'mew',
                    'chikorita',
                    'bayleef',
                    'meganium',
                    'cyndaquil',
                    'quilava',
                    'typhlosion',
                    'totodile',
                    'croconaw',
                    'feraligatr',
                    'sentret',
                    'furret',
                    'hoothoot',
                    'noctowl',
                    'ledyba',
                    'ledian',
                    'spinarak',
                    'ariados',
                    'crobat',
                    'chinchou',
                    'lanturn',
                    'pichu',
                    'cleffa',
                    'igglybuff',
                    'togepi',
                    'togetic',
                    'natu',
                    'xatu',
                    'mareep',
                    'flaaffy',
                    'ampharos',
                    'bellossom',
                    'marill',
                    'azumarill',
                    'sudowoodo',
                    'politoed',
                    'hoppip',
                    'skiploom',
                    'jumpluff',
                    'aipom',
                    'sunkern',
                    'sunflora',
                    'yanma',
                    'wooper',
                    'quagsire',
                    'espeon',
                    'umbreon',
                    'murkrow',
                    'slowking',
                    'misdreavus',
                    'unown',
                    'wobbuffet',
                    'girafarig',
                    'pineco',
                    'forretress',
                    'dunsparce',
                    'gligar',
                    'steelix',
                    'snubbull',
                    'granbull',
                    'qwilfish',
                    'scizor',
                    'shuckle',
                    'heracross',
                    'sneasel',
                    'teddiursa',
                    'ursaring',
                    'slugma',
                    'magcargo',
                    'swinub',
                    'piloswine',
                    'corsola',
                    'remoraid',
                    'octillery',
                    'delibird',
                    'mantine',
                    'skarmory',
                    'houndour',
                    'houndoom',
                    'kingdra',
                    'phanpy',
                    'donphan',
                    'porygon2',
                    'stantler',
                    'smeargle',
                    'tyrogue',
                    'hitmontop',
                    'smoochum',
                    'elekid',
                    'magby',
                    'miltank',
                    'blissey',
                    'raikou',
                    'entei',
                    'suicune',
                    'larvitar',
                    'pupitar',
                    'tyranitar',
                    'lugia',
                    'ho-oh',
                    'celebi',
                    '?????',
                    'egg',
                    '?????',
                    '']
pokedex_gs = ['#000 Er',
              '#001 Bulbasaur',
              '#002 Ivysaur',
              '#003 Venusaur',
              '#004 Charmander',
              '#005 Charmeleon',
              '#006 Charizard',
              '#007 Squirtle',
              '#008 Wartortle',
              '#009 Blastoise',
              '#010 Caterpie',
              '#011 Metapod',
              '#012 Butterfree',
              '#013 Weedle',
              '#014 Kakuna',
              '#015 Beedrill',
              '#016 Pidgey',
              '#017 Pidgeotto',
              '#018 Pidgeot',
              '#019 Rattata',
              '#020 Raticate',
              '#021 Spearow',
              '#022 Fearow',
              '#023 Ekans',
              '#024 Arbok',
              '#025 Pikachu',
              '#026 Raichu',
              '#027 Sandshrew',
              '#028 Sandslash',
              '#029 Nidoranh',
              '#030 Nidorina',
              '#031 Nidoqueen',
              '#032 Nidoranm',
              '#033 Nidorino',
              '#034 Nidoking',
              '#035 Clefairy',
              '#036 Clefable',
              '#037 Vulpix',
              '#038 Ninetales',
              '#039 Jigglypuff',
              '#040 Wigglytuff',
              '#041 Zubat',
              '#042 Golbat',
              '#043 Oddish',
              '#044 Gloom',
              '#045 Vileplume',
              '#046 Paras',
              '#047 Parasect',
              '#048 Venonat',
              '#049 Venomoth',
              '#050 Diglett',
              '#051 Dugtrio',
              '#052 Meowth',
              '#053 Persian',
              '#054 Psyduck',
              '#055 Golduck',
              '#056 Mankey',
              '#057 Primeape',
              '#058 Growlithe',
              '#059 Arcanine',
              '#060 Poliwag',
              '#061 Poliwhirl',
              '#062 Poliwrath',
              '#063 Abra',
              '#064 Kadabra',
              '#065 Alakazam',
              '#066 Machop',
              '#067 Machoke',
              '#068 Machamp',
              '#069 Bellsprout',
              '#070 Weepinbell',
              '#071 Victreebel',
              '#072 Tentacool',
              '#073 Tentacruel',
              '#074 Geodude',
              '#075 Graveler',
              '#076 Golem',
              '#077 Ponyta',
              '#078 Rapidash',
              '#079 Slowpoke',
              '#080 Slowbro',
              '#081 Magnemite',
              '#082 Magneton',
              "#083 Farfetch'd",
              '#084 Doduo',
              '#085 Dodrio',
              '#086 Seel',
              '#087 Dewgong',
              '#088 Grimer',
              '#089 Muk',
              '#090 Shellder',
              '#091 Cloyster',
              '#092 Gastly',
              '#093 Haunter',
              '#094 Gengar',
              '#095 Onix',
              '#096 Drowzee',
              '#097 Hypno',
              '#098 Krabby',
              '#099 Kingler',
              '#100 Voltorb',
              '#101 Electrode',
              '#102 Exeggcute',
              '#103 Exeggutor',
              '#104 Cubone',
              '#105 Marowak',
              '#106 Hitmonlee',
              '#107 Hitmonchan',
              '#108 Lickitung',
              '#109 Koffing',
              '#110 Weezing',
              '#111 Rhyhorn',
              '#112 Rhydon',
              '#113 Chansey',
              '#163 Tangela',
              '#115 Kangaskhan',
              '#116 Horsea',
              '#117 Seadra',
              '#118 Goldeen',
              '#119 Seaking',
              '#120 Staryu',
              '#121 Starmie',
              '#122 Mr. Mime',
              '#123 Scyther',
              '#124 Jynx',
              '#125 Electabuzz',
              '#126 Magmar',
              '#127 Pinsir',
              '#128 Tauros',
              '#129 Magikarp',
              '#130 Gyarados',
              '#131 Lapras',
              '#132 Ditto',
              '#133 Eevee',
              '#134 Vaporeon',
              '#135 Jolteon',
              '#136 Flareon',
              '#137 Porygon',
              '#138 Omanyte',
              '#139 Omastar',
              '#140 Kabuto',
              '#141 Kabutops',
              '#142 Aerodactyl',
              '#143 Snorlax',
              '#144 Articuno',
              '#145 Zapdos',
              '#146 Moltres',
              '#147 Dratini',
              '#148 Dragonair',
              '#149 Dragonite',
              '#150 Mewtwo',
              '#151 Mew',
              '#152 Chikorita',
              '#153 Bayleef',
              '#154 Meganium',
              '#155 Cyndaquil',
              '#156 Quilava',
              '#163 Typhlosion',
              '#158 Totodile',
              '#159 Croconaw',
              '#160 Feraligatr',
              '#161 Sentret',
              '#162 Furret',
              '#163 Hoothoot',
              '#164 Noctowl',
              '#165 Ledyba',
              '#166 Ledian',
              '#167 Spinarak',
              '#168 Ariados',
              '#169 Crobat',
              '#170 Chinchou',
              '#171 Lanturn',
              '#172 Pichu',
              '#173 Cleffa',
              '#174 Igglybuff',
              '#175 Togepi',
              '#176 Togetic',
              '#177 Natu',
              '#178 Xatu',
              '#179 Mareep',
              '#180 Flaaffy',
              '#181 Ampharos',
              '#182 Bellossom',
              '#183 Marill',
              '#184 Azumarill',
              '#185 Sudowoodo',
              '#186 Politoed',
              '#187 Hoppip',
              '#188 Skiploom',
              '#189 Jumpluff',
              '#190 Aipom',
              '#191 Sunkern',
              '#192 Sunflora',
              '#193 Yanma',
              '#194 Wooper',
              '#195 Quagsire',
              '#196 Espeon',
              '#197 Umbreon',
              '#198 Murkrow',
              '#199 Slowking',
              '#200 Misdreavus',
              '#201 Unown',
              '#202 Wobbuffet',
              '#203 Girafarig',
              '#204 Pineco',
              '#205 Forretress',
              '#206 Dunsparce',
              '#207 Gligar',
              '#208 Steelix',
              '#209 Snubbull',
              '#210 Granbull',
              '#211 Qwilfish',
              '#212 Scizor',
              '#213 Shuckle',
              '#214 Heracross',
              '#215 Sneasel',
              '#216 Teddiursa',
              '#217 Ursaring',
              '#218 Slugma',
              '#219 Magcargo',
              '#220 Swinub',
              '#221 Piloswine',
              '#222 Corsola',
              '#223 Remoraid',
              '#224 Octillery',
              '#225 Delibird',
              '#226 Mantine',
              '#227 Skarmory',
              '#228 Houndour',
              '#229 Houndoom',
              '#230 Kingdra',
              '#231 Phanpy',
              '#232 Donphan',
              '#233 Porygon2',
              '#234 Stantler',
              '#235 Smeargle',
              '#236 Tyrogue',
              '#237 Hitmontop',
              '#238 Smoochum',
              '#239 Elekid',
              '#240 Magby',
              '#241 Miltank',
              '#242 Blissey',
              '#243 Raikou',
              '#244 Entei',
              '#245 Suicune',
              '#246 Larvitar',
              '#247 Pupitar',
              '#248 Tyranitar',
              '#249 Lugia',
              '#250 Ho-oh',
              '#251 Celebi',
              '#252 ?????',
              '#253 Egg',
              '#254 ?????',
              '#255 ?????']
moves_gs = ['-- No Move -- (0)',
            'Pound',
            'Karate Chop',
            'Doubleslap',
            'Comet Punch',
            'Mega Punch',
            'Pay Day',
            'Fire Punch',
            'Ice Punch',
            'Thunderpunch',
            'Scratch',
            'Vicegrip',
            'Guillotine',
            'Razor Wind',
            'Swords Dance',
            'Cut',
            'Gust',
            'Wing Attack',
            'Whirlwind',
            'Fly',
            'Bind',
            'Slam',
            'Vine Whip',
            'Stomp',
            'Double Kick',
            'Mega Kick',
            'Jump Kick',
            'Rolling Kick',
            'Sand-attack',
            'Headbutt',
            'Horn Attack',
            'Fury Attack',
            'Horn Drill',
            'Tackle',
            'Body Slam',
            'Wrap',
            'Take Down',
            'Thrash',
            'Double-edge',
            'Tail Whip',
            'Poison Sting',
            'Twineedle',
            'Pin Missile',
            'Leer',
            'Bite',
            'Growl',
            'Roar',
            'Sing',
            'Supersonic',
            'Sonicboom',
            'Disable',
            'Acid',
            'Ember',
            'Flamethrower',
            'Mist',
            'Water Gun',
            'Hydro Pump',
            'Surf',
            'Ice Beam',
            'Blizzard',
            'Psybeam',
            'Bubblebeam',
            'Aurora Beam',
            'Hyper Beam',
            'Peck',
            'Drill Peck',
            'Submission',
            'Low Kick',
            'Counter',
            'Seismic Toss',
            'Strength',
            'Absorb',
            'Mega Drain',
            'Leech Seed',
            'Growth',
            'Razor Leaf',
            'Solarbeam',
            'Poisonpowder',
            'Stun Spore',
            'Sleep Powder',
            'Petal Dance',
            'String Shot',
            'Dragon Rage',
            'Fire Spin',
            'Thundershock',
            'Thunderbolt',
            'Thunder Wave',
            'Thunder',
            'Rock Throw',
            'Earthquake',
            'Fissure',
            'Dig',
            'Toxic',
            'Confusion',
            'Psychic',
            'Hypnosis',
            'Meditate',
            'Agility',
            'Quick Attack',
            'Rage',
            'Teleport',
            'Night Shade',
            'Mimic',
            'Screech',
            'Double Team',
            'Recover',
            'Harden',
            'Minimize',
            'Smokescreen',
            'Confuse Ray',
            'Withdraw',
            'Defense Curl',
            'Barrier',
            'Light Screen',
            'Haze',
            'Reflect',
            'Focus Energy',
            'Bide',
            'Metronome',
            'Mirror Move',
            'Selfdestruct',
            'Egg Bomb',
            'Lick',
            'Smog',
            'Sludge',
            'Bone Club',
            'Fire Blast',
            'Waterfall',
            'Clamp',
            'Swift',
            'Skull Bash',
            'Spike Cannon',
            'Constrict',
            'Amnesia',
            'Kinesis',
            'Softboiled',
            'Hi Jump Kick',
            'Glare',
            'Dream Eater',
            'Poison Gas',
            'Barrage',
            'Leech Life',
            'Lovely Kiss',
            'Sky Attack',
            'Transform',
            'Bubble',
            'Dizzy Punch',
            'Spore',
            'Flash',
            'Psywave',
            'Splash',
            'Acid Armor',
            'Crabhammer',
            'Explosion',
            'Fury Swipes',
            'Bonemerang',
            'Rest',
            'Rock Slide',
            'Hyper Fang',
            'Sharpen',
            'Conversion',
            'Tri Attack',
            'Super Fang',
            'Slash',
            'Substitute',
            'Struggle',
            'Sketch',
            'Triple Kick',
            'Thief',
            'Spider Web',
            'Mind Reader',
            'Nightmare',
            'Flame Wheel',
            'Snore',
            'Curse',
            'Flail',
            'Conversion2',
            'Aeroblast',
            'Cotton Spore',
            'Reversal',
            'Spite',
            'Powder Snow',
            'Protect',
            'Mach Punch',
            'Scary Face',
            'Faint Attack',
            'Sweet Kiss',
            'Belly Drum',
            'Sludge Bomb',
            'Mud-slap',
            'Octazooka',
            'Spikes',
            'Zap Cannon',
            'Foresight',
            'Destiny Bond',
            'Perish Song',
            'Icy Wind',
            'Detect',
            'Bone Rush',
            'Lock-on',
            'Outrage',
            'Sandstorm',
            'Giga Drain',
            'Endure',
            'Charm',
            'Rollout',
            'False Swipe',
            'Swagger',
            'Milk Drink',
            'Spark',
            'Fury Cutter',
            'Steel Wing',
            'Mean Look',
            'Attract',
            'Sleep Talk',
            'Heal Bell',
            'Return',
            'Present',
            'Frustration',
            'Safeguard',
            'Pain Split',
            'Sacred Fire',
            'Magnitude',
            'Dynamicpunch',
            'Megahorn',
            'Dragonbreath',
            'Baton Pass',
            'Encore',
            'Pursuit',
            'Rapid Spin',
            'Sweet Scent',
            'Iron Tail',
            'Metal Claw',
            'Vital Throw',
            'Morning Sun',
            'Synthesis',
            'Moonlight',
            'Hidden Power',
            'Cross Chop',
            'Twister',
            'Rain Dance',
            'Sunny Day',
            'Crunch',
            'Mirror Coat',
            'Psych Up',
            'Extremespeed',
            'Ancientpower',
            'Shadow Ball',
            'Future Sight',
            'Rock Smash',
            'Whirlpool',
            'Beat Up',
            '~252',
            '~253',
            '~254',
            '~255']
types_gs = ['Normal',
            'Fighting',
            'Flying',
            'Poison',
            'Ground',
            'Rock',
            'Bird',
            'Bug',
            'Ghost',
            'Steel',
            '~10',
            '~11',
            '~12',
            '~13',
            '~14',
            '~15',
            '~16',
            '~17',
            '~18',
            '~19',
            'Fire',
            'Water',
            'Grass',
            'Electric',
            'Psychic',
            'Ice',
            'Dragon',
            'Dark',
            '~28',
            '~29',
            '~30',
            '~31',
            '~32',
            '~33',
            '~34',
            '~35',
            '~36',
            '~37',
            '~38',
            '~39',
            '~40',
            '~41',
            '~42',
            '~43',
            '~44',
            '~45',
            '~46',
            '~47',
            '~48',
            '~49',
            '~50',
            '~51',
            '~52',
            '~53',
            '~54',
            '~55',
            '~56',
            '~57',
            '~58',
            '~59',
            '~60',
            '~61',
            '~62',
            '~63',
            '~64',
            '~65',
            '~66',
            '~67',
            '~68',
            '~69',
            '~70',
            '~71',
            '~72',
            '~73',
            '~74',
            '~75',
            '~76',
            '~77',
            '~78',
            '~79',
            '~80',
            '~81',
            '~82',
            '~83',
            '~84',
            '~85',
            '~86',
            '~87',
            '~88',
            '~89',
            '~90',
            '~91',
            '~92',
            '~93',
            '~94',
            '~95',
            '~96',
            '~97',
            '~98',
            '~99',
            '~100',
            '~101',
            '~102',
            '~103',
            '~104',
            '~105',
            '~106',
            '~107',
            '~108',
            '~109',
            '~110',
            '~111',
            '~112',
            '~113',
            '~163',
            '~115',
            '~116',
            '~117',
            '~118',
            '~119',
            '~120',
            '~121',
            '~122',
            '~123',
            '~124',
            '~125',
            '~126',
            '~127',
            '~128',
            '~129',
            '~130',
            '~131',
            '~132',
            '~133',
            '~134',
            '~135',
            '~136',
            '~137',
            '~138',
            '~139',
            '~140',
            '~141',
            '~142',
            '~143',
            '~144',
            '~145',
            '~146',
            '~147',
            '~148',
            '~149',
            '~150',
            '~151',
            '~152',
            '~153',
            '~154',
            '~155',
            '~156',
            '~163',
            '~158',
            '~159',
            '~160',
            '~161',
            '~162',
            '~163',
            '~164',
            '~165',
            '~166',
            '~167',
            '~168',
            '~169',
            '~170',
            '~171',
            '~172',
            '~173',
            '~174',
            '~175',
            '~176',
            '~177',
            '~178',
            '~179',
            '~180',
            '~181',
            '~182',
            '~183',
            '~184',
            '~185',
            '~186',
            '~187',
            '~188',
            '~189',
            '~190',
            '~191',
            '~192',
            '~193',
            '~194',
            '~195',
            '~196',
            '~197',
            '~198',
            '~199',
            '~200',
            '~201',
            '~202',
            '~203',
            '~204',
            '~205',
            '~206',
            '~207',
            '~208',
            '~209',
            '~210',
            '~211',
            '~212',
            '~213',
            '~214',
            '~215',
            '~216',
            '~217',
            '~218',
            '~219',
            '~220',
            '~221',
            '~222',
            '~223',
            '~224',
            '~225',
            '~226',
            '~227',
            '~228',
            '~229',
            '~230',
            '~231',
            '~232',
            '~233',
            '~234',
            '~235',
            '~236',
            '~237',
            '~238',
            '~239',
            '~240',
            '~241',
            '~242',
            '~243',
            '~244',
            '~245',
            '~246',
            '~247',
            '~248',
            '~249',
            '~250',
            '~251',
            '~252',
            '~253',
            '~254',
            '~255']
types_gs_hp = ['Fighting',
               'Flying',
               'Poison',
               'Ground',
               'Rock',
               'Bug',
               'Ghost',
               'Steel',
               'Fire',
               'Water',
               'Grass',
               'Electric',
               'Psychic',
               'Ice',
               'Dragon',
               'Dark']
items_rs = ['-- No Item --',
            'Master Ball',
            'Ultra Ball',
            'Great Ball',
            'Poke Ball',
            'Safari Ball',
            'Net Ball',
            'Dive Ball',
            'Nest Ball',
            'Repeat Ball',
            'Timer Ball',
            'Luxury Ball',
            'Premier Ball',
            'Potion',
            'Antidote',
            'Burn Heal',
            'Ice Heal',
            'Awakening',
            'Parlyz Heal',
            'Full Restore',
            'Max Potion',
            'Hyper Potion',
            'Super Potion',
            'Full Heal',
            'Revive',
            'Max Revive',
            'Fresh Water',
            'Soda Pop',
            'Lemonade',
            'Moomoo Milk',
            'Energypowder',
            'Energy Root',
            'Heal Powder',
            'Revival Herb',
            'Ether',
            'Max Ether',
            'Elixir',
            'Max Elixir',
            'Lava Cookie',
            'Blue Flute',
            'Yellow Flute',
            'Red Flute',
            'Black Flute',
            'White Flute',
            'Berry Juice',
            'Sacred Ash',
            'Shoal Salt',
            'Shoal Shell',
            'Red Shard',
            'Blue Shard',
            'Yellow Shard',
            'Green Shard',
            '???????? (52)',
            '???????? (53)',
            '???????? (54)',
            '???????? (55)',
            '???????? (56)',
            '???????? (57)',
            '???????? (58)',
            '???????? (59)',
            '???????? (60)',
            '???????? (61)',
            '???????? (62)',
            'Hp Up',
            'Protein',
            'Iron',
            'Carbos',
            'Calcium',
            'Rare Candy',
            'Pp Up',
            'Zinc',
            'Pp Max',
            '???????? (72)',
            'Guard Spec.',
            'Dire Hit',
            'X Attack',
            'X Defend',
            'X Speed',
            'X Accuracy',
            'X Special',
            'Poke Doll',
            'Fluffy Tail',
            '???????? (82)',
            'Super Repel',
            'Max Repel',
            'Escape Rope',
            'Repel',
            '???????? (87)',
            '???????? (88)',
            '???????? (89)',
            '???????? (90)',
            '???????? (91)',
            '???????? (92)',
            'Sun Stone',
            'Moon Stone',
            'Fire Stone',
            'Thunderstone',
            'Water Stone',
            'Leaf Stone',
            '???????? (99)',
            '???????? (100)',
            '???????? (101)',
            '???????? (102)',
            'Tinymushroom',
            'Big Mushroom',
            '???????? (105)',
            'Pearl',
            'Big Pearl',
            'Stardust',
            'Star Piece',
            'Nugget',
            'Heart Scale',
            '???????? (112)',
            '???????? (113)',
            '???????? (163)',
            '???????? (115)',
            '???????? (116)',
            '???????? (117)',
            '???????? (118)',
            '???????? (119)',
            '???????? (120)',
            'Orange Mail',
            'Harbor Mail',
            'Glitter Mail',
            'Mech Mail',
            'Wood Mail',
            'Wave Mail',
            'Bead Mail',
            'Shadow Mail',
            'Tropic Mail',
            'Dream Mail',
            'Fab Mail',
            'Retro Mail',
            'Cheri Berry',
            'Chesto Berry',
            'Pecha Berry',
            'Rawst Berry',
            'Aspear Berry',
            'Leppa Berry',
            'Oran Berry',
            'Persim Berry',
            'Lum Berry',
            'Sitrus Berry',
            'Figy Berry',
            'Wiki Berry',
            'Mago Berry',
            'Aguav Berry',
            'Iapapa Berry',
            'Razz Berry',
            'Bluk Berry',
            'Nanab Berry',
            'Wepear Berry',
            'Pinap Berry',
            'Pomeg Berry',
            'Kelpsy Berry',
            'Qualot Berry',
            'Hondew Berry',
            'Grepa Berry',
            'Tamato Berry',
            'Cornn Berry',
            'Magost Berry',
            'Rabuta Berry',
            'Nomel Berry',
            'Spelon Berry',
            'Pamtre Berry',
            'Watmel Berry',
            'Durin Berry',
            'Belue Berry',
            'Liechi Berry',
            'Ganlon Berry',
            'Salac Berry',
            'Petaya Berry',
            'Apicot Berry',
            'Lansat Berry',
            'Starf Berry',
            'Enigma Berry',
            '???????? (176)',
            '???????? (177)',
            '???????? (178)',
            'Brightpowder',
            'White Herb',
            'Macho Brace',
            'Exp. Share',
            'Quick Claw',
            'Soothe Bell',
            'Mental Herb',
            'Choice Band',
            "King's Rock",
            'Silverpowder',
            'Amulet Coin',
            'Cleanse Tag',
            'Soul Dew',
            'Deepseatooth',
            'Deepseascale',
            'Smoke Ball',
            'Everstone',
            'Focus Band',
            'Lucky Egg',
            'Scope Lens',
            'Metal Coat',
            'Leftovers',
            'Dragon Scale',
            'Light Ball',
            'Soft Sand',
            'Hard Stone',
            'Miracle Seed',
            'Blackglasses',
            'Black Belt',
            'Magnet',
            'Mystic Water',
            'Sharp Beak',
            'Poison Barb',
            'Nevermeltice',
            'Spell Tag',
            'Twistedspoon',
            'Charcoal',
            'Dragon Fang',
            'Silk Scarf',
            'Up-grade',
            'Shell Bell',
            'Sea Incense',
            'Lax Incense',
            'Lucky Punch',
            'Metal Powder',
            'Thick Club',
            'Stick',
            '???????? (226)',
            '???????? (227)',
            '???????? (228)',
            '???????? (229)',
            '???????? (230)',
            '???????? (231)',
            '???????? (232)',
            '???????? (233)',
            '???????? (234)',
            '???????? (235)',
            '???????? (236)',
            '???????? (237)',
            '???????? (238)',
            '???????? (239)',
            '???????? (240)',
            '???????? (241)',
            '???????? (242)',
            '???????? (243)',
            '???????? (244)',
            '???????? (245)',
            '???????? (246)',
            '???????? (247)',
            '???????? (248)',
            '???????? (249)',
            '???????? (250)',
            '???????? (251)',
            '???????? (252)',
            '???????? (253)',
            'Red Scarf',
            'Blue Scarf',
            'Pink Scarf',
            'Green Scarf',
            'Yellow Scarf',
            'Mach Bike',
            'Coin Case',
            'Itemfinder',
            'Old Rod',
            'Good Rod',
            'Super Rod',
            'S.s. Ticket',
            'Contest Pass',
            '???????? (267)',
            'Wailmer Pail',
            'Devon Goods',
            'Soot Sack',
            'Basement Key',
            'Acro Bike',
            'Pokeblock Case',
            'Letter',
            'Eon Ticket',
            'Red Orb',
            'Blue Orb',
            'Scanner',
            'Go-goggles',
            'Meteorite',
            'Rm. 1 Key',
            'Rm. 2 Key',
            'Rm. 4 Key',
            'Rm. 6 Key',
            'Storage Key',
            'Root Fossil',
            'Claw Fossil',
            'Devon Scope',
            'TM01',
            'TM02',
            'TM03',
            'TM04',
            'TM05',
            'TM06',
            'TM07',
            'TM08',
            'TM09',
            'TM10',
            'TM11',
            'TM12',
            'TM13',
            'TM14',
            'TM15',
            'TM16',
            'TM17',
            'TM18',
            'TM19',
            'TM20',
            'TM21',
            'TM22',
            'TM23',
            'TM24',
            'TM25',
            'TM26',
            'TM27',
            'TM28',
            'TM29',
            'TM30',
            'TM31',
            'TM32',
            'TM33',
            'TM34',
            'TM35',
            'TM36',
            'TM37',
            'TM38',
            'TM39',
            'TM40',
            'TM41',
            'TM42',
            'TM43',
            'TM44',
            'TM45',
            'TM46',
            'TM47',
            'TM48',
            'TM49',
            'TM50',
            'HM01',
            'HM02',
            'HM03',
            'HM04',
            'HM05',
            'HM06',
            'HM07',
            'HM08',
            '???????? (347)',
            '???????? (348)']
pokemon_rs = ['-- No Pokemon -- (0)',
              'Bulbasaur',
              'Ivysaur',
              'Venusaur',
              'Charmander',
              'Charmeleon',
              'Charizard',
              'Squirtle',
              'Wartortle',
              'Blastoise',
              'Caterpie',
              'Metapod',
              'Butterfree',
              'Weedle',
              'Kakuna',
              'Beedrill',
              'Pidgey',
              'Pidgeotto',
              'Pidgeot',
              'Rattata',
              'Raticate',
              'Spearow',
              'Fearow',
              'Ekans',
              'Arbok',
              'Pikachu',
              'Raichu',
              'Sandshrew',
              'Sandslash',
              'Nidoranf',
              'Nidorina',
              'Nidoqueen',
              'Nidoranm',
              'Nidorino',
              'Nidoking',
              'Clefairy',
              'Clefable',
              'Vulpix',
              'Ninetales',
              'Jigglypuff',
              'Wigglytuff',
              'Zubat',
              'Golbat',
              'Oddish',
              'Gloom',
              'Vileplume',
              'Paras',
              'Parasect',
              'Venonat',
              'Venomoth',
              'Diglett',
              'Dugtrio',
              'Meowth',
              'Persian',
              'Psyduck',
              'Golduck',
              'Mankey',
              'Primeape',
              'Growlithe',
              'Arcanine',
              'Poliwag',
              'Poliwhirl',
              'Poliwrath',
              'Abra',
              'Kadabra',
              'Alakazam',
              'Machop',
              'Machoke',
              'Machamp',
              'Bellsprout',
              'Weepinbell',
              'Victreebel',
              'Tentacool',
              'Tentacruel',
              'Geodude',
              'Graveler',
              'Golem',
              'Ponyta',
              'Rapidash',
              'Slowpoke',
              'Slowbro',
              'Magnemite',
              'Magneton',
              "Farfetch'd",
              'Doduo',
              'Dodrio',
              'Seel',
              'Dewgong',
              'Grimer',
              'Muk',
              'Shellder',
              'Cloyster',
              'Gastly',
              'Haunter',
              'Gengar',
              'Onix',
              'Drowzee',
              'Hypno',
              'Krabby',
              'Kingler',
              'Voltorb',
              'Electrode',
              'Exeggcute',
              'Exeggutor',
              'Cubone',
              'Marowak',
              'Hitmonlee',
              'Hitmonchan',
              'Lickitung',
              'Koffing',
              'Weezing',
              'Rhyhorn',
              'Rhydon',
              'Chansey',
              'Tangela',
              'Kangaskhan',
              'Horsea',
              'Seadra',
              'Goldeen',
              'Seaking',
              'Staryu',
              'Starmie',
              'Mr. Mime',
              'Scyther',
              'Jynx',
              'Electabuzz',
              'Magmar',
              'Pinsir',
              'Tauros',
              'Magikarp',
              'Gyarados',
              'Lapras',
              'Ditto',
              'Eevee',
              'Vaporeon',
              'Jolteon',
              'Flareon',
              'Porygon',
              'Omanyte',
              'Omastar',
              'Kabuto',
              'Kabutops',
              'Aerodactyl',
              'Snorlax',
              'Articuno',
              'Zapdos',
              'Moltres',
              'Dratini',
              'Dragonair',
              'Dragonite',
              'Mewtwo',
              'Mew',
              'Chikorita',
              'Bayleef',
              'Meganium',
              'Cyndaquil',
              'Quilava',
              'Typhlosion',
              'Totodile',
              'Croconaw',
              'Feraligatr',
              'Sentret',
              'Furret',
              'Hoothoot',
              'Noctowl',
              'Ledyba',
              'Ledian',
              'Spinarak',
              'Ariados',
              'Crobat',
              'Chinchou',
              'Lanturn',
              'Pichu',
              'Cleffa',
              'Igglybuff',
              'Togepi',
              'Togetic',
              'Natu',
              'Xatu',
              'Mareep',
              'Flaaffy',
              'Ampharos',
              'Bellossom',
              'Marill',
              'Azumarill',
              'Sudowoodo',
              'Politoed',
              'Hoppip',
              'Skiploom',
              'Jumpluff',
              'Aipom',
              'Sunkern',
              'Sunflora',
              'Yanma',
              'Wooper',
              'Quagsire',
              'Espeon',
              'Umbreon',
              'Murkrow',
              'Slowking',
              'Misdreavus',
              'Unown',
              'Wobbuffet',
              'Girafarig',
              'Pineco',
              'Forretress',
              'Dunsparce',
              'Gligar',
              'Steelix',
              'Snubbull',
              'Granbull',
              'Qwilfish',
              'Scizor',
              'Shuckle',
              'Heracross',
              'Sneasel',
              'Teddiursa',
              'Ursaring',
              'Slugma',
              'Magcargo',
              'Swinub',
              'Piloswine',
              'Corsola',
              'Remoraid',
              'Octillery',
              'Delibird',
              'Mantine',
              'Skarmory',
              'Houndour',
              'Houndoom',
              'Kingdra',
              'Phanpy',
              'Donphan',
              'Porygon2',
              'Stantler',
              'Smeargle',
              'Tyrogue',
              'Hitmontop',
              'Smoochum',
              'Elekid',
              'Magby',
              'Miltank',
              'Blissey',
              'Raikou',
              'Entei',
              'Suicune',
              'Larvitar',
              'Pupitar',
              'Tyranitar',
              'Lugia',
              'Ho-oh',
              'Celebi',
              '? (252)',
              '? (253)',
              '? (254)',
              '? (255)',
              '? (256)',
              '? (257)',
              '? (258)',
              '? (259)',
              '? (260)',
              '? (261)',
              '? (262)',
              '? (263)',
              '? (264)',
              '? (265)',
              '? (266)',
              '? (267)',
              '? (268)',
              '? (269)',
              '? (270)',
              '? (271)',
              '? (272)',
              '? (273)',
              '? (274)',
              '? (275)',
              '? (276)',
              'Treecko',
              'Grovyle',
              'Sceptile',
              'Torchic',
              'Combusken',
              'Blaziken',
              'Mudkip',
              'Marshtomp',
              'Swampert',
              'Poochyena',
              'Mightyena',
              'Zigzagoon',
              'Linoone',
              'Wurmple',
              'Silcoon',
              'Beautifly',
              'Cascoon',
              'Dustox',
              'Lotad',
              'Lombre',
              'Ludicolo',
              'Seedot',
              'Nuzleaf',
              'Shiftry',
              'Nincada',
              'Ninjask',
              'Shedinja',
              'Taillow',
              'Swellow',
              'Shroomish',
              'Breloom',
              'Spinda',
              'Wingull',
              'Pelipper',
              'Surskit',
              'Masquerain',
              'Wailmer',
              'Wailord',
              'Skitty',
              'Delcatty',
              'Kecleon',
              'Baltoy',
              'Claydol',
              'Nosepass',
              'Torkoal',
              'Sableye',
              'Barboach',
              'Whiscash',
              'Luvdisc',
              'Corphish',
              'Crawdaunt',
              'Feebas',
              'Milotic',
              'Carvanha',
              'Sharpedo',
              'Trapinch',
              'Vibrava',
              'Flygon',
              'Makuhita',
              'Hariyama',
              'Electrike',
              'Manectric',
              'Numel',
              'Camerupt',
              'Spheal',
              'Sealeo',
              'Walrein',
              'Cacnea',
              'Cacturne',
              'Snorunt',
              'Glalie',
              'Lunatone',
              'Solrock',
              'Azurill',
              'Spoink',
              'Grumpig',
              'Plusle',
              'Minun',
              'Mawile',
              'Meditite',
              'Medicham',
              'Swablu',
              'Altaria',
              'Wynaut',
              'Duskull',
              'Dusclops',
              'Roselia',
              'Slakoth',
              'Vigoroth',
              'Slaking',
              'Gulpin',
              'Swalot',
              'Tropius',
              'Whismur',
              'Loudred',
              'Exploud',
              'Clamperl',
              'Huntail',
              'Gorebyss',
              'Absol',
              'Shuppet',
              'Banette',
              'Seviper',
              'Zangoose',
              'Relicanth',
              'Aron',
              'Lairon',
              'Aggron',
              'Castform',
              'Volbeat',
              'Illumise',
              'Lileep',
              'Cradily',
              'Anorith',
              'Armaldo',
              'Ralts',
              'Kirlia',
              'Gardevoir',
              'Bagon',
              'Shelgon',
              'Salamence',
              'Beldum',
              'Metang',
              'Metagross',
              'Regirock',
              'Regice',
              'Registeel',
              'Kyogre',
              'Groudon',
              'Rayquaza',
              'Latias',
              'Latios',
              'Jirachi',
              'Deoxys',
              'Chimecho',
              '- (412)']
pokemon_lower_rs = ['',
                    'bulbasaur',
                    'ivysaur',
                    'venusaur',
                    'charmander',
                    'charmeleon',
                    'charizard',
                    'squirtle',
                    'wartortle',
                    'blastoise',
                    'caterpie',
                    'metapod',
                    'butterfree',
                    'weedle',
                    'kakuna',
                    'beedrill',
                    'pidgey',
                    'pidgeotto',
                    'pidgeot',
                    'rattata',
                    'raticate',
                    'spearow',
                    'fearow',
                    'ekans',
                    'arbok',
                    'pikachu',
                    'raichu',
                    'sandshrew',
                    'sandslash',
                    'nidoranf',
                    'nidorina',
                    'nidoqueen',
                    'nidoranm',
                    'nidorino',
                    'nidoking',
                    'clefairy',
                    'clefable',
                    'vulpix',
                    'ninetales',
                    'jigglypuff',
                    'wigglytuff',
                    'zubat',
                    'golbat',
                    'oddish',
                    'gloom',
                    'vileplume',
                    'paras',
                    'parasect',
                    'venonat',
                    'venomoth',
                    'diglett',
                    'dugtrio',
                    'meowth',
                    'persian',
                    'psyduck',
                    'golduck',
                    'mankey',
                    'primeape',
                    'growlithe',
                    'arcanine',
                    'poliwag',
                    'poliwhirl',
                    'poliwrath',
                    'abra',
                    'kadabra',
                    'alakazam',
                    'machop',
                    'machoke',
                    'machamp',
                    'bellsprout',
                    'weepinbell',
                    'victreebel',
                    'tentacool',
                    'tentacruel',
                    'geodude',
                    'graveler',
                    'golem',
                    'ponyta',
                    'rapidash',
                    'slowpoke',
                    'slowbro',
                    'magnemite',
                    'magneton',
                    "farfetch'd",
                    'doduo',
                    'dodrio',
                    'seel',
                    'dewgong',
                    'grimer',
                    'muk',
                    'shellder',
                    'cloyster',
                    'gastly',
                    'haunter',
                    'gengar',
                    'onix',
                    'drowzee',
                    'hypno',
                    'krabby',
                    'kingler',
                    'voltorb',
                    'electrode',
                    'exeggcute',
                    'exeggutor',
                    'cubone',
                    'marowak',
                    'hitmonlee',
                    'hitmonchan',
                    'lickitung',
                    'koffing',
                    'weezing',
                    'rhyhorn',
                    'rhydon',
                    'chansey',
                    'tangela',
                    'kangaskhan',
                    'horsea',
                    'seadra',
                    'goldeen',
                    'seaking',
                    'staryu',
                    'starmie',
                    'mr. mime',
                    'scyther',
                    'jynx',
                    'electabuzz',
                    'magmar',
                    'pinsir',
                    'tauros',
                    'magikarp',
                    'gyarados',
                    'lapras',
                    'ditto',
                    'eevee',
                    'vaporeon',
                    'jolteon',
                    'flareon',
                    'porygon',
                    'omanyte',
                    'omastar',
                    'kabuto',
                    'kabutops',
                    'aerodactyl',
                    'snorlax',
                    'articuno',
                    'zapdos',
                    'moltres',
                    'dratini',
                    'dragonair',
                    'dragonite',
                    'mewtwo',
                    'mew',
                    'chikorita',
                    'bayleef',
                    'meganium',
                    'cyndaquil',
                    'quilava',
                    'typhlosion',
                    'totodile',
                    'croconaw',
                    'feraligatr',
                    'sentret',
                    'furret',
                    'hoothoot',
                    'noctowl',
                    'ledyba',
                    'ledian',
                    'spinarak',
                    'ariados',
                    'crobat',
                    'chinchou',
                    'lanturn',
                    'pichu',
                    'cleffa',
                    'igglybuff',
                    'togepi',
                    'togetic',
                    'natu',
                    'xatu',
                    'mareep',
                    'flaaffy',
                    'ampharos',
                    'bellossom',
                    'marill',
                    'azumarill',
                    'sudowoodo',
                    'politoed',
                    'hoppip',
                    'skiploom',
                    'jumpluff',
                    'aipom',
                    'sunkern',
                    'sunflora',
                    'yanma',
                    'wooper',
                    'quagsire',
                    'espeon',
                    'umbreon',
                    'murkrow',
                    'slowking',
                    'misdreavus',
                    'unown',
                    'wobbuffet',
                    'girafarig',
                    'pineco',
                    'forretress',
                    'dunsparce',
                    'gligar',
                    'steelix',
                    'snubbull',
                    'granbull',
                    'qwilfish',
                    'scizor',
                    'shuckle',
                    'heracross',
                    'sneasel',
                    'teddiursa',
                    'ursaring',
                    'slugma',
                    'magcargo',
                    'swinub',
                    'piloswine',
                    'corsola',
                    'remoraid',
                    'octillery',
                    'delibird',
                    'mantine',
                    'skarmory',
                    'houndour',
                    'houndoom',
                    'kingdra',
                    'phanpy',
                    'donphan',
                    'porygon2',
                    'stantler',
                    'smeargle',
                    'tyrogue',
                    'hitmontop',
                    'smoochum',
                    'elekid',
                    'magby',
                    'miltank',
                    'blissey',
                    'raikou',
                    'entei',
                    'suicune',
                    'larvitar',
                    'pupitar',
                    'tyranitar',
                    'lugia',
                    'ho-oh',
                    'celebi',
                    'treecko',
                    'grovyle',
                    'sceptile',
                    'torchic',
                    'combusken',
                    'blaziken',
                    'mudkip',
                    'marshtomp',
                    'swampert',
                    'poochyena',
                    'mightyena',
                    'zigzagoon',
                    'linoone',
                    'wurmple',
                    'silcoon',
                    'beautifly',
                    'cascoon',
                    'dustox',
                    'lotad',
                    'lombre',
                    'ludicolo',
                    'seedot',
                    'nuzleaf',
                    'shiftry',
                    'taillow',
                    'swellow',
                    'wingull',
                    'pelipper',
                    'ralts',
                    'kirlia',
                    'gardevoir',
                    'surskit',
                    'masquerain',
                    'shroomish',
                    'breloom',
                    'slakoth',
                    'vigoroth',
                    'slaking',
                    'nincada',
                    'ninjask',
                    'shedinja',
                    'whismur',
                    'loudred',
                    'exploud',
                    'makuhita',
                    'hariyama',
                    'azurill',
                    'nosepass',
                    'skitty',
                    'delcatty',
                    'sableye',
                    'mawile',
                    'aron',
                    'lairon',
                    'aggron',
                    'meditite',
                    'medicham',
                    'electrike',
                    'manectric',
                    'plusle',
                    'minun',
                    'volbeat',
                    'illumise',
                    'roselia',
                    'gulpin',
                    'swalot',
                    'carvanha',
                    'sharpedo',
                    'wailmer',
                    'wailord',
                    'numel',
                    'camerupt',
                    'torkoal',
                    'spoink',
                    'grumpig',
                    'spinda',
                    'trapinch',
                    'vibrava',
                    'flygon',
                    'cacnea',
                    'cacturne',
                    'swablu',
                    'altaria',
                    'zangoose',
                    'seviper',
                    'lunatone',
                    'solrock',
                    'barboach',
                    'whiscash',
                    'corphish',
                    'crawdaunt',
                    'baltoy',
                    'claydol',
                    'lileep',
                    'cradily',
                    'anorith',
                    'armaldo',
                    'feebas',
                    'milotic',
                    'castform',
                    'kecleon',
                    'shuppet',
                    'banette',
                    'duskull',
                    'dusclops',
                    'tropius',
                    'chimecho',
                    'absol',
                    'wynaut',
                    'snorunt',
                    'glalie',
                    'spheal',
                    'sealeo',
                    'walrein',
                    'clamperl',
                    'huntail',
                    'gorebyss',
                    'relicanth',
                    'luvdisc',
                    'bagon',
                    'shelgon',
                    'salamence',
                    'beldum',
                    'metang',
                    'metagross',
                    'regirock',
                    'regice',
                    'registeel',
                    'latias',
                    'latios',
                    'kyogre',
                    'groudon',
                    'rayquaza',
                    'jirachi',
                    'deoxys']
pokedex_rs = ['#000 ?????',
              '#001 Bulbasaur',
              '#002 Ivysaur',
              '#003 Venusaur',
              '#004 Charmander',
              '#005 Charmeleon',
              '#006 Charizard',
              '#007 Squirtle',
              '#008 Wartortle',
              '#009 Blastoise',
              '#010 Caterpie',
              '#011 Metapod',
              '#012 Butterfree',
              '#013 Weedle',
              '#014 Kakuna',
              '#015 Beedrill',
              '#016 Pidgey',
              '#017 Pidgeotto',
              '#018 Pidgeot',
              '#019 Rattata',
              '#020 Raticate',
              '#021 Spearow',
              '#022 Fearow',
              '#023 Ekans',
              '#024 Arbok',
              '#025 Pikachu',
              '#026 Raichu',
              '#027 Sandshrew',
              '#028 Sandslash',
              '#029 Nidoran?',
              '#030 Nidorina',
              '#031 Nidoqueen',
              '#032 Nidoran?',
              '#033 Nidorino',
              '#034 Nidoking',
              '#035 Clefairy',
              '#036 Clefable',
              '#037 Vulpix',
              '#038 Ninetales',
              '#039 Jigglypuff',
              '#040 Wigglytuff',
              '#041 Zubat',
              '#042 Golbat',
              '#043 Oddish',
              '#044 Gloom',
              '#045 Vileplume',
              '#046 Paras',
              '#047 Parasect',
              '#048 Venonat',
              '#049 Venomoth',
              '#050 Diglett',
              '#051 Dugtrio',
              '#052 Meowth',
              '#053 Persian',
              '#054 Psyduck',
              '#055 Golduck',
              '#056 Mankey',
              '#057 Primeape',
              '#058 Growlithe',
              '#059 Arcanine',
              '#060 Poliwag',
              '#061 Poliwhirl',
              '#062 Poliwrath',
              '#063 Abra',
              '#064 Kadabra',
              '#065 Alakazam',
              '#066 Machop',
              '#067 Machoke',
              '#068 Machamp',
              '#069 Bellsprout',
              '#070 Weepinbell',
              '#071 Victreebel',
              '#072 Tentacool',
              '#073 Tentacruel',
              '#074 Geodude',
              '#075 Graveler',
              '#076 Golem',
              '#077 Ponyta',
              '#078 Rapidash',
              '#079 Slowpoke',
              '#080 Slowbro',
              '#081 Magnemite',
              '#082 Magneton',
              "#083 Farfetch'd",
              '#084 Doduo',
              '#085 Dodrio',
              '#086 Seel',
              '#087 Dewgong',
              '#088 Grimer',
              '#089 Muk',
              '#090 Shellder',
              '#091 Cloyster',
              '#092 Gastly',
              '#093 Haunter',
              '#094 Gengar',
              '#095 Onix',
              '#096 Drowzee',
              '#097 Hypno',
              '#098 Krabby',
              '#099 Kingler',
              '#100 Voltorb',
              '#101 Electrode',
              '#102 Exeggcute',
              '#103 Exeggutor',
              '#104 Cubone',
              '#105 Marowak',
              '#106 Hitmonlee',
              '#107 Hitmonchan',
              '#108 Lickitung',
              '#109 Koffing',
              '#110 Weezing',
              '#111 Rhyhorn',
              '#112 Rhydon',
              '#113 Chansey',
              '#163 Tangela',
              '#115 Kangaskhan',
              '#116 Horsea',
              '#117 Seadra',
              '#118 Goldeen',
              '#119 Seaking',
              '#120 Staryu',
              '#121 Starmie',
              '#122 Mr. Mime',
              '#123 Scyther',
              '#124 Jynx',
              '#125 Electabuzz',
              '#126 Magmar',
              '#127 Pinsir',
              '#128 Tauros',
              '#129 Magikarp',
              '#130 Gyarados',
              '#131 Lapras',
              '#132 Ditto',
              '#133 Eevee',
              '#134 Vaporeon',
              '#135 Jolteon',
              '#136 Flareon',
              '#137 Porygon',
              '#138 Omanyte',
              '#139 Omastar',
              '#140 Kabuto',
              '#141 Kabutops',
              '#142 Aerodactyl',
              '#143 Snorlax',
              '#144 Articuno',
              '#145 Zapdos',
              '#146 Moltres',
              '#147 Dratini',
              '#148 Dragonair',
              '#149 Dragonite',
              '#150 Mewtwo',
              '#151 Mew',
              '#152 Chikorita',
              '#153 Bayleef',
              '#154 Meganium',
              '#155 Cyndaquil',
              '#156 Quilava',
              '#163 Typhlosion',
              '#158 Totodile',
              '#159 Croconaw',
              '#160 Feraligatr',
              '#161 Sentret',
              '#162 Furret',
              '#163 Hoothoot',
              '#164 Noctowl',
              '#165 Ledyba',
              '#166 Ledian',
              '#167 Spinarak',
              '#168 Ariados',
              '#169 Crobat',
              '#170 Chinchou',
              '#171 Lanturn',
              '#172 Pichu',
              '#173 Cleffa',
              '#174 Igglybuff',
              '#175 Togepi',
              '#176 Togetic',
              '#177 Natu',
              '#178 Xatu',
              '#179 Mareep',
              '#180 Flaaffy',
              '#181 Ampharos',
              '#182 Bellossom',
              '#183 Marill',
              '#184 Azumarill',
              '#185 Sudowoodo',
              '#186 Politoed',
              '#187 Hoppip',
              '#188 Skiploom',
              '#189 Jumpluff',
              '#190 Aipom',
              '#191 Sunkern',
              '#192 Sunflora',
              '#193 Yanma',
              '#194 Wooper',
              '#195 Quagsire',
              '#196 Espeon',
              '#197 Umbreon',
              '#198 Murkrow',
              '#199 Slowking',
              '#200 Misdreavus',
              '#201 Unown',
              '#202 Wobbuffet',
              '#203 Girafarig',
              '#204 Pineco',
              '#205 Forretress',
              '#206 Dunsparce',
              '#207 Gligar',
              '#208 Steelix',
              '#209 Snubbull',
              '#210 Granbull',
              '#211 Qwilfish',
              '#212 Scizor',
              '#213 Shuckle',
              '#214 Heracross',
              '#215 Sneasel',
              '#216 Teddiursa',
              '#217 Ursaring',
              '#218 Slugma',
              '#219 Magcargo',
              '#220 Swinub',
              '#221 Piloswine',
              '#222 Corsola',
              '#223 Remoraid',
              '#224 Octillery',
              '#225 Delibird',
              '#226 Mantine',
              '#227 Skarmory',
              '#228 Houndour',
              '#229 Houndoom',
              '#230 Kingdra',
              '#231 Phanpy',
              '#232 Donphan',
              '#233 Porygon2',
              '#234 Stantler',
              '#235 Smeargle',
              '#236 Tyrogue',
              '#237 Hitmontop',
              '#238 Smoochum',
              '#239 Elekid',
              '#240 Magby',
              '#241 Miltank',
              '#242 Blissey',
              '#243 Raikou',
              '#244 Entei',
              '#245 Suicune',
              '#246 Larvitar',
              '#247 Pupitar',
              '#248 Tyranitar',
              '#249 Lugia',
              '#250 Ho-oh',
              '#251 Celebi',
              '#252 Treecko',
              '#253 Grovyle',
              '#254 Sceptile',
              '#255 Torchic',
              '#256 Combusken',
              '#257 Blaziken',
              '#258 Mudkip',
              '#259 Marshtomp',
              '#260 Swampert',
              '#261 Poochyena',
              '#262 Mightyena',
              '#263 Zigzagoon',
              '#264 Linoone',
              '#265 Wurmple',
              '#266 Silcoon',
              '#267 Beautifly',
              '#268 Cascoon',
              '#269 Dustox',
              '#270 Lotad',
              '#271 Lombre',
              '#272 Ludicolo',
              '#273 Seedot',
              '#274 Nuzleaf',
              '#275 Shiftry',
              '#276 Taillow',
              '#277 Swellow',
              '#278 Wingull',
              '#279 Pelipper',
              '#280 Ralts',
              '#281 Kirlia',
              '#282 Gardevoir',
              '#283 Surskit',
              '#284 Masquerain',
              '#285 Shroomish',
              '#286 Breloom',
              '#287 Slakoth',
              '#288 Vigoroth',
              '#289 Slaking',
              '#290 Nincada',
              '#291 Ninjask',
              '#292 Shedinja',
              '#293 Whismur',
              '#294 Loudred',
              '#295 Exploud',
              '#296 Makuhita',
              '#297 Hariyama',
              '#298 Azurill',
              '#299 Nosepass',
              '#300 Skitty',
              '#301 Delcatty',
              '#302 Sableye',
              '#303 Mawile',
              '#304 Aron',
              '#305 Lairon',
              '#306 Aggron',
              '#307 Meditite',
              '#308 Medicham',
              '#309 Electrike',
              '#310 Manectric',
              '#311 Plusle',
              '#312 Minun',
              '#313 Volbeat',
              '#314 Illumise',
              '#315 Roselia',
              '#316 Gulpin',
              '#317 Swalot',
              '#318 Carvanha',
              '#319 Sharpedo',
              '#320 Wailmer',
              '#321 Wailord',
              '#322 Numel',
              '#323 Camerupt',
              '#324 Torkoal',
              '#325 Spoink',
              '#326 Grumpig',
              '#327 Spinda',
              '#328 Trapinch',
              '#329 Vibrava',
              '#330 Flygon',
              '#331 Cacnea',
              '#332 Cacturne',
              '#333 Swablu',
              '#334 Altaria',
              '#335 Zangoose',
              '#336 Seviper',
              '#337 Lunatone',
              '#338 Solrock',
              '#339 Barboach',
              '#340 Whiscash',
              '#341 Corphish',
              '#342 Crawdaunt',
              '#343 Baltoy',
              '#344 Claydol',
              '#345 Lileep',
              '#346 Cradily',
              '#347 Anorith',
              '#348 Armaldo',
              '#349 Feebas',
              '#350 Milotic',
              '#351 Castform',
              '#352 Kecleon',
              '#353 Shuppet',
              '#354 Banette',
              '#355 Duskull',
              '#356 Dusclops',
              '#357 Tropius',
              '#358 Chimecho',
              '#359 Absol',
              '#360 Wynaut',
              '#361 Snorunt',
              '#362 Glalie',
              '#363 Spheal',
              '#364 Sealeo',
              '#365 Walrein',
              '#366 Clamperl',
              '#367 Huntail',
              '#368 Gorebyss',
              '#369 Relicanth',
              '#370 Luvdisc',
              '#371 Bagon',
              '#372 Shelgon',
              '#373 Salamence',
              '#374 Beldum',
              '#375 Metang',
              '#376 Metagross',
              '#377 Regirock',
              '#378 Regice',
              '#379 Registeel',
              '#380 Latias',
              '#381 Latios',
              '#382 Kyogre',
              '#383 Groudon',
              '#384 Rayquaza',
              '#385 Jirachi',
              '#386 Deoxys']
moves_rs = ['-- No Move -- (0)',
            'Pound',
            'Karate Chop',
            'Doubleslap',
            'Comet Punch',
            'Mega Punch',
            'Pay Day',
            'Fire Punch',
            'Ice Punch',
            'Thunderpunch',
            'Scratch',
            'Vicegrip',
            'Guillotine',
            'Razor Wind',
            'Swords Dance',
            'Cut',
            'Gust',
            'Wing Attack',
            'Whirlwind',
            'Fly',
            'Bind',
            'Slam',
            'Vine Whip',
            'Stomp',
            'Double Kick',
            'Mega Kick',
            'Jump Kick',
            'Rolling Kick',
            'Sand-attack',
            'Headbutt',
            'Horn Attack',
            'Fury Attack',
            'Horn Drill',
            'Tackle',
            'Body Slam',
            'Wrap',
            'Take Down',
            'Thrash',
            'Double-edge',
            'Tail Whip',
            'Poison Sting',
            'Twineedle',
            'Pin Missile',
            'Leer',
            'Bite',
            'Growl',
            'Roar',
            'Sing',
            'Supersonic',
            'Sonicboom',
            'Disable',
            'Acid',
            'Ember',
            'Flamethrower',
            'Mist',
            'Water Gun',
            'Hydro Pump',
            'Surf',
            'Ice Beam',
            'Blizzard',
            'Psybeam',
            'Bubblebeam',
            'Aurora Beam',
            'Hyper Beam',
            'Peck',
            'Drill Peck',
            'Submission',
            'Low Kick',
            'Counter',
            'Seismic Toss',
            'Strength',
            'Absorb',
            'Mega Drain',
            'Leech Seed',
            'Growth',
            'Razor Leaf',
            'Solarbeam',
            'Poisonpowder',
            'Stun Spore',
            'Sleep Powder',
            'Petal Dance',
            'String Shot',
            'Dragon Rage',
            'Fire Spin',
            'Thundershock',
            'Thunderbolt',
            'Thunder Wave',
            'Thunder',
            'Rock Throw',
            'Earthquake',
            'Fissure',
            'Dig',
            'Toxic',
            'Confusion',
            'Psychic',
            'Hypnosis',
            'Meditate',
            'Agility',
            'Quick Attack',
            'Rage',
            'Teleport',
            'Night Shade',
            'Mimic',
            'Screech',
            'Double Team',
            'Recover',
            'Harden',
            'Minimize',
            'Smokescreen',
            'Confuse Ray',
            'Withdraw',
            'Defense Curl',
            'Barrier',
            'Light Screen',
            'Haze',
            'Reflect',
            'Focus Energy',
            'Bide',
            'Metronome',
            'Mirror Move',
            'Selfdestruct',
            'Egg Bomb',
            'Lick',
            'Smog',
            'Sludge',
            'Bone Club',
            'Fire Blast',
            'Waterfall',
            'Clamp',
            'Swift',
            'Skull Bash',
            'Spike Cannon',
            'Constrict',
            'Amnesia',
            'Kinesis',
            'Softboiled',
            'Hi Jump Kick',
            'Glare',
            'Dream Eater',
            'Poison Gas',
            'Barrage',
            'Leech Life',
            'Lovely Kiss',
            'Sky Attack',
            'Transform',
            'Bubble',
            'Dizzy Punch',
            'Spore',
            'Flash',
            'Psywave',
            'Splash',
            'Acid Armor',
            'Crabhammer',
            'Explosion',
            'Fury Swipes',
            'Bonemerang',
            'Rest',
            'Rock Slide',
            'Hyper Fang',
            'Sharpen',
            'Conversion',
            'Tri Attack',
            'Super Fang',
            'Slash',
            'Substitute',
            'Struggle',
            'Sketch',
            'Triple Kick',
            'Thief',
            'Spider Web',
            'Mind Reader',
            'Nightmare',
            'Flame Wheel',
            'Snore',
            'Curse',
            'Flail',
            'Conversion 2',
            'Aeroblast',
            'Cotton Spore',
            'Reversal',
            'Spite',
            'Powder Snow',
            'Protect',
            'Mach Punch',
            'Scary Face',
            'Faint Attack',
            'Sweet Kiss',
            'Belly Drum',
            'Sludge Bomb',
            'Mud-slap',
            'Octazooka',
            'Spikes',
            'Zap Cannon',
            'Foresight',
            'Destiny Bond',
            'Perish Song',
            'Icy Wind',
            'Detect',
            'Bone Rush',
            'Lock-on',
            'Outrage',
            'Sandstorm',
            'Giga Drain',
            'Endure',
            'Charm',
            'Rollout',
            'False Swipe',
            'Swagger',
            'Milk Drink',
            'Spark',
            'Fury Cutter',
            'Steel Wing',
            'Mean Look',
            'Attract',
            'Sleep Talk',
            'Heal Bell',
            'Return',
            'Present',
            'Frustration',
            'Safeguard',
            'Pain Split',
            'Sacred Fire',
            'Magnitude',
            'Dynamicpunch',
            'Megahorn',
            'Dragonbreath',
            'Baton Pass',
            'Encore',
            'Pursuit',
            'Rapid Spin',
            'Sweet Scent',
            'Iron Tail',
            'Metal Claw',
            'Vital Throw',
            'Morning Sun',
            'Synthesis',
            'Moonlight',
            'Hidden Power',
            'Cross Chop',
            'Twister',
            'Rain Dance',
            'Sunny Day',
            'Crunch',
            'Mirror Coat',
            'Psych Up',
            'Extremespeed',
            'Ancientpower',
            'Shadow Ball',
            'Future Sight',
            'Rock Smash',
            'Whirlpool',
            'Beat Up',
            'Fake Out',
            'Uproar',
            'Stockpile',
            'Spit Up',
            'Swallow',
            'Heat Wave',
            'Hail',
            'Torment',
            'Flatter',
            'Will-o-wisp',
            'Memento',
            'Facade',
            'Focus Punch',
            'Smellingsalt',
            'Follow Me',
            'Nature Power',
            'Charge',
            'Taunt',
            'Helping Hand',
            'Trick',
            'Role Play',
            'Wish',
            'Assist',
            'Ingrain',
            'Superpower',
            'Magic Coat',
            'Recycle',
            'Revenge',
            'Brick Break',
            'Yawn',
            'Knock Off',
            'Endeavor',
            'Eruption',
            'Skill Swap',
            'Imprison',
            'Refresh',
            'Grudge',
            'Snatch',
            'Secret Power',
            'Dive',
            'Arm Thrust',
            'Camouflage',
            'Tail Glow',
            'Luster Purge',
            'Mist Ball',
            'Featherdance',
            'Teeter Dance',
            'Blaze Kick',
            'Mud Sport',
            'Ice Ball',
            'Needle Arm',
            'Slack Off',
            'Hyper Voice',
            'Poison Fang',
            'Crush Claw',
            'Blast Burn',
            'Hydro Cannon',
            'Meteor Mash',
            'Astonish',
            'Weather Ball',
            'Aromatherapy',
            'Fake Tears',
            'Air Cutter',
            'Overheat',
            'Odor Sleuth',
            'Rock Tomb',
            'Silver Wind',
            'Metal Sound',
            'Grasswhistle',
            'Tickle',
            'Cosmic Power',
            'Water Spout',
            'Signal Beam',
            'Shadow Punch',
            'Extrasensory',
            'Sky Uppercut',
            'Sand Tomb',
            'Sheer Cold',
            'Muddy Water',
            'Bullet Seed',
            'Aerial Ace',
            'Icicle Spear',
            'Iron Defense',
            'Block',
            'Howl',
            'Dragon Claw',
            'Frenzy Plant',
            'Bulk Up',
            'Bounce',
            'Mud Shot',
            'Poison Tail',
            'Covet',
            'Volt Tackle',
            'Magical Leaf',
            'Water Sport',
            'Calm Mind',
            'Leaf Blade',
            'Dragon Dance',
            'Rock Blast',
            'Shock Wave',
            'Water Pulse',
            'Doom Desire',
            'Psycho Boost']
types_rs = ['Normal',
            'Fighting',
            'Flying',
            'Poison',
            'Ground',
            'Rock',
            'Bird',
            'Bug',
            'Ghost',
            'Steel',
            '~10',
            '~11',
            '~12',
            '~13',
            '~14',
            '~15',
            '~16',
            '~17',
            '~18',
            '~19',
            'Fire',
            'Water',
            'Grass',
            'Electric',
            'Psychic',
            'Ice',
            'Dragon',
            'Dark',
            '~28',
            '~29',
            '~30',
            '~31',
            '~32',
            '~33',
            '~34',
            '~35',
            '~36',
            '~37',
            '~38',
            '~39',
            '~40',
            '~41',
            '~42',
            '~43',
            '~44',
            '~45',
            '~46',
            '~47',
            '~48',
            '~49',
            '~50',
            '~51',
            '~52',
            '~53',
            '~54',
            '~55',
            '~56',
            '~57',
            '~58',
            '~59',
            '~60',
            '~61',
            '~62',
            '~63',
            '~64',
            '~65',
            '~66',
            '~67',
            '~68',
            '~69',
            '~70',
            '~71',
            '~72',
            '~73',
            '~74',
            '~75',
            '~76',
            '~77',
            '~78',
            '~79',
            '~80',
            '~81',
            '~82',
            '~83',
            '~84',
            '~85',
            '~86',
            '~87',
            '~88',
            '~89',
            '~90',
            '~91',
            '~92',
            '~93',
            '~94',
            '~95',
            '~96',
            '~97',
            '~98',
            '~99',
            '~100',
            '~101',
            '~102',
            '~103',
            '~104',
            '~105',
            '~106',
            '~107',
            '~108',
            '~109',
            '~110',
            '~111',
            '~112',
            '~113',
            '~163',
            '~115',
            '~116',
            '~117',
            '~118',
            '~119',
            '~120',
            '~121',
            '~122',
            '~123',
            '~124',
            '~125',
            '~126',
            '~127',
            '~128',
            '~129',
            '~130',
            '~131',
            '~132',
            '~133',
            '~134',
            '~135',
            '~136',
            '~137',
            '~138',
            '~139',
            '~140',
            '~141',
            '~142',
            '~143',
            '~144',
            '~145',
            '~146',
            '~147',
            '~148',
            '~149',
            '~150',
            '~151',
            '~152',
            '~153',
            '~154',
            '~155',
            '~156',
            '~163',
            '~158',
            '~159',
            '~160',
            '~161',
            '~162',
            '~163',
            '~164',
            '~165',
            '~166',
            '~167',
            '~168',
            '~169',
            '~170',
            '~171',
            '~172',
            '~173',
            '~174',
            '~175',
            '~176',
            '~177',
            '~178',
            '~179',
            '~180',
            '~181',
            '~182',
            '~183',
            '~184',
            '~185',
            '~186',
            '~187',
            '~188',
            '~189',
            '~190',
            '~191',
            '~192',
            '~193',
            '~194',
            '~195',
            '~196',
            '~197',
            '~198',
            '~199',
            '~200',
            '~201',
            '~202',
            '~203',
            '~204',
            '~205',
            '~206',
            '~207',
            '~208',
            '~209',
            '~210',
            '~211',
            '~212',
            '~213',
            '~214',
            '~215',
            '~216',
            '~217',
            '~218',
            '~219',
            '~220',
            '~221',
            '~222',
            '~223',
            '~224',
            '~225',
            '~226',
            '~227',
            '~228',
            '~229',
            '~230',
            '~231',
            '~232',
            '~233',
            '~234',
            '~235',
            '~236',
            '~237',
            '~238',
            '~239',
            '~240',
            '~241',
            '~242',
            '~243',
            '~244',
            '~245',
            '~246',
            '~247',
            '~248',
            '~249',
            '~250',
            '~251',
            '~252',
            '~253',
            '~254',
            '~255']
growthrates = [205,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               3,
               3,
               3,
               3,
               3,
               3,
               4,
               4,
               0,
               0,
               4,
               4,
               0,
               0,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               5,
               5,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               4,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               5,
               5,
               5,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               4,
               4,
               4,
               4,
               0,
               5,
               5,
               0,
               4,
               4,
               4,
               4,
               0,
               0,
               3,
               3,
               3,
               3,
               4,
               4,
               0,
               3,
               3,
               3,
               3,
               4,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               3,
               0,
               4,
               0,
               0,
               0,
               0,
               0,
               0,
               3,
               0,
               4,
               4,
               0,
               0,
               3,
               5,
               3,
               0,
               0,
               0,
               0,
               5,
               5,
               4,
               0,
               0,
               4,
               5,
               5,
               5,
               5,
               0,
               0,
               0,
               0,
               5,
               4,
               0,
               0,
               0,
               0,
               0,
               5,
               4,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               3,
               3,
               3,
               3,
               3,
               3,
               1,
               1,
               1,
               3,
               3,
               2,
               2,
               4,
               0,
               0,
               0,
               0,
               2,
               2,
               4,
               4,
               3,
               0,
               0,
               0,
               0,
               3,
               0,
               0,
               4,
               2,
               2,
               1,
               1,
               5,
               5,
               3,
               3,
               3,
               2,
               2,
               5,
               5,
               0,
               0,
               3,
               3,
               3,
               3,
               3,
               0,
               0,
               4,
               4,
               4,
               4,
               4,
               0,
               0,
               4,
               0,
               0,
               1,
               1,
               0,
               4,
               4,
               3,
               5,
               5,
               5,
               2,
               2,
               5,
               3,
               3,
               3,
               1,
               1,
               1,
               3,
               4,
               4,
               2,
               1,
               5,
               5,
               5,
               5,
               0,
               1,
               2,
               1,
               1,
               1,
               1,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               4,
               255,
               15,
               224,
               255]
base_hp = [255,
           45,
           60,
           80,
           39,
           58,
           78,
           44,
           59,
           79,
           45,
           50,
           60,
           40,
           45,
           65,
           40,
           63,
           83,
           30,
           55,
           40,
           65,
           35,
           60,
           35,
           60,
           50,
           75,
           55,
           70,
           90,
           46,
           61,
           81,
           70,
           95,
           38,
           73,
           115,
           140,
           40,
           75,
           45,
           60,
           75,
           35,
           60,
           60,
           70,
           10,
           35,
           40,
           65,
           50,
           80,
           40,
           65,
           55,
           90,
           40,
           65,
           90,
           25,
           40,
           55,
           70,
           80,
           90,
           50,
           65,
           80,
           40,
           80,
           40,
           55,
           80,
           50,
           65,
           90,
           95,
           25,
           50,
           52,
           35,
           60,
           65,
           90,
           80,
           105,
           30,
           50,
           30,
           45,
           60,
           35,
           60,
           85,
           30,
           55,
           40,
           60,
           60,
           95,
           50,
           60,
           50,
           50,
           90,
           40,
           65,
           80,
           105,
           250,
           65,
           105,
           30,
           55,
           45,
           80,
           30,
           60,
           40,
           70,
           65,
           65,
           65,
           65,
           75,
           20,
           95,
           130,
           48,
           55,
           130,
           65,
           65,
           65,
           35,
           70,
           30,
           60,
           80,
           160,
           90,
           90,
           90,
           41,
           61,
           91,
           106,
           100,
           45,
           60,
           80,
           39,
           58,
           78,
           50,
           65,
           85,
           35,
           85,
           60,
           100,
           40,
           55,
           40,
           70,
           85,
           75,
           125,
           20,
           50,
           90,
           35,
           55,
           40,
           65,
           55,
           70,
           90,
           75,
           70,
           100,
           70,
           90,
           35,
           55,
           75,
           55,
           30,
           75,
           65,
           55,
           95,
           65,
           95,
           60,
           95,
           60,
           48,
           190,
           70,
           50,
           75,
           100,
           65,
           75,
           60,
           90,
           65,
           70,
           20,
           80,
           55,
           60,
           90,
           40,
           50,
           50,
           100,
           55,
           35,
           75,
           45,
           65,
           65,
           45,
           75,
           75,
           90,
           90,
           85,
           73,
           55,
           35,
           50,
           45,
           45,
           45,
           95,
           255,
           90,
           115,
           100,
           50,
           70,
           100,
           106,
           106,
           100,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           255,
           40,
           50,
           70,
           45,
           60,
           80,
           50,
           70,
           100,
           35,
           70,
           38,
           78,
           45,
           50,
           60,
           50,
           60,
           40,
           60,
           80,
           40,
           70,
           90,
           31,
           61,
           1,
           40,
           60,
           60,
           60,
           60,
           40,
           60,
           40,
           70,
           130,
           170,
           50,
           70,
           60,
           40,
           60,
           30,
           70,
           50,
           50,
           110,
           43,
           43,
           63,
           20,
           95,
           45,
           70,
           45,
           50,
           80,
           72,
           144,
           40,
           70,
           60,
           70,
           70,
           90,
           110,
           50,
           70,
           50,
           80,
           70,
           70,
           50,
           60,
           80,
           60,
           60,
           50,
           30,
           60,
           45,
           75,
           95,
           20,
           40,
           50,
           60,
           80,
           150,
           70,
           100,
           99,
           64,
           84,
           104,
           35,
           55,
           55,
           65,
           44,
           64,
           73,
           73,
           100,
           50,
           60,
           70,
           70,
           65,
           65,
           66,
           86,
           45,
           75,
           28,
           38,
           68,
           45,
           65,
           95,
           40,
           60,
           80,
           80,
           80,
           80,
           100,
           100,
           105,
           80,
           80,
           100,
           50,
           65,
           255
           ]
base_attack = [255,
               49,
               62,
               82,
               52,
               64,
               84,
               48,
               63,
               83,
               30,
               20,
               45,
               35,
               25,
               80,
               45,
               60,
               80,
               56,
               81,
               60,
               90,
               60,
               85,
               55,
               90,
               75,
               100,
               47,
               62,
               82,
               57,
               72,
               92,
               45,
               70,
               41,
               76,
               45,
               70,
               45,
               80,
               50,
               65,
               80,
               70,
               95,
               55,
               65,
               55,
               80,
               45,
               70,
               52,
               82,
               80,
               105,
               70,
               110,
               50,
               65,
               85,
               20,
               35,
               50,
               80,
               100,
               130,
               75,
               90,
               105,
               40,
               70,
               80,
               95,
               110,
               85,
               100,
               65,
               75,
               35,
               60,
               65,
               85,
               110,
               45,
               70,
               80,
               105,
               65,
               95,
               35,
               50,
               65,
               45,
               48,
               73,
               105,
               130,
               30,
               50,
               40,
               95,
               50,
               80,
               120,
               105,
               55,
               65,
               90,
               85,
               130,
               5,
               55,
               95,
               40,
               65,
               67,
               92,
               45,
               75,
               45,
               110,
               50,
               83,
               95,
               125,
               100,
               10,
               125,
               85,
               48,
               55,
               65,
               65,
               130,
               60,
               40,
               60,
               80,
               115,
               105,
               110,
               85,
               90,
               100,
               64,
               84,
               134,
               110,
               100,
               49,
               62,
               82,
               52,
               64,
               84,
               65,
               80,
               105,
               46,
               76,
               30,
               50,
               20,
               35,
               60,
               90,
               90,
               38,
               58,
               40,
               25,
               30,
               20,
               40,
               50,
               75,
               40,
               55,
               75,
               80,
               20,
               50,
               100,
               75,
               35,
               45,
               55,
               70,
               30,
               75,
               65,
               45,
               85,
               65,
               65,
               85,
               75,
               60,
               72,
               33,
               80,
               65,
               90,
               70,
               75,
               85,
               80,
               120,
               95,
               130,
               10,
               125,
               95,
               80,
               130,
               40,
               50,
               50,
               100,
               55,
               65,
               105,
               55,
               40,
               80,
               60,
               90,
               95,
               60,
               120,
               80,
               95,
               20,
               35,
               95,
               30,
               63,
               75,
               80,
               10,
               85,
               115,
               75,
               64,
               84,
               134,
               90,
               130,
               100,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               255,
               45,
               65,
               85,
               60,
               85,
               120,
               70,
               85,
               110,
               55,
               90,
               30,
               70,
               45,
               35,
               70,
               35,
               50,
               30,
               50,
               70,
               40,
               70,
               100,
               45,
               90,
               90,
               55,
               85,
               40,
               130,
               60,
               30,
               50,
               30,
               60,
               70,
               90,
               45,
               65,
               90,
               40,
               70,
               45,
               85,
               75,
               48,
               78,
               30,
               80,
               120,
               15,
               60,
               90,
               120,
               100,
               70,
               100,
               60,
               120,
               45,
               75,
               60,
               100,
               40,
               60,
               80,
               85,
               115,
               50,
               80,
               55,
               95,
               20,
               25,
               45,
               50,
               40,
               85,
               40,
               60,
               40,
               70,
               23,
               40,
               70,
               60,
               60,
               80,
               160,
               43,
               73,
               68,
               51,
               71,
               91,
               64,
               104,
               84,
               130,
               75,
               115,
               100,
               115,
               90,
               70,
               90,
               110,
               70,
               73,
               47,
               41,
               81,
               95,
               125,
               25,
               35,
               65,
               75,
               95,
               135,
               55,
               75,
               135,
               100,
               50,
               75,
               100,
               150,
               150,
               80,
               90,
               100,
               150,
               50]
base_defense = [255,
                49,
                63,
                83,
                43,
                58,
                78,
                65,
                80,
                100,
                35,
                55,
                50,
                30,
                50,
                40,
                40,
                55,
                75,
                35,
                60,
                30,
                65,
                44,
                69,
                30,
                55,
                85,
                110,
                52,
                67,
                87,
                40,
                57,
                77,
                48,
                73,
                40,
                75,
                20,
                45,
                35,
                70,
                55,
                70,
                85,
                55,
                80,
                50,
                60,
                25,
                50,
                35,
                60,
                48,
                78,
                35,
                60,
                45,
                80,
                40,
                65,
                95,
                15,
                30,
                45,
                50,
                70,
                80,
                35,
                50,
                65,
                35,
                65,
                100,
                115,
                130,
                55,
                70,
                65,
                110,
                70,
                95,
                55,
                45,
                70,
                55,
                80,
                50,
                75,
                100,
                180,
                30,
                45,
                60,
                160,
                45,
                70,
                90,
                115,
                50,
                70,
                80,
                85,
                95,
                110,
                53,
                79,
                75,
                95,
                120,
                95,
                120,
                5,
                115,
                80,
                70,
                95,
                60,
                65,
                55,
                85,
                65,
                80,
                35,
                57,
                57,
                100,
                95,
                55,
                79,
                80,
                48,
                50,
                60,
                60,
                60,
                70,
                100,
                125,
                90,
                105,
                65,
                65,
                100,
                85,
                90,
                45,
                65,
                95,
                90,
                100,
                65,
                80,
                100,
                43,
                58,
                78,
                64,
                80,
                100,
                34,
                64,
                30,
                50,
                30,
                50,
                40,
                70,
                80,
                38,
                58,
                15,
                28,
                15,
                65,
                85,
                45,
                70,
                40,
                55,
                75,
                85,
                50,
                80,
                115,
                75,
                40,
                50,
                70,
                55,
                30,
                55,
                45,
                45,
                85,
                60,
                110,
                42,
                80,
                60,
                48,
                58,
                65,
                90,
                140,
                70,
                105,
                200,
                50,
                75,
                75,
                100,
                230,
                75,
                55,
                50,
                75,
                40,
                120,
                40,
                80,
                85,
                35,
                75,
                45,
                70,
                140,
                30,
                50,
                95,
                60,
                120,
                90,
                62,
                35,
                35,
                95,
                15,
                37,
                37,
                105,
                10,
                75,
                85,
                115,
                50,
                70,
                110,
                130,
                90,
                100,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                35,
                45,
                65,
                40,
                60,
                70,
                50,
                70,
                90,
                35,
                70,
                41,
                61,
                35,
                55,
                50,
                55,
                70,
                30,
                50,
                70,
                50,
                40,
                60,
                90,
                45,
                45,
                30,
                60,
                60,
                80,
                60,
                30,
                100,
                32,
                62,
                35,
                45,
                45,
                65,
                70,
                55,
                105,
                135,
                140,
                75,
                43,
                73,
                55,
                65,
                85,
                20,
                79,
                20,
                40,
                45,
                50,
                80,
                30,
                60,
                40,
                60,
                40,
                70,
                50,
                70,
                90,
                40,
                60,
                50,
                80,
                65,
                85,
                40,
                35,
                65,
                40,
                50,
                85,
                55,
                75,
                60,
                90,
                48,
                90,
                130,
                45,
                60,
                80,
                100,
                53,
                83,
                83,
                23,
                43,
                63,
                85,
                105,
                105,
                60,
                35,
                65,
                60,
                60,
                130,
                100,
                140,
                180,
                70,
                55,
                55,
                77,
                97,
                50,
                100,
                25,
                35,
                65,
                60,
                100,
                80,
                80,
                100,
                130,
                200,
                100,
                150,
                90,
                140,
                90,
                90,
                80,
                100,
                50,
                70
                ]
base_speed = [255,
              45,
              60,
              80,
              65,
              80,
              100,
              43,
              58,
              78,
              45,
              30,
              70,
              50,
              35,
              75,
              56,
              71,
              91,
              72,
              97,
              70,
              100,
              55,
              80,
              90,
              100,
              40,
              65,
              41,
              56,
              76,
              50,
              65,
              85,
              35,
              60,
              65,
              100,
              20,
              45,
              55,
              90,
              30,
              40,
              50,
              25,
              30,
              45,
              90,
              95,
              120,
              90,
              115,
              55,
              85,
              70,
              95,
              60,
              95,
              90,
              90,
              70,
              90,
              105,
              120,
              35,
              45,
              55,
              40,
              55,
              70,
              70,
              100,
              20,
              35,
              45,
              90,
              105,
              15,
              30,
              45,
              70,
              60,
              75,
              100,
              45,
              70,
              25,
              50,
              40,
              70,
              80,
              95,
              110,
              70,
              42,
              67,
              50,
              75,
              100,
              140,
              40,
              55,
              35,
              45,
              87,
              76,
              30,
              35,
              60,
              25,
              40,
              50,
              60,
              90,
              60,
              85,
              63,
              68,
              85,
              115,
              90,
              105,
              95,
              105,
              93,
              85,
              110,
              80,
              81,
              60,
              48,
              55,
              65,
              130,
              65,
              40,
              35,
              55,
              55,
              80,
              130,
              30,
              85,
              100,
              90,
              50,
              70,
              80,
              130,
              100,
              45,
              60,
              80,
              65,
              80,
              100,
              43,
              58,
              78,
              20,
              90,
              50,
              70,
              55,
              85,
              30,
              40,
              130,
              67,
              67,
              60,
              15,
              15,
              20,
              40,
              70,
              95,
              35,
              45,
              55,
              50,
              40,
              50,
              30,
              70,
              50,
              80,
              110,
              85,
              30,
              30,
              95,
              15,
              35,
              110,
              65,
              91,
              30,
              85,
              48,
              33,
              85,
              15,
              40,
              45,
              85,
              30,
              30,
              45,
              85,
              65,
              5,
              85,
              115,
              40,
              55,
              20,
              30,
              50,
              50,
              35,
              65,
              45,
              75,
              70,
              70,
              65,
              95,
              85,
              40,
              50,
              60,
              85,
              75,
              35,
              70,
              65,
              95,
              83,
              100,
              55,
              115,
              100,
              85,
              41,
              51,
              61,
              110,
              90,
              100,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              255,
              70,
              95,
              120,
              45,
              55,
              80,
              40,
              50,
              60,
              35,
              70,
              60,
              100,
              20,
              15,
              65,
              15,
              65,
              30,
              50,
              70,
              30,
              60,
              80,
              40,
              160,
              40,
              85,
              125,
              35,
              70,
              60,
              85,
              65,
              65,
              60,
              60,
              60,
              50,
              70,
              40,
              55,
              75,
              30,
              20,
              50,
              60,
              60,
              97,
              35,
              55,
              80,
              81,
              65,
              95,
              10,
              70,
              100,
              25,
              50,
              65,
              105,
              35,
              40,
              25,
              45,
              65,
              35,
              55,
              50,
              80,
              70,
              70,
              20,
              60,
              80,
              95,
              95,
              50,
              60,
              80,
              50,
              80,
              23,
              25,
              25,
              65,
              30,
              90,
              100,
              40,
              55,
              51,
              28,
              48,
              68,
              32,
              52,
              52,
              75,
              45,
              65,
              65,
              90,
              55,
              30,
              40,
              50,
              70,
              85,
              85,
              23,
              43,
              75,
              45,
              40,
              50,
              80,
              50,
              50,
              100,
              30,
              50,
              70,
              50,
              50,
              50,
              90,
              90,
              95,
              110,
              110,
              100,
              150,
              65
              ]
base_specialattack = [255,
                      65,
                      80,
                      100,
                      60,
                      80,
                      109,
                      50,
                      65,
                      85,
                      20,
                      25,
                      80,
                      20,
                      25,
                      45,
                      35,
                      50,
                      70,
                      25,
                      50,
                      31,
                      61,
                      40,
                      65,
                      50,
                      90,
                      20,
                      45,
                      40,
                      55,
                      75,
                      40,
                      55,
                      85,
                      60,
                      85,
                      50,
                      81,
                      45,
                      75,
                      30,
                      65,
                      75,
                      85,
                      100,
                      45,
                      60,
                      40,
                      90,
                      35,
                      50,
                      40,
                      65,
                      65,
                      95,
                      35,
                      60,
                      70,
                      100,
                      40,
                      50,
                      70,
                      105,
                      120,
                      135,
                      35,
                      50,
                      65,
                      70,
                      85,
                      100,
                      50,
                      80,
                      30,
                      45,
                      55,
                      65,
                      80,
                      40,
                      100,
                      95,
                      120,
                      58,
                      35,
                      60,
                      45,
                      70,
                      40,
                      65,
                      45,
                      85,
                      100,
                      115,
                      130,
                      30,
                      43,
                      73,
                      25,
                      50,
                      55,
                      80,
                      60,
                      125,
                      40,
                      50,
                      35,
                      35,
                      60,
                      60,
                      85,
                      30,
                      45,
                      35,
                      100,
                      40,
                      70,
                      95,
                      35,
                      65,
                      70,
                      100,
                      100,
                      55,
                      115,
                      95,
                      100,
                      55,
                      40,
                      15,
                      60,
                      85,
                      48,
                      45,
                      110,
                      110,
                      95,
                      85,
                      90,
                      115,
                      55,
                      65,
                      60,
                      65,
                      95,
                      125,
                      125,
                      50,
                      70,
                      100,
                      154,
                      100,
                      49,
                      63,
                      83,
                      60,
                      80,
                      109,
                      44,
                      59,
                      79,
                      35,
                      45,
                      36,
                      76,
                      40,
                      55,
                      40,
                      60,
                      70,
                      56,
                      76,
                      35,
                      45,
                      40,
                      40,
                      80,
                      70,
                      95,
                      65,
                      80,
                      115,
                      90,
                      20,
                      50,
                      30,
                      90,
                      35,
                      45,
                      55,
                      40,
                      30,
                      105,
                      75,
                      25,
                      65,
                      130,
                      60,
                      85,
                      100,
                      85,
                      72,
                      33,
                      90,
                      35,
                      60,
                      65,
                      35,
                      55,
                      40,
                      60,
                      55,
                      55,
                      10,
                      40,
                      35,
                      50,
                      75,
                      70,
                      80,
                      30,
                      60,
                      65,
                      65,
                      105,
                      65,
                      80,
                      40,
                      80,
                      110,
                      95,
                      40,
                      60,
                      105,
                      85,
                      20,
                      35,
                      35,
                      85,
                      65,
                      70,
                      40,
                      75,
                      115,
                      90,
                      90,
                      45,
                      65,
                      95,
                      90,
                      110,
                      100,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      255,
                      65,
                      85,
                      105,
                      70,
                      85,
                      110,
                      50,
                      60,
                      85,
                      30,
                      60,
                      30,
                      50,
                      20,
                      25,
                      100,
                      25,
                      50,
                      40,
                      60,
                      90,
                      30,
                      60,
                      90,
                      30,
                      50,
                      30,
                      30,
                      50,
                      40,
                      60,
                      60,
                      55,
                      85,
                      50,
                      80,
                      70,
                      90,
                      35,
                      55,
                      60,
                      40,
                      70,
                      45,
                      85,
                      65,
                      46,
                      76,
                      40,
                      50,
                      90,
                      10,
                      100,
                      65,
                      95,
                      45,
                      50,
                      80,
                      20,
                      40,
                      65,
                      105,
                      65,
                      105,
                      55,
                      75,
                      95,
                      85,
                      115,
                      50,
                      80,
                      95,
                      55,
                      20,
                      70,
                      90,
                      85,
                      75,
                      55,
                      40,
                      60,
                      40,
                      70,
                      23,
                      30,
                      60,
                      100,
                      35,
                      55,
                      95,
                      43,
                      73,
                      72,
                      51,
                      71,
                      91,
                      74,
                      94,
                      114,
                      75,
                      63,
                      83,
                      100,
                      60,
                      45,
                      40,
                      50,
                      60,
                      70,
                      47,
                      73,
                      61,
                      81,
                      40,
                      70,
                      45,
                      65,
                      125,
                      40,
                      60,
                      110,
                      35,
                      55,
                      95,
                      50,
                      100,
                      75,
                      150,
                      100,
                      150,
                      110,
                      130,
                      100,
                      150,
                      95
                      ]
base_specialdefense = [255,
                       65,
                       80,
                       100,
                       50,
                       65,
                       85,
                       64,
                       80,
                       105,
                       20,
                       25,
                       80,
                       20,
                       25,
                       80,
                       35,
                       50,
                       70,
                       35,
                       70,
                       31,
                       61,
                       54,
                       79,
                       40,
                       80,
                       30,
                       55,
                       40,
                       55,
                       85,
                       40,
                       55,
                       75,
                       65,
                       90,
                       65,
                       100,
                       25,
                       50,
                       40,
                       75,
                       65,
                       75,
                       90,
                       55,
                       80,
                       55,
                       75,
                       45,
                       70,
                       40,
                       65,
                       50,
                       80,
                       45,
                       70,
                       50,
                       80,
                       40,
                       50,
                       90,
                       55,
                       70,
                       85,
                       35,
                       60,
                       85,
                       30,
                       45,
                       60,
                       100,
                       120,
                       30,
                       45,
                       65,
                       65,
                       80,
                       40,
                       80,
                       55,
                       70,
                       62,
                       35,
                       60,
                       70,
                       95,
                       50,
                       100,
                       25,
                       45,
                       35,
                       55,
                       75,
                       45,
                       90,
                       115,
                       25,
                       50,
                       55,
                       80,
                       45,
                       65,
                       50,
                       80,
                       110,
                       110,
                       75,
                       45,
                       70,
                       30,
                       45,
                       105,
                       40,
                       80,
                       25,
                       45,
                       50,
                       80,
                       55,
                       85,
                       120,
                       80,
                       95,
                       85,
                       85,
                       70,
                       70,
                       20,
                       100,
                       95,
                       48,
                       65,
                       95,
                       95,
                       110,
                       75,
                       55,
                       70,
                       45,
                       70,
                       75,
                       110,
                       125,
                       90,
                       85,
                       50,
                       70,
                       100,
                       90,
                       100,
                       65,
                       80,
                       100,
                       50,
                       65,
                       85,
                       48,
                       63,
                       83,
                       45,
                       55,
                       56,
                       96,
                       80,
                       110,
                       40,
                       60,
                       80,
                       56,
                       76,
                       35,
                       55,
                       20,
                       65,
                       105,
                       45,
                       70,
                       45,
                       60,
                       90,
                       100,
                       50,
                       80,
                       65,
                       100,
                       55,
                       65,
                       85,
                       55,
                       30,
                       85,
                       45,
                       25,
                       65,
                       95,
                       130,
                       42,
                       110,
                       85,
                       48,
                       58,
                       65,
                       35,
                       60,
                       65,
                       65,
                       65,
                       40,
                       60,
                       55,
                       80,
                       230,
                       95,
                       75,
                       50,
                       75,
                       40,
                       80,
                       30,
                       60,
                       85,
                       35,
                       75,
                       45,
                       140,
                       70,
                       50,
                       80,
                       95,
                       40,
                       60,
                       95,
                       65,
                       45,
                       35,
                       110,
                       65,
                       55,
                       55,
                       70,
                       135,
                       100,
                       75,
                       115,
                       50,
                       70,
                       100,
                       154,
                       154,
                       100,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       255,
                       55,
                       65,
                       85,
                       50,
                       60,
                       70,
                       50,
                       70,
                       90,
                       30,
                       60,
                       41,
                       61,
                       30,
                       25,
                       50,
                       25,
                       90,
                       50,
                       70,
                       100,
                       30,
                       40,
                       60,
                       30,
                       50,
                       30,
                       30,
                       50,
                       60,
                       60,
                       60,
                       30,
                       70,
                       52,
                       82,
                       35,
                       45,
                       35,
                       55,
                       120,
                       70,
                       120,
                       90,
                       70,
                       65,
                       41,
                       71,
                       65,
                       35,
                       55,
                       55,
                       125,
                       20,
                       40,
                       45,
                       50,
                       80,
                       30,
                       60,
                       40,
                       60,
                       45,
                       75,
                       50,
                       70,
                       90,
                       40,
                       60,
                       50,
                       80,
                       85,
                       65,
                       40,
                       80,
                       110,
                       75,
                       85,
                       55,
                       55,
                       75,
                       75,
                       105,
                       48,
                       90,
                       130,
                       80,
                       35,
                       55,
                       65,
                       53,
                       83,
                       87,
                       23,
                       43,
                       73,
                       55,
                       75,
                       75,
                       60,
                       33,
                       63,
                       60,
                       60,
                       65,
                       40,
                       50,
                       60,
                       70,
                       75,
                       75,
                       87,
                       107,
                       50,
                       80,
                       35,
                       55,
                       115,
                       30,
                       50,
                       80,
                       60,
                       80,
                       90,
                       100,
                       200,
                       150,
                       140,
                       90,
                       90,
                       130,
                       110,
                       100,
                       50,
                       80
                       ]
base_special = [255,
                65,
                80,
                100,
                50,
                65,
                85,
                50,
                65,
                85,
                20,
                25,
                80,
                20,
                25,
                45,
                35,
                50,
                70,
                25,
                50,
                31,
                61,
                40,
                65,
                50,
                90,
                30,
                55,
                40,
                55,
                75,
                40,
                55,
                75,
                60,
                85,
                65,
                100,
                25,
                50,
                40,
                75,
                75,
                85,
                100,
                55,
                80,
                40,
                90,
                45,
                70,
                40,
                65,
                50,
                80,
                35,
                60,
                50,
                80,
                40,
                50,
                70,
                105,
                120,
                135,
                35,
                50,
                65,
                70,
                85,
                100,
                100,
                120,
                30,
                45,
                55,
                65,
                80,
                40,
                80,
                95,
                120,
                58,
                35,
                60,
                70,
                95,
                40,
                65,
                45,
                85,
                100,
                115,
                130,
                30,
                90,
                115,
                25,
                50,
                55,
                80,
                60,
                125,
                40,
                50,
                35,
                35,
                60,
                60,
                85,
                30,
                45,
                105,
                100,
                40,
                70,
                95,
                50,
                80,
                70,
                100,
                100,
                55,
                95,
                85,
                85,
                55,
                70,
                20,
                100,
                95,
                48,
                65,
                110,
                110,
                110,
                75,
                90,
                115,
                45,
                70,
                60,
                65,
                125,
                125,
                125,
                50,
                70,
                100,
                154,
                100,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255,
                255]

move_pp = [0,
           35,
           25,
           10,
           15,
           20,
           20,
           15,
           15,
           15,
           35,
           30,
           5,
           10,
           30,
           30,
           35,
           35,
           20,
           15,
           20,
           20,
           10,
           20,
           30,
           5,
           25,
           15,
           15,
           15,
           25,
           20,
           5,
           35,
           15,
           20,
           20,
           20,
           15,
           30,
           35,
           20,
           20,
           30,
           25,
           40,
           20,
           15,
           20,
           20,
           20,
           30,
           25,
           15,
           30,
           25,
           5,
           15,
           10,
           5,
           20,
           20,
           20,
           5,
           35,
           20,
           25,
           20,
           20,
           20,
           15,
           20,
           10,
           10,
           40,
           25,
           10,
           35,
           30,
           15,
           20,
           40,
           10,
           15,
           30,
           15,
           20,
           10,
           15,
           10,
           5,
           10,
           10,
           25,
           10,
           20,
           40,
           30,
           30,
           20,
           20,
           15,
           10,
           40,
           15,
           20,
           30,
           20,
           20,
           10,
           40,
           40,
           30,
           30,
           30,
           20,
           30,
           10,
           10,
           20,
           5,
           10,
           30,
           20,
           20,
           20,
           5,
           15,
           10,
           20,
           15,
           15,
           35,
           20,
           15,
           10,
           20,
           30,
           15,
           40,
           20,
           15,
           10,
           5,
           10,
           30,
           10,
           15,
           20,
           15,
           40,
           40,
           10,
           5,
           15,
           10,
           10,
           10,
           15,
           30,
           30,
           10,
           10,
           20,
           10,
           1,
           1,
           10,
           10,
           10,
           5,
           15,
           25,
           15,
           10,
           15,
           30,
           5,
           40,
           15,
           10,
           25,
           10,
           30,
           10,
           20,
           10,
           10,
           10,
           10,
           10,
           20,
           5,
           40,
           5,
           5,
           15,
           5,
           10,
           5,
           15,
           10,
           5,
           10,
           20,
           20,
           40,
           15,
           10,
           20,
           20,
           25,
           5,
           15,
           10,
           5,
           20,
           15,
           20,
           25,
           20,
           5,
           30,
           5,
           10,
           20,
           40,
           5,
           20,
           40,
           20,
           15,
           35,
           10,
           5,
           5,
           5,
           15,
           5,
           20,
           5,
           5,
           15,
           20,
           10,
           5,
           5,
           15,
           15,
           15,
           15,
           10,
           10,
           10,
           10,
           10,
           10,
           10,
           10,
           15,
           15,
           15,
           10,
           20,
           20,
           10,
           20,
           20,
           20,
           20,
           20,
           10,
           10,
           10,
           20,
           20,
           5,
           15,
           10,
           10,
           15,
           10,
           20,
           5,
           5,
           10,
           10,
           20,
           5,
           10,
           20,
           10,
           20,
           20,
           20,
           5,
           5,
           15,
           20,
           10,
           15,
           20,
           15,
           10,
           10,
           15,
           10,
           5,
           5,
           10,
           15,
           10,
           5,
           20,
           25,
           5,
           40,
           10,
           5,
           40,
           15,
           20,
           20,
           5,
           15,
           20,
           30,
           15,
           15,
           5,
           10,
           30,
           20,
           30,
           15,
           5,
           40,
           15,
           5,
           20,
           5,
           15,
           25,
           40,
           15,
           20,
           15,
           20,
           15,
           20,
           10,
           20,
           20,
           5,
           5]
hidden_power_ivs = [[12,
                     12,
                     15,
                     15],
                    [12,
                     13,
                     15,
                     15],
                    [12,
                     14,
                     15,
                     15],
                    [12,
                     15,
                     15,
                     15],
                    [13,
                     12,
                     15,
                     15],
                    [13,
                     13,
                     15,
                     15],
                    [13,
                     14,
                     15,
                     15],
                    [13,
                     15,
                     15,
                     15],
                    [14,
                     12,
                     15,
                     15],
                    [14,
                     13,
                     15,
                     15],
                    [14,
                     14,
                     15,
                     15],
                    [14,
                     15,
                     15,
                     15],
                    [15,
                     12,
                     15,
                     15],
                    [15,
                     13,
                     15,
                     15],
                    [15,
                     14,
                     15,
                     15],
                    [15,
                     15,
                     15,
                     15]]
hidden_power_ivs_rs = [
    # Hp, Atk, Def, SpA, SpD, Spe
    [31, 31, 30, 30, 30, 30],
    [30, 30, 30, 30, 30, 31],
    [31, 31, 30, 30, 30, 31],
    [31, 31, 31, 30, 30, 31],
    [31, 31, 30, 31, 30, 30],
    [31, 30, 30, 31, 30, 31],
    [31, 31, 30, 31, 30, 31],
    [31, 31, 31, 31, 30, 31],
    [31, 30, 31, 30, 31, 30],
    [31, 30, 30, 30, 31, 31],
    [31, 30, 31, 30, 31, 31],
    [31, 31, 31, 30, 31, 31],
    [31, 30, 31, 31, 31, 30],
    [31, 30, 30, 31, 31, 31],
    [31, 30, 31, 31, 31, 31],
    [31, 31, 31, 31, 31, 31]
]
rb2dex = [201,
          112,
          115,
          32,
          35,
          21,
          100,
          34,
          80,
          2,
          103,
          108,
          102,
          88,
          94,
          29,
          31,
          104,
          111,
          131,
          59,
          151,
          130,
          90,
          72,
          92,
          123,
          120,
          9,
          127,
          114,
          0,
          0,
          58,
          95,
          22,
          16,
          79,
          64,
          75,
          113,
          67,
          122,
          106,
          107,
          24,
          47,
          54,
          96,
          76,
          0,
          126,
          0,
          125,
          82,
          109,
          0,
          56,
          86,
          50,
          128,
          0,
          0,
          0,
          83,
          48,
          149,
          0,
          0,
          0,
          84,
          60,
          124,
          146,
          144,
          145,
          132,
          52,
          98,
          0,
          0,
          0,
          37,
          38,
          25,
          26,
          0,
          0,
          147,
          148,
          140,
          141,
          116,
          117,
          0,
          0,
          27,
          28,
          138,
          139,
          39,
          40,
          133,
          136,
          135,
          134,
          66,
          41,
          23,
          46,
          61,
          62,
          13,
          14,
          15,
          0,
          85,
          57,
          51,
          49,
          87,
          0,
          0,
          10,
          11,
          12,
          68,
          0,
          55,
          97,
          42,
          150,
          143,
          129,
          0,
          0,
          89,
          0,
          99,
          91,
          0,
          101,
          36,
          110,
          53,
          105,
          0,
          93,
          63,
          65,
          17,
          18,
          121,
          1,
          3,
          73,
          0,
          118,
          119,
          0,
          0,
          0,
          0,
          77,
          78,
          19,
          20,
          33,
          30,
          74,
          137,
          142,
          0,
          81,
          0,
          0,
          4,
          7,
          5,
          8,
          6,
          0,
          0,
          0,
          0,
          43,
          44,
          45,
          69,
          70,
          71,
          250,
          61,
          205,
          234,
          94,
          205,
          250,
          62,
          205,
          234,
          95,
          205,
          17,
          200,
          80,
          24,
          15,
          250,
          62,
          205,
          234,
          94,
          205,
          250,
          61,
          205,
          234,
          95,
          205,
          17,
          217,
          80,
          250,
          90,
          211,
          245,
          240,
          175,
          245,
          240,
          174,
          245,
          175,
          234,
          90,
          211,
          224,
          175,
          224,
          174,
          213,
          209,
          26,
          254,
          255,
          40,
          18,
          19,
          213,
          33,
          239,
          80,
          135,
          79,
          6]

pokemon_types_rb = {
    1: (22, 3),
    2: (22, 3),
    3: (22, 3),
    4: (20, 20),
    5: (20, 20),
    6: (20, 2),
    7: (21, 21),
    8: (21, 21),
    9: (21, 21),
    10: (7, 7),
    11: (7, 7),
    12: (7, 2),
    13: (7, 3),
    14: (7, 3),
    15: (7, 3),
    16: (0, 2),
    17: (0, 2),
    18: (0, 2),
    19: (0, 0),
    20: (0, 0),
    21: (0, 2),
    22: (0, 2),
    23: (3, 3),
    24: (3, 3),
    25: (23, 23),
    26: (23, 23),
    27: (4, 4),
    28: (4, 4),
    29: (3, 3),
    30: (3, 3),
    31: (3, 4),
    32: (3, 3),
    33: (3, 3),
    34: (3, 4),
    35: (0, 0),
    36: (0, 0),
    37: (20, 20),
    38: (20, 20),
    39: (0, 0),
    40: (0, 0),
    41: (3, 2),
    42: (3, 2),
    43: (22, 3),
    44: (22, 3),
    45: (22, 3),
    46: (7, 22),
    47: (7, 22),
    48: (7, 3),
    49: (7, 3),
    50: (4, 4),
    51: (4, 4),
    52: (0, 0),
    53: (0, 0),
    54: (21, 21),
    55: (21, 21),
    56: (1, 1),
    57: (1, 1),
    58: (20, 20),
    59: (20, 20),
    60: (21, 21),
    61: (21, 21),
    62: (21, 1),
    63: (24, 24),
    64: (24, 24),
    65: (24, 24),
    66: (1, 1),
    67: (1, 1),
    68: (1, 1,),
    69: (22, 3),
    70: (22, 3),
    71: (22, 3),
    72: (21, 3),
    73: (21, 3),
    74: (5, 4),
    75: (5, 4),
    76: (5, 4),
    77: (20, 20),
    78: (20, 20),
    79: (21, 24),
    80: (21, 24),
    81: (23, 23),
    82: (23, 23),
    83: (0, 2),
    84: (0, 2),
    85: (0, 2),
    86: (20, 20),
    87: (20, 25),
    88: (3, 3),
    89: (3, 3),
    90: (21, 21),
    91: (21, 24),
    92: (8, 3),
    93: (8, 3),
    94: (8, 3),
    95: (5, 4),
    96: (24, 24),
    97: (24, 24),
    98: (21, 21),
    99: (21, 21),
    100: (23, 23),
    101: (23, 23),
    102: (22, 24),
    103: (22, 24),
    104: (4, 4),
    105: (4, 4),
    106: (1, 1),
    107: (1, 1),
    108: (0, 0),
    109: (3, 3),
    110: (3, 3),
    111: (4, 5),
    112: (4, 5),
    113: (0, 0),
    114: (22, 22),
    115: (0, 0),
    116: (21, 21),
    117: (21, 21),
    118: (21, 21),
    119: (21, 21),
    120: (21, 21),
    121: (21, 24),
    122: (24, 24),
    123: (7, 2),
    124: (25, 24),
    125: (23, 23),
    126: (20, 20),
    127: (7, 7),
    128: (0, 0),
    129: (21, 21),
    130: (21, 2),
    131: (21, 25),
    132: (0, 0),
    133: (0, 0),
    134: (21, 21),
    135: (23, 23),
    136: (20, 20),
    137: (0, 0),
    138: (5, 21),
    139: (5, 21),
    140: (5, 21),
    141: (5, 21),
    142: (5, 2),
    143: (0, 0),
    144: (25, 2),
    145: (23, 2),
    146: (20, 2),
    147: (26, 26),
    148: (26, 26),
    149: (26, 2),
    150: (24, 24),
    151: (24, 24)
}

new2oldMoveNames_rb = {
    'Bubble Beam': 61,
    'Double-Edge': 38,
    'Double Slap': 3,
    'High Jump Kick': 136,
    'Poison Powder': 77,
    'Sand Attack': 28,
    'Self-Destruct': 120,
    'Smokescreen': 108,
    'Soft-Boiled': 135,
    'Solar Beam': 76,
    'Sonic Boom': 49,
    'Thunder Punch': 9,
    'Thunder Shock': 84,
    'Vice Grip': 11
}

new2oldMoveNames_gs = {
    'Ancient Power': 246,
    'Bubble Beam': 61,
    'Conversion 2': 176,
    'Double-Edge': 38,
    'Double Slap': 3,
    'Dragon Breath': 225,
    'Dynamic Punch': 223,
    'Extreme Speed': 245,
    'Feint Attack': 185,
    'High Jump Kick': 136,
    'Lock-On': 199,
    'Mud-Slap': 189,
    'Poison Powder': 77,
    'Sand Attack': 28,
    'Self-Destruct': 120,
    'Smokescreen': 108,
    'Soft-Boiled': 135,
    'Solar Beam': 76,
    'Sonic Boom': 49,
    'Thunder Punch': 9,
    'Thunder Shock': 84,
    'Vice Grip': 11
}

new2oldMoveNames_rs = {
    'Ancient Power': 246,
    'Bubble Beam': 61,
    'Conversion 2': 176,
    'Double-Edge': 38,
    'Double Slap': 3,
    'Dragon Breath': 225,
    'Dynamic Punch': 223,
    'Extreme Speed': 245,
    'Feint Attack': 185,
    'Feather Dance': 297,
    'Grass Whistle': 320,
    'High Jump Kick': 136,
    'Lock-On': 199,
    'Mud-Slap': 189,
    'Poison Powder': 77,
    'Sand Attack': 28,
    'Self-Destruct': 120,
    'Smelling Salts': 265,
    'Smokescreen': 108,
    'Soft-Boiled': 135,
    'Solar Beam': 76,
    'Sonic Boom': 49,
    'Thunder Punch': 9,
    'Thunder Shock': 84,
    'Vice Grip': 11
}

natures = [
    'Hardy (Neutral)',
    'Lonely (+Atk, -Def)',
    'Brave (+Atk, -Spe)',
    'Adamant (+Atk, -SpA)',
    'Naughty (+Atk, -SpD)',
    'Bold (+Def, -Atk)',
    'Docile (Neutral)',
    'Relaxed (+Def, -Spe)',
    'Impish (+Def, -SpA)',
    'Lax (+Def, -SpD)',
    'Timid (+Spe, -Atk)',
    'Hasty (+Spe, -Def)',
    'Serious (Neutral)',
    'Jolly (+Spe, -SpA)',
    'Naive (+Spe, -SpD)',
    'Modest (+SpA, -Atk) ',
    'Mild (+SpA, -Def)',
    'Quiet (+SpA, -Spe)',
    'Bashful (Neutral)',
    'Rash (+SpA, -Spd)',
    'Calm (+SpD, -Atk)',
    'Gentle (+SpD, -Def)',
    'Sassy (+SpD, -Spe)',
    'Careful (+SpD, Spe)',
    'Quirky (SpD, SpA)'
]

natures_atk = [
    1,
    1.1,
    1.1,
    1.1,
    1.1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1
]

natures_def = [
    1,
    0.9,
    1,
    1,
    1,
    1.1,
    1,
    1.1,
    1.1,
    1.1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1
]

natures_spatk = [
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1.1,
    1.1,
    1.1,
    1,
    1.1,
    1,
    1,
    1,
    0.9,
    1
]

natures_spdef = [
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1.1,
    1.1,
    1.1,
    1.1,
    1
]

natures_spe = [
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1,
    1.1,
    1.1,
    1,
    1.1,
    1.1,
    1,
    1,
    0.9,
    1,
    1,
    1,
    1,
    0.9,
    1,
    1
]

gender_rate = {
    32: 0,
    33: 0,
    34: 0,
    10
    : 0,
    107: 0,
    128: 0,
    236: 0,
    237: 0,
    386: 0,
    408: 0,
    1: 31,
    2: 31,
    3: 31,
    4: 31,
    5: 31,
    6: 31,
    7: 31,
    8: 31,
    9: 31,
    133: 31,
    134: 31,
    135: 31,
    136: 31,
    138: 31,
    139: 31,
    140: 31,
    141: 31,
    142: 31,
    143: 31,
    152: 31,
    153: 31,
    154: 31,
    155: 31,
    156: 31,
    157: 31,
    158: 31,
    159: 31,
    160: 31,
    175: 31,
    176: 31,
    196: 31,
    197: 31,
    277: 31,
    278: 31,
    279: 31,
    280: 31,
    281: 31,
    282: 31,
    283: 31,
    284: 31,
    285: 31,
    381: 31,
    388: 31,
    389: 31,
    390: 31,
    391: 31,
    58: 63,
    59: 63,
    63: 63,
    64: 63,
    65: 63,
    66: 63,
    67: 63,
    68: 63,
    125: 63,
    126: 63,
    239: 63,
    240: 63,
    335: 63,
    336: 63,
    35: 191,
    36: 191,
    37: 191,
    38: 191,
    39: 191,
    40: 191,
    173: 191,
    174: 191,
    209: 191,
    210: 191,
    222: 191,
    315: 191,
    316: 191,
    325: 191,
    350: 191,
    29: 254,
    30: 254,
    31: 254,
    113: 254,
    115: 254,
    124: 254,
    238: 254,
    241: 254,
    242: 254,
    387: 254,
    407: 254,
    81: 255,
    82: 255,
    100: 255,
    101: 255,
    120: 255,
    121: 255,
    132: 255,
    137: 255,
    144: 255,
    145: 255,
    146: 255,
    150: 255,
    151: 255,
    201: 255,
    233: 255,
    243: 255,
    244: 255,
    245: 255,
    249: 255,
    250: 255,
    251: 255,
    303: 255,
    348: 255,
    349: 255,
    318: 255,
    319: 255,
    398: 255,
    399: 255,
    400: 255,
    401: 255,
    402: 255,
    403: 255,
    404: 255,
    405: 255,
    406: 255,
    409: 255,
    410: 255
}

pokemon_abilities = {
    1: ('Overgrow'),
    2: ('Overgrow'),
    3: ('Overgrow'),
    4: ('Blaze'),
    5: ('Blaze'),
    6: ('Blaze'),
    7: ('Torrent'),
    8: ('Torrent'),
    9: ('Torrent'),
    10: ('Shield Dust'),
    11: ('Shed Skin'),
    12: ('Compoundeyes'),
    13: ('Shield Dust'),
    14: ('Shed Skin'),
    15: ('Swarm'),
    16: ('Keen Eye'),
    17: ('Keen Eye'),
    18: ('Keen Eye'),
    19: ('Run Away', 'Guts'),
    20: ('Run Away', 'Guts'),
    21: ('Keen Eye'),
    22: ('Keen Eye'),
    23: ('Intimidate', 'Shed Skin'),
    24: ('Intimidate', 'Shed Skin'),
    25: ('Static'),
    26: ('Static'),
    27: ('Sand Veil'),
    28: ('Sand Veil'),
    29: ('Poison Point'),
    30: ('Poison Point'),
    31: ('Poison Point'),
    32: ('Poison Point'),
    33: ('Poison Point'),
    34: ('Poison Point'),
    35: ('Cute Charm'),
    36: ('Cute Charm'),
    37: ('Flash Fire'),
    38: ('Flash Fire'),
    39: ('Cute Charm'),
    40: ('Cute Charm'),
    41: ('Inner Focus'),
    42: ('Inner Focus'),
    43: ('Chlorophyll'),
    44: ('Chlorophyll'),
    45: ('Chlorophyll'),
    46: ('Effect Spore'),
    47: ('Effect Spore'),
    48: ('Compoundeyes'),
    49: ('Shield Dust'),
    50: ('Sand Veil', 'Arena Trap'),
    51: ('Sand Veil', 'Arena Trap'),
    52: ('Pickup'),
    53: ('Limber'),
    54: ('Damp', 'Cloud Nine'),
    55: ('Damp', 'Cloud Nine'),
    56: ('Vital Spirit'),
    57: ('Vital Spirit'),
    58: ('Intimidate', 'Flash Fire'),
    59: ('Intimidate', 'Flash Fire'),
    60: ('Water Absorb', 'Damp'),
    61: ('Water Absorb', 'Damp'),
    62: ('Water Absorb', 'Damp'),
    63: ('Synchronize', 'Inner Focus'),
    64: ('Synchronize', 'Inner Focus'),
    65: ('Synchronize', 'Inner Focus'),
    66: ('Guts'),
    67: ('Guts'),
    68: ('Guts'),
    69: ('Chlorophyll'),
    70: ('Chlorophyll'),
    71: ('Chlorophyll'),
    72: ('Clear Body', 'Liquid Ooze'),
    73: ('Clear Body', 'Liquid Ooze'),
    74: ('Rock Head', 'Sturdy'),
    75: ('Rock Head', 'Sturdy'),
    76: ('Rock Head', 'Sturdy'),
    77: ('Run Away', 'Flash Fire'),
    78: ('Run Away', 'Flash Fire'),
    79: ('Oblivious', 'Own Tempo'),
    80: ('Oblivious', 'Own Tempo'),
    81: ('Magnet Pull', 'Sturdy'),
    82: ('Magnet Pull', 'Sturdy'),
    83: ('Keen Eye', 'Inner Focus'),
    84: ('Run Away', 'Early Bird'),
    85: ('Run Away', 'Early Bird'),
    86: ('Thick Fat'),
    87: ('Thick Fat'),
    88: ('Stench', 'Sticky Hold'),
    89: ('Stench', 'Sticky Hold'),
    90: ('Shell Armor'),
    91: ('Shell Armor'),
    92: ('Levitate'),
    93: ('Levitate'),
    94: ('Levitate'),
    95: ('Rock Head', 'Sturdy'),
    96: ('Insomnia'),
    97: ('Insomnia'),
    98: ('Hyper Cutter', 'Shell Armor'),
    99: ('Hyper Cutter', 'Shell Armor'),
    100: ('Soundproof', 'Static'),
    101: ('Soundproof', 'Static'),
    102: ('Chlorophyll'),
    103: ('Chlorophyll'),
    104: ('Rock Head', 'Lightingrod'),
    105: ('Rock Head', 'Lightingrod'),
    106: ('Limber'),
    107: ('Keen Eye'),
    108: ('Own Tempo', 'Oblivious'),
    109: ('Levitate'),
    110: ('Levitate'),
    111: ('Lightingrod', 'Rock Head'),
    112: ('Lightingrod', 'Rock Head'),
    113: ('Natural Cure', 'Serene Grace'),
    114: ('Chlorophyll'),
    115: ('Early Bird'),
    116: ('Swift Swim'),
    117: ('Poison Point'),
    118: ('Swift Swim', 'Water Veil'),
    119: ('Swift Swim', 'Water Veil'),
    120: ('Illuminate', 'Natural Cure'),
    121: ('Illuminate', 'Natural Cure'),
    122: ('Soundproof'),
    123: ('Swarm'),
    124: ('Oblivious'),
    125: ('Static'),
    126: ('Flame Body'),
    127: ('Hyper Cutter'),
    128: ('Intimidate'),
    129: ('Swift Swim'),
    130: ('Intimidate'),
    131: ('Water Absorb', 'Shell Armor'),
    132: ('Limber'),
    133: ('Run Away'),
    134: ('Water Absorb'),
    135: ('Volt Absorb'),
    136: ('Flash Fire'),
    137: ('Trace'),
    138: ('Swift Swim', 'Shell Armor'),
    139: ('Swift Swim', 'Shell Armor'),
    140: ('Swift Swim', 'Shell Armor'),
    141: ('Swift Swim', 'Shell Armor'),
    142: ('Rock Head', 'Pressure'),
    143: ('Immunity', 'Thick Fat'),
    144: ('Pressure'),
    145: ('Pressure'),
    146: ('Pressure'),
    147: ('Shed Skin'),
    148: ('Shed Skin'),
    149: ('Inner Focus'),
    150: ('Pressure'),
    151: ('Synchronize'),
    152: ('Overgrow'),
    153: ('Overgrow'),
    154: ('Overgrow'),
    155: ('Blaze'),
    156: ('Blaze'),
    157: ('Blaze'),
    158: ('Torrent'),
    159: ('Torrent'),
    160: ('Torrent'),
    161: ('Run Away', 'Keen Eye'),
    162: ('Run Away', 'Keen Eye'),
    163: ('Insomnia', 'Keen Eye'),
    164: ('Insomnia', 'Keen Eye'),
    165: ('Swarm', 'Early Bird'),
    166: ('Swarm', 'Early Bird'),
    167: ('Swarm', 'Insomnia'),
    168: ('Swarm', 'Insomnia'),
    169: ('Inner Focus'),
    170: ('Volt Absorb', 'Illuminate'),
    171: ('Volt Absorb', 'Illuminate'),
    172: ('Static'),
    173: ('Cute Charm'),
    174: ('Cute Charm'),
    175: ('Hustle', 'Serene Grace'),
    176: ('Hustle', 'Serene Grace'),
    177: ('Synchronize', 'Early Bird'),
    178: ('Synchronize', 'Early Bird'),
    179: ('Static'),
    180: ('Static'),
    181: ('Static'),
    182: ('Chlorophyll'),
    183: ('Thick Fat', 'Huge Power'),
    184: ('Thick Fat', 'Huge Power'),
    185: ('Sturdy', 'Rock Head'),
    186: ('Water Absorb', 'Damp'),
    187: ('Chlorophyll'),
    188: ('Chlorophyll'),
    189: ('Chlorophyll'),
    190: ('Run Away', 'Pickup'),
    191: ('Chlorophyll'),
    192: ('Chlorophyll'),
    193: ('Speed Boost', 'Compoundeyes'),
    194: ('Damp', 'Water Absorb'),
    195: ('Damp', 'Water Absorb'),
    196: ('Synchronize'),
    197: ('Synchronize'),
    198: ('Insomnia'),
    199: ('Oblivious', 'Own Tempo'),
    200: ('Levitate'),
    201: ('Levitate'),
    202: ('Shadow Tag'),
    203: ('Inner Focus', 'Early Bird'),
    204: ('Sturdy'),
    205: ('Sturdy'),
    206: ('Serene Grace', 'Run Away'),
    207: ('Hyper Cutter', 'Sand Veil'),
    208: ('Rock Head', 'Sturdy'),
    209: ('Intimidate', 'Run Away'),
    210: ('Intimidate'),
    211: ('Poison Point', 'Swift Swim'),
    212: ('Swarm'),
    213: ('Sturdy'),
    214: ('Swarm', 'Guts'),
    215: ('Inner Focus', 'Keen Eye'),
    216: ('Pickup'),
    217: ('Guts'),
    218: ('Magma Armor', 'Flame Body'),
    219: ('Magma Armor', 'Flame Body'),
    220: ('Oblivious'),
    221: ('Oblivious'),
    222: ('Hustle', 'Natural Cure'),
    223: ('Hustle'),
    224: ('Suction Cups'),
    225: ('Vital Spirit', 'Hustle'),
    226: ('Swift Swim', 'Water Absorb'),
    227: ('Keen Eye', 'Sturdy'),
    228: ('Early Bird', 'Flash Fire'),
    229: ('Early Bird', 'Flash Fire'),
    230: ('Swift Swim'),
    231: ('Pickup'),
    232: ('Sturdy'),
    233: ('Trace'),
    234: ('Intimidate'),
    235: ('Own Tempo'),
    236: ('Guts'),
    237: ('Intimidate'),
    238: ('Oblivious'),
    239: ('Static'),
    240: ('Flame Body'),
    241: ('Thick Fat'),
    242: ('Natural Cure', 'Serene Grace'),
    243: ('Pressure'),
    244: ('Pressure'),
    245: ('Pressure'),
    246: ('Guts'),
    247: ('Shed Skin'),
    248: ('Sand Stream'),
    249: ('Pressure'),
    250: ('Pressure'),
    251: ('Natural Cure'),
    252: ('Overgrow'),
    253: ('Overgrow'),
    254: ('Overgrow'),
    255: ('Blaze'),
    256: ('Blaze'),
    257: ('Blaze'),
    258: ('Torrent'),
    259: ('Torrent'),
    260: ('Torrent'),
    261: ('Run Away'),
    262: ('Intimidate'),
    263: ('Pickup'),
    264: ('Pickup'),
    265: ('Shield Dust'),
    266: ('Shed Skin'),
    267: ('Swarm'),
    268: ('Shed Skin'),
    269: ('Shield Dust'),
    270: ('Swift Swim', 'Rain Dish'),
    271: ('Swift Swim', 'Rain Dish'),
    272: ('Swift Swim', 'Rain Dish'),
    273: ('Chlorophyll', 'Early Bird'),
    274: ('Chlorophyll', 'Early Bird'),
    275: ('Chlorophyll', 'Early Bird'),
    276: ('Guts'),
    277: ('Guts'),
    278: ('Keen Eye'),
    279: ('Keen Eye'),
    280: ('Synchronize', 'Trace'),
    281: ('Synchronize', 'Trace'),
    282: ('Synchronize', 'Trace'),
    283: ('Swift Swim'),
    284: ('Intimidate'),
    285: ('Effect Spore'),
    286: ('Effect Spore'),
    287: ('Truant'),
    288: ('Vital Spirit'),
    289: ('Truant'),
    290: ('Compoundeyes'),
    291: ('Speed Boost'),
    292: ('Wonder Guard'),
    293: ('Soundproof'),
    294: ('Soundproof'),
    295: ('Soundproof'),
    296: ('Thick Fat', 'Guts'),
    297: ('Thick Fat', 'Guts'),
    298: ('Thick Fat', 'Huge Power'),
    299: ('Sturdy', 'Magnet Pull'),
    300: ('Cute Charm'),
    301: ('Cute Charm'),
    302: ('Keen Eye'),
    303: ('Hyper Cutter', 'Intimidate'),
    304: ('Sturdy', 'Rock Head'),
    305: ('Sturdy', 'Rock Head'),
    306: ('Sturdy', 'Rock Head'),
    307: ('Pure Power'),
    308: ('Pure Power'),
    309: ('Static', 'Lightningrod'),
    310: ('Static', 'Lightningrod'),
    311: ('Plus'),
    312: ('Minus'),
    313: ('Illuminate', 'Swarm'),
    314: ('Oblivious'),
    315: ('Natural Cure', 'Poison Point'),
    316: ('Liquid Ooze', 'Sticky Hold'),
    317: ('Liquid Ooze', 'Sticky Hold'),
    318: ('Rough Skin'),
    319: ('Rough Skin'),
    320: ('Water Veil', 'Oblivious'),
    321: ('Water Veil', 'Oblivious'),
    322: ('Oblivious'),
    323: ('Magma Armor'),
    324: ('White Smoke'),
    325: ('Thick Fat', 'Own Tempo'),
    326: ('Thick Fat', 'Own Tempo'),
    327: ('Own Tempo'),
    328: ('Hyper Cutter', 'Arena Trap'),
    329: ('Levitate'),
    330: ('Levitate'),
    331: ('Sand Veil'),
    332: ('Sand Veil'),
    333: ('Natural Cure'),
    334: ('Natural Cure'),
    335: ('Immunity'),
    336: ('Shed Skin'),
    337: ('Levitate'),
    338: ('Levitate'),
    339: ('Oblivious'),
    340: ('Oblivious'),
    341: ('Hyper Cutter', 'Shell Armor'),
    342: ('Hyper Cutter', 'Shell Armor'),
    343: ('Levitate'),
    344: ('Levitate'),
    345: ('Suction Cups'),
    346: ('Suction Cups'),
    347: ('Battle Armor'),
    348: ('Battle Armor'),
    349: ('Swift Swim'),
    350: ('Marvel Scale'),
    351: ('Forecast'),
    352: ('Color Change'),
    353: ('Insomnia'),
    354: ('Insomnia'),
    355: ('Levitate'),
    356: ('Pressure'),
    357: ('Chlorophyll'),
    358: ('Levitate'),
    359: ('Pressure'),
    360: ('Shadow Tag'),
    361: ('Inner Focus'),
    362: ('Inner Focus'),
    363: ('Thick Fat'),
    364: ('Thick Fat'),
    365: ('Thick Fat'),
    366: ('Shell Armor'),
    367: ('Swift Swim'),
    368: ('Swift Swim'),
    369: ('Swift Swim', 'Rock Head'),
    370: ('Swift Swim'),
    371: ('Rock Head'),
    372: ('Rock Head'),
    373: ('Intimidate'),
    374: ('Clear Body'),
    375: ('Clear Body'),
    376: ('Clear Body'),
    377: ('Clear Body'),
    378: ('Clear Body'),
    379: ('Clear Body'),
    380: ('Levitate'),
    381: ('Levitate'),
    382: ('Drizzle'),
    383: ('Drought'),
    384: ('Air Lock'),
    385: ('Serene Grace'),
    386: ('Pressure')
}

items = None
pokemon = None
pokemon_lower = None
pokedex = None
moves = None
types = None


class PikaSav():
    def repair_rby(self):
        global items
        global pokemon_lower
        global moves
        global pokemon
        global pokedex
        global types
        file = askopenfilename(filetypes=[('All files', '*.*')])
        if file:
            sav = RBSav(file, True)
            self.gen = 1
            self.bn = 12
            self.root.title(self.title + ' - Red/Blue/Yellow')
            items = items_rb[:]
            pokemon = pokemon_rb[:]
            pokemon_lower = pokemon_lower_rb[:]
            pokedex = pokedex_rb[:]
            moves = moves_rb[:]
            types = types_rb[:]
            self.sav = sav
            self.show_data()
            self.close_frames()

    def repair_gs(self):
        global pokemon_lower
        global items
        global moves
        global pokemon
        global pokedex
        global types
        file = askopenfilename(filetypes=[('All files', '*.*')])
        if file:
            sav = GSSav(file, True)
            items = items_gs[:]
            pokemon = pokemon_gs[:]
            pokemon_lower = pokemon_lower_gs[:]
            pokedex = pokedex_gs[:]
            moves = moves_gs[:]
            types = types_gs[:]
            self.gen = 2
            self.bn = 14
            self.root.title(self.title + ' - Gold/Silver')
            self.sav = sav
            self.show_data()
            self.close_frames()

    def repair_cr(self):
        global pokemon_lower
        global items
        global moves
        global pokemon
        global pokedex
        global types
        file = askopenfilename(filetypes=[('All files', '*.*')])
        if file:
            sav = CRSav(file, True)
            items = items_gs[:]
            pokemon = pokemon_gs[:]
            pokemon_lower = pokemon_lower_gs[:]
            pokedex = pokedex_gs[:]
            moves = moves_gs[:]
            types = types_gs[:]
            self.gen = 2
            self.bn = 14
            self.root.title(self.title + ' - Crystal')
            self.sav = sav
            self.show_data()
            self.close_frames()

    def repair_rs(self):
        global pokemon_lower
        global items
        global moves
        global pokemon
        global pokedex
        global types
        file = askopenfilename(filetypes=[('All files', '*.*')])
        if file:
            sav = RSSav(file, 1)
            items = items_rs[:]
            pokemon = pokemon_rs[:]
            pokemon_lower = pokemon_lower_rs[:]
            pokedex = pokedex_rs[:]
            moves = moves_rs[:]
            types = types_rs[:]
            self.gen = 3
            self.bn = 14
            self.root.title(self.title + ' - Ruby/Sapphire')
            self.sav = sav
            self.show_data()
            self.close_frames()

    def open_sav(self):
        global pokemon_lower
        global items
        global moves
        global pokemon
        global pokedex
        global types
        file = askopenfilename(filetypes=[('All files', '*.*')])
        if file:
            sav = RSSav(file)
            if not sav.ok:
                sav = CRSav(file)
                if not sav.ok:
                    sav = GSSav(file)
                    if not sav.ok:
                        sav = RBSav(file)
                        if not sav.ok:
                            showerror('Something went wrong =(',
                                      "The .sav is corrupted or not supported by this program.\nIn case of corruption, use the 'File -> Force SAV' function.")
                            return False
                        self.gen = 1
                        self.bn = 12
                        self.root.title(self.title + ' - Red/Blue/Yellow')
                        items = items_rb[:]
                        pokemon = pokemon_rb[:]
                        pokemon_lower = pokemon_lower_rb[:]
                        pokedex = pokedex_rb[:]
                        moves = moves_rb[:]
                        types = types_rb[:]
                    else:
                        items = items_gs[:]
                        pokemon = pokemon_gs[:]
                        pokemon_lower = pokemon_lower_gs[:]
                        pokedex = pokedex_gs[:]
                        moves = moves_gs[:]
                        types = types_gs[:]
                        self.gen = 2
                        self.bn = 14
                        self.root.title(self.title + ' - Gold/Silver')
                else:
                    items = items_gs[:]
                    pokemon = pokemon_gs[:]
                    pokemon_lower = pokemon_lower_gs[:]
                    pokedex = pokedex_gs[:]
                    moves = moves_gs[:]
                    types = types_gs[:]
                    self.gen = 2
                    self.bn = 14
                    self.root.title(self.title + ' - Crystal')
            else:
                items = items_rs[:]
                pokemon = pokemon_rs[:]
                pokemon_lower = pokemon_lower_rs[:]
                pokedex = pokedex_rs[:]
                moves = moves_rs[:]
                types = types_rs[:]
                self.gen = 3
                self.bn = 14
                self.root.title(self.title + ' - Ruby/Sapphire')
            self.sav = sav
            self.show_data()
            self.close_frames()

    def save_sav(self):
        if self.sav != None:
            self.store_changes()
            self.sav.save()
        else:
            showerror('Something went wrong =(', 'You need to load a .sav first')

    def saveas_sav(self):
        if self.sav != None:
            self.store_changes()
            file = asksaveasfilename(filetypes=[('RBY/GSC/RS SaveGame', '.sav')])
            if file:
                if file[-4:] != '.sav':
                    file = '%s.sav' % file
                self.sav.saveas(file)
        else:
            showerror('Something went wrong =(', 'You need to load a .sav first')

    def store_changes(self):
        if self.trname.get() != self.sav.name:
            self.sav.set('name', self.trname.get())
        if self.rivalname.get() != self.sav.rivalname:
            self.sav.set('rivalname', self.rivalname.get())
        self.sav.set('money', self.money.get())
        self.sav.set('chips', self.chips.get())
        self.sav.set('hours', self.hours.get())
        self.sav.set('minutes', self.minutes.get())
        self.sav.set('seconds', self.seconds.get())
        self.store_items()
        self.store_pcitems()
        self.store_pokedex1()
        self.store_pokedex2()
        self.store_pokemon()
        self.store_pokeedit()
        self.store_boxedit()
        self.sav.refresh()

    def show_data(self):
        self.bp = 20
        if self.gen == 3:
            self.bp = 30
        self.trname.delete(0, END)
        self.trname.insert(0, self.sav.name)
        self.rivalname.delete(0, END)
        self.rivalname.insert(0, self.sav.rivalname)
        self.money.delete(0, END)
        self.money.insert(0, self.sav.money)
        self.chips.delete(0, END)
        self.chips.insert(0, self.sav.chips)
        self.hours.delete(0, END)
        self.hours.insert(0, self.sav.hours)
        self.minutes.delete(0, END)
        self.minutes.insert(0, self.sav.minutes)
        self.seconds.delete(0, END)
        self.seconds.insert(0, self.sav.seconds)

    def add_menus(self):
        menu = Menu(self.root)
        menu_repair = Menu(menu, tearoff=0)
        menu_repair.add_command(label='Red/Blue/Yellow', command=self.repair_rby)
        menu_repair.add_command(label='Gold/Silver', command=self.repair_gs)
        menu_repair.add_command(label='Crystal', command=self.repair_cr)
        menu_repair.add_command(label='Ruby/Sapphire', command=self.repair_rs)
        menu_file = Menu(menu, tearoff=0)
        menu_file.add_command(label='Open SAV', command=self.open_sav)
        menu_file.add_separator()
        menu_file.add_command(label='Save SAV', command=self.save_sav)
        menu_file.add_command(label='Save SAV As..', command=self.saveas_sav)
        menu_file.add_separator()
        menu_file.add_cascade(label='Force SAV', menu=menu_repair)
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.exit)
        menu.add_cascade(label='File', menu=menu_file)
        menu_help = Menu(menu, tearoff=0)
        menu_help.add_command(label='SAV Info', command=self.show_savinfo)
        menu_help.add_separator()
        menu_help.add_command(label='About', command=self.show_about)
        menu.add_cascade(label='Help', menu=menu_help)
        self.root.configure(menu=menu)

    def add_pokeedit_menus(self):
        menu = Menu(self.pokeedit)
        menu_pkm = Menu(menu, tearoff=0)
        menu_pkm.add_command(label='New from scratch', command=self.scratch_pkm)
        menu_pkm.add_command(label='Open .PKM', command=self.open_pkm)
        menu_pkm.add_separator()
        menu_pkm.add_command(label='Save .PKM', command=self.save_pkm)
        menu_pkm.add_separator()
        menu_pkm.add_command(label='Finished', command=self.wmdel_pokeedit)
        menu.add_cascade(label='Pokemon', menu=menu_pkm)
        menu_edit = Menu(menu, tearoff=0)
        menu_edit.add_command(label='Min everything', command=self.min_everything)
        menu_edit.add_command(label='MAX EVERYTHING', command=self.max_everything)
        menu_edit.add_separator()
        menu_edit.add_command(label='Adjust exp to level', command=self.adjust_exp)
        menu_edit.add_command(label='Adjust stats to level/values', command=self.adjust_stats)
        if self.gen == 1:
            menu_edit.add_command(label='Adjust sprite/type', command=self.adjust_sprite_type)
        if self.gen == 2:
            menu_edit.add_command(label='Adjust sprite', command=self.adjust_sprite_type)
        menu_edit.add_separator()
        menu_edit.add_command(label='Heal Pokemon', command=self.heal_pkm)
        if self.gen == 2:
            menu_edit.add_separator()
            menu_edit.add_command(label='Make Shiny', command=self.make_shiny)
        menu.add_cascade(label='Fast editing', menu=menu_edit)
        menu_hp = Menu(menu, tearoff=0)
        for t in range(len(types_gs_hp)):
            menu_hp.add_command(label='Base 70, %s type' % types_gs_hp[t], command=lambda t=t: self.hidden_power_set(t))
        menu.add_cascade(label='Hidden Power', menu=menu_hp)
        menu_info = Menu(menu, tearoff=0)
        if self.gen <= 2:
            menu_info.add_command(label='Hidden Power? Shiny? HP?', command=self.iv_info)
        else:
            menu_info.add_command(label='Check Hidden Power', command=self.iv_info)
        menu_info.add_separator()
        menu_info.add_command(label='.PKM info', command=self.pkm_info)
        menu.add_cascade(label='About this .PKM', menu=menu_info)
        self.pokeedit.configure(menu=menu)

    def hidden_power_set(self, type):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        if self.gen <= 2:
            iv_set = hidden_power_ivs[type]
            self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', iv_set[0])
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', iv_set[1])
            self.pkm = self.sav.pkm_set(self.pkm, 'speediv', iv_set[2])
            self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', iv_set[3])
        else:
            iv_set = hidden_power_ivs_rs[type]
            self.pkm = self.sav.pkm_set(self.pkm, 'maxhpiv', iv_set[0])
            self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', iv_set[1])
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', iv_set[2])
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattackiv', iv_set[3])
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseiv', iv_set[4])
            self.pkm = self.sav.pkm_set(self.pkm, 'speediv', iv_set[5])
        self.adjust_stats()
        self.reload_pkm()

    def swap_pkm(self, p, box=None):
        if not hasattr(self, 'swap'):
            self.swap = p
        else:
            if box is None:
                pkm = self.sav.pokemon[p]
                self.sav.setpokemon(p, self.sav.pokemon[self.swap])
                self.sav.setpokemon(self.swap, pkm)
                self.wmdel_pokemon()
                self.show_pokemon()
            else:
                pkm = self.sav.pcpokemon[box * self.bp + p]
                self.sav.setpcpokemon(p, self.sav.pcpokemon[box * self.bp + self.swap])
                self.sav.setpcpokemon(box * self.bp + self.swap, pkm)
                del self.swap
                self.wmdel_boxedit()
                self.show_boxedit(box)

    def delete_pkm(self, index, box = None):
        if box is None:
            for i in xrange(index + 1, 6):
                self.sav.setpokemon(i-1, self.sav.pokemon[i])
            if self.gen <= 2:
                self.sav.pokemoncount -= 1
                self.sav.set('pokemoncount', self.sav.pokemoncount)
                self.pokecount.delete(0, END)
                self.pokecount.insert(0, self.sav.pokemoncount)
            self.wmdel_pokemon()
            self.show_pokemon()
        else:
            for i in xrange(index + 1, self.bp):
                self.sav.setpcpokemon(box * self.bp + i - 1, self.sav.pcpokemon[box * self.bp + i])
            if self.gen <= 2:
                self.boxpokecount.delete(0, END)
                self.boxpokecount.insert(0, str(self.sav.boxpokemoncount[box]-1))
            self.wmdel_boxedit()
            self.show_boxedit(box)


    def scratch_pkm(self):
        if askyesno('About to delete this .PKM', 'Do you really want to delete this Pokemon?', parent=self.pokeedit):
            if self.pokeedit != None:
                self.wmdel_pokeedit()
            self.pkm = chr(0) * len(self.pkm)
            self.reload_pkm()

    def pkm_info(self):
        if self.b == None:
            showinfo('.PKM info',
                     'This .PKM is located at Party, Pokemon %d.\nIt is %d bytes long (Gen %d, Party Pokemon)' % (
                         self.p + 1, len(self.pkm), self.gen), parent=self.pokeedit)
        else:
            showinfo('.PKM info',
                     'This .PKM is located at Box %d, Pokemon %d.\nIt is %d bytes long (Gen %d, PC Pokemon)' % (
                         self.b + 1,
                         self.p + 1,
                         len(self.pkm),
                         self.gen), parent=self.pokeedit)

    def make_shiny(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', 15)
        self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', 10)
        self.pkm = self.sav.pkm_set(self.pkm, 'speediv', 10)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', 10)
        self.reload_pkm()

    def iv_info(self):
        self.reload_pkm()
        if self.gen <= 2:
            iv_attack = self.sav.pkm_get(self.pkm, 'attackiv')
            iv_defense = self.sav.pkm_get(self.pkm, 'defenseiv')
            iv_speed = self.sav.pkm_get(self.pkm, 'speediv')
            iv_special = self.sav.pkm_get(self.pkm, 'specialiv')
            iv_hp = iv_attack % 2 * 8 + iv_defense % 2 * 4 + iv_speed % 2 * 2 + iv_special % 2
            is_shiny = 'not shiny'
            if iv_defense == 10 and iv_speed == 10 and iv_special == 10 and iv_attack & 2:
                is_shiny = 'shiny'
            hp_a = (iv_attack & 8) + (iv_defense & 8) / 2 + (iv_speed & 8) / 4 + (iv_special & 8) / 8
            hp_b = iv_special & 3
            hp_power = int((5 * hp_a + hp_b) / 2 + 31)
            hp_type_id = (iv_attack & 3) * 4 + (iv_defense & 3)
            hp_type = types_gs_hp[hp_type_id]
            showinfo('About the IV combination',
                     'Your Pok\xc3\xa9mon is %s and its HP IV is %d.\nIts Hidden Power is %s type and its power is %d.' % (
                         is_shiny,
                         iv_hp,
                         hp_type,
                         hp_power), parent=self.pokeedit)
        else:
            iv_hp = self.sav.pkm_get(self.pkm, 'maxhpiv')
            iv_attack = self.sav.pkm_get(self.pkm, 'attackiv')
            iv_defense = self.sav.pkm_get(self.pkm, 'defenseiv')
            iv_speed = self.sav.pkm_get(self.pkm, 'speediv')
            iv_spatk = self.sav.pkm_get(self.pkm, 'specialattackiv')
            iv_spdef = self.sav.pkm_get(self.pkm, 'specialdefenseiv')
            bits = (iv_hp & 1) + (iv_attack & 1) * 2 + (iv_defense & 1) * 4 + (iv_speed & 1) * 8 + (
                                                                                                       iv_spatk & 1) * 16 + (
                                                                                                                                iv_spdef & 1) * 32
            hp_type_id = int((bits * 15) / 63)
            hp_type = types_gs_hp[hp_type_id]
            bits = (iv_hp & 2) / 2 + (iv_attack & 2) + (iv_defense & 2) * 2 + (iv_speed & 2) * 4 + (
                                                                                                       iv_spatk & 2) * 8 + (
                                                                                                                               iv_spdef & 2) * 16
            hp_power = int(((bits * 40) / 63) + 30)
            showinfo('About the IV combination',
                     'Your Pokemon\'s Hidden Power is %s type and its power is %d.' % (hp_type, hp_power),
                     parent=self.pokeedit)

    def reload_pkm(self):
        p = self.p
        b = self.b
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        if b == None:
            self.sav.setpokemon(p, self.pkm)
            self.sav.refresh()
            if self.pokemon != None:
                self.wmdel_pokemon()
                self.show_pokemon()
        else:
            self.sav.setpcpokemon(b * self.bp + p, self.pkm)
            self.sav.refresh()
            if self.boxedit != None:
                self.wmdel_boxedit()
                self.show_boxedit(b)
        self.show_pokeedit(p, b)
        self.pokeedit.focus_force()

    def open_pkm(self):
        file = askopenfilename(filetypes=[('PKM File', '.pkm')])
        if not file:
            return
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        fb = open(file, 'rb')
        pkm = fb.read()
        fb.close()
        if len(pkm) == len(self.pkm):
            self.pkm = pkm
            self.reload_pkm()
            showinfo('.PKM loaded', 'Loaded %d bytes from %s.' % (len(pkm), file), parent=self.pokeedit)
        else:
            showerror('Invalid .PKM file',
                      "Invalid .PKM for this location. Your .PKM has %d bytes, but the savefile's one has %d." % (
                          len(pkm), len(self.pkm)), parent=self.pokeedit)

    def max_everything(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        if self.gen <= 2:
            self.pkm = self.sav.pkm_set(self.pkm, 'maxhpev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'attackev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'speedev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'speediv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattackiv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseiv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', 15)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseev', 65535)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattackev', 65535)
        else:
            self.pkm = self.sav.pkm_set(self.pkm, 'maxhpev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'attackev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'speedev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'maxhpiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'speediv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattackiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', 31)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseev', 252)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattackev', 252)
        self.pkm = self.sav.pkm_set(self.pkm, 'happiness', 255)
        self.pkm = self.sav.pkm_set(self.pkm, 'move1ppup', 3)
        self.pkm = self.sav.pkm_set(self.pkm, 'move2ppup', 3)
        self.pkm = self.sav.pkm_set(self.pkm, 'move3ppup', 3)
        self.pkm = self.sav.pkm_set(self.pkm, 'move4ppup', 3)
        self.pkm = self.sav.pkm_set(self.pkm, 'level', 100)
        self.pkm = self.sav.pkm_set(self.pkm, 'curlevel', 100)
        self.pkm = self.sav.pkm_set(self.pkm, 'pokerus', 255)
        self.adjust_exp(100)
        self.adjust_stats()
        self.heal_pkm()

    def heal_pkm(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        if self.b == None:
            self.pkm = self.sav.pkm_set(self.pkm, 'hp', self.sav.pkm_get(self.pkm, 'maxhp'))
        else:
            num = self.sav.pkm_get(self.pkm, 'num')
            if self.gen == 1:
                num = rb2dex[num]
            level = self.sav.pkm_get(self.pkm, 'level')
            curlevel = 0
            if self.b == None:
                curlevel = self.sav.pkm_get(self.pkm, 'curlevel')
            level = max(level, curlevel)
            iv_attack = self.sav.pkm_get(self.pkm, 'attackiv')
            iv_defense = self.sav.pkm_get(self.pkm, 'defenseiv')
            iv_speed = self.sav.pkm_get(self.pkm, 'speediv')
            iv_special = self.sav.pkm_get(self.pkm, 'specialiv')
            iv_hp = iv_attack % 2 * 8 + iv_defense % 2 * 4 + iv_speed % 2 * 2 + iv_special % 2
            ev_hp = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'maxhpev')) / 400)
            self.pkm = self.sav.pkm_set(self.pkm, 'hp', int(10 + level * (base_hp[num] + iv_hp + 50) / 50) + ev_hp)
        self.pkm = self.sav.pkm_set(self.pkm, 'asleep', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'poisoned', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'paralyzed', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'burned', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'frozen', 0)
        for m in range(4):
            base_pp = move_pp[self.sav.pkm_get(self.pkm, 'move%d' % (m + 1))]
            ppup = self.sav.pkm_get(self.pkm, 'move%dppup' % (m + 1))
            self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % (m + 1), base_pp + base_pp * ppup / 5)

        self.reload_pkm()

    def adjust_sprite_type(self):
        if self.gen == 1:
            pkmn = self.pokeclass['selection']
            num = pokemon_rb.index(pkmn)
            self.pokesprite['selection'] = (pokemon[num])
            for i in range(len(pokedex_rb)):
                if pokedex_rb[i].find(pkmn) != -1:
                    num = i
                    break
            else:
                num = 255
            self.type1['selection'] = types_rb[pokemon_types_rb[num][0]]
            self.type2['selection'] = types_rb[pokemon_types_rb[num][1]]
        else:
            num = pokemon_gs.index(self.pokeclass['selection'])
            self.pkm = self.sav.pkm_set(self.pkm, 'num', num)
            self.pokesprite['selection'] = (pokemon[num])
        self.reload_pkm()

    def adjust_stats(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        num = self.sav.pkm_get(self.pkm, 'num')
        if self.gen == 1:
            num = rb2dex[num]
        level = self.sav.pkm_get(self.pkm, 'level')
        curlevel = 0
        if self.b == None:
            curlevel = self.sav.pkm_get(self.pkm, 'curlevel')
        level = max(level, curlevel)
        if self.gen <= 2:
            iv_attack = self.sav.pkm_get(self.pkm, 'attackiv')
            iv_defense = self.sav.pkm_get(self.pkm, 'defenseiv')
            iv_speed = self.sav.pkm_get(self.pkm, 'speediv')
            iv_special = self.sav.pkm_get(self.pkm, 'specialiv')
            iv_hp = iv_attack % 2 * 8 + iv_defense % 2 * 4 + iv_speed % 2 * 2 + iv_special % 2
            ev_hp = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'maxhpev')) / 400)
            ev_attack = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'attackev')) / 400)
            ev_defense = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'defenseev')) / 400)
            ev_speed = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'speedev')) / 400)
            ev_special = int(level * math.sqrt(self.sav.pkm_get(self.pkm, 'specialev')) / 400)
            self.pkm = self.sav.pkm_set(self.pkm, 'hp', int(10 + level * (base_hp[num] + iv_hp + 50) / 50) + ev_hp)
            if self.b == None:
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhp',
                                            int(10 + level * (base_hp[num] + iv_hp + 50) / 50) + ev_hp)
                self.pkm = self.sav.pkm_set(self.pkm, 'attack',
                                            int(5 + level * (base_attack[num] + iv_attack) / 50) + ev_attack)
                self.pkm = self.sav.pkm_set(self.pkm, 'defense',
                                            int(5 + level * (base_defense[num] + iv_defense) / 50) + ev_defense)
                self.pkm = self.sav.pkm_set(self.pkm, 'speed',
                                            int(5 + level * (base_speed[num] + iv_speed) / 50) + ev_speed)
                self.pkm = self.sav.pkm_set(self.pkm, 'specialattack',
                                            int(5 + level * (base_specialattack[num] + iv_special) / 50) + ev_special)
                self.pkm = self.sav.pkm_set(self.pkm, 'specialdefense',
                                            int(5 + level * (base_specialdefense[num] + iv_special) / 50) + ev_special)
                self.pkm = self.sav.pkm_set(self.pkm, 'special',
                                            int(5 + level * (base_special[num] + iv_special) / 50) + ev_attack)
        else:
            iv_hp = self.sav.pkm_get(self.pkm, 'maxhpiv')
            iv_attack = self.sav.pkm_get(self.pkm, 'attackiv')
            iv_defense = self.sav.pkm_get(self.pkm, 'defenseiv')
            iv_speed = self.sav.pkm_get(self.pkm, 'speediv')
            iv_spatk = self.sav.pkm_get(self.pkm, 'specialattackiv')
            iv_spdef = self.sav.pkm_get(self.pkm, 'specialdefenseiv')
            ev_hp = self.sav.pkm_get(self.pkm, 'maxhpev')
            ev_attack = self.sav.pkm_get(self.pkm, 'attackev')
            ev_defense = self.sav.pkm_get(self.pkm, 'defenseev')
            ev_speed = self.sav.pkm_get(self.pkm, 'speedev')
            ev_spatk = self.sav.pkm_get(self.pkm, 'specialattackev')
            ev_spdef = self.sav.pkm_get(self.pkm, 'specialdefenseev')
            pid = self.sav.pkm_get(self.pkm, 'pid')
            nature = pid % 25
            hp = int((2 * base_hp[num] + iv_hp + int(ev_hp / 4)) * level / 100) + level + 10
            atk = int((int(((2 * base_attack[num] + iv_attack + int(ev_attack / 4)) * level) / 100) + 5) * natures_atk[
                nature])
            dfc = int((int((2 * base_defense[num] + iv_defense + int(ev_defense / 4)) * level / 100) + 5) * natures_def[
                nature])
            spatk = int(
                (int((2 * base_specialattack[num] + iv_spatk + int(ev_spatk / 4)) * level / 100) + 5) * natures_spatk[
                    nature])
            spdef = int(
                (int((2 * base_specialdefense[num] + iv_spdef + int(ev_spdef / 4)) * level / 100) + 5) * natures_spdef[
                    nature])
            spe = int(
                (int((2 * base_speed[num] + iv_speed + int(ev_speed / 4)) * level / 100) + 5) * natures_spe[nature])
            self.pkm = self.sav.pkm_set(self.pkm, 'hp', hp)
            self.pkm = self.sav.pkm_set(self.pkm, 'maxhp', hp)
            self.pkm = self.sav.pkm_set(self.pkm, 'attack', atk)
            self.pkm = self.sav.pkm_set(self.pkm, 'defense', dfc)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialattack', spatk)
            self.pkm = self.sav.pkm_set(self.pkm, 'specialdefense', spdef)
            self.pkm = self.sav.pkm_set(self.pkm, 'speed', spe)

        self.reload_pkm()

    def adjust_exp(self, level=None):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        num = self.sav.pkm_get(self.pkm, 'num')
        if self.gen == 1:
            num = rb2dex[num]
        growth = growthrates[num]
        if level == None:
            level = self.sav.pkm_get(self.pkm, 'level')
            curlevel = 0
            if self.b == None:
                curlevel = self.sav.pkm_get(self.pkm, 'curlevel')
            level = max(level, curlevel)
        exp = int(level ** 3)  # Medium Fast
        if growth == 1:  # Erratic
            if level <= 50:
                exp = (level ** 3 * (100 - level)) / 50
            elif level <= 68:
                exp = (level ** 3 * (150 - level)) / 100
            elif level <= 98:
                exp = (level ** 3 * int((1911 - 10 * level) / 3)) / 500
            else:
                exp = (level ** 3 * (160 - level)) / 100
        if growth == 2:  # Fluctuating
            if level <= 15:
                exp = int((level ** 3) * ((int((level + 1) / 3) + 24) / 50.0))
            elif level <= 36:
                exp = int((level ** 3) * ((level + 14) / 50.0))
            else:
                exp = int((level ** 3) * ((int(level / 2) + 32) / 50.0))
        if growth == 3:  # Medium Slow
            exp = int(math.floor(level ** 3 * 1.2 - level * level * 15 + level * 100 - 140))
        if growth == 4:  # Fast
            exp = int(math.floor(level ** 3 * 0.8))
        if growth == 5:  # Slow
            exp = int(math.floor(level ** 3 * 1.25))
        self.pkm = self.sav.pkm_set(self.pkm, 'exp', exp)
        self.reload_pkm()

    def min_everything(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        self.pkm = self.sav.pkm_set(self.pkm, 'maxhpev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'attackev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'defenseev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'speedev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialattackev', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'happiness', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'speediv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialattackiv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseiv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'move1ppup', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'move2ppup', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'move3ppup', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'move4ppup', 0)
        self.pkm = self.sav.pkm_set(self.pkm, 'level', 2)
        self.pkm = self.sav.pkm_set(self.pkm, 'curlevel', 2)
        self.pkm = self.sav.pkm_set(self.pkm, 'pokerus', 0)
        self.adjust_exp(2)
        self.adjust_stats()
        self.heal_pkm()

    def get_pmkm_info(self):
        pokemons = []

        for p in range(6):
            pokemon = {}
            num = self.sav.pkm_get(self.sav.pokemon[p], 'sprite')
            if num == 255:
                break
            if self.gen == 1:
                pkmn = pokemon_lower_rb[num].capitalize()
            elif self.gen == 2:
                pkmn = pokemon_lower_gs[num].capitalize()
            else:
                pkmn = pokemon_rs[num]
            if pkmn.find('Nidoran') != -1:
                if pkmn == 'Nidoranm':
                    pkmn = 'Nidoran-M'
                    num = 32
                elif pkmn == 'Nidoranh':
                    pkmn = 'Nidoran-F'
                    num = 29
                else:
                    if pokemon_lower_rs[num - 1] == 'sandslash':
                        pkmn = 'Nidoran-F'
                        num = 29
                    else:
                        pkmn = 'Nidoran-M'
                        num = 32
            else:
                for i in range(len(pokedex_rs)):
                    if pokedex_rs[i].find(pokemon_rs[num]) != -1:
                        num = i
                        break
                else:
                    return
            nickname = self.sav.pkm_get(self.sav.pokemon[p], 'name')
            level = self.sav.pkm_get(self.sav.pokemon[p], 'curlevel')
            hp_ev = self.sav.pkm_get(self.sav.pokemon[p], 'maxhpev')
            atk_ev = self.sav.pkm_get(self.sav.pokemon[p], 'attackev')
            def_ev = self.sav.pkm_get(self.sav.pokemon[p], 'defenseev')
            spe_ev = self.sav.pkm_get(self.sav.pokemon[p], 'speedev')
            atk_iv = self.sav.pkm_get(self.sav.pokemon[p], 'attackiv')
            def_iv = self.sav.pkm_get(self.sav.pokemon[p], 'defenseiv')
            spe_iv = self.sav.pkm_get(self.sav.pokemon[p], 'speediv')
            if self.gen <= 2:
                spc_iv = self.sav.pkm_get(self.sav.pokemon[p], 'specialiv')
                spc_ev = int(math.sqrt(self.sav.pkm_get(self.sav.pokemon[p], 'specialev')))
                hp_iv = atk_iv % 2 * 8 + def_iv % 2 * 4 + spe_iv % 2 * 2 + spc_iv % 2
                hp_iv = hp_iv * 2 + 1
                atk_iv = atk_iv * 2 + 1
                def_iv = def_iv * 2 + 1
                spe_iv = spe_iv * 2 + 1
                spc_iv = spc_iv * 2 + 1
                hp_ev = int(math.sqrt(hp_ev))
                atk_ev = int(math.sqrt(atk_ev))
                def_ev = int(math.sqrt(def_ev))
                spe_ev = int(math.sqrt(spe_ev))
            else:
                hp_iv = self.sav.pkm_get(self.sav.pokemon[p], 'maxhpiv')
                spd_iv = self.sav.pkm_get(self.sav.pokemon[p], 'specialdefenseiv')
                spa_iv = self.sav.pkm_get(self.sav.pokemon[p], 'specialattackiv')
                spd_ev = self.sav.pkm_get(self.sav.pokemon[p], 'specialdefenseev')
                spa_ev = self.sav.pkm_get(self.sav.pokemon[p], 'specialattackev')

            moves = []
            for i in range(4):
                move = self.sav.pkm_get(self.sav.pokemon[p], 'move%d' % (i + 1))
                if move == 0:
                    break
                move = moves_rs[move]
                if move == 'Hidden Power':
                    if self.gen == 2:
                        hp_type_id = ((atk_iv / 2) & 3) * 4 + ((def_iv / 2) & 3)
                        hp_type = types_gs_hp[hp_type_id]
                        move += ' [' + hp_type + ']'
                    elif self.gen == 3:
                        bits = (hp_iv & 1) + (atk_iv & 1) * 2 + (def_iv & 1) * 4 + (spe_iv & 1) * 8 + (
                                                                                                          spa_iv & 1) * 16 + (
                                                                                                                                 spd_iv & 1) * 32
                        hp_type_id = int((bits * 15) / 63)
                        hp_type = types_gs_hp[hp_type_id]
                        move += ' [' + hp_type + ']'
                moves.append(move)

            gender = 'L'
            item = ''
            shiny = 'No'
            happiness = 255
            if isinstance(pokemon_abilities[num], str):
                ability = pokemon_abilities[num]
            else:
                ability = pokemon_abilities[num][0]
            nature = ''

            if self.gen >= 2:
                item = self.sav.pkm_get(self.sav.pokemon[p], 'item')
                if item == 0:
                    item = ''
                elif self.gen == 2:
                    item = items_gs[item]
                else:
                    item = items_rs[item]
                happiness = self.sav.pkm_get(self.sav.pokemon[p], 'happiness')
                if self.gen == 2:
                    if def_iv == 10 and spe_iv == 10 and spc_iv == 10 and atk_iv & 2:
                        shiny = 'Yes'
                    else:
                        shiny = 'No'
                    if num in gender_rate:
                        if gender_rate[num] == 0:
                            gender = 'M'
                        elif gender_rate[num] == 254:
                            gender = 'F'
                        elif gender_rate[num] == 255:
                            gender = 'L'
                        elif gender_rate[num] == 31:
                            if int(atk_iv) < 2:
                                gender = 'F'
                            else:
                                gender = 'M'
                        elif gender_rate[num] == 63:
                            if int(atk_iv) < 4:
                                gender = 'F'
                            else:
                                gender = 'M'
                        elif gender_rate[num] == 191:
                            if int(atk_iv) < 12:
                                gender = 'F'
                            else:
                                gender = 'M'
                    else:
                        if int(atk_iv) < 8:
                            gender = 'F'
                        else:
                            gender = 'M'

                else:
                    pid = self.sav.pkm_get(self.sav.pokemon[p], 'pid')
                    if (not isinstance(pokemon_abilities[num], str)) and ((pid % 2) == 1):
                        ability = pokemon_abilities[num][1]
                    nature = natures[pid % 25][:natures[pid % 25].find(' ')]
                    if self.sav.pkm_get(self.sav.pokemon[p], 'num') in gender_rate:
                        if gender_rate[self.sav.pkm_get(self.sav.pokemon[p], 'num')] == 254:
                            gender = 'F'
                        elif gender_rate[self.sav.pkm_get(self.sav.pokemon[p], 'num')] == 255:
                            gender = 'L'
                        else:
                            if gender >= gender_rate[self.sav.pkm_get(self.sav.pokemon[p], 'num')]:
                                gender = 'M'
                            else:
                                gender = 'F'
                    else:
                        if gender >= 127:
                            gender = 'M'
                        else:
                            gender = 'F'
                    p1 = pid / 65536
                    p2 = pid % 65536
                    otnum = self.sav.pkm_get(self.sav.pokemon[p], 'otnum')
                    secretid = self.sav.pkm_get(self.sav.pokemon[p], 'secretid')
                    if (p1 ^ p2 ^ otnum ^ secretid) < 8:
                        shiny = 'Yes'
                    else:
                        shiny = 'No'

            pokemon['Pokemon'] = pkmn
            pokemon['Nickname'] = nickname
            pokemon['Level'] = level
            pokemon['Moves'] = moves
            if self.gen <= 2:
                pokemon['IVs'] = [hp_iv, atk_iv, def_iv, spc_iv, spc_iv, spe_iv]
                pokemon['EVs'] = [hp_ev, atk_ev, def_ev, spc_ev, spc_ev, spe_ev]
            else:
                pokemon['IVs'] = [hp_iv, atk_iv, def_iv, spa_iv, spd_iv, spe_iv]
                pokemon['EVs'] = [hp_ev, atk_ev, def_ev, spa_ev, spd_ev, spe_ev]
            pokemon['Ability'] = ability
            pokemon['Gender'] = gender
            pokemon['Item'] = item
            pokemon['Shiny'] = shiny
            pokemon['Happiness'] = happiness
            pokemon['Nature'] = nature

            pokemons.append(pokemon)

        return create_exportable(pokemons)

    def save_pkm(self):
        file = asksaveasfilename(filetypes=[('PKM File', '.pkm')])
        if not file:
            return
        if file[-4:] != '.pkm':
            file = '%s.pkm' % file
        fb = open(file, 'wb')
        fb.write(self.pkm)
        fb.close()
        showinfo('Saved .PKM file', 'Saved %d bytes to %s.' % (len(self.pkm), file), parent=self.pokeedit)

    def save_teams(self, pokemons, locations):
        teams_size = []
        locations_raw = []
        boxpokemoncount = list(self.sav.boxpokemoncount)
        for key in locations:
            if locations[key]['selection'] == 'Party':
                locations_raw.append(locations[key]['selection'])
            else:
                l = int(parse('Box {}', locations[key]['selection']).fixed[0]) - 1
                locations_raw.append(l)
            teams_size.append(len(pokemons[key]))

        if locations_raw.count('Party') > 1:
            showerror('Something went wrong =(', 'You can only store one team in the party!')
            return

        for i in range(len(teams_size)):
            if locations_raw[i] == 'Party':
                continue
            boxpokemoncount[locations_raw[i]] += teams_size[i]
            if boxpokemoncount[int(locations_raw[i])] > 20:
                showerror('Something went wrong =(',
                          'Box ' + str(locations_raw[i]+1) + ' overflow! Please change your team'
                                                           'locations and try again.')
                return

        for key in pokemons:
            self.save_team(pokemons[key], locations[key]['selection'])
        self.choose.destroy()
        self.wmdel_pokemon()

    def save_team(self, pokemons, location):
        self.b = None
        if location == 'Party':
            bin_pkm = 0
        else:
            self.b = int(parse('Box {}', location).fixed[0]) - 1
            bin_pkm = self.sav.boxpokemoncount[self.b] if self.sav.boxpokemoncount[self.b] < self.bp else 0
        for i in range(len(pokemons)):
            self.pkm = self.sav.pokemon[0]
            self.p = bin_pkm
            pkmn = pokemons[i]

            # Species
            if pkmn['Pokemon'].find('Nidoran-M') != -1:
                num = 3
                pkm_no = 29
            elif pkmn['Pokemon'].find('Nidoran-F') != -1:
                num = 15
                pkm_no = 32
            else:
                try:
                    if self.gen == 2:
                        num = pokemon_lower_gs.index(pkmn['Pokemon'].lower())
                    elif self.gen == 1:
                        num = pokemon_lower_rb.index(pkmn['Pokemon'].lower())
                        for index in range(len(pokedex_rb)):
                            if pokedex_rb[index].find(pkmn['Pokemon']) != -1:
                                pkm_no = index
                                break
                        else:
                            continue
                    else:
                        pkm_no = pokemon_lower_rs.index(pkmn['Pokemon'].lower())
                        for index in range(len(pokemon_rs)):
                            if pokemon_rs[index].find(pkmn['Pokemon']) != -1:
                                num = index
                                break
                        else:
                            continue
                except ValueError:
                    continue

            # Original trainer name and num
            otname = self.sav.pkm_get(self.sav.pokemon[0], 'otname')
            otnum = self.sav.pkm_get(self.sav.pokemon[0], 'otnum')
            self.pkm = self.sav.pkm_set(self.pkm, 'otname', otname)
            self.pkm = self.sav.pkm_set(self.pkm, 'otnum', otnum)
            if self.gen == 3:
                secretid = self.sav.pkm_get(self.sav.pokemon[0], 'secretid')
                self.pkm = self.sav.pkm_set(self.pkm, 'secretid', secretid)

            # Nickname
            if pkmn['Nickname'] == "":
                if pkmn['Pokemon'].find('Nidoran-M') != -1 or pkmn['Pokemon'].find('Nidoran-F') != -1:
                    nickname = 'NIDORAN'
                else:
                    nickname = pkmn['Pokemon'].upper()
            else:
                nickname = pkmn['Nickname']
            self.pkm = self.sav.pkm_set(self.pkm, 'name', nickname)
            self.pkm = self.sav.pkm_set(self.pkm, 'sprite', num)
            self.pkm = self.sav.pkm_set(self.pkm, 'num', num)

            if self.gen != 2:
                num = pkm_no

            # Level
            if pkmn['Level'] == '':
                level = 100
            else:
                level = int(pkmn['Level'])
            self.pkm = self.sav.pkm_set(self.pkm, 'level', level)
            if self.gen == 1:
                self.pkm = self.sav.pkm_set(self.pkm, 'curlevel', level)

            # Types
            if self.gen == 1:
                self.pkm = self.sav.pkm_set(self.pkm, 'type1', pokemon_types_rb[num][0])
                self.pkm = self.sav.pkm_set(self.pkm, 'type2', pokemon_types_rb[num][1])

            # PID
            if self.gen == 3:
                if not isinstance(pokemon_abilities, str):
                    if pokemon_abilities[num][1] == pkmn['Ability']:
                        ability = 1
                    else:
                        ability = 0
                else:
                    ability = 0
                if pkmn['Shiny'] == 'Yes':
                    shiny = 0
                else:
                    shiny = 1
                for j in range(len(natures)):
                    if natures[j].find(pkmn['Nature']) != -1:
                        nature = j
                        break
                else:
                    nature = 0
                if pkmn['Gender'] == '':
                    gender = randint(0, 1)
                elif pkmn['Gender'] == 'M':
                    gender = 0
                else:
                    gender = 1
                pid = self.generate_pid(num, otnum, secretid, nature, gender, ability, shiny)
                self.pkm = self.sav.pkm_set(self.pkm, 'pid', pid)

            # Stats

            # Get IVs/EVs
            if self.gen <= 2:
                stats = ['HP', 'Atk', 'Def', 'SpA', 'Spe']
                if empty_evs(pkmn['EVs']):
                    evs = [65535, 65535, 65535, 65535, 65535]
                else:
                    evs = [0, 0, 0, 0, 0]
                ivs = [15, 15, 15, 15, 15, 15]
                for j in range(5):
                    if pkmn['EVs'][stats[j]] != '':
                        evs[j] = int(pkmn['EVs'][stats[j]]) ** 2
                    if pkmn['IVs'][stats[j]] != '' and int(pkmn['IVs'][stats[j]]) < 31:
                        ivs[j] = int(pkmn['IVs'][stats[j]]) / 2
                self.pkm = self.sav.pkm_set(self.pkm, 'specialev', evs[3])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', ivs[3])
                iv_hp = ivs[1] / 2 % 2 * 8 + ivs[2] % 2 * 4 + ivs[4] % 2 * 2 + ivs[3] % 2
            else:
                stats = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
                evs = [0, 0, 0, 0, 0, 0]
                ivs = [31, 31, 31, 31, 31, 31]
                for j in range(6):
                    if pkmn['EVs'][stats[j]] != '':
                        evs[j] = int(pkmn['EVs'][stats[j]])
                    if pkmn['IVs'][stats[j]] != '':
                        ivs[j] = int(pkmn['IVs'][stats[j]])

            # Set EVs/IVs
            if self.gen <= 2:
                iv_hp = ivs[1] / 2 % 2 * 8 + ivs[2] % 2 * 4 + ivs[4] % 2 * 2 + ivs[3] % 2
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhpev', evs[0])
                self.pkm = self.sav.pkm_set(self.pkm, 'attackev', evs[1])
                self.pkm = self.sav.pkm_set(self.pkm, 'defenseev', evs[2])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialev', evs[3])
                self.pkm = self.sav.pkm_set(self.pkm, 'speedev', evs[4])
                self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', ivs[1])
                self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', ivs[2])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialiv', ivs[3])
                self.pkm = self.sav.pkm_set(self.pkm, 'speediv', ivs[4])
            else:
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhpiv', ivs[0])
                self.pkm = self.sav.pkm_set(self.pkm, 'attackiv', ivs[1])
                self.pkm = self.sav.pkm_set(self.pkm, 'defenseiv', ivs[2])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialattackiv', ivs[3])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseiv', ivs[4])
                self.pkm = self.sav.pkm_set(self.pkm, 'speediv', ivs[5])
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhpev', evs[0])
                self.pkm = self.sav.pkm_set(self.pkm, 'attackev', evs[1])
                self.pkm = self.sav.pkm_set(self.pkm, 'defenseev', evs[2])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialattackev', evs[3])
                self.pkm = self.sav.pkm_set(self.pkm, 'specialdefenseev', evs[4])
                self.pkm = self.sav.pkm_set(self.pkm, 'speedev', evs[5])

            # Calc stats
            if self.gen <= 2:
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhp', int(10 + level * (base_hp[num] + iv_hp + 50) / 50 +
                                                                   (math.sqrt(evs[0]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'hp', int(10 + level * (base_hp[num] + iv_hp + 50) / 50 +
                                                                (math.sqrt(evs[0]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'attack',
                                            int(5 + level * (base_attack[num] + ivs[1]) / 50 + (math.sqrt(evs[1]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'defense',
                                            int(5 + level * (base_defense[num] + ivs[2]) / 50 + (
                                                math.sqrt(evs[2]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'speed',
                                            int(5 + level * (base_speed[num] + ivs[4]) / 50 + (math.sqrt(evs[4]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'specialattack',
                                            int(5 + level * (base_specialattack[num] + ivs[3]) / 50 +
                                                (math.sqrt(evs[3]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'specialdefense',
                                            int(5 + level * (base_specialdefense[num] + ivs[3]) / 50 +
                                                (math.sqrt(evs[3]) / 4)))
                self.pkm = self.sav.pkm_set(self.pkm, 'special',
                                            int(5 + level * (base_special[num] + ivs[3]) / 50 + (
                                                math.sqrt(evs[3]) / 4)))
            else:
                hp = int((2 * base_hp[num] + ivs[0] + int(evs[0] / 4)) * level / 100) + level + 10
                atk = int(
                    (int(((2 * base_attack[num] + ivs[1] + int(evs[1] / 4)) * level) / 100) + 5) * natures_atk[nature])
                dfc = int(
                    (int((2 * base_defense[num] + ivs[2] + int(evs[2] / 4)) * level / 100) + 5) * natures_def[nature])
                spatk = int(
                    (int((2 * base_specialattack[num] + ivs[3] + int(evs[3] / 4)) * level / 100) + 5) * natures_spatk[
                        nature])
                spdef = int(
                    (int((2 * base_specialdefense[num] + ivs[4] + int(evs[4] / 4)) * level / 100) + 5) * natures_spdef[
                        nature])
                spe = int(
                    (int((2 * base_speed[num] + ivs[5] + int(evs[5] / 4)) * level / 100) + 5) * natures_spe[nature])
                self.pkm = self.sav.pkm_set(self.pkm, 'hp', hp)
                self.pkm = self.sav.pkm_set(self.pkm, 'maxhp', hp)
                self.pkm = self.sav.pkm_set(self.pkm, 'attack', atk)
                self.pkm = self.sav.pkm_set(self.pkm, 'defense', dfc)
                self.pkm = self.sav.pkm_set(self.pkm, 'specialattack', spatk)
                self.pkm = self.sav.pkm_set(self.pkm, 'specialdefense', spdef)
                self.pkm = self.sav.pkm_set(self.pkm, 'speed', spe)

            # Moves
            current_move = 0
            for j in range(len(pkmn['Moves'])):
                current_move += 1
                if self.gen >= 2 and pkmn['Moves'][j].find('Hidden Power') != -1:
                    self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move, 237)
                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                move_pp[237] + 3 * move_pp[237] / 5)
                else:
                    if self.gen == 1:
                        for index in range(len(moves_rb)):
                            if moves_rb[index].find(pkmn['Moves'][j]) != -1:
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move, index)
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                if move_pp[index] != 40:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[index] + 3 * move_pp[index] / 5)
                                else:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move, 61)
                                break
                        else:
                            for key in new2oldMoveNames_rb:
                                if key.find(pkmn['Moves'][j]) != -1:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move,
                                                                new2oldMoveNames_rb[key])
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[new2oldMoveNames_rb[key]] +
                                                                3 * move_pp[new2oldMoveNames_rb[key]] / 5)
                                    break
                            else:
                                current_move -= 1

                    elif self.gen == 2:
                        for index in range(len(moves_gs)):
                            if moves_gs[index].find(pkmn['Moves'][j]) != -1:
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move, index)
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                if move_pp[index] != 40:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[index] + 3 * move_pp[index] / 5)
                                else:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move, 61)
                                break
                        else:
                            for key in new2oldMoveNames_gs:
                                if key.find(pkmn['Moves'][j]) != -1:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move,
                                                                new2oldMoveNames_gs[key])
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[new2oldMoveNames_gs[key]] +
                                                                3 * move_pp[new2oldMoveNames_gs[key]] / 5)
                                    break
                            else:
                                current_move -= 1
                    else:
                        for index in range(len(moves_rs)):
                            if moves_rs[index].find(pkmn['Moves'][j]) != -1:
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move, index)
                                self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                if move_pp[index] != 40:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[index] + 3 * move_pp[index] / 5)
                                else:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move, 61)
                                break
                        else:
                            for key in new2oldMoveNames_rs:
                                if key.find(pkmn['Moves'][j]) != -1:
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move,
                                                                new2oldMoveNames_rs[key])
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dppup' % current_move, 3)
                                    self.pkm = self.sav.pkm_set(self.pkm, 'move%dpp' % current_move,
                                                                move_pp[new2oldMoveNames_rs[key]] +
                                                                3 * move_pp[new2oldMoveNames_rs[key]] / 5)
                                    break
                            else:
                                current_move -= 1

            while current_move < len(pkmn['Moves']):
                current_move += 1
                self.pkm = self.sav.pkm_set(self.pkm, 'move%d' % current_move, 0)

            # Item
            if self.gen == 2:
                for index in range(len(items_gs)):
                    if unicode(items_gs[index], 'utf-8').find(pkmn['Item']) != -1:
                        self.pkm = self.sav.pkm_set(self.pkm, 'item', index)
                        break
                else:
                    self.pkm = self.sav.pkm_set(self.pkm, 'item', 0)
            elif self.gen == 3:
                for index in range(len(items_rs)):
                    if unicode(items_rs[index], 'utf-8').find(pkmn['Item']) != -1:
                        self.pkm = self.sav.pkm_set(self.pkm, 'item', index)
                        break
                else:
                    self.pkm = self.sav.pkm_set(self.pkm, 'item', 0)
            # Happiness
            if self.gen >= 2:
                if pkmn['Happiness'] == "":
                    self.pkm = self.sav.pkm_set(self.pkm, 'happiness', 255)
                else:
                    self.pkm = self.sav.pkm_set(self.pkm, 'happiness', int(pkmn['Happiness']))

            # Shenanigans
            if self.gen == 2:
                self.pkm = self.sav.pkm_set(self.pkm, 'caughttime', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'caughtzone', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'caughtlevel', 0)
            elif self.gen == 1:
                self.pkm = self.sav.pkm_set(self.pkm, 'catchrate', 0)
            else:
                self.pkm = self.sav.pkm_set(self.pkm, 'coolness', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'beauty', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'cuteness', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'smartness', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'toughness', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'feel', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'pokerus', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'caughtlevel', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'caughtball', 0)
                self.pkm = self.sav.pkm_set(self.pkm, 'caughtlocation', 0)

            # Experience
            growth = growthrates[num]
            exp = int(level ** 3)
            if growth == 3:
                exp = int(math.floor(level ** 3 * 1.2 - level * level * 15 + level * 100 - 140))
            if growth == 4:
                exp = int(math.floor(level ** 3 * 0.8))
            if growth == 5:
                exp = int(math.floor(level ** 3 * 1.25))
            self.pkm = self.sav.pkm_set(self.pkm, 'exp', exp)
            if location == 'Party':
                self.sav.setpokemon(bin_pkm, self.pkm)
            else:
                self.sav.setpcpokemon(self.b * self.bp + bin_pkm, self.pkm)
            bin_pkm += 1
        if location == 'Party':
            slots = 6
            if self.gen <= 2:
                self.sav.set('pokemoncount', bin_pkm)
                self.sav.pokemoncount = bin_pkm
        else:
            slots = self.bp
            if self.gen <= 2:
                self.sav.set('box' + str(self.b) + 'pokemoncount', bin_pkm)
                self.sav.boxpokemoncount[self.b] = bin_pkm

        while bin_pkm != slots:
            self.pkm = self.sav.pokemon[0]
            self.pkm = chr(0) * len(self.pkm)
            self.pkm = self.sav.pkm_set(self.pkm, 'num', 255)
            self.pkm = self.sav.pkm_set(self.pkm, 'sprite', 255)
            if location == 'Party':
                self.sav.setpokemon(bin_pkm, self.pkm)
            else:
                self.sav.setpcpokemon(self.b * self.bp + bin_pkm, self.pkm)
            bin_pkm += 1

    def on_pid_change(self, name, index, mode):
        if self.pid.get() == '':
            return
        self.changingPid = True
        pid = int(self.pidInt.get())
        otnum = int(self.otnum.get())
        secretid = int(self.secretid.get())
        pkm = pokemon.index(self.pokeclass['selection'])
        self.natureInt.set(natures[pid % 25])
        pokemon_name = pokemon[pkm]
        for i in range(len(pokedex_rs)):
            if pokedex_rs[i].find(pokemon_name) != -1:
                dex_num = i
                break
        if isinstance(pokemon_abilities[dex_num], str):
            self.ability.set(0)
        else:
            self.ability.set(pid % 2)
        gen_rate = 127
        for key in gender_rate:
            if pkm == key:
                gen_rate = gender_rate[key]
        if gen_rate == 255 or (pid % 256) >= gen_rate:
            self.gender.set(0)
        else:
            self.gender.set(1)
        p1 = pid / 65536
        p2 = pid % 65536
        if (p1 ^ p2 ^ otnum ^ secretid) < 8:
            self.shiny.set(0)
        else:
            self.shiny.set(1)
        self.changingPid = False

    def generate_pid(self, pkm, trainerid, secretid, nature=None, gender=None, ability=None, shiny=None):
        pid = randint(0, 2 ** 32 - 1)
        iterations = 0
        gen_rate = 127
        if pkm == 29:
            gen_rate = 254
        elif pkm == 32:
            gen_rate = 0
        else:
            name = pokemon_lower_rs[pkm].capitalize()
            for i in range(len(pokemon_rs)):
                if pokemon_rs[i].find(name):
                    mem_num = i
                    break
            else:
                return
            if pkm in gender_rate:
                gen_rate = gender_rate[pkm]
        if isinstance(pokemon_abilities[pkm], str):
            skip_ability_check = True
        else:
            skip_ability_check = False
        while True:
            if (pid % 25 == nature or nature is None) and (pid % 2 == ability or ability is None or skip_ability_check):
                if gen_rate >= 254 or gen_rate == 0 or (gender == 1 and ((pid % 256) < gen_rate)) or (
                                gender == 0 and ((pid % 256) >= gen_rate)) or gender is None:
                    if shiny == 1 or shiny is None:
                        return pid
                    else:
                        p1 = pid / 65536
                        p2 = pid % 65536
                        if (p1 ^ p2 ^ trainerid ^ secretid) < 8:
                            return pid
            if iterations % 1000000 == 0:
                pid = randint(0, 2 ** 32 - 1)
            else:
                pid += 1
            iterations += 1
            if pid >= (2 ** 32 - 1):
                pid = 0

    def adjust_pid(self, event=None):
        if self.changingPid:
            return
        pid = self.generate_pid(self.sav.pkm_get(self.pkm, 'num'), int(self.otnum.get()), int(self.secretid.get()),
                                natures.index(self.natureInt.get()), self.gender.get(), self.ability.get(),
                                self.shiny.get())
        self.pid.delete(0, END)
        self.pid.insert(0, pid)
        self.sav.pkm_set(self.pkm, 'pid', pid)

    def add_fields(self):
        self.frame.grid_forget()
        Label(self.root, text='   ').grid(row=1000, column=1000)
        Label(text='').grid(row=0)
        Label(text='      Trainer Name:  ', anchor=W).grid(row=1, sticky=W)
        self.trname = Entry()
        self.trname.grid(row=1, column=1)
        Label(text='      Rival Name:  ').grid(row=1, column=2, sticky=W)
        self.rivalname = Entry()
        self.rivalname.grid(row=1, column=3)
        Label(text='      Money:  ').grid(row=2, column=0, sticky=W)
        self.money = Entry()
        self.money.grid(row=2, column=1)
        Label(text='      Casino Chips:  ').grid(row=2, column=2, sticky=W)
        self.chips = Entry()
        self.chips.grid(row=2, column=3)
        Label(text='      h/m/s Played  ').grid(row=3, column=0, sticky=W)
        self.hours = Entry(width=5)
        self.hours.grid(row=3, column=1, sticky=W)
        self.minutes = Entry(width=5)
        self.minutes.grid(row=3, column=1)
        self.seconds = Entry(width=5)
        self.seconds.grid(row=3, column=1, sticky=E)
        Label(text='').grid(row=4)
        Button(text='Pok\xc3\xa9mon', width=10, command=self.show_pokemon).grid(row=5)
        Label(text='Edit the Pok\xc3\xa9mon from the party.').grid(row=5, column=1, sticky=W, columnspan=3)
        Label(text='', font=('Times', 4)).grid(row=6)
        Button(text='PC Pok\xc3\xa9mon', width=10, command=self.show_boxes).grid(row=7)
        Label(text="Edit the Pok\xc3\xa9mon stored at Bill's PC.").grid(row=7, column=1, sticky=W, columnspan=3)
        Label(text='', font=('Times', 4)).grid(row=8)
        Button(text='Bag Items', width=10, command=self.show_items).grid(row=9)
        Label(text='Change the class or quantity of every item in the bag.').grid(row=9, column=1, sticky=W,
                                                                                  columnspan=3)
        Label(text='', font=('Times', 4)).grid(row=10)
        Button(text='PC Items', width=10, command=self.show_pcitems).grid(row=11)
        Label(text='Change the class or quantity of every item in the PC.').grid(row=11, column=1, sticky=W,
                                                                                 columnspan=3)
        Label(text='', font=('Times', 4)).grid(row=12)
        Button(text='Pokedex 1/2', width=10, command=self.show_pokedex1).grid(row=13)
        Label(text='Mark a certain Pok\xc3\xa9mon as seen or catched at the Pok\xc3\xa9dex.').grid(row=13, column=1,
                                                                                                   sticky=W,
                                                                                                   columnspan=3)
        Label(text='', font=('Times', 4)).grid(row=14)
        Button(text='Pokedex 2/2', width=10, command=self.show_pokedex2).grid(row=15)
        Label(text='Mark a certain Pok\xc3\xa9mon as seen or catched at the Pok\xc3\xa9dex.').grid(row=15, column=1,
                                                                                                   sticky=W,
                                                                                                   columnspan=3)

    def show_frame(self):
        self.title = 'PikaSav v0.4 RC 2'
        self.root.title(self.title)
        self.frame = Frame(self.root)
        self.add_fields()
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.frame.mainloop()

    def close_frames(self):
        if self.items != None:
            self.items.destroy()
            self.items = None
        if self.pcitems != None:
            self.pcitems.destroy()
            self.pcitems = None
        if self.pokemon != None:
            self.pokemon.destroy()
            self.pokemon = None
        if self.boxes != None:
            self.boxes.destroy()
            self.boxes = None
        if self.boxedit != None:
            self.boxedit.destroy()
            self.boxedit = None
        if self.pokedex1 != None:
            self.pokedex1.destroy()
            self.pokedex1 = None
        if self.pokedex2 != None:
            self.pokedex2.destroy()
            self.pokedex2 = None
        if self.pokeedit != None:
            self.pokeedit.destroy()
            self.pokeedit = None

    def exit(self):
        self.close_frames()
        self.root.destroy()

    def __init__(self):
        self.gen = 0
        self.root = Tk()
        self.sav = None
        self.pokemon = None
        self.items = None
        self.boxes = None
        self.pokeedit = None
        self.pcpokeedit = None
        self.boxedit = None
        self.pcitems = None
        self.pokedex1 = None
        self.pokedex2 = None
        self.iclass = [None] * 163
        self.icount = [None] * 163
        self.pciclass = [None] * 50
        self.pcicount = [None] * 50
        self.dexseen = [None] * 387
        self.dexcatched = [None] * 387
        self.add_menus()
        self.show_frame()

    def save_items(self):
        if self.items != None:
            for i in range(20):
                self.sav.items[i][1] = self.icount[i]

    def show_items(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.items != None:
            self.items.focus_force()
            return
        self.items = Toplevel()
        self.items.title('Bag Items - %s' % self.title)
        self.items.protocol('WM_DELETE_WINDOW', self.wmdel_items)
        Label(self.items, text='   ').grid(row=1000, column=1000)
        Label(self.items, text='Item class').grid(row=0, column=1)
        Label(self.items, text='Quantity').grid(row=0, column=2)
        array = items * 1
        array.sort(reverse=True)
        inum = 20
        if self.gen >= 3:
            inum = 33
        for i in range(inum):
            iclass = self.sav.items[i][0]
            if iclass < len(items):
                iclass = items[iclass]
            else:
                iclass = str(iclass)
            icount = self.sav.items[i][1]
            Label(self.items, text='    Item %d' % (i + 1)).grid(row=i + 1, sticky=W)
            self.iclass[i] = ComboBox(self.items, dropdown=1, editable=1, width=20, value=iclass)
            for t in array:
                self.iclass[i].insert(0, t)

            self.iclass[i].grid(row=i + 1, column=1)
            self.icount[i] = Entry(self.items, width=4)
            self.icount[i].insert(0, icount)
            self.icount[i].grid(row=i + 1, column=2)

        if self.gen >= 3:
            Label(self.items, text='Item class').grid(row=0, column=4)
            Label(self.items, text='Quantity').grid(row=0, column=5)
            for i in range(33, 66):
                iclass = self.sav.items[i][0]
                if iclass < len(items):
                    iclass = items[iclass]
                else:
                    iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items, text='    Item %d' % (i + 1)).grid(row=i % 33 + 1, column=3, sticky=W)
                self.iclass[i] = ComboBox(self.items, dropdown=1, editable=1, width=20, value=iclass)
                for t in array:
                    self.iclass[i].insert(0, t)

                self.iclass[i].grid(row=i % 33 + 1, column=4)
                self.icount[i] = Entry(self.items, width=4)
                self.icount[i].insert(0, icount)
                self.icount[i].grid(row=i % 33 + 1, column=5)

            Label(self.items, text='Item class').grid(row=0, column=7)
            Label(self.items, text='Quantity').grid(row=0, column=8)
            for i in range(66, 99):
                iclass = self.sav.items[i][0]
                if iclass < len(items):
                    iclass = items[iclass]
                else:
                    iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items, text='    Item %d' % (i + 1)).grid(row=i % 33 + 1, column=6, sticky=W)
                self.iclass[i] = ComboBox(self.items, dropdown=1, editable=1, width=20, value=iclass)
                for t in array:
                    self.iclass[i].insert(0, t)

                self.iclass[i].grid(row=i % 33 + 1, column=7)
                self.icount[i] = Entry(self.items, width=7)
                self.icount[i].insert(0, icount)
                self.icount[i].grid(row=i % 33 + 1, column=8)

            Label(self.items, text='Item class').grid(row=0, column=10)
            Label(self.items, text='Quantity').grid(row=0, column=11)
            for i in range(99, 132):
                iclass = self.sav.items[i][0]
                if iclass < len(items):
                    iclass = items[iclass]
                else:
                    iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items, text='    Item %d' % (i + 1)).grid(row=i % 33 + 1, column=9, sticky=W)
                self.iclass[i] = ComboBox(self.items, dropdown=1, editable=1, width=20, value=iclass)
                for t in array:
                    self.iclass[i].insert(0, t)

                self.iclass[i].grid(row=i % 33 + 1, column=10)
                self.icount[i] = Entry(self.items, width=7)
                self.icount[i].insert(0, icount)
                self.icount[i].grid(row=i % 33 + 1, column=11)

            Label(self.items, text='Item class').grid(row=0, column=13)
            Label(self.items, text='Quantity').grid(row=0, column=14)
            for i in range(132, 163):
                iclass = self.sav.items[i][0]
                if iclass < len(items):
                    iclass = items[iclass]
                else:
                    iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items, text='    Item %d' % (i + 1)).grid(row=i % 33 + 1, column=12, sticky=W)
                self.iclass[i] = ComboBox(self.items, dropdown=1, editable=1, width=20, value=iclass)
                for t in array:
                    self.iclass[i].insert(0, t)

                self.iclass[i].grid(row=i % 33 + 1, column=13)
                self.icount[i] = Entry(self.items, width=7)
                self.icount[i].insert(0, icount)
                self.icount[i].grid(row=i % 33 + 1, column=14)

        if self.gen <= 2:
            Label(self.items, text='    Item # (Set this to number of items)').grid(row=21, columnspan=2, sticky=W)
            self.itemcount = Entry(self.items, width=4)
            self.itemcount.insert(0, str(self.sav.itemcount))
            self.itemcount.grid(row=21, column=2)

    def show_pcitems(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.pcitems != None:
            self.pcitems.focus_force()
            return
        self.pcitems = Toplevel()
        self.pcitems.title('PC Items - %s' % self.title)
        self.pcitems.protocol('WM_DELETE_WINDOW', self.wmdel_pcitems)
        Label(self.pcitems, text='   ').grid(row=1000, column=1000)
        Label(self.pcitems, text='Item class').grid(row=0, column=1)
        Label(self.pcitems, text='Quantity').grid(row=0, column=2)
        array = items * 1
        array.sort(reverse=True)
        for i in range(25):
            iclass = self.sav.pcitems[i][0]
            if iclass < len(items):
                iclass = items[iclass]
            else:
                iclass = str(iclass)
            icount = self.sav.pcitems[i][1]
            Label(self.pcitems, text='    Item %d' % (i + 1)).grid(row=i + 1, sticky=W)
            self.pciclass[i] = ComboBox(self.pcitems, dropdown=1, editable=1, width=20, value=iclass)
            for t in array:
                self.pciclass[i].insert(0, t)

            self.pciclass[i].grid(row=i + 1, column=1)
            self.pcicount[i] = Entry(self.pcitems, width=4)
            self.pcicount[i].insert(0, icount)
            self.pcicount[i].grid(row=i + 1, column=2)

        Label(self.pcitems, text='Item class').grid(row=0, column=4)
        Label(self.pcitems, text='Quantity').grid(row=0, column=5)
        for i in range(25, 50):
            iclass = self.sav.pcitems[i][0]
            if iclass < len(items):
                iclass = items[iclass]
            else:
                iclass = str(iclass)
            icount = self.sav.pcitems[i][1]
            Label(self.pcitems, text='    Item %d' % (i + 1)).grid(row=i % 25 + 1, column=3, sticky=W)
            self.pciclass[i] = ComboBox(self.pcitems, dropdown=1, editable=1, width=20, value=iclass)
            for t in array:
                self.pciclass[i].insert(0, t)

            self.pciclass[i].grid(row=i % 25 + 1, column=4)
            self.pcicount[i] = Entry(self.pcitems, width=4)
            self.pcicount[i].insert(0, icount)
            self.pcicount[i].grid(row=i % 25 + 1, column=5)

        if self.gen <= 2:
            Label(self.pcitems, text='    Item # (Set this to number of items)').grid(row=26, columnspan=2, sticky=W)
            self.pcitemcount = Entry(self.pcitems, width=4)
            self.pcitemcount.insert(0, str(self.sav.pcitemcount))
            self.pcitemcount.grid(row=26, column=2)

    def store_items(self):
        if self.items != None:
            if self.gen <= 2:
                for i in range(20):
                    self.sav.setitem(i, items.index(self.iclass[i]['selection']), int(self.icount[i].get()))

                self.sav.set('itemcount', self.itemcount.get())
            if self.gen >= 3:
                for i in range(163):
                    self.sav.setitem(i, items.index(self.iclass[i]['selection']), int(self.icount[i].get()))

            self.sav.refresh()

    def store_pokemon(self):
        if self.pokemon != None:
            if self.gen <= 2:
                self.sav.set('pokemoncount', self.pokecount.get())
                self.sav.refresh()

    def store_boxedit(self):
        if self.boxedit != None:
            if self.gen <= 2:
                self.sav.set('box%dpokemoncount' % self.curbox, self.boxpokecount.get())
                self.sav.refresh()

    def store_pokedex1(self):
        if self.pokedex1 != None:
            stop = 76
            if self.gen == 2:
                stop = 125
            if self.gen == 3:
                stop = 196
            for p in range(stop):
                self.sav.setpokedex(p + 1, self.dexseen[p].get(), self.dexcatched[p].get())

            self.sav.refresh()

    def store_pokedex2(self):
        if self.pokedex2 != None:
            start = 76
            stop = 151
            if self.gen == 2:
                start = 125
                stop = 251
            if self.gen == 3:
                start = 196
                stop = 386
            for p in range(start, stop):
                self.sav.setpokedex(p + 1, self.dexseen[p].get(), self.dexcatched[p].get())

            self.sav.refresh()

    def store_pcitems(self):
        if self.pcitems != None:
            for i in range(50):
                if self.gen <= 2:
                    self.sav.setitem(i + 20, items.index(self.pciclass[i]['selection']), int(self.pcicount[i].get()))
                if self.gen >= 3:
                    self.sav.setitem(i + 163, items.index(self.pciclass[i]['selection']), int(self.pcicount[i].get()))

            if self.gen <= 2:
                self.sav.set('pcitemcount', self.pcitemcount.get())
            self.sav.refresh()

    def store_pokeedit(self):
        if self.pokeedit != None:
            p = self.p
            b = self.b
            pkm = self.pkm
            snames = ['maxhp',
                      'attack',
                      'defense',
                      'speed',
                      'special']
            snames2 = snames[:]
            if self.gen == 2:
                snames2 = ['maxhp',
                           'attack',
                           'defense',
                           'speed',
                           'specialattack',
                           'specialdefense']
            if self.gen >= 3:
                snames = ['maxhp',
                          'attack',
                          'defense',
                          'speed',
                          'specialattack',
                          'specialdefense']
                snames2 = snames[:]
            if self.gen == 1 or b == None:
                pkm = self.sav.pkm_set(pkm, 'hp', int(self.curhp.get()))
            if self.gen == 1:
                pkm = self.sav.pkm_set(pkm, 'catchrate', int(self.catchrate.get()))
            else:
                pkm = self.sav.pkm_set(pkm, 'item', items.index(self.helditem['selection']))
                pkm = self.sav.pkm_set(pkm, 'pokerus', int(self.pokerus.get()))
                pkm = self.sav.pkm_set(pkm, 'happiness', int(self.happiness.get()))
                pkm = self.sav.pkm_set(pkm, 'caughtlocation', int(self.caughtlocation.get()))
                if self.gen == 2:
                    pkm = self.sav.pkm_set(pkm, 'caughttime', int(self.caughttime.get()))
                if self.gen >= 3:
                    pkm = self.sav.pkm_set(pkm, 'caughtball', int(self.caughtball.get()))
                pkm = self.sav.pkm_set(pkm, 'caughtlevel', int(self.caughtlevel.get()))
            pkm = self.sav.pkm_set(pkm, 'otnum', int(self.otnum.get()))
            if self.gen == 3:
                pkm = self.sav.pkm_set(pkm, 'pid', int(self.pid.get()))
                pkm = self.sav.pkm_set(pkm, 'secretid', int(self.secretid.get()))
            pkm = self.sav.pkm_set(pkm, 'exp', int(self.exp.get()))
            pkm = self.sav.pkm_set(pkm, 'otname', self.otname.get())
            pkm = self.sav.pkm_set(pkm, 'name', self.nickname.get())
            try:
                pkm = self.sav.pkm_set(pkm, 'num', pokemon.index(self.pokeclass['selection']))
            except:
                pkm = self.sav.pkm_set(pkm, 'num', pokemon_lower.index(self.pokeclass['selection'].lower()))

            if self.gen <= 2:
                try:
                    pkm = self.sav.pkm_set(pkm, 'sprite', pokemon.index(self.pokesprite['selection']))
                except:
                    pkm = self.sav.pkm_set(pkm, 'sprite', pokemon_lower.index(self.pokesprite['selection'].lower()))

            if self.gen == 1:
                pkm = self.sav.pkm_set(pkm, 'type1', types.index(self.type1['selection']))
                pkm = self.sav.pkm_set(pkm, 'type2', types.index(self.type2['selection']))
            if self.gen <= 2:
                if len(pkm) >= 67:
                    pkm = self.sav.pkm_set(pkm, 'curlevel', int(self.level.get()))
                else:
                    pkm = self.sav.pkm_set(pkm, 'level', int(self.level.get()))
            if self.gen >= 3:
                if len(pkm) >= 100:
                    pkm = self.sav.pkm_set(pkm, 'level', int(self.level.get()))
            if self.gen == 1 or b is None:
                pkm = self.sav.pkm_set(pkm, 'asleep', self.asleep.get())
                pkm = self.sav.pkm_set(pkm, 'poisoned', self.poisoned.get())
                pkm = self.sav.pkm_set(pkm, 'frozen', self.frozen.get())
                pkm = self.sav.pkm_set(pkm, 'paralyzed', self.paralyzed.get())
            for m in range(4):
                pkm = self.sav.pkm_set(pkm, 'move%d' % (m + 1), moves.index(self.moveclass[m]['selection']))
                pkm = self.sav.pkm_set(pkm, 'move%dpp' % (m + 1), int(self.movepp[m].get()))
                pkm = self.sav.pkm_set(pkm, 'move%dppup' % (m + 1), int(self.moveppup[m].get()))

            for s in range(len(snames2)):
                if s != 5 or self.gen == 3:
                    if s or self.gen == 3:
                        pkm = self.sav.pkm_set(pkm, '%siv' % snames[s], int(self.stativs[s].get()))
                    pkm = self.sav.pkm_set(pkm, '%sev' % snames[s], int(self.statevs[s].get()))
                if b == None:
                    if s != 5 or self.gen >= 2:
                        pkm = self.sav.pkm_set(pkm, snames2[s], int(self.statcur[s].get()))

            if self.gen >= 3:
                cnames = ['coolness',
                          'beauty',
                          'cuteness',
                          'smartness',
                          'toughness',
                          'feel']
                for s in range(len(cnames)):
                    pkm = self.sav.pkm_set(pkm, cnames[s], int(self.constat[s].get()))

            if b == None:
                self.sav.setpokemon(p, pkm)
            else:
                self.sav.setpcpokemon(b * self.bp + p, pkm)
            self.pkm = pkm
            self.sav.refresh()

    def wmdel_items(self):
        self.store_items()
        self.items.destroy()
        self.items = None

    def wmdel_boxes(self):
        self.boxes.destroy()
        self.boxes = None

    def wmdel_pcitems(self):
        self.store_pcitems()
        self.pcitems.destroy()
        self.pcitems = None

    def wmdel_pokedex1(self):
        self.store_pokedex1()
        self.pokedex1.destroy()
        self.pokedex1 = None

    def wmdel_pokedex2(self):
        self.store_pokedex2()
        self.pokedex2.destroy()
        self.pokedex2 = None

    def wmdel_pokeedit(self):
        self.store_pokeedit()
        self.pokeedit.destroy()
        self.sav.refresh()
        if self.b == None:
            if self.pokemon != None:
                self.wmdel_pokemon()
                self.show_pokemon()
            elif self.boxedit != None:
                if self.curbox == self.b:
                    self.wmdel_boxedit()
                    self.show_boxedit(self.curbox)
        self.pokeedit = None

    def wmdel_pokemon(self):
        if hasattr(self, 'swap'):
            del self.swap
        self.store_pokemon()
        self.pokemon.destroy()
        self.pokemon = None

    def wmdel_boxedit(self):
        if hasattr(self, 'swap'):
            del self.swap
        self.store_boxedit()
        self.boxedit.destroy()
        if self.boxes != None:
            self.wmdel_boxes()
            self.show_boxes()
        self.boxedit = None

    def show_pokemon(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.pokemon != None:
            self.pokemon.focus_force()
            return
        self.pokemon = Toplevel()
        self.pokemon.title('Party Pok\xc3\xa9mon - %s' % self.title)
        Label(self.pokemon, text='   ').grid(row=1000, column=1000)
        self.pokemon.protocol('WM_DELETE_WINDOW', self.wmdel_pokemon)
        Label(self.pokemon, text='', font=('Times', 4)).grid(row=0)
        for p in range(6):
            pclass = self.sav.pkm_get(self.sav.pokemon[p], 'sprite')
            plevel = self.sav.pkm_get(self.sav.pokemon[p], 'curlevel')
            Label(self.pokemon, text='    Pok\xc3\xa9mon %d' % (p + 1)).grid(row=p * 2 + 2, column=0, sticky=W)
            Label(self.pokemon, text='    Lv. %d    ' % plevel).grid(row=p * 2 + 2, column=1)
            Label(self.pokemon, text=pokemon[pclass] + '    ').grid(row=p * 2 + 2, column=2, sticky=W)
            Button(self.pokemon, text='Edit', width=6, command=lambda p=p: self.show_pokeedit(p)).grid(row=p * 2 + 2,
                                                                                                       column=3)
            Button(self.pokemon, text='Swap', width=6, command=lambda p=p: self.swap_pkm(p)).grid(row=p * 2 + 2,
                                                                                                       column=4)
            Button(self.pokemon, text='Delete', width=6, command=lambda p=p: self.delete_pkm(p)).grid(row=p * 2 + 2,
                                                                                                       column=5)
            if self.gen == 1:
                box_no = 12
                box_size = 20
            elif self.gen == 2:
                box_no = 14
                box_size = 20
            else:
                box_no = 14
                box_size = 30
            move = ComboBox(self.pokemon, label='Move: ', dropdown=1, editable=0, width=20, value='Party')
            move.insert(END, 'Party')
            for x in range(0, box_no):
                if self.sav.boxpokemoncount[x] < box_size:
                    move.insert(END, 'Box ' + str(x+1))
            move.grid(row=p * 2 + 2, column=6, sticky=Tkinter.W)

        if self.gen <= 2:
            Label(self.pokemon, text='', font=('Times', 4)).grid(row=13)
            Label(self.pokemon, text='    Pok\xc3\xa9mon #  (Pok\xc3\xa9mon in the party)').grid(row=14, columnspan=3,
                                                                                                 sticky=W)
            self.pokecount = Entry(self.pokemon, width=7)
            self.pokecount.insert(0, str(self.sav.pokemoncount))
            self.pokecount.grid(row=14, column=3)
        if self.gen <= 2:
            Label(self.pokemon, text='', font=('Times', 4)).grid(row=15)
            Button(self.pokemon, text='Import/Export', width=15, command=self.show_import).grid(row=14, column=6)

    def show_boxes(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.boxes != None:
            self.boxes.focus_force()
            return
        self.boxes = Toplevel()
        self.boxes.title('PC Boxes - %s' % self.title)
        Label(self.boxes, text='   ').grid(row=1000, column=1000)
        self.boxes.protocol('WM_DELETE_WINDOW', self.wmdel_boxes)
        Label(self.boxes, text='', font=('Times', 4)).grid(row=0)
        curbox = self.sav.currentbox
        for b in range(self.bn):
            boxnum = self.sav.boxpokemoncount[b]
            if b == curbox:
                Label(self.boxes, text='    Box %d (Selected)' % (b + 1)).grid(row=b * 2 + 2, column=0, sticky=W)
            else:
                Label(self.boxes, text='    Box %d' % (b + 1)).grid(row=b * 2 + 2, column=0, sticky=W)
            if self.gen < 3:
                Label(self.boxes, text='    %d / 20 Pok\xc3\xa9mon    ' % boxnum).grid(row=b * 2 + 2, column=1)
            else:
                Label(self.boxes, text='    %d / 30 Pok\xc3\xa9mon    ' % boxnum).grid(row=b * 2 + 2, column=1)
            Button(self.boxes, text='Edit', width=6, command=lambda b=b: self.show_boxedit(b)).grid(row=b * 2 + 2,
                                                                                                    column=3)

    def show_boxedit(self, b):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.boxedit != None:
            self.boxedit.focus_force()
            return
        self.curbox = b
        self.boxedit = Toplevel()
        self.boxedit.title('Box %d - %s' % (b + 1, self.title))
        if self.gen <= 2:
            menu = Menu(self.boxedit)
            menu_file = Menu(menu, tearoff=0)
            menu_file.add_command(label='Reorder & recount...', command=self.box_reorder)
            menu.add_cascade(label='Box %d management' % (b + 1), menu=menu_file)
            self.boxedit.configure(menu=menu)
        Label(self.boxedit, text='   ').grid(row=1000, column=1000)
        self.boxedit.protocol('WM_DELETE_WINDOW', self.wmdel_boxedit)
        Label(self.boxedit, text='', font=('Times', 4)).grid(row=0)
        plevel = 0
        for p in range(self.bp):
            pclass = self.sav.pkm_get(self.sav.pcpokemon[b * self.bp + p], 'sprite')
            if self.gen <= 2:
                plevel = self.sav.pkm_get(self.sav.pcpokemon[b * self.bp + p], 'level')
            Label(self.boxedit, text='    Pok\xc3\xa9mon %d' % (p + 1)).grid(row=p * 2 + 2, column=0, sticky=W)
            Label(self.boxedit, text='    Lv. %d    ' % plevel).grid(row=p * 2 + 2, column=1)
            text = '??????????'
            if pclass < len(pokemon):
                text = pokemon[pclass]
            Label(self.boxedit, text=text + '    ').grid(row=p * 2 + 2, column=2, sticky=W)
            Button(self.boxedit, text='Edit', width=6, command=lambda p=p: self.show_pokeedit(p, b)).grid(row=p * 2 + 2,
                                                                                                          column=3)
            Button(self.boxedit, text='Swap', width=6, command=lambda p=p: self.swap_pkm(p, b)).grid(row=p * 2 + 2,
                                                                                                       column=4)

            Button(self.boxedit, text='Delete', width=6, command=lambda p=p: self.delete_pkm(p, b)).grid(row=p * 2 + 2,
                                                                                                      column=5)
            if self.gen == 1:
                box_no = 12
                box_size = 20
            elif self.gen == 2:
                box_no = 14
                box_size = 20
            else:
                box_no = 14
                box_size = 30
            move = ComboBox(self.boxedit, label='Move: ', dropdown=1, editable=0, width=20, value='Party')
            move.insert(END, 'Party')
            for x in range(0, box_no):
                if self.sav.boxpokemoncount[x] < box_size:
                    move.insert(END, 'Box ' + str(x + 1))
            move.grid(row=p * 2 + 2, column=6, sticky=Tkinter.W)

            if self.gen <= 2:
                Label(self.boxedit, text='', font=('Times', 4)).grid(row=self.bp * 2 + 1)
                Label(self.boxedit, text='    Pok\xc3\xa9mon #  (Pok\xc3\xa9mon in the box)').grid(row=self.bp * 2 + 2,
                                                                                                   columnspan=3, sticky=W)
                self.boxpokecount = Entry(self.boxedit, width=7)
                self.boxpokecount.insert(0, str(self.sav.boxpokemoncount[b]))
                self.boxpokecount.grid(row=self.bp * 2 + 2, column=3)

    def box_reorder(self):
        if self.pokeedit != None:
            self.wmdel_pokeedit()
        if self.boxedit != None:
            self.wmdel_boxedit()
        b = self.curbox
        pkmlen = len(self.sav.pcpokemon[0])
        newbox = ''
        boxtrash = ''
        for p in range(self.bp):
            pkm = self.sav.pcpokemon[b * self.bp + p]
            if pkm[0] != chr(255) and pkm[0] != chr(0):
                newbox += pkm
            else:
                boxtrash += pkm

        pkmcount = len(newbox) / pkmlen
        newbox += boxtrash
        for p in range(self.bp):
            self.sav.setpcpokemon(b * self.bp + p, newbox[pkmlen * p:pkmlen * (p + 1)])

        self.sav.refresh()
        self.show_boxedit(b)
        self.boxpokecount.delete(0, END)
        self.boxpokecount.insert(0, pkmcount)
        self.boxedit.focus_force()

    def show_import(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        self.imp = Toplevel()
        Label(self.imp, text='', font=('Times', 4)).grid(row=0)
        team = Text(self.imp, height=30, width=100, font=('Consolas', 10))
        team.insert('1.0', self.get_pmkm_info())
        team.grid(row=1, columnspan=2)
        Label(self.imp, text='', font=('Times', 4)).grid(row=2)
        Button(self.imp, text='Continue', width=10,
               command=lambda team=team: self.show_choose_team_location(team.get('1.0', 'end-1c'))).grid(row=3)
        Button(self.imp, text="What's this?", width=10,
               command=lambda team=team: self.help_import()).grid(row=3, column=1)
        Label(self.imp, text='', font=('Times', 2)).grid(row=4)

    def show_choose_team_location(self, t):
        if self.sav is None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        pokemons = parse_exportable(t)
        if not pokemons:
            self.imp.focus_force()
            showerror('Something went wrong =(', 'Your exportable is not valid. Check it and try again.\nIf you copied'
                                                 ' correctly, perhaps one of your Pok\xc3\xa9mon\'s nickname has more'
                                                 ' than 10 characters?')
            return

        self.imp.destroy()
        if self.gen >= 2:
            box_no = 15
        else:
            box_no = 13
        self.choose = Toplevel()
        Label(self.choose, text='', font=('Times', 4)).grid(row=0)
        Label(self.choose, text='Please insert where you want the team(s) to be placed.   ').grid(row=1, column=1,
                                                                                                  columnspan=3)
        Label(self.choose, text='', font=('Times', 4)).grid(column=1)
        Label(self.choose, text='', font=('Times', 4)).grid(row=2)

        locations = {}

        for key, i in zip(pokemons, range(len(pokemons))):
            Label(self.choose, text=key).grid(row=3 + i * 2, column=1, sticky=Tkinter.W)
            locations[key] = ComboBox(self.choose, dropdown=1, editable=0, width=20, value='Party')
            locations[key].insert(END, 'Party')
            for x in range(1, box_no):
                locations[key].insert(END, 'Box ' + str(x))
            locations[key].grid(row=3 + i * 2, column=2, sticky=Tkinter.W)
            Label(self.choose, text='', font=('Times', 4)).grid(row=4 + i * 2)
        Button(self.choose, text='Save', width=10,
               command=lambda: self.save_teams(pokemons, locations)).grid(row=5 + len(pokemons) * 2, column=2,
                                                                          sticky=Tkinter.E)
        Label(self.choose, text='', font=('Times', 4)).grid(row=6 + len(pokemons) * 2)

    def help_import(self):
        showinfo("What's this?", 'With this, you can import your teams from simulators such as Pok\xc3\xa9mon Showdown!'
                                 ' for convenience (very useful if you do Wi-Fi battles). Just paste the exportable,'
                                 ' click Save and you\'re good to go. If you are having problems exporting, remember'
                                 ' that Pok\xc3\xa9mon names can\'t be longer than 10 characters. The number of'
                                 ' whitespaces between each part of the exportable matters, so don\'t change those. You'
                                 ' can import teams from anywhere, as long as they use the same format as'
                                 ' Pok\xc3\xa9mon Showdown!. Before clicking Save, remember to backup your party if you'
                                 ' want to use it later, because it will be wiped out entirely.')

    def show_pokeedit(self, p, b=None):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.pokeedit != None:
            self.pokeedit.focus_force()
            return
        self.pokeedit = Toplevel()
        self.add_pokeedit_menus()
        if b == None:
            pkm = self.sav.pokemon[p]
            self.pkm = pkm
            self.p = p
            self.b = None
            self.pokeedit.title('Party Pok\xc3\xa9mon %d - %s' % (p + 1, self.title))
        else:
            pkm = self.sav.pcpokemon[b * self.bp + p]
            self.pkm = pkm
            self.p = p
            self.b = b
            self.pokeedit.title('PC Box %d, Pok\xc3\xa9mon %d - %s' % (b + 1, p + 1, self.title))
        Label(self.pokeedit).grid()
        Label(self.pokeedit, text='   ').grid(row=1000, column=1000)
        self.pokeedit.protocol('WM_DELETE_WINDOW', self.wmdel_pokeedit)
        Label(self.pokeedit, text='    Pok\xc3\xa9mon Class:  ').grid(row=10, column=10, columnspan=10)
        Label(self.pokeedit, text='    Nickname:  ').grid(row=25, column=10, columnspan=10)
        Label(self.pokeedit, text='    OT Num / OT Name:  ').grid(row=10, column=30, columnspan=10)
        Label(self.pokeedit, text='    Level / Exp. Points:  ').grid(row=20, column=30, columnspan=10)
        self.otnum = Entry(self.pokeedit, width=6)
        self.otnum.insert(0, self.sav.pkm_get(pkm, 'otnum'))
        self.otnum.grid(row=10, column=40, columnspan=10)
        self.otname = Entry(self.pokeedit, width=10)
        self.otname.insert(0, self.sav.pkm_get(pkm, 'otname'))
        self.otname.grid(row=10, column=50, columnspan=10)
        if self.gen <= 2:
            Label(self.pokeedit, text='    Pok\xc3\xa9mon Sprite:  ').grid(row=20, column=10, columnspan=10)
        else:
            Label(self.pokeedit, text='    Personality / PID:  ').grid(row=20, column=10, columnspan=10, sticky=E)
            self.pidInt = IntVar()
            self.pidInt.set(self.sav.pkm_get(pkm, 'pid'))
            self.pidInt.trace('w', lambda name, index, mode: self.on_pid_change(name, index, mode))
            self.pid = Entry(self.pokeedit, width=22, textvariable=self.pidInt)
            self.pid.grid(row=20, column=20, columnspan=10)
        if self.gen >= 2:
            Label(self.pokeedit, text='    Held Item:  ').grid(row=23, column=10, columnspan=10)
            self.helditem = ComboBox(self.pokeedit, dropdown=1, editable=1, width=20,
                                     value=items[self.sav.pkm_get(pkm, 'item')])
            array = items * 1
            array.sort(reverse=False)
            for x in range(len(array)):
                if len(array[x]) > 4:
                    self.helditem.insert(END, array[x])

            self.helditem.grid(row=23, column=20, columnspan=10)
            if self.gen <= 2:
                Label(self.pokeedit, text='    Pok\xc3\xa9rus:  ').grid(row=25, column=30, columnspan=10)
            else:
                Label(self.pokeedit, text='    Pok\xc3\xa9rus / Secret ID:  ').grid(row=25, column=30, columnspan=10)
                self.secretid = Entry(self.pokeedit, width=10)
                self.secretid.insert(0, self.sav.pkm_get(pkm, 'secretid'))
                self.secretid.grid(row=25, column=50, columnspan=10)
            self.pokerus = Entry(self.pokeedit, width=6)
            self.pokerus.insert(0, self.sav.pkm_get(pkm, 'pokerus'))
            self.pokerus.grid(row=25, column=40, columnspan=10)
            if self.gen == 2:
                Label(self.pokeedit, text='    Caught zone / level / time:  ').grid(row=23, column=30, columnspan=10)
            if self.gen >= 3:
                Label(self.pokeedit, text='    Caught zone / level / Ball:  ').grid(row=23, column=30, columnspan=10)
            self.caughtlocation = Entry(self.pokeedit, width=6)
            self.caughtlocation.insert(0, self.sav.pkm_get(pkm, 'caughtlocation'))
            self.caughtlocation.grid(row=23, column=40, columnspan=10)
            self.caughtlevel = Entry(self.pokeedit, width=5)
            self.caughtlevel.insert(0, self.sav.pkm_get(pkm, 'caughtlevel'))
            self.caughtlevel.grid(row=23, column=50, columnspan=5)
        if self.gen == 2:
            self.caughttime = Entry(self.pokeedit, width=4)
            self.caughttime.insert(0, self.sav.pkm_get(pkm, 'caughttime'))
            self.caughttime.grid(row=23, column=55, columnspan=5)
        if self.gen >= 3:
            self.caughtball = Entry(self.pokeedit, width=4)
            self.caughtball.insert(0, self.sav.pkm_get(pkm, 'caughtball'))
            self.caughtball.grid(row=23, column=55, columnspan=5)
        self.level = Entry(self.pokeedit, width=6)
        if b == None:
            self.level.insert(0, self.sav.pkm_get(pkm, 'curlevel'))
        elif self.gen <= 2:
            self.level.insert(0, self.sav.pkm_get(pkm, 'level'))
        self.level.grid(row=20, column=40, columnspan=10)
        self.exp = Entry(self.pokeedit, width=10)
        self.exp.insert(0, self.sav.pkm_get(pkm, 'exp'))
        self.exp.grid(row=20, column=50, columnspan=10)
        self.nickname = Entry(self.pokeedit, width=22)
        self.nickname.insert(0, self.sav.pkm_get(pkm, 'name'))
        self.nickname.grid(row=25, column=20, columnspan=10)
        Label(self.pokeedit).grid(row=30)
        if self.gen == 1 or b == None:
            Label(self.pokeedit, text='    Curr. HP:  ').grid(row=40, column=10, columnspan=10, sticky=W)
            self.curhp = Entry(self.pokeedit, width=6)
            self.curhp.insert(0, self.sav.pkm_get(pkm, 'hp'))
            self.curhp.grid(row=40, column=10, columnspan=10, sticky=E)
        self.asleep = IntVar()
        self.poisoned = IntVar()
        self.paralyzed = IntVar()
        self.frozen = IntVar()
        if self.gen == 1 or b == None:
            Checkbutton(self.pokeedit, variable=self.asleep, text='SLP').grid(row=40, column=20, columnspan=5, sticky=E)
            if self.sav.pkm_get(pkm, 'asleep'):
                self.asleep.set(1)
            Checkbutton(self.pokeedit, variable=self.poisoned, text='PSN').grid(row=40, column=25, columnspan=5,
                                                                                sticky=E)
            if self.sav.pkm_get(pkm, 'poisoned'):
                self.poisoned.set(1)
            Checkbutton(self.pokeedit, variable=self.frozen, text='FRZ').grid(row=40, column=30, columnspan=5, sticky=E)
            if self.sav.pkm_get(pkm, 'frozen'):
                self.frozen.set(1)
            Checkbutton(self.pokeedit, variable=self.paralyzed, text='PAR').grid(row=40, column=35, columnspan=5,
                                                                                 sticky=E)
            if self.sav.pkm_get(pkm, 'paralyzed'):
                self.paralyzed.set(1)
        if self.gen == 1:
            Label(self.pokeedit, text='    Catch rate:').grid(row=40, column=40, columnspan=10, sticky=W)
            self.catchrate = Entry(self.pokeedit, width=6)
            self.catchrate.insert(0, self.sav.pkm_get(pkm, 'catchrate'))
            self.catchrate.grid(row=40, column=50, columnspan=10, sticky=W)
        else:
            Label(self.pokeedit, text='    Happiness:').grid(row=40, column=40, columnspan=10, sticky=W)
            self.happiness = Entry(self.pokeedit, width=6)
            self.happiness.insert(0, self.sav.pkm_get(pkm, 'happiness'))
            self.happiness.grid(row=40, column=50, columnspan=10, sticky=W)
        if self.gen == 1:
            Label(self.pokeedit, text='    Type1 / Type2:').grid(row=28, column=10, columnspan=10)
            self.type1 = ComboBox(self.pokeedit, dropdown=1, editable=1, value=types[self.sav.pkm_get(pkm, 'type1')])
            array = types * 1
            array.sort(reverse=False)
            self.type2 = ComboBox(self.pokeedit, dropdown=1, editable=1, value=types[self.sav.pkm_get(pkm, 'type2')])
            for x in range(256):
                if len(array[x]) > 4:
                    self.type1.insert(END, array[x])
                    self.type2.insert(END, array[x])

            self.type1.grid(row=28, column=20, columnspan=10, sticky=E)
            self.type2.grid(row=28, column=30, columnspan=10, sticky=E)
        self.pokeclass = ComboBox(self.pokeedit, dropdown=1, editable=1, width=20,
                                  command=lambda event: self.on_class_change(event),
                                  value=pokemon[self.sav.pkm_get(pkm, 'num')])
        if self.gen <= 2:
            self.pokesprite = ComboBox(self.pokeedit, dropdown=1, editable=1, width=20,
                                       value=pokemon[self.sav.pkm_get(pkm, 'sprite')])
        array = pokemon * 1
        array.sort(reverse=False)
        for x in range(len(array)):
            if len(array[x]) > 4:
                self.pokeclass.insert(END, array[x])
                if self.gen <= 2:
                    self.pokesprite.insert(END, array[x])

        self.pokeclass.grid(row=10, column=20, columnspan=10)
        if self.gen <= 2:
            self.pokesprite.grid(row=20, column=20, columnspan=10)

        self.moveclass = [None] * 4
        self.movepp = [None] * 4
        self.moveppup = [None] * 4
        Label(self.pokeedit).grid(row=50)
        for m in range(4):
            self.moveclass[m] = ComboBox(self.pokeedit, dropdown=1, editable=1, width=20,
                                         value=moves[self.sav.pkm_get(pkm, 'move%d' % (m + 1))])
            array = moves * 1
            array.sort(reverse=False)
            Label(self.pokeedit, text='Move %d:' % (m + 1)).grid(row=60 + 10 * m, column=10, columnspan=10)
            Label(self.pokeedit, text='PP / PP up:').grid(row=60 + 10 * m, column=30, columnspan=10)
            for x in range(256):
                if len(array[x]) > 4:
                    self.moveclass[m].insert(END, array[x])

            self.moveclass[m].grid(row=60 + 10 * m, column=20, columnspan=10)
            self.movepp[m] = Entry(self.pokeedit, width=6)
            self.movepp[m].insert(0, self.sav.pkm_get(pkm, 'move%dpp' % (m + 1)))
            self.movepp[m].grid(row=60 + 10 * m, column=40, columnspan=5)
            self.moveppup[m] = Entry(self.pokeedit, width=6)
            self.moveppup[m].insert(0, self.sav.pkm_get(pkm, 'move%dppup' % (m + 1)))
            self.moveppup[m].grid(row=60 + 10 * m, column=45, columnspan=5)

        Label(self.pokeedit).grid(row=100)
        Label(self.pokeedit, text='HP (Max.)').grid(row=110, column=20, columnspan=5)
        Label(self.pokeedit, text='Attack').grid(row=110, column=25, columnspan=5)
        Label(self.pokeedit, text='Defense').grid(row=110, column=30, columnspan=5)
        Label(self.pokeedit, text='Speed').grid(row=110, column=35, columnspan=5)
        if self.gen == 1:
            Label(self.pokeedit, text='Special').grid(row=110, column=40, columnspan=5)
        if self.gen > 1:
            Label(self.pokeedit, text='Special Att./Def.').grid(row=110, column=40, columnspan=10)
        Label(self.pokeedit, text='Individual values:   ').grid(row=120, column=10, columnspan=10, sticky=E)
        Label(self.pokeedit, text='Effort values:   ').grid(row=130, column=10, columnspan=10, sticky=E)
        if b == None:
            Label(self.pokeedit, text='Current values:   ').grid(row=140, column=10, columnspan=10, sticky=E)
        scol = 20
        snames = ['maxhp',
                  'attack',
                  'defense',
                  'speed',
                  'special']
        snames2 = ['maxhp',
                   'attack',
                   'defense',
                   'speed',
                   'specialattack',
                   'specialdefense']
        if self.gen == 1:
            snames2 = snames
        if self.gen >= 3:
            snames = snames2
        self.statevs = [None] * 6
        self.stativs = [None] * 6
        self.statcur = [None] * 6
        self.constat = [None] * 6
        for s in range(len(snames2)):
            if scol > 20 and s != 5 or self.gen >= 3:
                self.stativs[s] = Entry(self.pokeedit, width=6)
                self.stativs[s].insert(0, self.sav.pkm_get(pkm, '%siv' % snames[s]))
                self.stativs[s].grid(row=120, column=scol, columnspan=5)
            if s != 5 or self.gen >= 3:
                self.statevs[s] = Entry(self.pokeedit, width=6)
                self.statevs[s].insert(0, self.sav.pkm_get(pkm, '%sev' % snames[s]))
                self.statevs[s].grid(row=130, column=scol, columnspan=5)
            if b == None:
                self.statcur[s] = Entry(self.pokeedit, width=6)
                self.statcur[s].insert(0, self.sav.pkm_get(pkm, snames2[s]))
                self.statcur[s].grid(row=140, column=scol, columnspan=5)
            scol += 5

        if self.gen >= 3:
            cnames = ['coolness',
                      'beauty',
                      'cuteness',
                      'smartness',
                      'toughness',
                      'feel']

            self.changingPid = False
            pid = self.pidInt.get()
            self.natureInt = StringVar()
            self.natureInt.set(natures[pid % 25])
            self.gender = IntVar()
            gen_rate = 127
            for key in gender_rate:
                if key == self.sav.pkm_get(pkm, 'num'):
                    gen_rate = gender_rate[key]
                    break
            if gen_rate == 255 or (pid % 256) >= gen_rate:
                self.gender.set(0)
            else:
                self.gender.set(1)

            self.ability = IntVar()
            self.shiny = IntVar()
            p1 = pid / 65536
            p2 = pid % 65536
            if (p1 ^ p2 ^ self.sav.pkm_get(pkm, 'otnum') ^ self.sav.pkm_get(pkm, 'secretid')) < 8:
                self.shiny.set(0)
            else:
                self.shiny.set(1)
            Label(self.pokeedit).grid(row=150)
            Label(self.pokeedit, text='    Nature:  ').grid(row=160, column=10, columnspan=10)
            self.nature = ComboBox(self.pokeedit, dropdown=1, editable=1,
                                   command=lambda event: self.adjust_pid(event), variable=self.natureInt)
            self.nature.grid(row=160, column=20, columnspan=10, sticky=E)
            array = natures
            pkmn = pokemon[self.sav.pkm_get(pkm, 'num')]
            try:
                num = pokemon_lower_rs.index(pkmn.lower())
                if isinstance(pokemon_abilities[num], str):
                    self.ability.set(0)
                    abilities = (pokemon_abilities[num], pokemon_abilities[num])
                else:
                    abilities = (pokemon_abilities[num][0], pokemon_abilities[num][1])
                    self.ability.set(pid % 2)
            except:
                num = 0
                abilities = (0, 0)
            for i in range(len(array)):
                self.nature.insert(END, array[i])
            Label(self.pokeedit, text='   Gender:').grid(row=170, column=10, columnspan=10)

            if self.sav.pkm_get(pkm, 'num') in gender_rate:
                gr = gender_rate[self.sav.pkm_get(pkm, 'num')]
            else:
                gr = 127

            if gr == 255:
                Radiobutton(self.pokeedit, text='Genderless', variable=self.gender, value=0, command=self.adjust_pid) \
                    .grid(row=170, column=20, columnspan=2)
            elif gr == 254:
                Radiobutton(self.pokeedit, text='F', variable=self.gender, value=0, command=self.adjust_pid) \
                    .grid(row=170, column=20, columnspan=2)
            elif gr == 0:
                Radiobutton(self.pokeedit, text='M', variable=self.gender, value=0, command=self.adjust_pid) \
                    .grid(row=170, column=20, columnspan=2)
            else:
                Radiobutton(self.pokeedit, text='M', variable=self.gender, value=0, command=self.adjust_pid) \
                    .grid(row=170, column=20, columnspan=2)
                Radiobutton(self.pokeedit, text='F', variable=self.gender, value=1, command=self.adjust_pid) \
                    .grid(row=170, column=22, columnspan=2)
            Label(self.pokeedit, text=' Ability:').grid(row=170, column=35, columnspan=5)
            Radiobutton(self.pokeedit, text=abilities[0], variable=self.ability, value=0, command=self.adjust_pid) \
                .grid(row=170, column=40, sticky=W)
            if num == 0 or not isinstance(pokemon_abilities[num], str):
                Radiobutton(self.pokeedit, text=abilities[1], variable=self.ability, value=1, command=self.adjust_pid) \
                    .grid(row=170, column=45, sticky=W)
            Label(self.pokeedit, text='  Shiny:').grid(row=160, column=35, columnspan=5)
            Radiobutton(self.pokeedit, text='Yes', variable=self.shiny, value=0, command=self.adjust_pid) \
                .grid(row=160, column=40, sticky=W)
            Radiobutton(self.pokeedit, text='No', variable=self.shiny, value=1, command=self.adjust_pid) \
                .grid(row=160, column=45, sticky=W)

            Label(self.pokeedit).grid(row=180)
            Label(self.pokeedit, text='Contest values:   ').grid(row=200, column=10, columnspan=10, sticky=E)
            Label(self.pokeedit, text='Coolness').grid(row=190, column=20, columnspan=5)
            Label(self.pokeedit, text='Beauty').grid(row=190, column=25, columnspan=5)
            Label(self.pokeedit, text='Cuteness').grid(row=190, column=30, columnspan=5)
            Label(self.pokeedit, text='Smartness').grid(row=190, column=35, columnspan=5)
            Label(self.pokeedit, text='Toughness').grid(row=190, column=40, columnspan=5)
            Label(self.pokeedit, text='Feel').grid(row=190, column=45, columnspan=5)
            scol = 20
            for s in range(len(cnames)):
                self.constat[s] = Entry(self.pokeedit, width=6)
                self.constat[s].insert(0, self.sav.pkm_get(pkm, '%s' % cnames[s]))
                self.constat[s].grid(row=200, column=scol, columnspan=5)
                scol += 5

    def show_pokedex1(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.pokedex1 != None:
            self.pokedex1.focus_force()
            return
        self.pokedex1 = Toplevel()
        self.pokedex1.title('Pok\xc3\xa9dex 1/2 - %s' % self.title)
        self.pokedex1.protocol('WM_DELETE_WINDOW', self.wmdel_pokedex1)
        Label(self.pokedex1, text='   ').grid(row=1000, column=1000)
        start = 0
        stop = 76
        step = 4
        if self.gen == 2:
            start = 0
            stop = 125
            step = 5
        if self.gen == 3:
            start = 0
            stop = 196
            step = 7
        for p in range(step):
            Label(self.pokedex1, text=' S').grid(row=0, column=1 + 3 * p, sticky=W)
            Label(self.pokedex1, text=' C').grid(row=0, column=2 + 3 * p, sticky=W)

        for p in range(start, stop):
            Label(self.pokedex1, text='    ' + pokedex[p + 1]).grid(row=p // step + 1, column=p % step * 3, sticky=W)
            self.dexseen[p] = IntVar()
            var = IntVar()
            Checkbutton(self.pokedex1, variable=var).grid(row=p // step + 1, column=p % step * 3 + 1, sticky=W)
            self.dexseen[p] = var
            del var
            var = IntVar()
            Checkbutton(self.pokedex1, variable=var).grid(row=p // step + 1, column=p % step * 3 + 2, sticky=W)
            self.dexcatched[p] = var
            del var
            if self.sav.catched[p + 1]:
                self.dexcatched[p].set(1)
            if self.sav.seen[p + 1]:
                self.dexseen[p].set(1)

    def show_pokedex2(self):
        if self.sav == None:
            showerror('Something went wrong =(', 'You need to load a .sav first')
            return
        if self.pokedex2 != None:
            self.pokedex2.focus_force()
            return
        self.pokedex2 = Toplevel()
        self.pokedex2.title('Pok\xc3\xa9dex 2/2 - %s' % self.title)
        self.pokedex2.protocol('WM_DELETE_WINDOW', self.wmdel_pokedex2)
        Label(self.pokedex2, text='   ').grid(row=1000, column=1000)
        start = 76
        stop = 151
        step = 4
        if self.gen == 2:
            start = 125
            stop = 251
            step = 5
        if self.gen == 3:
            start = 196
            stop = 386
            step = 7
        for p in range(step):
            Label(self.pokedex2, text=' S').grid(row=0, column=1 + 3 * p, sticky=W)
            Label(self.pokedex2, text=' C').grid(row=0, column=2 + 3 * p, sticky=W)

        for p in range(start, stop):
            Label(self.pokedex2, text='    ' + pokedex[p + 1]).grid(row=(p - start) // step + 1, column=p % step * 3,
                                                                    sticky=W)
            self.dexseen[p] = IntVar()
            var = IntVar()
            Checkbutton(self.pokedex2, variable=var).grid(row=(p - start) // step + 1, column=p % step * 3 + 1,
                                                          sticky=W)
            self.dexseen[p] = var
            del var
            var = IntVar()
            Checkbutton(self.pokedex2, variable=var).grid(row=(p - start) // step + 1, column=p % step * 3 + 2,
                                                          sticky=W)
            self.dexcatched[p] = var
            del var
            if self.sav.catched[p + 1]:
                self.dexcatched[p].set(1)
            if self.sav.seen[p + 1]:
                self.dexseen[p].set(1)

    def show_about(self):
        showinfo('About PikaSav', "Made by Ritchie. I'm cool. Yes, you're cool too.")

    def show_savinfo(self):
        if self.sav == None:
            showinfo('SAV Info', 'There is no .sav file loaded.')
        else:
            showinfo('SAV Info', 'Handler: %s\n- Sav filesize: %d\n- %d bytes loaded' % (
                self.sav.version, os.path.getsize(self.sav.file), len(self.sav.buffer)))

    def on_class_change(self, event):
        if self.gen == 3:
            try:
                self.reload_pkm()
            except AttributeError:
                return
            except TclError:
                return


pikasav = PikaSav()
