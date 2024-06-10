# =================================================================================================#
# Constants for working with de440s file ,
# and converting ephemerides to HD , FD , Astro and Numerology info
# =================================================================================================#

PATHTODIR: str = "files/"
FILENAME: str = "de440s.bsp"
FILENAME_NODES: str = "nodes.json"
EXPECTEDSHA512: str = "a244335d9eddc1e4fd2f3f8ddabf360020f650bc8fca2c4e7e0f66018db7fd2691dd63f52e3652653e096d97ad74cd48c10b4587a4d5a9bb68dbae5cecf06449"
FILELENGTH: int = 32726016
SIZEOFREC: int = 1024
SEGMENT_START_TIME = -4734072000  # de440s.bsp
SEGMENT_LAST_TIME = 4735368000  # de440s.bsp
TOTAL_SUMMARIES_NUMBER: int = 14  # de440s.bsp

AU = 0.1495978707e9  # km 149597870.7

SEC_IN_1_DAY: int = 86400

MED_EPS: float = 0.4090928042223289
MIN_EPS = 0.38571776469074687
MAX_EPS = 0.4276056667386107


SSB: int = 0
MERCURY: int = 1
VENUS: int = 2
EARTH: int = 3
MARS: int = 4
JUPITER: int = 5
SATURN: int = 6
URANUS: int = 7
NEPTUNE: int = 8
PLUTO: int = 9
SUN: int = 10
MOON: int = 11
NORTHNODE: int = 12
SOUTHNODE: int = 13
HIRON: int = 14

HEAD: int = 0
AJNA: int = 1
THROAT: int = 2
G: int = 3
SACRAL: int = 4
ROOT: int = 5
EGO: int = 6
SPLEEN: int = 7
EMO: int = 8

NUMBEROFGATES: int = 65  # from 1 to 64
NUMBEROFCHANNELS: int = 37  # from 1 to 36
NUMBEROFPLANETS: int = 14
NUMBEROFCENTERS: int = 9

# Earth Barycenter (3) -> Moon (301)
MOONtoEARTH = 301
EARTH_NOT_BARYCENTER = 399
MERCURY_NOT_BARYCENTER = 199
VENUS_NOT_BARYCENTER = 299

"""
degrees = radians*(180/pi)
radians = degrees*(pi/180)
"""

SEC_TO_RAD: float = 4.8481368110953599359e-6
# 1 Radians is equal to Degrees : 57.29577951308232 = 180/math.pi
DEGREE_RATIO = 57.29577951308232
RAD_TO_DEG: float = 5.7295779513082320877e1
# 1 Radians is equal to Arcseconds : 206264.80624709636 = 180*3600/pi
RAD_PER_ARCSECONDS = 4.8481368110953599359e-6  # STR radians per arc second

JD2000 = 2451545.0  # 12:00 UT on January 1, 2000
JD1950 = 2433282.5

PI = 3.14159265358979324
# 1 Degrees is equal to Radians : 0.017453292519943295
RAD_RATIO = 0.017453292519943295

# 88 градусов = 1.535889741755
RAD_88_DEGREES = 1.53588974175500991848

# Солнце проходит за день 1 градус, берем для верности 1.3
# за 1 секунду Солнце проходит 0.000015046296296296297 градусов или 0.0000002626074106009986440 радиана
# (1.535889741755/7689600).toFixed(20) =  0.00000019973597349082
MED_SUN_PATH_IN_1_SEC = 0.000000199

# время, за которое Солнце проходит 88 градусов
# 7_718_038.91 секунд
SEC_FOR_88_DEGREES_SUN = RAD_88_DEGREES / MED_SUN_PATH_IN_1_SEC


"""	
according to tests
7_714_285.72 sec = 88 degrees
and deviation is +- 3.044 days == 263001.6 seconds

"""


# 359 deg converted to radians
# const _359_DEG_IN_RAD = 6.26574

# размер одной гексаграммы в десятичных градусах
# const one_hex_in_dec = 5.625

# размер одной линии в десятичных градусах
oneLineInDec = 0.9375

# размер одного цвета в десятичных градусах
oneColorInDec = 0.15625

# размер одного тона в десятичных градусах
oneToneInDec = 0.026041666666666668

