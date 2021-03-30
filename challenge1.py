#!/usr/bin/env python3
char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }
value = heroes[char_name][char_stat]

print(char_name + "'s" + char_stat + " is " value
print(char_name + "'s" + char_stat + " is " value
