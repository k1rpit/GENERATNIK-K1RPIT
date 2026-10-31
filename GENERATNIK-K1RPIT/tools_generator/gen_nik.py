import random
import uuid

basic_int = list(range(1000))
basic_world = ["Aurora", "Canyon", "Comet", "Dawn", "Dusk", "Eclipse", "Fern", "Frost", "Horizon", "Mist", "Ocean", "Oasis", "Rain", "Ridge", "Storm", "Summit", "Valley", "Willow", "Century", "Echo", "Era", "Infinity", "Journey", "Mirage", "Moment", "Orbit", "Rhythm", "Shadow", "Silence", "Solitude", "Spark", "Zenith", "Amber", "Canvas", "Compass", "Crystal", "Marble", "Melody", "Neon", "Novella", "Poem", "Quartz", "Sable", "Sapphire", "Symphony", "Velvet", "Essence", "Grace", "Illusion", "Legacy"]

years = list(range(1939,2002))
name_real = ['Oliver', 'Evelyn', 'Arthur', 'Hazel', 'Jasper', 'Conrad', 'Ilse', 'Milo', 'Greta', 'Ansel', 'Gintaras', 'Gabija', 'Linus', 'Egle', 'Mantas', 'Eino', 'Aino', 'Otso', 'Lumi', 'Ilmari', 'Dragos', 'Sorina', 'Ciprian', 'Doina', 'Lucian', 'Zoran', 'Vesna', 'Milan', 'Danica', 'Luka']

gamer_words = [
"pixel", "glitch", "vortex", "cyber", "phantom", "specter", "wraith", "nexus","matrix", "vector", "binary", "kernel", "daemon", "proxy", "shadow", "ghost","void", "null", "apex", "zenith", "quantum", "neon", "crypto", "static","buffer", "packet", "shell", "socket", "beacon", "bypass", "cipher", "macro","syntax", "hertz", "pulse", "hazard", "toxic", "rogue", "rebel", "titan","alpha", "omega", "delta", "radar", "sonar", "laser", "plasma", "alpha","omega", "frenzy"
]
adjectives = [
"silent", "hidden", "secret", "latent", "crypto", "broken", "frozen", "bitter","hollow", "savage", "vivid", "liquid", "solid", "atomic", "cosmic", "solar","lunar", "astral", "hybrid", "neural", "digital", "analog", "remote", "masked","blind"
]
cool_int = list(range(3000,9999))

def gen_basic(*,world=basic_world,int_=basic_int) -> str:
    random_world = random.choice(world);random_int=random.choice(int_)
    return f'{random_world}{random_int}'

def gen_anon() -> str:
    uuid_str = str(uuid.uuid4())[::random.randint(3,6)]
    random_int=random.randint(0,9)
    random_hex_more=hex(random.randint(10,100))

    uuid_str = uuid_str.replace(str(random_int),str(random_hex_more))
    uuid_list = list(uuid_str)[::-1]
    uuid_str = "".join(uuid_list)
    return uuid_str


def gen_real(*,year=years,name=name_real) -> str:
    random_year = random.choice(year);random_name = random.choice(name)
    return f'{random_name}{random_year}'

def gen_game(*,world=gamer_words,djectives=adjectives,cool_int=cool_int) -> str:
    random_world = random.choice(world);random_djectives = random.choice(djectives);random_int = random.choice(cool_int)
    return f'{random_world}_{random_djectives}{random_int}'
print(gen_game())