# размер одной базы в десятичных градусах
oneBaseInDec = 0.005208333333333334

hexSortByDeg = [
    # from 3.875 to 9.49
    [17, [3.875, 9.5]],
    [21, [9.5, 15.125]],
    [51, [15.125, 20.75]],
    [42, [20.75, 26.375]],
    [3, [26.375, 32.0]],
    [27, [32.0, 37.625]],
    [24, [37.625, 43.25]],
    [2, [43.25, 48.875]],
    [23, [48.875, 54.5]],
    [8, [54.5, 60.125]],
    [20, [60.125, 65.75]],
    [16, [65.75, 71.375]],
    [35, [71.375, 77.0]],
    [45, [77.0, 82.625]],
    [12, [82.625, 88.25]],
    [15, [88.25, 93.875]],
    [52, [93.875, 99.5]],
    [39, [99.5, 105.125]],
    [53, [105.125, 110.75]],
    [62, [110.75, 116.375]],
    [56, [116.375, 122.0]],
    [31, [122.0, 127.625]],
    [33, [127.625, 133.25]],
    [7, [133.25, 138.875]],
    [4, [138.875, 144.5]],
    [29, [144.5, 150.125]],
    [59, [150.125, 155.75]],
    [40, [155.75, 161.375]],
    [64, [161.375, 167.0]],
    [47, [167.0, 172.625]],
    [6, [172.625, 178.25]],
    [46, [178.25, 183.875]],
    [18, [183.875, 189.5]],
    [48, [189.5, 195.125]],
    [57, [195.125, 200.75]],
    [32, [200.75, 206.375]],
    [50, [206.375, 212.0]],
    [28, [212.0, 217.625]],
    [44, [217.625, 223.25]],
    [1, [223.25, 228.875]],
    [43, [228.875, 234.5]],
    [14, [234.5, 240.125]],
    [34, [240.125, 245.75]],
    [9, [245.75, 251.375]],
    [5, [251.375, 257.0]],
    [26, [257.0, 262.625]],
    [11, [262.625, 268.25]],
    [10, [268.25, 273.875]],
    [58, [273.875, 279.5]],
    [38, [279.5, 285.125]],
    [54, [285.125, 290.75]],
    [61, [290.75, 296.375]],
    [60, [296.375, 302.0]],
    [41, [302.0, 307.625]],
    [19, [307.625, 313.25]],
    [13, [313.25, 318.875]],
    [49, [318.875, 324.5]],
    [30, [324.5, 330.125]],
    [55, [330.125, 335.75]],
    [37, [335.75, 341.375]],
    [63, [341.375, 347.0]],
    [22, [347.0, 352.625]],
    [36, [352.625, 358.25]],
    [25, [358.25, 3.875]],
]

planetsNumbers = {
    1: "mercury",  # 7,01° (относительно эклиптики)
    2: "venus",  # 3,39458° (относительно эклиптики)
    3: "earth",
    4: "mars",  # 1,85061° (относительно эклиптики)
    5: "jupiter",  # 1,304° (относительно эклиптики)
    6: "saturn",  # 2,485 240° (относительно эклиптики)
    7: "uranus",  # 0,772556° (относительно эклиптики)
    8: "neptune",  # 1,767975° (относительно эклиптики)
    9: "pluto",  # 17°,14 (относительно эклиптики)
    10: "sun",
    11: "moon",  # 5,14° (относительно эклиптики)
    12: "north_node",
    13: "south_node",
    14: "hiron",
}

# zodiac names from 0 to 11
zodiacNames = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]


# для каждого знака зодиака определяется сила планеты
# поиск идет от 6 к 0, берется первое найденное


