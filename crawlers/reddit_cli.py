import argparse

parser = argparse.ArgumentParser(description="Get threads of reddit that have more than N points (default 5k points).")
parser.add_argument(
    dest="subreddits",
    help="<REQUIRED> List of subreddits separated by ;"
)
parser.add_argument(
    "points", "--n",
    dest='points', 
    help="Minimum of points that a reddit thread should have to be listed.",
    default=5000,
    type=int
)

args = parser.parse_args()
subreddits = args.subreddits.split(';')
minimum_points = args.points
