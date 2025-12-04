# -*- coding: utf-8 -*-
{
    'name': "To-Do List",

    'summary': "Gestiona tus tareas con un tablero Kanban",

    'description': """
Aplicación de gestión de tareas con:
- Vista Kanban arrastrando tareas entre estados
- Prioridades y etiquetas
- Fechas límite con alertas de tareas atrasadas
- Asignación de tareas a usuarios
    """,

    'author': "Tu Nombre",
    'website': "https://www.tuempresa.com",

    'category': 'Productivity',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/stages.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

