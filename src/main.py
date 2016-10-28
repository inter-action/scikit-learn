from nlp import term_frequency
from nlp import tf_idf

def main():
    # term_frequency.test_fr()
    tf_idf.run()
     

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
