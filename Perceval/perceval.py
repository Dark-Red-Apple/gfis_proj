import argparse

from perceval.backends.core.github import GitHub

# Parse command line arguments
parser = argparse.ArgumentParser(
    description = "Simple parser for GitHub issues and pull requests"
    )
parser.add_argument("-t", "--token",
                    '--nargs', nargs='+',
                    help = "GitHub token")
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo'")
args = parser.parse_args()

# Owner and repository names
(owner, repo) = args.repo.split('/')
print(args.token)
# create a Git object, pointing to repo_url, using repo_dir for cloning
repo = GitHub(owner=owner, repository=repo, api_token=args.token)
# fetch all issues/pull requests as an iterator, and iterate it printing
# their number, and whether they are issues or pull requests
for item in repo.fetch(category='issue'):
    print(item['data']['url'])
