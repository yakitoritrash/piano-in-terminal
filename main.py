import inquirer

def main():
    options = ['improv', 'songs']
    questions = [inquirer.List('choice', message='Pick a choice', choices = options)]
    answers = inquirer.prompt(questions) # {'choice': 'improv'}
    print(answers)
main();
