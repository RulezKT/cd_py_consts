# =================================================================================================#
# Constants for working with de440s file ,
# and converting ephemerides to HD , FD , Astro and Numerology info
# =================================================================================================#
AU = 0.1495978707e9  # km 149597870.7

SEC_IN_1_DAY: int = 86400


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
MOONtoEARTH: int = 301
EARTH_NOT_BARYCENTER: int = 399
MERCURY_NOT_BARYCENTER: int = 199
VENUS_NOT_BARYCENTER: int = 299

"""
degrees = radians*(180/pi)
radians = degrees*(pi/180)
"""

SEC_TO_RAD: float = 4.8481368110953599359e-6
# 1 Radians is equal to Degrees : 57.29577951308232 = 180/math.pi
DEGREE_RATIO = 57.29577951308232
RAD_TO_DEG: float = 5.7295779513082320877e1
# 1 Radians is equal to Arcseconds : 206264.80624709636 = 180*3600/pi
RAD_PER_ARCSECONDS: float = 4.8481368110953599359e-6  # STR radians per arc second

JD2000: float = 2451545.0  # 12:00 UT on January 1, 2000
JD1950: float = 2433282.5

# 1 Degrees is equal to Radians : 0.017453292519943295
RAD_RATIO: float = 0.017453292519943295

# 88 градусов = 1.535889741755
RAD_88_DEGREES: float = 1.53588974175500991848

# med speed of sun is around 1 degree in a day, we'll take 1.3
# in 1 second it is  0.000015046296296296297 гof degree
# or 0.0000002626074106009986440 RAD
# (1.535889741755/7689600).toFixed(20) =  0.00000019973597349082
MED_SUN_PATH_IN_1_SEC: float = 0.000000199

# time for the sun to go through 88 degrees
# 7_718_038.91 seconds
SEC_FOR_88_DEGREES_SUN: float = RAD_88_DEGREES / MED_SUN_PATH_IN_1_SEC
"""	
according to tests
7_714_285.72 sec = 88 degrees
and deviation is +- 3.044 days == 263001.6 seconds

"""

# 359 deg converted to radians
# const _359_DEG_IN_RAD = 6.26574

# size of 1 hex in degrees
one_hex_in_dec: float = 5.625

# line
oneLineInDec: float = 0.9375

# color
oneColorInDec: float = 0.15625

# tone
oneToneInDec: float = 0.026041666666666668

# base
oneBaseInDec: float = 0.005208333333333334

hexSortByDeg: tuple[int, tuple[float, float]] = (
    # from 3.875 to 9.49
    (17, (3.875, 9.5)),
    (21, (9.5, 15.125)),
    (51, (15.125, 20.75)),
    (42, (20.75, 26.375)),
    (3, (26.375, 32.0)),
    (27, (32.0, 37.625)),
    (24, (37.625, 43.25)),
    (2, (43.25, 48.875)),
    (23, (48.875, 54.5)),
    (8, (54.5, 60.125)),
    (20, (60.125, 65.75)),
    (16, (65.75, 71.375)),
    (35, (71.375, 77.0)),
    (45, (77.0, 82.625)),
    (12, (82.625, 88.25)),
    (15, (88.25, 93.875)),
    (52, (93.875, 99.5)),
    (39, (99.5, 105.125)),
    (53, (105.125, 110.75)),
    (62, (110.75, 116.375)),
    (56, (116.375, 122.0)),
    (31, (122.0, 127.625)),
    (33, (127.625, 133.25)),
    (7, (133.25, 138.875)),
    (4, (138.875, 144.5)),
    (29, (144.5, 150.125)),
    (59, (150.125, 155.75)),
    (40, (155.75, 161.375)),
    (64, (161.375, 167.0)),
    (47, (167.0, 172.625)),
    (6, (172.625, 178.25)),
    (46, (178.25, 183.875)),
    (18, (183.875, 189.5)),
    (48, (189.5, 195.125)),
    (57, (195.125, 200.75)),
    (32, (200.75, 206.375)),
    (50, (206.375, 212.0)),
    (28, (212.0, 217.625)),
    (44, (217.625, 223.25)),
    (1, (223.25, 228.875)),
    (43, (228.875, 234.5)),
    (14, (234.5, 240.125)),
    (34, (240.125, 245.75)),
    (9, (245.75, 251.375)),
    (5, (251.375, 257.0)),
    (26, (257.0, 262.625)),
    (11, (262.625, 268.25)),
    (10, (268.25, 273.875)),
    (58, (273.875, 279.5)),
    (38, (279.5, 285.125)),
    (54, (285.125, 290.75)),
    (61, (290.75, 296.375)),
    (60, (296.375, 302.0)),
    (41, (302.0, 307.625)),
    (19, (307.625, 313.25)),
    (13, (313.25, 318.875)),
    (49, (318.875, 324.5)),
    (30, (324.5, 330.125)),
    (55, (330.125, 335.75)),
    (37, (335.75, 341.375)),
    (63, (341.375, 347.0)),
    (22, (347.0, 352.625)),
    (36, (352.625, 358.25)),
    (25, (358.25, 3.875)),
)

