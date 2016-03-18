from viterbi import VitebiAlgorithm
from hmm import get_hmm

observations = ('normal', 'cold', 'dizzy')


def main():
	hmm = get_hmm()
	result = VitebiAlgorithm(hmm, observations).get_result()
	print 'result', result



if __name__ == '__main__':
	main()