# Tier 1: The Literal Assistant
# A literal machine only does what it is told, with exact items, amounts and
# conditions. Nothing is guessed. Every step is explicit.

def run():
    kitchen = {
        "eggs_in_fridge": 6,
        "eggs_in_hand": 0,
        "eggs_in_bowl": 0,
        "eggs_cooked": 0,
        "burner_on": False,
        "pan_on_burner": False,
        "plate_on_table": False,
        "pan_in_sink": False,
    }

    def step(number, text):
        print(f"Step {number}: {text}")

    step(1, "Go to the kitchen and stand in front of the fridge.")

    step(2, "Take 2 eggs from the fridge.")
    kitchen["eggs_in_fridge"] -= 2
    kitchen["eggs_in_hand"] = 2

    step(3, "Take a non-stick frying pan and put it on the front left burner.")
    kitchen["pan_on_burner"] = True

    step(4, "Crack both eggs into a small bowl. Throw the shells in the bin.")
    kitchen["eggs_in_bowl"] = kitchen["eggs_in_hand"]
    kitchen["eggs_in_hand"] = 0

    step(5, "Add a pinch of salt and beat with a fork for 20 seconds.")

    step(6, "Turn the burner to medium heat and add 1 tablespoon of oil.")
    kitchen["burner_on"] = True

    step(7, "Wait 1 minute for the pan to heat up.")

    step(8, "Pour the eggs into the pan.")

    step(9, "Stir gently every 10 seconds until no liquid egg is visible (about 2 minutes).")
    kitchen["eggs_cooked"] = kitchen["eggs_in_bowl"]
    kitchen["eggs_in_bowl"] = 0

    step(10, "Turn off the burner.")
    kitchen["burner_on"] = False

    step(11, "Slide the eggs onto a plate, put the plate on the table, place a fork next to it.")
    kitchen["plate_on_table"] = True

    step(12, "Put the pan in the sink.")
    kitchen["pan_in_sink"] = True
    kitchen["pan_on_burner"] = False

    # How do we know the task is finished? We check it, we don't assume it.
    finished = (
        kitchen["plate_on_table"]
        and kitchen["eggs_cooked"] == 2
        and not kitchen["burner_on"]
        and kitchen["pan_in_sink"]
    )
    print()
    print("Task finished:", finished)
    print("Eggs left in fridge:", kitchen["eggs_in_fridge"])


if __name__ == "__main__":
    run()
