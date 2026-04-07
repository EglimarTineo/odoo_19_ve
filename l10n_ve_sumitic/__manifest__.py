{
    'name': 'Venezuela - Contabilidad Sumitic',
    'version': '19.0.1.0.0',
    'summary': 'Localización Contable para Venezuela adaptada para Odoo 19',
    'category': 'Accounting/Localizations/Account Chart',
    'author': 'Sumitic',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'base_vat',
        'l10n_ve',
    ],
    'data': [
        # 1. Seguridad siempre primero
        'security/ir.model.access.csv',
        
        # 2. Datos Maestros (En este orden exacto para evitar errores de referencia)
        'data/res_country_state_data.xml',
        'data/account.account.csv',        # Primero las cuentas
        'data/account_tax_group_data.xml', # Luego los grupos de impuestos
        'data/account_tax_data.xml',       # AHORA SÍ: Los impuestos vinculados a cuentas y grupos
        'data/account_chart_template.xml', # Al final el template que une todo
        
        # 3. Interfaz de Usuario (Vistas)
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move.xml',          # No olvides incluir esta para el Número de Control
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
