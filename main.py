from cli import parse_args
import os

args = parse_args()
if args.env:
 os.environ["APP_ENV"] = args.env
# else: