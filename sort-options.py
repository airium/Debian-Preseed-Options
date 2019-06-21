class Option():

    def __init__(self):
        self.comments = []
        self.commands = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_command(self, command):
        self.commands.append(command)

    def getlines(self):
        return self.comments + self.commands

    def __lt__(self, option):
        return self.commands[0].lower() < option.commands[0].lower()



if __name__ == '__main__':
    with open('preseed-raw.cfg', encoding='utf-8') as file:
        lines = file.readlines()

    print(len(lines))
    options = []
    last_is_comment = False
    for line in lines:
        if line[0] == '#' and not last_is_comment:
            last_is_comment = True
            options.append(Option())
            options[-1].add_comment(line)
            continue
        if line[0] == '#' and last_is_comment:
            options[-1].add_comment(line)
            continue
        if line[0] != '#' and last_is_comment:
            last_is_comment = False
            options[-1].add_command(line)
            continue
        if line[0] != '#' and not last_is_comment:
            options[-1].add_command(line)
            continue

    with open('preseed.cfg', 'w', encoding='utf-8') as file:
        for option in sorted(options):
            file.writelines(option.getlines())
