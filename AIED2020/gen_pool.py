import argparse
from isomorphic import gen_pool_brds

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A utility to generate a big pool of brds for fraction arithmetic')
    parser.add_argument('-n',
    					default=100,
                        help="The number of files to generate.")
    parser.add_argument('-dir',
    					default="pool",
                        help="The datashop transaction file to use.")
    parser.add_argument('-mpd',
    					default="mass_production",
                        help="The datashop transaction file to use.")

    args = parser.parse_args()


    gen_pool_brds(args.n, args.dir, args.mpd)