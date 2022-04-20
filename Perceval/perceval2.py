import argparse

from perceval.backends.core.github import GitHub

parser = argparse.ArgumentParser(
    description = "Simple parser for GitHub issues and pull requests"
    )
parser.add_argument("-t", "--token",
                    '--nargs', nargs='+',
                    help = "GitHub token")
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo'")
args = parser.parse_args()

# create a Git object, pointing to repo_url, using repo_dir for cloning
repo = GitHub(owner='grimoirelab', repository='perceval', api_token=['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'])
# fetch all issues/pull requests as an iterator, and iterate it printing
# their number, and whether they are issues or pull requests
for item in repo.fetch(category='issue'):
    print(item['data']['url'])