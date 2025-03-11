## SSH Nuke v1.0

### Overview
SSH Nuke is a brute-force program designed to find a valid password for a given username on a specified host. It utilizes the `paramiko` library to attempt SSH connections with a list of passwords.

### Features
- Attempts to connect to an SSH server using a known username and a list of potential passwords.
- Provides feedback on each password attempt.
- Displays the found password if successful.
- Handles file not found errors gracefully.

### Requirements
- Python 3.x
- `paramiko` library

### Installation
1. Ensure you have Python 3.x installed on your machine.
2. Install the `paramiko` library using pip:
   ```bash
   pip install paramiko
   ````

### Usage
- Clone or download the repository containig `sshnuke.py` file.
- Have a list containing a list of possible passwords.
- Run the script:
```bash
python3 sshnuke.py
```
- When prompted enter the following:
- `IP address`
- `Known username`
- `path to password list`

### Example 
```sh
╔═╗╔═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗
╚═╗╚═╗╠═╣  ║║║║ ║╠╩╗║╣ 
╚═╝╚═╝╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝
Version 1.0
by: NomesPaladin       

[?]Enter host IP:
[?]Enter known username:
[?]Enter password filename:
```
### Output 
```sh
[!] Password found >>> <password> <<<

[-] Password not found.
```
### Important note 
- Use this tool responsibly and only on systems you have permission to test.
- Brute-forcing passwords can be illegal and unethical if done without consent.

### License 
This project is licensed under the MIT License - see the LICENSE file for details.

### Version 
- 1.0
