SOURCE_FNAME = 'true_events.txt'
TARGET_FNAME = 'true_events{}.txt'


def read_out(source_fname, target_fname, lim=1000):

    def write_in(indexed_fname):
        ind = 0
        with open(indexed_fname, 'wb') as target_handler:
            while ind < lim:
                ind += 1
                try:
                    target_handler.write(next(source_handler))
                except StopIteration:
                    return True

    iteration = 0
    with open(source_fname, 'rb') as source_handler:
        while True:
            iteration += 1
            end = write_in(target_fname.format(iteration))
            if end:
                break


if __name__ == '__main__':
    read_out(SOURCE_FNAME, TARGET_FNAME)
