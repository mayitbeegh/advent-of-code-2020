import re
def part_one(passports):
    return len(list(filter(check_required_fields_exist, passports)))

def check_required_fields_exist(passport):
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(passport)

def filter_byr_iyr_eyr(passport):
    return 1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030

def filter_hgt(passport):
    if 'cm' in passport['hgt']:
        return 150 <= int(passport['hgt'][:-2]) <= 193
    elif 'in' in passport['hgt']:
        return 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        return False

assert filter_hgt({'hgt':'149cm'}) == False
assert filter_hgt({'hgt':'150cm'}) == True
assert filter_hgt({'hgt':'58in'}) == False
assert filter_hgt({'hgt':'59in'}) == True

def filter_hcl(passport):
    return re.fullmatch(r'#[0-9|a-f]{6}', passport['hcl']) != None

assert filter_hcl({'hcl':'#123abc'}) == True
assert filter_hcl({'hcl':'123abc'}) == False
assert filter_hcl({'hcl':'#123ab'}) == False
assert filter_hcl({'hcl':'#123abg'}) == False

def filter_ecl(passport):
    return passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

assert filter_ecl({'ecl':'amb'}) == True
assert filter_ecl({'ecl':'wht'}) == False

def filter_pid(passport):
    return re.fullmatch(r'[0-9]{9}', passport['pid']) != None

assert filter_pid({'pid':'000000001'}) == True
assert filter_pid({'pid':'0123456789'}) == False



def part_two(passports):
    return len(list(filter(lambda x: all(f(x) for f in [check_required_fields_exist, filter_byr_iyr_eyr, filter_ecl, filter_hcl, filter_hgt, filter_pid]), passports)))

def preprocess(raw_input):
    return [{f.split(':')[0]:f.split(':')[1] for f in t.split()} for t in raw_input.split('\n\n')]

test_inputs = preprocess("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""")

test_inputs_2 = preprocess("""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""")

test_inputs_3 = preprocess("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""")

assert part_one(test_inputs) == 2
assert part_two(test_inputs_2) == 0
assert part_two(test_inputs_3) == 4
with open('day4.input') as f:
    passports = preprocess(f.read())

    print(part_one(passports))
    print(part_two(passports))