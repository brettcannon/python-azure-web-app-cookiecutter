:: cwd == D:\home\site\repository
call D:\home\Python{{ cookiecutter.python_version|replace('.', '')|truncate(2, end='') }}\python.exe -m pip --disable-pip-version-check install -r D:\home\site\wwwroot\{{ cookiecutter.requirements_filename }}
