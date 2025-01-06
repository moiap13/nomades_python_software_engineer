#!/bin/bash

validate_pse_version() {
    if [[ ! "$1" =~ ^(pse|wpr|ppl)_2025_[0-1][0-9][0-1][0-9]$ ]]; then
        echo "Invalid PSE version. It should be in the format 'pse_2025_xxyy' where xx and yy are digits from 01 to 12."
        exit 1
    fi
}

# Check if exactly two arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <YOUR_GITHUB_REPO_FOR_THE_COURSE> <GITHUB_COURSE_REPO> <PSE_VERSION>"
    exit 1
fi

# Validate the PSE version
validate_pse_version "$3"

USER_GITHUB_REPO="$1"
COURSE_GITHUB_REPO="$2"
PSE_VERSION="$3"

# Detect Windows home directory for the current user in WSL
NOMADES_DIR="$HOME/Documents/nomades"

# Ensure the target directory exists
mkdir -p "$NOMADES_DIR"
cd "$NOMADES_DIR" || exit

# Adding the SSH key to the ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/"$PSE_VERSION"

# Clone the repository
git clone "$USER_GITHUB_REPO" "$PSE_VERSION"

# Change directory to the cloned repository
cd "$PSE_VERSION" || exit

# Add template course for materials
git remote add course "$COURSE_GITHUB_REPO"

# Fetch the course materials
git pull course "$PSE_VERSION"
git push

echo "Setup completed successfully in $NOMADES_DIR"