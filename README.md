# python-azure-web-app-cookiecutter

[Cookiecutter](http://cookiecutter.readthedocs.io/) template for a
[Python](https://www.python.org/) site running on
[Azure Web Apps](https://azure.microsoft.com/en-us/services/app-service/web/).


## How to use

1. `cookiecutter gh:brettcannon/python-azure-web-app-cookiecutter`
2. Add your site's code to the generated skeleton
3. [Deploy the ARM template](https://azure.microsoft.com/en-us/documentation/articles/resource-group-template-deploy/)
   in `azuredeploy.json` to create and minimally configure your site
4. [Deploy your site's code](https://azure.microsoft.com/en-us/documentation/articles/app-service-deployment-readme/)

### Cookiecutter items

- `site_name`: the name of the site, e.g. `site_name.azurewebsites.net`
- `python_version`: the full Python version to use
- `cpu_arch`: 32 or 64-bit Python?
- `site_type`: choose whether to use a socket or
  [WSGI](https://docs.python.org/3/library/wsgiref.html#module-wsgiref)
- `socket_port_env_var`: for a socket site, the environment variable
  to store the incoming port number in
- `socket_python_arguments`: for a socket site, the arguments to the
  Python interpreter to launch your server, e.g. `-m app` will be
  equivalent to `python -m app`
- `wsgi_app_object`: for a WSGI site, what Python callable contains
  the WSGI app object, e.g. `app.wsgi_app` means the `wsgi_app`
  object in the `app` module
- `log_file_path`: where to store logs relating to the execution of
  the Python interpreter
- `post_deployment_scripts_directory`: the directory where the
  [post-deployment action hooks](https://github.com/projectkudu/kudu/wiki/Post-Deployment-Action-Hooks)
  are to be stored, e.g. the script to execute `pip` after each site
  deployment
- `requirements_filename`: the name of the `pip` requirements file,
  e.g. `requirements.txt`


## TODO

- Validate Web App name is acceptable
- Default app templates?
  + Just enough to explain how to structure the startup script
  + Will require adding a template item for naming the startup script
- README.md
  + https://deploy.azure.com button?
  + Instructions on how to deploy site from the CLI
  + Explanation of files
- Any way to make it easier to set up the deployment source?
  + Might be too varied to provide template support for
  + But is only step that requires using the Azure Portal to finish
    setup
