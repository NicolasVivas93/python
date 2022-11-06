import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]

verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]

adjectives = ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]

prepositions = ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]

adverbs = ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]

noun = [random.choice(nouns) for i in range(3)]
print(noun)

verb = [random.choice(verbs) for i in range(3)]
print(verb)

adjec = [random.choice(adjectives) for i in range(3)]
print(adjec)

prep = [random.choice(prepositions) for i in range(2)]
print(prep)

adv = random.choice(adverbs)
print(adv)

def es_vocal(lista):
    vocales = ['a','e','i','o','u']
    if lista[0][0] in vocales:
        return True
    else:
        return False

article = ''

if es_vocal(adjec) == True:
    article = 'An'
else:
    article = 'A'

print(f"""
{article} {adjec[0]} {noun[0]}

{article} {adjec[0]} {noun[0]} {verb[0]} {prep[0]} the {adjec[1]} {noun[1]} 
{adv}, the {noun[0]} {verb[1]}
the {noun[1]} {verb[2]} {prep[1]} a {adjec[2]} {noun[2]}
""")