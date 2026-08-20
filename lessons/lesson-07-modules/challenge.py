import random 
import sys

def parse_args(argv):
    args = sys.argv[1:]
    count = 0
    names = []
    seed = None
    
    if "--seed" == args[0]:
        seed = int(args[1]) # seed value is set after --seed, so that it is the second index in args
        count = int(args[2])
        names = args[3:]
    else:
        count = args[0]
        names = args[1:]
        
    return names, count, seed

def pick(names, count, seed=None):
    if seed is not None:
        random.seed(seed)
        
    return random.sample(names, count)

def print_winners(winners):
    print("=== winners ===")
    print('\n'.join(f"{i+1}. {winner}" for i, winner in enumerate(winners)))

def main():
    argv = sys.argv
    
    if len(argv) < 3:
        return
    
    names, count, seed = parse_args(argv)
    
    if count < len(names):
        return
    
    winners = pick(names, count, seed)
    print_winners(winners)
    return

if __name__ == "__main__":
    main()