# copyright-adder

Simple tool to add the copyrights to all the files in a directory. 

# Usage

Select: 
	* path: directory containing the files and subdirectories to which the license notice has to be added. 
	* extensions: list of extensions of files to which the license notice has to be added.
	* copyright: string contining the license notice to be added to the files. 
	* ignore: list of directory names to be ignored. 

Run copyright-adder.py. It has been tested in Ubuntu 18.0.

Example: 

```
path = "/path/to/files/"
extensions = ["cpp", "h"]
copyright = ["/**********************************************\n",\
             "* Invented License 2022 \n"
             "**********************************************/\n\n"]
ignore = ["dir_to_ignore1", "dir_to_ignore2"]
```
