# -*- coding: utf-8 -*-

from colorama import Fore

WARNING = u'\U000026A0'



class RuntimeErrorCQ:

    last_menu_triggered_error = False
    last_error_message = ''
    last_codequick_route = ''
    last_codequick_callback_params = ''

    all_errors = []
    all_warnings = []

    @classmethod
    def reset_error_trigger(cls):
        cls.last_menu_triggered_error = False
        cls.last_error_message = ''
        cls.last_codequick_route = ''
        cls.last_codequick_callback_params = ''

    @classmethod
    def print_encountered_errors(cls):
        if len(cls.all_errors) == 0:
            print('\n* No error encountered')
            return 0

        print('\n* Encountered errors list:\n')
        cnt = 0
        for error in cls.all_errors:
            print('\t- Error %s' % cnt)
            print(error)
            cnt += 1
        return 1


    @classmethod
    def print_encountered_warnings(cls):
        if len(cls.all_warnings) == 0:
            print('\n* No warning encountered')
            return 0

        print('\n* Encountered warnings list:\n')
        cnt = 0
        for error in cls.all_warnings:
            print('\t- Warning %s' % cnt)
            print(error)
            cnt += 1
        return 1


    def __init__(self, path):
        self.route = RuntimeErrorCQ.last_codequick_route
        self.params = dict(RuntimeErrorCQ.last_codequick_callback_params)
        self.msg = RuntimeErrorCQ.last_error_message
        self.pp_path = str(path)
        if 'RuntimeError: No items found' in self.msg:
            RuntimeErrorCQ.all_warnings.append(self)
        else:
            RuntimeErrorCQ.all_errors.append(self)

    def __str__(self):
        s = ''
        s += '* Path: {}'.format(self.pp_path) + '\n'
        s += '* Route: {}'.format(self.route) + '\n'
        s += '* Params: {}'.format(self.params) + '\n'
        s += '* Message: \n{}'.format(self.msg) + '\n'
        return s


