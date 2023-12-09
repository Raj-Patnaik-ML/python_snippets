# JP Morgan Interview question
from collections import defaultdict

info_buy = [
    {'qty': 100,
     'price': 1500},
    {'qty': 25,
     'price': 1550},
]

info_sell = [
    {'qty': 50,
     'price': 1550},
    {'qty': 25,
     'price': 1600},
    {50: 1550},
    {25: 1600},
]
tcs_buy = [
    {'qty': 50,
     'price': 3000},
]

ds = {
    'infosys': {
        'buy': [
            {'qty': 100,
             'price': 1500},
            {'qty': 25,
             'price': 1550},
        ],
        'sell': [
            {'qty': 50,
             'price': 1550},
            {'qty': 25,
             'price': 1600},
            {'qty': 50,
             'price': 1600},

        ]
    },
    'tcs': {
        'buy': [
            {'qty': 50,
             'price': 3000},
        ],
        'sell': [
            {'qty': 20,
             'price': 3100},
            {'qty': 10,
             'price': 3200},
            {'qty': 30,
             'price': 3200},
        ]
    }

}


def calc(ds_sent):
    running_total = defaultdict(float)
    for company_name, trxn_data in ds_sent.items():
        for qty_pr in trxn_data['buy']:
            running_total[company_name] -= (qty_pr['qty'] * qty_pr['price'])

        for qty_pr in trxn_data['sell']:
            running_total[company_name] += (qty_pr['qty'] * qty_pr['price'])

    return running_total

# How yo handle continuous stream of buy requests and sel requests
# since I am taking list for buy and sell trxns that list can be changed to a deque where completed requests can be
# popped from left and new requets can be added from right. we Can handle parallel requests overlap using Thread.Lock()
# so no race condition
print(calc(ds))
