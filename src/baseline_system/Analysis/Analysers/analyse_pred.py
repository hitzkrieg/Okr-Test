"""
Receives the validation set and the test set, runs the baseline system for proposition extraction,
and prints analysis logs of propositions

Author: Hitesh Golchha
"""

import sys

sys.path.append('../../../common')
sys.path.append('../../../agreement')
sys.path.append('../..')



from okr import *
from docopt import docopt
from eval_predicate_mention import *
from prop_extraction import prop_extraction


def main():
    """
    Receives the validation set and the test set, runs the baseline system for proposition extraction,
    and prints analysis logs of propositions. You can manually redirect the standard output to a file as 
    convenient.
    """
    args = docopt("""Receives the validation set and the test set, runs the baseline systems,
    and prints analysis logs of propositions
    

    Usage:
        analyse_pred.py <val_set_folder>

        <val_set_folder> = the validation set file
        
    """)

    val_folder = args['<val_set_folder>']
    
    # Load the annotation files to OKR objects
    val_graphs = load_graphs_from_folder(val_folder)

    # Load a common proposition extraction model
    logging.debug('Loading proposition extraction module')
    prop_ex = prop_extraction()

    logging.debug('Running analysis of predicates')
    # Run the predicate mentions component and evaluate them
    analyse_predicate_mentions(val_graphs, prop_ex, '../../nominalizations/nominalizations.reuters.txt')



if __name__ == '__main__':
    main()
