r = [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
o = [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
t = [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
ra = [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
Dr = [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
s = [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]
h = [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]
g = [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]
m = [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]
ros = [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]
dog = [1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018]
p = [1923, 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019]

year = int(input("Enter your birth year: "))

if year := r:
    print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
elif year := o:
    print("Your Chinese Zodiac Sign is : Ox (牛 / Niú")
elif year := t:
    print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
elif year := ra:
    print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
elif year := Dr:
    print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
elif year := s:
    print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")
elif year := h:
    print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")
elif year := g:
    print("Your Chinese Zodiac Sign is :  Goat (羊 / Yáng)")
elif year := m:
    print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
elif year := ros:
    print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
elif year := dog:
    print("Your Chinese Zodiac Sign is :  Dog (狗 / Gǒu)")
elif year := p:
    print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")
else:
    print("Invalid Year, it should not be earlier than 1900")

