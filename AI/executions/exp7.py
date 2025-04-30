def monkey_banana():
    # Initial positions
    monkey_pos = 'A'
    box_pos = 'B'
    monkey_status = 'on_floor'
    banana_pos = 'C'  # Removed extra 'r'

    actions = []

    # Step 1: Move to box
    if monkey_pos != box_pos:
        actions.append(f"Go({box_pos})")
        monkey_pos = box_pos

    # Step 2: Push box to banana position
    if monkey_pos == box_pos:  # This condition was redundant, simplified
        actions.append(f"Push(Box, {banana_pos})")
        box_pos = banana_pos
        monkey_pos = banana_pos

    # Step 3: Climb on box
    if monkey_pos == box_pos and monkey_status == 'on_floor':
        actions.append("Climb(Box)")
        monkey_status = 'on_box'

    # Step 4: Grasp banana
    if monkey_pos == banana_pos and box_pos == banana_pos and monkey_status == 'on_box':
        actions.append("Grasp")
        monkey_status = 'has_banana'

    # Final state
    if monkey_status == 'has_banana':
        actions.append("Goal Reached: Monkey has the banana!")

    return actions

# Run the simulation
steps = monkey_banana()

# Print the steps
print("Plan to get the banana:")
for step in steps:
    print(step)
