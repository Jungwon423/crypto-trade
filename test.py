import pyupbit

access = "CirAMYaEKYufmfTTUu8se7BoHZpt3AEMxlCEP4jH"          # 본인 값으로 변경
secret = "BC0TBtsxPziQmhq7zuMNSZ1Emu2xFrzedUlBNREE"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회