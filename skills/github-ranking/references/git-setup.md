# Git Setup for oss-radar

## Authentication Options

### Option A: HTTPS + Personal Access Token (Recommended)

1. Create a token at https://github.com/settings/tokens
   - Scope: `public_repo` (for public repos) or `repo` (for private)
2. Configure git credential helper:

```bash
# macOS (stores in keychain)
git config --global credential.helper osxkeychain

# Linux (stores in file)
git config --global credential.helper store

# Windows
git config --global credential.helper manager
```

3. Trigger first pull/push, enter username + token (saved automatically):

```bash
git pull
# Username: your-github-username
# Password: <paste token>
```

### Option B: SSH Key

```bash
# Generate key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
# Paste ~/.ssh/id_ed25519.pub

# Change remote URL
git remote set-url origin git@github.com:shouyuandong/oss-radar.git
```

## Obsidian Git Plugin Notes

- Obsidian Git plugin uses commit-and-sync (commit + pull + push)
- Token is needed even for pull-only usage (plugin may trigger push)
- Mobile (iOS/Android) does NOT support SSH — must use HTTPS + token
- Configure auto-pull interval (30 min recommended)

## Git Identity

```bash
git config user.email "your@email.com"
git config user.name "Your Name"
```

## Remote URL with Token (for sandbox/CI)

```bash
git remote set-url origin https://<username>:<token>@github.com/<username>/oss-radar.git
```

> ⚠️ Token in URL is visible in `.git/config`. For shared environments, use credential helper instead.
