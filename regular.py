# 正则

s = 'ABC\\-001' # python的字符串，对应正则表达式的字符串编程'ABC\-001'
# 不考虑转移可以加上r前缀
s = r'ABC\-001'
import re
# 判断是否匹配
r = re.match(r'^\d{3}\-\d{3,8}/div>', '010-12345')
print(r)

# 切分字符串
# 识别连续空格
print(re.split(r'\s+', 'a b  c'))
# 识别所有空格
print(re.split(r'[\s\,]+', 'a, b,     c,   d'))


# 分组

# 贪婪匹配


####################
# 内建模块
####################

# datetime Python处理日期和时间的标准库
from datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)
print(dt) #2015-04-19 12:20:00

# datetime 转为timestamp
t = dt.timestamp()
print(t) #1429417200.0
# timestamp 转为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) #2015-04-19 12:20:00
# timestamp 是一个浮点数，没有时区的概念，datetime是有时区的，本地时间是指当前操作系统设定的时区 北京时间为UTC+8:00 时区
# 转换为UTC标准时间
print(datetime.utcfromtimestamp(t))

# str 转为datetime
cday = datetime.strptime('2015-01-01', '%Y-%m-%d')
print(cday)

# datetime 转为str
now = datetime.now()
print(now.strftime('%a, %b, %d, %H:%M')) #Mon, Oct, 08, 17:39

# datetime加减
from datetime import timedelta
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=1, hours=12))

# 本地时间转换为UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换
# 通过utcnow()拿到当前的UTC时间
utc_dt = datetime.utcnow()


