19_site_generator
===================
The script generate_site.py generates the site using articles written with markdown and configuration file config.json with information about these articles. 

The script takes the path to the desired site directory as input.  

It creates main index page with list of all articles' names and their links.

The script converts articles markdown files to html files. Then it creates valid pages using jinja2. 

The result you can see on https://kajojify.github.io/19_site_generator/

How to run
----------
Clone this repository. Then go to the repository directory.

Install all requirements:
```
pip3 install -r requirements.txt
```
Run the script:
```
python3 generate_site.py
```

Usage
-----

```
~$ python3 generate_site.py
Enter the path to the site folder:  ---  site

```
