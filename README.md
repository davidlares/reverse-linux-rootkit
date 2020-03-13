# Linux Rootkit Reverse Shell

This script performs two main functions, the first and main one is a local reverse-shell (Backdoor) program in order to take remote access for Linux-based machines. The other part does a certain functionality of hiding the execution process for avoiding being detected by sysadmins or related people.

The whole idea is to hide the `PID` of a running process from the `/proc` directory, this directory contains an internal-directory for each executing process in the OS, the `PID` itself, identifies the process internal call procedures and details of the project. This `PID` can be shown via `top` or `htop` commands.

Internally the rootkit is made by grabbing the real `PID` of the process, setting up a string random `token` and after that perform a directory creation in the `/tmp` directory and a bound process from the `/tmp` to the `/proc` directory itself, this won't show any information when you list the process with `ps aux | grep <file>` or if you `cd` to the related `PID` directory itself.

## Mount bind functionality

According to multiple sources, the `bind` option of the `mount` command allows you to remount part of a file hierarchy at a different
location remaining available at the original location.

This [Link](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/global_file_system_2/s1-manage-pathnames) explains it way better.

## Usage

Just `python rootkit.py`

You can also complement the functionality of this, by generating an `ELF` file for simplicity (this can be done with `pyinstaller`)

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
