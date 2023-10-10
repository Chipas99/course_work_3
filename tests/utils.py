def mask_card(card_num):
    return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]

def mask_account(account_num):
    return "**" + account_num[-4:]
