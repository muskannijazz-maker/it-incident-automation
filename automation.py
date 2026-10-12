def recommend_action(priority):
    if priority == "P1":
        return "Immediate alert to IT operations team"

    elif priority == "P2":
        return "Create an investigation task"

    else:
        return "Schedule a routine check"
    