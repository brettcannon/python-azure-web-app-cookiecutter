# python-azure-web-app-cookiecutter

[Cookiecutter](http://cookiecutter.readthedocs.io/) template for a
[Python](https://www.python.org/) site on
[Azure Web Apps](https://azure.microsoft.com/en-us/services/app-service/web/).


## How to use

1. Run Cookiecutter to generate a new Web App skeleton
2. Add your code to the skeleton to make your Web App do what you want
3. Run the `deploy.json` ARM template to create a new Web App on Azure
4. Specify a deployment source for your Web App to get your code
   deployed
5. Enjoy your new Web App!


## TODO

- Validate Web App name is acceptable
- Default app templates?
  + Just enough to explain how to structure the startup script
  + Will require adding a template item for naming the startup script
- README
  + https://deploy.azure.com button?
  + Instructions on how to deploy site from the CLI
- Any way to make it easier to set up the deployment source?
  + Might be too varied to provide template support for
  + But is only step that requires using the Azure Portal to finish
    setup
