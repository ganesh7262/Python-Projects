
def input_names(name):
    with open(r"100 days of python\projects\mail_merger\names.txt", mode="a") as name_file:
        name_file.write(f"\n{name}")
    




with open(r'100 days of python\projects\mail_merger\names.txt') as data:
    r=data.read()
    for name in r.split():
        with open(fr"100 days of python\projects\mail_merger\letters\{name}.txt",mode='w') as letters:
            letters.write(f"hello {name} how are you")