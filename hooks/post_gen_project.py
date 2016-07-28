python_version = "{{ cookiecutter.python_version }}"
cpu_arch = "{{ cookiecutter.cpu_arch }}"

site_extensions_base_url = "{}"
extension_name = "Python{}{}".format(python_version.replace(".", ""), cpu_arch)

print()
print("**NOTE**: Don't forget to install the proper Python site extension:\n"
      "    http://www.siteextensions.net/packages/{}".format(extension_name))
print("Also make sure to add the following App setting:\n"
      "    SCM_POST_DEPLOYMENT_ACTIONS_PATH -> "
      "D:\\home\\site\\wwwroot\\post-deployment")