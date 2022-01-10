from unittest.mock import MagicMock


# class CoreMock(object):
#     def get_user(self, user_id=1, data=None):
#         user = User(
#             id=user_id,
#             user_name='exchange',
#             full_name='Exchange Order',
#             first_name='Exchange',
#             last_name='Order',
#             middle_name='',
#             email='exchange@order.com',
#             constant_balance=10000,
#             constant_balance_holding=0,
#             constant_balance_debt=0,
#             address_country='US',
#             tax_country='US',
#             status=1,
#             verified_level=6,
#             referral_code='REFERRAL',
#             language='en',
#             membership=1,
#             withdraw_confirmed_email_on=0,
#             suspend_withdrawal_to=None
#         )
#         if data:
#             user.constant_balance = data.get('constant_balance', user.constant_balance)
#             user.constant_balance_holding = data.get('constant_balance_holding', user.constant_balance_holding)
#             user.constant_balance_debt = data.get('constant_balance_debt', user.constant_balance_debt)
#             user.verified_level = data.get('verified_level', user.verified_level)
#             user.agent_user = data.get('agent_user', user.agent_user)
#             user.user_role_id = data.get('user_role_id', user.user_role_id)
#             user.tax_country = data.get('tax_country', user.tax_country)
#             user.lo_user = data.get('lo_user', user.lo_user)
#
#         mock = MagicMock(return_value=user)
#         ConstantCoreBusiness.get_user = mock
#
#         return mock
