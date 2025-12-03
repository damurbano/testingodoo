{
    "name": "Mi Primer Addon",
    "version": "17.0.1.0.0",
    "author": "Prueba Tecnica",
    "category": "Tools",
    "summary": "Ejemplo simple para aprender Odoo",
    "description": "Modulo de ejemplo con un modelo sencillo y una vista de lista.",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/mi_modelo_views.xml"
    ],
    "installable": True,
    "application": True,
}
