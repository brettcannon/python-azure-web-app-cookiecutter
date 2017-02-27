# $pwd == D:\home\site\repository
$PYTHON = 'D:\home\Python{{ cookiecutter.python_version|replace('.', '')|truncate(2, end='', leeway=0) }}\python.exe'
$AllArgs = @('-m', 'pip',
             '--disable-pip-version-check',
             'install', '--upgrade', '-r', 'D:\home\site\wwwroot\{{ cookiecutter.requirements_file_name }}')
& $PYTHON $AllArgs
