def get_view_code(view_name='view_name', app_name='app_name', include_imports=True):
    code = ''

    if include_imports:
        code = 'from django.shortcuts import render\n'

    code += """
def {view_name}(request):
    context = dict()
    return render(request, "{app_name}/{view_name}.html", context)
    """

    return code.format(app_name=app_name, view_name=view_name)


def get_logging_code(logger_var='logger', logger_name='__name__', include_examples=True, include_imports=True, help_comment=True):
    code = ''
    if include_imports:
        code += 'import logging\n\n'

    code += '{logger_var} = logging.getLogger({logger_name})\n\n'.format(logger_var=logger_var, logger_name=logger_name)

    if include_examples:
        logger_types = {
            'info': 'info',
            'warning': 'warning',
            'error': 'error',
            'critical': 'critical',
            'exception': 'exception',
            'debug': 'debug',
            'log': 'log'
        }

        for logger_type in logger_types:
            code +=  "{logger_var}.{logger_type}('{logger_type_upper} MESSAGE')\n".format(
                logger_var=logger_var, 
                logger_type=logger_type, 
                logger_type_upper=logger_type.upper()
            )
    else: 
        code = code.strip() + "  # logging.log('LOG MESSAGE'), logging.info('INFO MESSAGE')"  

    return code

if __name__ == '__main__':
    print(get_view_code())
    # print('\n')

    print(get_view_code('index'))
    # print('\n')

    print(get_view_code(app_name='users'))
    # print('\n')

    print(get_view_code(app_name='users', view_name='home'))
    # print('\n')

    print(get_view_code('app', 'view',include_imports=False))
    # print('\n')

    print(get_logging_code())

    print(get_logging_code(include_examples=False))

    
    
