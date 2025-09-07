# Systemctl

- in some cases program.service file is not added to the .service file directory by package managers (if we install manually)
- So we have to create that
- Basics steps
  - create a user with home directory
  - copy the program code to the home directory
  - change the file owner ship to the program user
  - create the .service file
