# with open('03data.txt', 'r', encoding='utf-8') as f:
#     sar = []
#     for eilute in f:
#         # print(eilute)
#         for simbolis in eilute.split():
#             sar.append(int(simbolis))


with open('03data.txt', 'r', encoding='utf-8') as f:
    sar = [int(simbolis) for eilute in f for simbolis in eilute.split()]
  

print(sar)