planetsNumbers: dict[int, str] = {
    1: "mercury",  # 7,01° to ecliptic
    2: "venus",  # 3,39458°
    3: "earth",
    4: "mars",  # 1,85061°
    5: "jupiter",  # 1,304°
    6: "saturn",  # 2,485 240°
    7: "uranus",  # 0,772556°
    8: "neptune",  # 1,767975°
    9: "pluto",  # 17°,14
    10: "sun",
    11: "moon",  # 5,14°
    12: "north_node",
    13: "south_node",
    14: "hiron",
}


pl_names: tuple[str] = (
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
)

# zodiac names from 0 to 12
zodiacNames: tuple[str] = (
    "",
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
)


# planets power acoording to zodiac
# from 6 to 0, first match is taken
"""	
  # [0,1,2,3,4,5,6]
  # 6 - tenement
  # 5 - exaltation
  # 4 - kinship, friendship
  # 3 - neutral
  # 2 - enmity
  # 1 - fall
  # 0 - exile
"""
planetsPower: tuple[tuple[tuple[str]]] = (
    (
        # Aries
        ("venus",),
        ("saturn",),
        ("mercury", "uranus"),
        ("moon",),
        ("jupiter", "neptune"),
        ("sun",),
        ("mars", "pluto"),
    ),
    # Taurus
    (
        ("mars", "pluto"),
        ("uranus",),
        ("jupiter", "neptune"),
        ("sun",),
        ("mercury", "saturn"),
        ("moon",),
        ("venus",),
    ),
    # Gemini
    (
        ("jupiter", "neptune"),
        ("hiron",),
        ("sun", "mars", "pluto"),
        ("moon",),
        ("venus", "saturn", "uranus"),
        ("mercury",),
        ("mercury",),
    ),
    # Cancer
    (
        ("saturn", "uranus"),
        ("mars",),
        ("mercury", "venus"),
        ("sun",),
        ("neptune", "pluto"),
        ("jupiter",),
        ("moon",),
    ),
    # Leo
    (
        ("saturn", "uranus"),
        ("neptune",),
        ("mercury", "venus"),
        ("moon",),
        ("jupiter", "mars"),
        ("pluto",),
        ("sun",),
    ),
    # Virgo
    (
        ("jupiter", "neptune"),
        ("venus",),
        ("mars", "pluto", "moon"),
        ("sun",),
        ("saturn", "uranus"),
        ("mercury",),
        ("mercury",),
    ),
    # Libra
    (
        ("mars", "pluto"),
        ("sun",),
        ("jupiter", "neptune"),
        ("moon",),
        ("mercury", "uranus"),
        ("saturn",),
        ("venus",),
    ),
    # Scorpio
    (
        ("venus",),
        ("moon",),
        ("mercury", "saturn"),
        ("sun",),
        ("jupiter", "neptune"),
        ("uranus",),
        ("mars", "pluto"),
    ),
    # Sagittarius
    (
        ("mercury",),
        ("mercury",),
        ("saturn", "uranus", "venus"),
        ("moon",),
        ("mars", "pluto", "sun"),
        ("hiron",),
        ("jupiter", "neptune"),
    ),
    # Capricorn
    (
        ("moon",),
        ("jupiter",),
        ("neptune", "pluto"),
        ("sun",),
        ("mercury", "venus"),
        ("mars",),
        ("saturn", "uranus"),
    ),
    # Aquarius
    (
        ("sun",),
        ("pluto",),
        ("jupiter", "mars"),
        ("moon",),
        ("mercury", "venus"),
        ("neptune",),
        ("saturn", "uranus"),
    ),
    # Pisces
    (
        ("mercury",),
        ("mercury",),
        ("saturn", "uranus"),
        ("sun",),
        ("mars", "pluto", "moon"),
        ("venus",),
        ("jupiter", "neptune"),
    ),
)
