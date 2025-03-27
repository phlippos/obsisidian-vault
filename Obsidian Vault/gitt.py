from github import Github
import sys
def upload_md_to_github(token, username, repository_name, file_path, file_content):
    # Authenticate with GitHub using personal access token
    g = Github(token)
    
    try:
        # Get the user
        user = g.get_user(username)
        # Get the repository
        repo = user.get_repo(repository_name)
        
        # Create a new file in the repository
        contents = repo.get_contents(file_path)
        existing_content = contents.decoded_content.decode("utf-8")
        
        # Compare content
        if existing_content == file_content:
            print(f"File {file_path} is already up to date in {repository_name}. No update needed.")
            return
        
        # Create a new file in the repository
        repo.create_file(file_path, "Upload from script", file_content)
        
        print(f"Successfully uploaded {file_path} to {repository_name}!")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    # GitHub access token (generate one from GitHub)
    token = "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"
    # Your GitHub username
    username = "phlippos"
    # Name of the repository where you want to upload the file
    repository_name = "Obsidian"
    # Path to the Markdown file you want to upload
    file_path = sys.argv[1]
    
    # Read the content of the Markdown file
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
    
    # Upload the Markdown file to GitHub
    upload_md_to_github(token, username, repository_name, file_path, file_content)

