# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

brand_data = {
    "status": "success",
    "msg": "message",
    "brand": [
        {
            "first_letter": "A",
            "name": "奥迪",
            "logo_img": "7206452af3747880ddd07398a95b9bdbebbc963e.jpg",
            "slug": "audi"
        },
        {
            "first_letter": "A",
            "name": "阿尔法罗米欧",
            "logo_img": "87ab618897b3bb2a7d9db46115dd530a3112a852.jpg",
            "slug": "alfaromeo"
        },
        {
            "first_letter": "A",
            "name": "阿斯顿马丁",
            "logo_img": "b0f5d53415311b0213a14f38ec1e418aacc50fd1.jpg",
            "slug": "astonmartin"
        },
        {
            "first_letter": "B",
            "name": "北京汽车",
            "logo_img": "24d27284cdefceb40b3f1823f5c2f33b30aee7b3.jpg",
            "slug": "beijingqiche"
        },
        {
            "first_letter": "B",
            "name": "布嘉迪",
            "logo_img": "2fd616b866c4f39e0d4a7c5b100b21236739d4a5.jpg",
            "slug": "bujiadi"
        },
        {
            "first_letter": "B",
            "name": "北汽制造",
            "logo_img": "4b1863e20390ab2f1f99958b088ce37fa31e9d9a.jpg",
            "slug": "beiqizhizao"
        },
        {
            "first_letter": "B",
            "name": "奔腾",
            "logo_img": "365a8ff700d99f8f08222e3b99ebbb8d2352ad26.jpg",
            "slug": "benteng"
        },
        {
            "first_letter": "B",
            "name": "北汽威旺",
            "logo_img": "beiqiweiwang_brang.jpg",
            "slug": "beiqiweiwang"
        },
        {
            "first_letter": "B",
            "name": "巴博斯",
            "logo_img": "11e6cf2c0ec7d07054a307cd1d15d09c0ca63131.jpg",
            "slug": "barbus"
        },
        {
            "first_letter": "B",
            "name": "宝骏",
            "logo_img": "3a7dcb137ccb9f2bac719e83086297a834d23b38.jpg",
            "slug": "baojun"
        },
        {
            "first_letter": "B",
            "name": "标致",
            "logo_img": "c744073977d5dd9b3159877f1c363ded68302e6a.jpg",
            "slug": "biaozhi"
        },
        {
            "first_letter": "B",
            "name": "比亚迪",
            "logo_img": "9ab84ee208790afd5ca6eec976afd3c16f02d129.jpg",
            "slug": "byd"
        },
        {
            "first_letter": "B",
            "name": "本田",
            "logo_img": "59968bfbb45afb00ea342e619d987968f20dddc3.jpg",
            "slug": "honda"
        },
        {
            "first_letter": "B",
            "name": "保时捷",
            "logo_img": "4e0dd4abda81f410a8f59e9792820963f4a14de2.jpg",
            "slug": "porsche"
        },
        {
            "first_letter": "B",
            "name": "宝马",
            "logo_img": "3b0b703a786121af9f02e7bfc9725db7361a208e.jpg",
            "slug": "bmw"
        },
        {
            "first_letter": "B",
            "name": "宾利",
            "logo_img": "9b6f2c7d180342e0ce9915a711d7e225c187b0d7.jpg",
            "slug": "bentley"
        },
        {
            "first_letter": "B",
            "name": "别克",
            "logo_img": "721577ad1a23f31ebd31c593926c001faf5b30e9.jpg",
            "slug": "buick"
        },
        {
            "first_letter": "B",
            "name": "奔驰",
            "logo_img": "14fd54bf2c4f3e9e006775433368b17d6e8c739c.png",
            "slug": "benz"
        },
        {
            "first_letter": "C",
            "name": "长安商用",
            "logo_img": "b3506e2d2f57855fd8635975842e04dbfc266de3.jpg",
            "slug": "changanshangyong"
        },
        {
            "first_letter": "C",
            "name": "昌河",
            "logo_img": "dbeb5c33fa455d2967d01f4d7cda6f262a13276f.jpg",
            "slug": "changhe"
        },
        {
            "first_letter": "C",
            "name": "长城",
            "logo_img": "82151b390370600e9d702ca3f8b45eaec2f4dff7.jpg",
            "slug": "changcheng"
        },
        {
            "first_letter": "C",
            "name": "长安",
            "logo_img": "7ac69764409007e1b7847164982c2ef112749781.jpg",
            "slug": "changan"
        },
        {
            "first_letter": "C",
            "name": "长丰猎豹",
            "logo_img": "6b65c7598adcd4e0eb8364f801b5ee7fde2e9e2e.jpg",
            "slug": "liebao"
        },
        {
            "first_letter": "D",
            "name": "东风风行",
            "logo_img": "logo_dongfengfengxing.png",
            "slug": "dongfengfengxing"
        },
        {
            "first_letter": "D",
            "name": "东风风度",
            "logo_img": "logo_dongfengfengdu.png",
            "slug": "dongfengfengdu"
        },
        {
            "first_letter": "D",
            "name": "DS(谛艾仕)",
            "logo_img": "270_80.jpg",
            "slug": "logo_270"
        },
        {
            "first_letter": "D",
            "name": "东风小康",
            "logo_img": "41f2bcf4441fbe6d47af5fa435abd429640a8814.jpg",
            "slug": "dongfengxiaokang"
        },
        {
            "first_letter": "D",
            "name": "大迪",
            "logo_img": "cfbc4c85d4a3c1095600eaaf4a775dc4e97af911.jpg",
            "slug": "dadi"
        },
        {
            "first_letter": "D",
            "name": "东风风神",
            "logo_img": "logo_dongfengfengshen.png",
            "slug": "dongfengfengshen"
        },
        {
            "first_letter": "D",
            "name": "东风",
            "logo_img": "41f2bcf4441fbe6d47af5fa435abd429640a8814.jpg",
            "slug": "dongfeng"
        },
        {
            "first_letter": "D",
            "name": "东南",
            "logo_img": "57f936959b98b801e21dae8c3f27c5cb630715a1.jpg",
            "slug": "dongnan"
        },
        {
            "first_letter": "D",
            "name": "道奇",
            "logo_img": "4373d859e3c557884969223db95c44b30a98b9f5.jpg",
            "slug": "daoqi"
        },
        {
            "first_letter": "D",
            "name": "大众",
            "logo_img": "debfdc24b86c217862ce1bd1110a66b39459c20e.jpg",
            "slug": "dazhong"
        },
        {
            "first_letter": "D",
            "name": "大通",
            "logo_img": "dfa9d23d646857981ccd5852bcfa732d9bb97311.jpg",
            "slug": "datong"
        },
        {
            "first_letter": "D",
            "name": "大宇",
            "logo_img": "20120620180830330.jpg",
            "slug": "dayu"
        },
        {
            "first_letter": "F",
            "name": "菲亚特",
            "logo_img": "5bafc8593648209cdd7d1cfc11c0464c4b15d94a.jpg",
            "slug": "fiat"
        },
        {
            "first_letter": "F",
            "name": "福田",
            "logo_img": "735c41c51aad17c94ac10a248167bbc0dd6f8d00.jpg",
            "slug": "futian"
        },
        {
            "first_letter": "F",
            "name": "丰田",
            "logo_img": "7ce1a1b5b42beba90b03776151871a2315a1fa6a.jpg",
            "slug": "toyota"
        },
        {
            "first_letter": "F",
            "name": "福特",
            "logo_img": "85cac1c58bef0a0173f78270d136ecbcf19db627.jpg",
            "slug": "ford"
        },
        {
            "first_letter": "F",
            "name": "法拉利",
            "logo_img": "bd50523a8dc7a63574d92fe0aa81afe4ef600dd3.jpg",
            "slug": "ferrari"
        },
        {
            "first_letter": "F",
            "name": "福迪",
            "logo_img": "cd34b027e88e42e96e822e79261e499e8cae9b21.jpg",
            "slug": "fudi"
        },
        {
            "first_letter": "G",
            "name": "观致",
            "logo_img": "guanzi_brand.jpg",
            "slug": "guanzhi"
        },
        {
            "first_letter": "G",
            "name": "GMC",
            "logo_img": "gmc.jpg",
            "slug": "gmc"
        },
        {
            "first_letter": "G",
            "name": "光冈",
            "logo_img": "341d94bd870b6fb0d219107ee208fb929341b9e1.jpg",
            "slug": "galue"
        },
        {
            "first_letter": "G",
            "name": "贵州云雀",
            "logo_img": "20120619133345827.jpg",
            "slug": "yunque"
        },
        {
            "first_letter": "G",
            "name": "广汽传祺",
            "logo_img": "a3937e6653db90dc3d3dca998673d43fe4d48c03.jpg",
            "slug": "guangqichengyongche"
        },
        {
            "first_letter": "H",
            "name": "海马",
            "logo_img": "3e6be478081980da23f057b64dda19a6d29cf1a2.jpg",
            "slug": "haima"
        },
        {
            "first_letter": "H",
            "name": "哈飞",
            "logo_img": "d6347d45a819ead1ae9d728a24fb93b2d3a87223.jpg",
            "slug": "hafei"
        },
        {
            "first_letter": "H",
            "name": "哈弗",
            "logo_img": "logo_hafu.png",
            "slug": "hafu"
        },
        {
            "first_letter": "H",
            "name": "恒天",
            "logo_img": "e79a18e26209ba3b2fbabcda191401ec3d7aa0b1.jpg",
            "slug": "logo_266"
        },
        {
            "first_letter": "H",
            "name": "华普",
            "logo_img": "53d5a104e119e18b47bc63cf722d95b34169b7ac.jpg",
            "slug": "huapu"
        },
        {
            "first_letter": "H",
            "name": "黄海",
            "logo_img": "9593c2a50b0463540cd6a1dcd8dc5ff0cf85503b.jpg",
            "slug": "huanghai"
        },
        {
            "first_letter": "H",
            "name": "海格",
            "logo_img": "haige.jpg",
            "slug": "haige"
        },
        {
            "first_letter": "H",
            "name": "汇众",
            "logo_img": "dd33a942fa8cb56cc48df986e97136f6dd485a8f.jpg",
            "slug": "sh-huizhong"
        },
        {
            "first_letter": "H",
            "name": "华泰",
            "logo_img": "c25e2d74376c2080a13c550222a2c3fd518d1388.jpg",
            "slug": "huatai"
        },
        {
            "first_letter": "H",
            "name": "红旗",
            "logo_img": "2cc8fd8d4f4106ba13677736180ec2deab1f5ed1.jpg",
            "slug": "hongqi"
        },
        {
            "first_letter": "H",
            "name": "悍马",
            "logo_img": "d180b00b6f1e3788f4f2ec11db1cb432959e8fce.jpg",
            "slug": "hanma"
        },
        {
            "first_letter": "J",
            "name": "江南",
            "logo_img": "5269c6f022f904936dfbcf86ff439da78af70bbb.jpg",
            "slug": "jiangnanauto"
        },
        {
            "first_letter": "J",
            "name": "金杯",
            "logo_img": "3a70cf43a734f1a77f561932b4551f3484993041.jpg",
            "slug": "huachen"
        },
        {
            "first_letter": "J",
            "name": "吉奥",
            "logo_img": "1fb5d3c64254aa7523143a45c78814eb2b72239c.jpg",
            "slug": "jiao"
        },
        {
            "first_letter": "J",
            "name": "吉利英伦",
            "logo_img": "618e03251cceeed806e5cac5935cf19aaa95b5cf.jpg",
            "slug": "yinglunqiche"
        },
        {
            "first_letter": "J",
            "name": "九龙",
            "logo_img": "d540a4e452e641a9b430f7c3ff7a09a07d7a531a.jpg",
            "slug": "logo_258"
        },
        {
            "first_letter": "J",
            "name": "吉利帝豪",
            "logo_img": "e17e34e8b34abe3f25b309862569f49c770cee9b.jpg",
            "slug": "dihao"
        },
        {
            "first_letter": "J",
            "name": "江淮",
            "logo_img": "9f7d428ae7e6b5d26601734c4ab6c3d73037208c.jpg",
            "slug": "jianghuai"
        },
        {
            "first_letter": "J",
            "name": "吉利全球鹰",
            "logo_img": "logo_jiliquanqiuying.png",
            "slug": "jiliqunaqiuying"
        },
        {
            "first_letter": "J",
            "name": "吉利",
            "logo_img": "bf8436517fa0a80fb6a8a86d3bf18a3cbb6244c2.jpg",
            "slug": "jili"
        },
        {
            "first_letter": "J",
            "name": "江铃",
            "logo_img": "beb2aeb522268aca012ad0f4d3a86d2e8994486b.jpg",
            "slug": "jiangling"
        },
        {
            "first_letter": "J",
            "name": "金龙",
            "logo_img": "ab88439b7781b960f06d4c92d9204b153502381e.jpg",
            "slug": "jinlvkeche"
        },
        {
            "first_letter": "J",
            "name": "吉普",
            "logo_img": "c88f6d7c10de7683d0315d701ee6899ebb8a5342.jpg",
            "slug": "jeep"
        },
        {
            "first_letter": "J",
            "name": "捷豹",
            "logo_img": "035f2ea5c6cb8425ca20231a88286f780136cd5f.jpg",
            "slug": "jiebao"
        },
        {
            "first_letter": "K",
            "name": "柯尼赛格",
            "logo_img": "229_80.jpg",
            "slug": "kenisaige"
        },
        {
            "first_letter": "K",
            "name": "凯迪拉克",
            "logo_img": "9aa40803a577dea04de01ee7dacfa6a71d95342a.jpg",
            "slug": "cadillac"
        },
        {
            "first_letter": "K",
            "name": "卡尔森",
            "logo_img": "2f22b78d0075feb3a109b92e9233b4c26e1ed751.jpg",
            "slug": "logo_269"
        },
        {
            "first_letter": "K",
            "name": "克莱斯勒",
            "logo_img": "0c1943c8be70bfc6b5a0c8b95b2a59500ec010ba.jpg",
            "slug": "chrysler"
        },
        {
            "first_letter": "K",
            "name": "开瑞",
            "logo_img": "1a68ffdc6402a8e0a398960b90ed6f86abf7540d.jpg",
            "slug": "kairui"
        },
        {
            "first_letter": "L",
            "name": "莲花",
            "logo_img": "428355d32386f45e4d5690141f7a433002996b39.jpg",
            "slug": "lotus"
        },
        {
            "first_letter": "L",
            "name": "雷诺",
            "logo_img": "5aba92252f6c9a104569bbae242621410e133c26.jpg",
            "slug": "renault"
        },
        {
            "first_letter": "L",
            "name": "理念",
            "logo_img": "ec2fe09d0fc8fdef7e64b789190c9ee5e34c2d27.jpg",
            "slug": "linian"
        },
        {
            "first_letter": "L",
            "name": "铃木",
            "logo_img": "9947996a043900da5aa8c849f562de473cf0be0c.jpg",
            "slug": "suzuki"
        },
        {
            "first_letter": "L",
            "name": "雷克萨斯",
            "logo_img": "21f682022cc96c33cd592ac0fe288331fa3b2d37.jpg",
            "slug": "lexus"
        },
        {
            "first_letter": "L",
            "name": "林肯",
            "logo_img": "1e177d32d0126bff6fe0160ae2cdeb2ac5129b10.jpg",
            "slug": "lincoln"
        },
        {
            "first_letter": "L",
            "name": "陆风",
            "logo_img": "904887a346a719ca6aba18d85552456bcb7b5c6a.jpg",
            "slug": "lufeng"
        },
        {
            "first_letter": "L",
            "name": "路特斯",
            "logo_img": "lotus_brang.jpg",
            "slug": "lutesi"
        },
        {
            "first_letter": "L",
            "name": "路虎",
            "logo_img": "60c7eb4d5b0dcd60f3df5778ca13dda742fa345f.jpg",
            "slug": "landrover"
        },
        {
            "first_letter": "L",
            "name": "力帆",
            "logo_img": "976d9dd3a3f54a8a264ac9c8be01e3162f64d3cd.jpg",
            "slug": "lifan"
        },
        {
            "first_letter": "L",
            "name": "兰博基尼",
            "logo_img": "e28ea693aa34d9ff50bfb284f2529b29741f2df8.jpg",
            "slug": "lamborghini"
        },
        {
            "first_letter": "L",
            "name": "劳斯莱斯",
            "logo_img": "7ccfc739cab69042255a20b572e44fac79729645.jpg",
            "slug": "rolls-royce"
        },
        {
            "first_letter": "M",
            "name": "MINI(迷你)",
            "logo_img": "a9b71bf7276702d7396117feff6cfb76103e9f35.jpg",
            "slug": "mini"
        },
        {
            "first_letter": "M",
            "name": "马自达",
            "logo_img": "7645f2638e6aabf4d7a269db85466af3a5352f51.jpg",
            "slug": "mazda"
        },
        {
            "first_letter": "M",
            "name": "美亚",
            "logo_img": "ce6fe85110ad5c70524d876e959092998acbf371.jpg",
            "slug": "meiya"
        },
        {
            "first_letter": "M",
            "name": "迈巴赫",
            "logo_img": "1ba30ba8c5652d6fab29b8956d476b5a2cac86af.jpg",
            "slug": "maybach"
        },
        {
            "first_letter": "M",
            "name": "迈凯轮",
            "logo_img": "maikailun.jpg",
            "slug": "logo_259"
        },
        {
            "first_letter": "M",
            "name": "MG",
            "logo_img": "f6c112903bcae6dca1c76acf19c68caafce19421.jpg",
            "slug": "mg"
        },
        {
            "first_letter": "M",
            "name": "玛莎拉蒂",
            "logo_img": "b7fc10c3bf59d126f1335246c624bb9f2c8e9b1a.jpg",
            "slug": "maserati"
        },
        {
            "first_letter": "N",
            "name": "纳智捷",
            "logo_img": "078cc4b4926b0e64ee5b3391f176870b15f4fbde.jpg",
            "slug": "dongfengyulongnazhijie"
        },
        {
            "first_letter": "N",
            "name": "南汽新雅途",
            "logo_img": "dd12c417bf3d732d6ac8441185d951159ba01040.jpg",
            "slug": "nanqi"
        },
        {
            "first_letter": "O",
            "name": "欧朗",
            "logo_img": "365a8ff700d99f8f08222e3b99ebbb8d2352ad26.jpg",
            "slug": "logo_257"
        },
        {
            "first_letter": "O",
            "name": "讴歌",
            "logo_img": "7bfbe354a39cb8feb4933767c51ab3559268851d.jpg",
            "slug": "acura"
        },
        {
            "first_letter": "O",
            "name": "欧宝",
            "logo_img": "52dd24e40290b6148fe5cd0ab879993ab7d2ad6e.jpg",
            "slug": "opel"
        },
        {
            "first_letter": "P",
            "name": "Pagani",
            "logo_img": "191_80.jpg",
            "slug": "logo_191"
        },
        {
            "first_letter": "Q",
            "name": "启辰",
            "logo_img": "f375aa3049cba2bad8e427a7e9fbfcba9c512d1a.jpg",
            "slug": "logo_245"
        },
        {
            "first_letter": "Q",
            "name": "奇瑞",
            "logo_img": "a3f368ff1cbf3724fc275b8b4360f471c301d270.jpg",
            "slug": "chery"
        },
        {
            "first_letter": "Q",
            "name": "起亚",
            "logo_img": "1e25af1379f368fd56bc40eb59142cb51484bc91.jpg",
            "slug": "kia"
        },
        {
            "first_letter": "R",
            "name": "日产",
            "logo_img": "8272d2eed04e21df64c2ce44dfc327738a33a0e6.jpg",
            "slug": "richan"
        },
        {
            "first_letter": "R",
            "name": "荣威",
            "logo_img": "6e1a9c16eaf2613326c9cd85a1f4f0fd252a6b6e.jpg",
            "slug": "rongwei"
        },
        {
            "first_letter": "R",
            "name": "瑞麒",
            "logo_img": "d3284684167594dbc73d729f15da3d34cec55a84.jpg",
            "slug": "ruilin"
        },
        {
            "first_letter": "S",
            "name": "双龙",
            "logo_img": "c903a1cd441bec3222287f1dc68531468a499ef0.jpg",
            "slug": "shuanglong"
        },
        {
            "first_letter": "S",
            "name": "三菱",
            "logo_img": "81af6fde292974bfe4bc179a125799ec762f71b6.jpg",
            "slug": "mitsubishi"
        },
        {
            "first_letter": "S",
            "name": "斯柯达",
            "logo_img": "1917462ac1433bcc4d736f5b56eb4d7068fe2f6d.jpg",
            "slug": "skoda"
        },
        {
            "first_letter": "S",
            "name": "双环",
            "logo_img": "134bd363cbd58826c5d171a0c98eed19b744a3f7.jpg",
            "slug": "shuanghuan"
        },
        {
            "first_letter": "S",
            "name": "Smart",
            "logo_img": "cef0f98f9928fe55c797ee00a7d3f7ca65983d1f.jpg",
            "slug": "smart"
        },
        {
            "first_letter": "S",
            "name": "斯巴鲁",
            "logo_img": "47ead621de8bce3f46ad7df336182e4101d5b311.jpg",
            "slug": "subaru"
        },
        {
            "first_letter": "S",
            "name": "萨博",
            "logo_img": "13c25346c44b691be0a5ce1c3cf479d6969cfcdf.jpg",
            "slug": "saab"
        },
        {
            "first_letter": "S",
            "name": "世爵",
            "logo_img": "c27bf789c6bd69fc08e95d11422c52a9c962f650.jpg",
            "slug": "shijue"
        },
        {
            "first_letter": "T",
            "name": "天津一汽",
            "logo_img": "365a8ff700d99f8f08222e3b99ebbb8d2352ad26.jpg",
            "slug": "tj-yiqi"
        },
        {
            "first_letter": "T",
            "name": "天马",
            "logo_img": "20120619152341422.jpg",
            "slug": "tianma"
        },
        {
            "first_letter": "W",
            "name": "五菱",
            "logo_img": "21919ef3cde1641bc0c4c9ff8ce42fb2259d10cd.jpg",
            "slug": "wuling"
        },
        {
            "first_letter": "W",
            "name": "沃尔沃",
            "logo_img": "13a8409c1b4dc611e18afaf470a531bad874a244.jpg",
            "slug": "volvo"
        },
        {
            "first_letter": "W",
            "name": "威麟",
            "logo_img": "24375db49ddbbf58713d3951825d0beb93934d88.jpg",
            "slug": "weilin"
        },
        {
            "first_letter": "W",
            "name": "五十铃",
            "logo_img": "5755a185fa0533f7bb1f4b31bbbb6c6363874dad.jpg",
            "slug": "wushiling"
        },
        {
            "first_letter": "X",
            "name": "雪铁龙",
            "logo_img": "40659ec3fe73d8adf28022713421c95c56d29ca7.jpg",
            "slug": "citroen"
        },
        {
            "first_letter": "X",
            "name": "雪佛兰",
            "logo_img": "b01e4004dd145f0569c0ff61647f1eb3abb78d97.jpg",
            "slug": "chevrolet"
        },
        {
            "first_letter": "X",
            "name": "现代",
            "logo_img": "b40dffb2a265bbd592f5285ccf65db9f38ef4908.jpg",
            "slug": "hyundai"
        },
        {
            "first_letter": "X",
            "name": "新凯",
            "logo_img": "c5e96fd95f992cffea0a26c0bc2158765ee218d3.jpg",
            "slug": "xinkai"
        },
        {
            "first_letter": "X",
            "name": "西雅特",
            "logo_img": "bc9d55074c1f303af8ccf12d8e56a3e067a49c65.jpg",
            "slug": "xiyate"
        },
        {
            "first_letter": "Y",
            "name": "永源汽车",
            "logo_img": "799b9518bf19f1b73c04e66901e786daea0ba042.jpg",
            "slug": "yongyuanqiche"
        },
        {
            "first_letter": "Y",
            "name": "野马",
            "logo_img": "chuanqiyema.png",
            "slug": "chuanqiyema"
        },
        {
            "first_letter": "Y",
            "name": "英菲尼迪",
            "logo_img": "5e7b79c41a6d1ffab6b8915a09dbb0f2597f8f85.jpg",
            "slug": "infiniti"
        },
        {
            "first_letter": "Y",
            "name": "一汽吉林",
            "logo_img": "logo_yiqijilin.png",
            "slug": "yiqijilin"
        },
        {
            "first_letter": "Y",
            "name": "依维柯",
            "logo_img": "a5b2153834c4049a18f8d057adcddb5c185c44c4.jpg",
            "slug": "nj-iveco"
        },
        {
            "first_letter": "Y",
            "name": "一汽吉林大发",
            "logo_img": "bd67dea4ef5fa6b28bbc002cb62965eb6a140dfd.jpg",
            "slug": "jilindafa"
        },
        {
            "first_letter": "Y",
            "name": "一汽通用",
            "logo_img": "365a8ff700d99f8f08222e3b99ebbb8d2352ad26.jpg",
            "slug": "yiqitongyong"
        },
        {
            "first_letter": "Y",
            "name": "永源汽车UFO",
            "logo_img": "799b9518bf19f1b73c04e66901e786daea0ba042.jpg",
            "slug": "yongyuan-ufo"
        },
        {
            "first_letter": "Z",
            "name": "中华",
            "logo_img": "200482bb3022615f32640bdec646fd961a7980d2.jpg",
            "slug": "huachen-zhonghua"
        },
        {
            "first_letter": "Z",
            "name": "中顺",
            "logo_img": "d1f824c2016cef2d140425de3d91efe4a65689bb.jpg",
            "slug": "zhongshun"
        },
        {
            "first_letter": "Z",
            "name": "中兴",
            "logo_img": "acd1fd13ca0cb3d6a8f5c65176516826f611d32d.jpg",
            "slug": "zhongxing"
        },
        {
            "first_letter": "Z",
            "name": "众泰",
            "logo_img": "a2d48a13dfbe2c77645ade001790e63a82f8cbd8.jpg",
            "slug": "zhongtai"
        }
    ]
}