from pick_choice import pick_choice
from improv import improv

def main():
    choice_list = ["improv", "songs"]
    choice = pick_choice(choice_list);
    if choice == "improv":
        improv();
    elif choice == "songs":
        pass;

main()
