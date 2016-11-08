# {{ cookiecutter.site_name }}

An
[Azure Web App](https://azure.microsoft.com/en-us/services/app-service/web/)
skeleton for a [Python](https://www.python.org/) website, created from
[a Cookiecutter template](https://github.com/brettcannon/python-azure-web-app-cookiecutter).


## Skeleton contents

- `.skipPythonDeployment`: turn off some implicit Azure Web App Python
  support that is unnecessary when using this skeleton
- `azuredeploy.json`:
  [ARM template](https://azure.microsoft.com/en-us/documentation/articles/app-service-deployment-readme/)
- `README.md`: this file
- `web.config`: IIS configuration file to set up the server front-end
- `{{ cookiecutter.requirements_file_name }}`: your
  [pip requirements file](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)
- `{{ cookiecutter.main_module }}.py`: example server code
- `{{ cookiecutter.post_deployment_scripts_directory }}`: directory
  which contains
  [scripts that are executed after every site deployment](https://github.com/projectkudu/kudu/wiki/Post-Deployment-Action-Hooks)
  + `install-requirements.ps1`: script to run the equivalent of
    `python -m pip install -r {{ cookiecutter.requirements_file_name}}`
- `{{ cookiecutter.static_assets_directory }}`: directory to place
  static assets in so they can be served directly by IIS
  + `web.config`: configuration file to make the containing directory
    serve files via IIS directly


## Deploying

### If this site is publicly hosted on [GitHub](https://github.com/)

[![Deploy to Azure](http://azuredeploy.net/deploybutton.svg)](https://azuredeploy.net/)


### Manual deployment

1. Add your site's code
2. [Deploy the ARM template](https://azure.microsoft.com/en-us/documentation/articles/resource-group-template-deploy/)
   in `azuredeploy.json` to create and minimally configure your site
3. [Deploy your site's code](https://azure.microsoft.com/en-us/documentation/articles/app-service-deployment-readme/)
