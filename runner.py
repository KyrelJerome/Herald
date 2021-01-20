import argparse
from bot import PostBot

def setup():
    parser = argparse.ArgumentParser(description='Submit Advertisement sets to public accounts.')

    parser.add_argument('credential_yaml_path', metavar='c', type=str, nargs='1', help='Path to credential yaml file.')
    parser.add_argument('--post', metavar='p', type=str, nargs='+', help='Path to text and image files for the post.')

    parser.add_argument('--discord', dest='discord', type=str, const=True, default=False)
    parser.add_argument('--twitter', dest='twitter', type=str, const=True, default=False)
    parser.add_argument('--instagram', dest='instagram', type=str, const=True, default=False)
    parser.add_argument('--insta_stories', dest='insta_stories', type=str, const=True, default=False)
    return parser.parse_args()

def parse_credentials():
    return {
        'discord': 'password',
        'twitter': 'password',
        'instagram': 'instagram',
        'facebook': 'facebook',
        'email': 'email'
    }

def run_bots(args):
    if args.discord:
        credentialParser
        DiscordBot(args.creden)
        # name Wall E
    elif args.twitter:
        raise NotImplementedError
    elif args.instagram:
        raise NotImplementedError
    elif args.insta_stories:
        NotImplementedError


if __name__ == '__main__':
    args = parse()
    run_bots(args)