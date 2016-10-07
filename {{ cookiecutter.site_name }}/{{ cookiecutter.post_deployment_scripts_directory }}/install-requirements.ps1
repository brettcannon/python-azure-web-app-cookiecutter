# $pwd == D:\home\site\repository
$PYTHON = 'D:\home\Python{{ cookiecutter.python_version|replace('.', '')|truncate(2, end='') }}\python.exe'
$AllArgs = @('-m', 'pip',
             '--disable-pip-version-check',
             'install', '--upgrade', '-r', 'D:\home\site\wwwroot\{{ cookiecutter.requirements_filename }}')
& $PYTHON $AllArgs
