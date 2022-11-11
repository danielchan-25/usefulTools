from faker import Faker

fake = Faker(locale='zh_CN')

def personal():
    # 人物类信息
    name = fake.name()  ## 随机姓名
    name_male = fake.name_male() ## 男性姓名
    name_female = fake.name_female() ## 女性姓名
    id_card = fake.ssn()    ## 身份证号
    birth_date = id_card[6:14]  ## 出生年月
    print('人物类信息：\n' + '随机姓名：' + name + '\n男性姓名：' + name_male + '\n女性姓名：' + name_female + '\n身份证号：' + id_card + '\n出生年月：' + birth_date + '\n')

def address():
    # 地址类信息
    country = fake.country()    ## 国家
    city = fake.city()  ## 城市
    city_suffix = fake.city_suffix()  ## 城市的后缀,中文是：市或县
    address = fake.address()    ## 详细地址
    province = address[:3]  ## 所在省份
    street_address = fake.street_address()  ## 街道
    street_name = fake.street_name()  ## 街道名
    postcode = fake.postcode()  ## 邮编
    latitude = fake.latitude()  ## 维度
    longitude = fake.longitude()  ## 经度
    print('地址类信息：\n' + '国家：' + country + '\n城市：' + city + '\n省份：' + province + '\n详细地址：' + address + '\n街道：' + street_address + '\n街道名：' + street_name + '\n邮编：' + postcode + '\n维度：' + str(latitude) + '\n经度：' + str(longitude) + '\n')

def credit_card():
    # 银行卡/信用卡
    card_number = fake.credit_card_number(card_type=None)   ## 卡号
    card_provider = fake.credit_card_provider(card_type=None)   ## 卡的提供者
    card_security_code = fake.credit_card_security_code(card_type=None) ## 卡的安全密码
    card_expire = fake.credit_card_expire() ## 卡的有效期
    card_full = fake.credit_card_full(card_type=None)   ## 完整卡信息
    print('银行卡/信用卡信息：\n' + '卡号：' + card_number + '\n提供者：' + card_provider + '\n安全密码：' + card_security_code + '\n有效期：' + card_expire + '\n')
    #print('银行卡/信用卡信息：\n' + card_full)

def job():
    # 工作类信息
    company = fake.company()    ## 公司名
    company_suffix = fake.company_suffix()  ## 公司名后缀
    company_mail = fake.company_email() ## 公司邮箱
    job_name = fake.job()   ## 工作职位
    print('工作类信息：\n' + '公司名：' + company + '\n公司名后缀：' + company_suffix + '\n公司邮箱：' + company_mail +'\n工作职位：' + job_name + '\n')

def internet():
    # 网络类信息
    ipv4 = fake.ipv4(network=False) ## ipv4地址
    ipv6 = fake.ipv6(network=False)    ## ipv6地址
    uri = fake.uri() ## uri
    mac_address = fake.mac_address() # MAC地址
    user_agent = fake.user_agent() # UA
    safe_email = fake.safe_email() # 安全邮箱
    free_email = fake.free_email() # 免费邮箱
    phone_number = fake.phone_number()  ## 手机号码
    print('网络类信息：\n' + 'ipv4地址：' + ipv4 + '\nipv6地址：' + ipv6 + '\nuri地址：' + uri + '\nmac地址：' + mac_address + '\nUA：' + user_agent + '\n安全邮箱：' + safe_email + '\n免费邮箱：' +free_email + '\n手机号码：' +phone_number)


personal()
address()
credit_card()
job()
internet()