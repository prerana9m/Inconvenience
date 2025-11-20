from os import environ
ROOMS = [
    {
        'name': 'lab',
        'display_name': 'VSEEL (KRAN 701)',
        'participant_label_file': '_rooms/VSEEL701.txt',
    },
    {
        'name': 'lab2',
        'display_name': 'VSEEL (KRAN 701) S2',
        'participant_label_file': '_rooms/VSEEL701.txt',
    },
    {
        'name': 'lab3',
        'display_name': 'VSEEL (KRAN 701) S3',
        'participant_label_file': '_rooms/VSEEL701.txt',
    },
]

SESSION_CONFIGS = [
    # dict(
    #     name='Convenience',
    #     app_sequence=['survey'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='Convenience',
    #     app_sequence=['Consent', 'sliders_practice', 'bonustask1', 'normalization_task',
    #                   'treatment4',
    #                   'svo', 'survey', 'display_results', 'sliders_bdm', 'end'],
    #     num_demo_participants=2,
    # ),
  dict(
       name='Convenience',
       app_sequence=['Consent', 'sliders_practice', 'bonustask1', 'normalization_task',
                     'treatment1', 'treatment2', 'treatment3', 'treatment4',
                     'svo', 'survey', 'display_results', 'sliders_bdm', 'end'],
       num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['app_payoffs', 'switch_point', 'chosen_row', 'chosen_row_value', 'chosen_round',
                      'chosen_row_option', 'normalized_value', 'charity_payoff', 'chosen_slider_task_number',
                      'SVO_round', 'SVO_sender', 'SVO_receiver', 'SVO_to_self', 'SVO_to_other',
                      'SVO_points', 'app_to_pay', 'bonus_task_to_pay', 'selected_charity', 'bonus_row',
                      'bonus_row_option', 'bonus_task_payoff', 'bonus_row_value', 'decision_row', 'decision_row_option',
                      'decision_row_value', 'decision_task_payoff', 'slider_tasks_number', 'expiry',
                      'average_practice_slider_time', 'three_sliders_time', 'five_sliders_time', 'seven_sliders_time',
                      'charity_final_payoff']

SESSION_FIELDS = ['params', 'order']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7031043634821'

