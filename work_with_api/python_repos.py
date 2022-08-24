import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# Store API response in a variable
response_dict = r.json()
print("Total repositories: {}".format(response_dict['total_count']))
print(response_dict.keys())

# Explore info about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned: {}".format(len(repo_dicts)))

# Examine the first repository.
repo_dict = repo_dicts[0]
# print("\nRepository Keys: {0}\n".format(len(repo_dict)))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print("""
#     Name: {0}
#     Owner: {1}
#     Stars: {2}
#     Repository: {3}
#     Created: {4}
#     Updated: {5}
#     Description: {6}"""
#           .format(repo_dict['name'],
#                   repo_dict['owner']['login'],
#                   repo_dict['stargazers_count'],
#                   repo_dict['html_url'],
#                   repo_dict['created_at'],
#                   repo_dict['updated_at'],
#                   repo_dict['description']))
