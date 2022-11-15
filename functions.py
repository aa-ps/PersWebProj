def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]