"""	
   сила идет по порядку массива
  # [0,1,2,3,4,5,6]
  # 6 - обитель
  # 5 - экзальтация
  # 4 - родство, дружба
  # 3 - нейтрально
  # 2 - вражда
  # 1 - падение
  # 0 - изгнание
"""
planetsPower = [
    [
        # Aries
        ["venus"],
        ["saturn"],
        ["mercury", "uranus"],
        ["moon"],
        ["jupiter", "neptune"],
        ["sun"],
        ["mars", "pluto"],
    ],
    # Taurus
    [
        ["mars", "pluto"],
        ["uranus"],
        ["jupiter", "neptune"],
        ["sun"],
        ["mercury", "saturn"],
        ["moon"],
        ["venus"],
    ],
    # Gemini
    [
        ["jupiter", "neptune"],
        ["hiron"],
        ["sun", "mars", "pluto"],
        ["moon"],
        ["venus", "saturn", "uranus"],
        ["mercury"],
        ["mercury"],
    ],
    # Cancer
    [
        ["saturn", "uranus"],
        ["mars"],
        ["mercury", "venus"],
        ["sun"],
        ["neptune", "pluto"],
        ["jupiter"],
        ["moon"],
    ],
    # Leo
    [
        ["saturn", "uranus"],
        ["neptune"],
        ["mercury", "venus"],
        ["moon"],
        ["jupiter", "mars"],
        ["pluto"],
        ["sun"],
    ],
    # Virgo
    [
        ["jupiter", "neptune"],
        ["venus"],
        ["mars", "pluto", "moon"],
        ["sun"],
        ["saturn", "uranus"],
        ["mercury"],
        ["mercury"],
    ],
    # Libra
    [
        ["mars", "pluto"],
        ["sun"],
        ["jupiter", "neptune"],
        ["moon"],
        ["mercury", "uranus"],
        ["saturn"],
        ["venus"],
    ],
    # Scorpio
    [
        ["venus"],
        ["moon"],
        ["mercury", "saturn"],
        ["sun"],
        ["jupiter", "neptune"],
        ["uranus"],
        ["mars", "pluto"],
    ],
    # Sagittarius
    [
        ["mercury"],
        ["mercury"],
        ["saturn", "uranus", "venus"],
        ["moon"],
        ["mars", "pluto", "sun"],
        ["hiron"],
        ["jupiter", "neptune"],
    ],
    # Capricorn
    [
        ["moon"],
        ["jupiter"],
        ["neptune", "pluto"],
        ["sun"],
        ["mercury", "venus"],
        ["mars"],
        ["saturn", "uranus"],
    ],
    # Aquarius
    [
        ["sun"],
        ["pluto"],
        ["jupiter", "mars"],
        ["moon"],
        ["mercury", "venus"],
        ["neptune"],
        ["saturn", "uranus"],
    ],
    # Pisces
    [
        ["mercury"],
        ["mercury"],
        ["saturn", "uranus"],
        ["sun"],
        ["mars", "pluto", "moon"],
        ["venus"],
        ["jupiter", "neptune"],
    ],
]

"""
# массив с названиями планет в том порядке, в котором они находятся в файле de430.bsp
# +после 11 номера идут дополнительные планеты
"""
planetsArr = [
    "ssb",
    "mercury",
    "venus",
    "earth",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "pluto",
    "sun",
    "moon",
    "north_node",
    "south_node",
    "hiron",
]


DE440s = {
    "path": "..\\..\\files\\de440s.bsp",
    "MIN_DATA": -4734072000.0,
    "MAX_DATA": 4735368000.0,
    "RECLEN": 1024,
}


Nodes_file = {
    "path": "..\\..\\files\\nodes_file.json",
}

"""
File type DAF/SPK and format LTL-IEEE with 14 segments:
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Mercury Barycenter (1)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Venus Barycenter (2)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Earth Barycenter (3)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Mars Barycenter (4)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Jupiter Barycenter (5)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Saturn Barycenter (6)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Uranus Barycenter (7)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Neptune Barycenter (8)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Pluto Barycenter (9)
2396752.50..2506352.50  Type 2  Solar System Barycenter (0) -> Sun (10)
2396752.50..2506352.50  Type 2  Earth Barycenter (3) -> Moon (301)
2396752.50..2506352.50  Type 2  Earth Barycenter (3) -> Earth (399)
2396752.50..2506352.50  Type 2  Mercury Barycenter (1) -> Mercury (199)
2396752.50..2506352.50  Type 2  Venus Barycenter (2) -> Venus (299)
"""


# Year, Seconds
type DeltaTTableStructure = tuple[int, float]

# [-4733494022,"north"],[-4732252235,"south"]
type NodesJsonStruct = tuple[int, str]
