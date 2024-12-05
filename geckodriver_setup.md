If you're getting a "command not found" error when checking the version of `geckodriver`, it means the installation may not have completed correctly, or the system PATH is not set properly. Here’s how to troubleshoot and fix it:

### 1. **Ensure geckodriver is installed**

#### On Ubuntu:
If you're using Ubuntu or any Debian-based system, you can check if `geckodriver` is installed by running:

```bash
which geckodriver
```

This will give you the path where `geckodriver` is installed. If no output is returned, the installation didn't work. In that case, you can try reinstalling `geckodriver`:

```bash
sudo apt update
sudo apt install firefox-geckodriver
```

#### On macOS:
If you're using macOS, you can check if `geckodriver` is installed by running:

```bash
which geckodriver
```

If no path is returned, reinstall `geckodriver` using Homebrew:

```bash
brew install geckodriver
```

#### On Windows:
If you're on Windows, check whether `geckodriver` is in your PATH:

1. Open Command Prompt (`cmd`) and type:

```bash
where geckodriver
```

If it’s not found, you’ll need to manually add it to your PATH or ensure that you placed the `geckodriver.exe` file in a directory listed in your PATH.

### 2. **Manually set PATH (if needed)**

If `geckodriver` is installed but not recognized, you may need to add it to your PATH manually.

#### On Linux/MacOS:
Add `geckodriver` to your PATH by editing the `.bashrc` or `.zshrc` file (depending on your shell):

```bash
nano ~/.bashrc  # Or ~/.zshrc for Zsh users
```

Add the following line to the end of the file, replacing the path with the actual directory where `geckodriver` is installed:

```bash
export PATH=$PATH:/path/to/geckodriver
```

Then reload the file:

```bash
source ~/.bashrc  # Or source ~/.zshrc for Zsh
```

#### On Windows:
1. Open **System Properties** (Right-click on This PC > Properties > Advanced system settings).
2. Click on **Environment Variables**.
3. In the "System variables" section, find the **Path** variable, click **Edit**, and add the folder path where `geckodriver.exe` is located (e.g., `C:\path\to\geckodriver`).

After updating your PATH, restart your terminal/command prompt and try again to check the version.

### 3. **Verify Installation Again**
Once `geckodriver` is installed correctly and in the PATH, check the version again:

```bash
geckodriver --version
```

This should return the installed version.
