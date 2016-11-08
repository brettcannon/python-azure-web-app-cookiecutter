# python-azure-web-app-cookiecutter

A [Cookiecutter](http://cookiecutter.readthedocs.io/) template for a
[Python](https://www.python.org/) site running on
[Azure Web Apps](https://azure.microsoft.com/en-us/services/app-service/web/).

## Using this template

1. [Install Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)
2. `cookiecutter gh:brettcannon/python-azure-web-app-cookiecutter`
   (or `cookiecutter https://github.com/brettcannon/python-azure-web-app-cookiecutter.git`
   if you prefer)
3. Fill in the Cookiecutter itmes (see below as to what each item
   represents)
4. Read the `README.md` included with your new website skeleton on how
   to deploy your site

### Cookiecutter items

- `site_name`: the name of the site, e.g. `my-site` would create a
  site with an address of `my-site.azurewebsites.net`
- `python_version`: which version of Python to use
- `cpu_arch`: 32-bit or 64-bit Python?
- `post_deployment_scripts_directory`: the directory where the
  [post-deployment action hooks](https://github.com/projectkudu/kudu/wiki/Post-Deployment-Action-Hooks)
  are to be stored, e.g. the script to execute `pip` after each site
  deployment
- `requirements_file_path`: the path to the `pip` requirements file,
  e.g. `requirements.txt`
- `static_assets_directory`: the name of the directory to place your
  static assets so IIS can serve the files directly
- `log_file_path`: where to store logs relating to the execution of
  the Python interpreter
- `main_module`: The name of the Python module that contains the
  server code
- `site_type`: choose whether you are creating a socket/async- or
  [WSGI](https://docs.python.org/3/library/wsgiref.html#module-wsgiref)-based
  server
- `socket_port_env_var`: for a socket-based server, the environment
  variable to store the incoming port number in
- `socket_python_arguments`: for a socket-based server, the arguments
  to the Python interpreter to launch your server, e.g. `-m app` will
  be equivalent to `python -m app`
- `wsgi_app_object`: for a WSGI-based server, what Python callable
  contains the WSGI app object, e.g. `app.wsgi_app` means the
  `wsgi_app` callable object in the `app` module
