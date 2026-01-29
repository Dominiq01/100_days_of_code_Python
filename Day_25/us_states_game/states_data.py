import pandas

class StatesData:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.states_list = self.data["state"].to_list()

    def get_state_coords(self, state_name):
        state_data = self.data[self.data.state == state_name]
        state_coords = (state_data.x.item(), state_data.y.item())
        return state_coords