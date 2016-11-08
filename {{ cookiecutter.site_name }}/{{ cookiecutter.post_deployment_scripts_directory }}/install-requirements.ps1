# $pwd == D:\home\site\repository
$PYTHON = '{{ cookiecutter._python_dir }}\python.exe'
$AllArgs = @('-m', 'pip',
             '--disable-pip-version-check',
             'install', '--upgrade', '-r', 'D:\home\site\wwwroot\{{ cookiecutter.requirements_file_name }}')
& $PYTHON $AllArgs
