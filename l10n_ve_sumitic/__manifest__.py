{
    'name': 'Venezuela - Contabilidad Sumitic',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations/Account Chart',
    'author': 'Sumitic',
    'website': 'https://sumitic.lat',
    'depends': [
        'account',
        'base_vat',
        'l10n_ve', # Dependencia opcional si quieres heredar algo de la base oficial
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/account.account.csv',
        'data/account_tax_group_data.xml',
        'data/account_chart_template.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
