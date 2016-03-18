class VitebiAlgorithm(object):
    def __init__(self, hmm, observations):
        self.hmm = hmm
        self.observations = observations

    def get_result(self):
        observations = self.observations
        hmm = self.hmm
        hidden_states_set = hmm.hidden_states_set
        dp_max_probs = []
        dp_step_trace = []
        # dp_dic: {'state_2': {'p': 0.4, 'trace': ['state_1', 'state_2']}}
        # iterately update dp_dic
        for i in range(len(observations)):
            observation = observations[i]
            dp_max_probs_dic = {}
            dp_step_trace_dic = {}
            if i == 0:
                for state in hidden_states_set:
                    start_p = hmm.get_start_probability(state)
                    emission_p = hmm.get_emission_probability(state, observation)
                    dp_max_probs_dic[state] = start_p * emission_p
                    dp_step_trace_dic[state] = None
            else:
                for state in hidden_states_set:
                    max_p, max_pre_state = None, None
                    for pre_state in hidden_states_set:
                        pre_p = dp_max_probs[i-1][pre_state]
                        transition_p = hmm.get_transsition_probability(pre_state, state)
                        tmp_p = pre_p * transition_p
                        if max_p is None:
                            max_p = tmp_p
                            max_pre_state = pre_state
                        elif tmp_p > max_p:
                            max_p = tmp_p
                            max_pre_state = pre_state

                    # update new_dp_dic
                    emission_p = hmm.get_emission_probability(state, observation)
                    dp_max_probs_dic[state] = max_p * emission_p
                    dp_step_trace_dic[state] = max_pre_state

            dp_max_probs.append(dp_max_probs_dic)
            dp_step_trace.append(dp_step_trace_dic)

        # find out the most probable one in dp_dic
        arr = sorted(dp_max_probs[-1].items(), key=lambda t: t[1], reverse=True)
        print dp_max_probs
        print dp_step_trace
        last_state = arr[0][0]
        # back trace hidden state
        hidden_states = [last_state]
        state_trace = last_state
        for i in range(len(observations)-1, 0, -1):
            hidden_states.append(dp_step_trace[i][state_trace])
            state_trace = dp_step_trace[i][state_trace]

        hidden_states = list(reversed(hidden_states))
        return hidden_states
