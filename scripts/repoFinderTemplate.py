# generated with the help of Chat GPT

from github import Github

# Replace <YOUR_GITHUB_ACCESS_TOKEN> with your actual GitHub access token
g = Github("Github_API_Token")

batch_size = 490

# Replace the placeholders in the repositories list with the owner and name of each repository you want to analyze
repositories = [
    #{"owner": "GodotECS", "name": "godex"},
    #{"owner": "skypjack", "name": "entt"},
    {"owner": "SanderMertens", "name": "flecs"},
    #{"owner": "sschmid", "name": "Entitas"},
    #{"owner": "Ubpa", "name": "UECS"},

    #{"owner": "godotengine", "name": "godot"},
    #{"owner": "pixijs", "name": "pixijs"},
    #{"owner": "BabylonJS", "name": "Babylon.js"},
    #{"owner": "OpenDiablo2", "name": "OpenDiablo2"},
    #{"owner": "minetest", "name": "minetest"},
    # Add more repositories here as needed
]

# Open a file for writing the results
with open("results.txt", "w") as f:
    for repo_info in repositories:
        # Retrieve the repository object using the owner and name information
        repo = g.get_repo(f"{repo_info['owner']}/{repo_info['name']}")

        # Initialize counters for number of commits and file changes
        num_commits = 0
        num_file_changes = 0
        num_fix_commits = 0
        num_file_changes_in_fix_commits = 0

        commits = repo.get_commits()

        # Iterate over all commits in the repository
        for commit in repo.get_commits()[0:batch_size]:
            num_commits += 1

            # Check if the commit message contains the word "Fix" or Bug
            if "fix" in commit.commit.message.lower() or "bug" in commit.commit.message.lower():
                num_fix_commits += 1

                # Iterate over all files changed in the commit
                for file in commit.files:
                    num_file_changes_in_fix_commits += file.changes
                    num_file_changes += file.changes
                
                continue

            # Iterate over all files changed in the commit
            for file in commit.files:
                num_file_changes += file.changes

        # Write the results for the current repository to the file
        f.write(f"Results for {repo_info['owner']}/{repo_info['name']}:\n")
        f.write(f"Number of commits: {num_commits}\n")
        f.write(f"Number of file changes: {num_file_changes}\n")
        f.write(f"Number of fix commits: {num_fix_commits}\n")
        f.write(f"Number of file changes in fix commits: {num_file_changes_in_fix_commits}\n\n")
