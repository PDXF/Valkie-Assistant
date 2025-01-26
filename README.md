

```markdown
# Valkie Assistant

This repository contains the Python script `valkie_assistant.py`, which can be executed using the command `valkie` in the terminal.

## Prerequisites

1. **Python 3.x** installed on your system.
2. **pip** (Python package manager) for installing dependencies.

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/PDXF/valkie.git
```

### Step 2: Navigate into the Project Directory

```bash
cd valkie-assistant
```

### Step 3: Install Dependencies

Install the required Python dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Make the Python Script Executable

To be able to run the script with the `valkie` command directly, follow these steps:

#### 4.1 Create a New File Named `valkie` in `/usr/local/bin`

This will create a system-wide command that points to your Python script. You’ll need `sudo` permissions to create this file:

```bash
sudo nano /usr/local/bin/valkie
```

#### 4.2 Add the Following Code to the `valkie` File

```bash
#!/bin/bash
python3 /path/to/your/valkie/valkie_assistant.py "$@"
```

- Replace `/path/to/your/valkie/` with the full path to the `valkie` folder where `valkie_assistant.py` is located.

#### 4.3 Make the File Executable

```bash
sudo chmod +x /usr/local/bin/valkie
```

### Step 5: Verify the Installation

Now, you can run the `valkie` command directly from your terminal:

```bash
valkie
```

This will execute `valkie_assistant.py` without needing to specify `python3` or the script file name.

---

## Usage

Once the installation is complete, you can run the `valkie` command from anywhere in your terminal.

```bash
valkie
```

This will trigger the Python script's functionality.

## Troubleshooting

- If you encounter an error saying `valkie: command not found`, make sure that `/usr/local/bin` is in your `PATH`.
- Ensure the `valkie` script is marked as executable: `sudo chmod +x /usr/local/bin/valkie`.

---

Feel free to modify the Python script as needed, and contribute to this repository!
```

### Explanation:

1. **`/usr/local/bin/valkie`**: This is where the custom command `valkie` will be placed. The script in this file will tell the system to execute your Python script when you type `valkie` in the terminal.
2. **`"$@"`**: This passes any arguments you provide after `valkie` directly to the Python script, allowing for flexible usage if you want to add parameters.
3. **`sudo chmod +x /usr/local/bin/valkie`**: This ensures the file is executable.

With these steps, you should be able to execute the Python script with the `valkie` command from anywhere on your system!
