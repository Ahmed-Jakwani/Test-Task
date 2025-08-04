{
    'name': 'Reviews for Project Tasks',
    'version': '16.0',
    'author': 'Ahmed Jakwani',
    'depends': ['base','project'],
    'summary': 'Reviews for Project Tasks',
    'description': 'Reviews for Project Tasks',
    'sequence':'-1000',
    'data': [
        'security/ir.model.access.csv',

        'views/project_task.xml',
        'views/project_task_review.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
