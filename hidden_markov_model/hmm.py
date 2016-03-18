hidden_states_set = ('Healthy', 'Fever')
observations_set = ('normal', 'cold', 'dizzy')
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
transition_probability = {
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
}
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}


class HMM(object):
	def __init__(self, hidden_states_set, observations_set, start_probabilities, transition_probabilities, emission_probabilities):
		self.hidden_states_set = hidden_states_set
		self.observations_set = observations_set
		self.start_probabilities = start_probabilities
		self.transition_probabilities = transition_probabilities
		self.emission_probabilities = emission_probabilities

	def get_start_probability(self, state):
		return self.start_probabilities.get(state)

	def get_transsition_probability(self, pre_state, cur_state):
		return self.transition_probabilities.get(pre_state, {}).get(cur_state)

	def get_emission_probability(self, state, observation):
		return self.emission_probabilities.get(state, {}).get(observation)



def get_hmm():
	return HMM(hidden_states_set, observations_set, start_probability, transition_probability, emission_probability)
