
_list = ["19168534224","lizhiweke-susu","yangyang","18617009364","lizhiweike0103","15602975763","19925224142","lizhiweike-chenchen","18148557237","18520804170","15622812843","lzwk-cx","wujinzhen","jiayi.liu@tenclass.com","yu.cheng@lizhiweike.com","19166210439"]

d = []
for i in _list:
    d.append(
        {
          "match_phrase": {
            "wx_userid": i
          }
        }
    )

import pprint, json
print(json.dumps(d))
# print(d)