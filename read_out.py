FNAME_OUT = 'true_events.txt'
FNAME_IN = 'true_events{}.txt'


def read_out(fname_out, fname_in, lim=1000):

    def write_in(indexed_fname):
        ind = 0
        with open(indexed_fname, 'wb') as in_handler:
            while ind < lim:
                ind += 1
                try:
                    in_handler.write(next(out_handler))
                except StopIteration:
                    return True

    iteration = 0
    with open(fname_out, 'rb') as out_handler:
        while True:
            iteration += 1
            end = write_in(fname_in.format(iteration))
            if end:
                break

    
if __name__ == '__main__':
    read_out(FNAME_OUT, FNAME_IN)
