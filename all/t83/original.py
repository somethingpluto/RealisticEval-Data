def change_turn(self):  # change_turn written by ChatGPT 3.5
    if len(self.order) <= 1:
        # No need to shift for lists with 0 or 1 elements
        pass
    else:
        # Store the first element in a temporary variable
        first_element = self.order[0]

        # Loop through the list and shift each element to the left
        for i in range(len(self.order) - 1):
            self.order[i] = self.order[i + 1]

        # Assign the first element to the last position
        self.order[-1] = first_element