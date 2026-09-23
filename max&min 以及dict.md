对于一个dict 
    查找max与min时 使用result.item和result.value有很大差别
    前者返回的是tuple 后者则是dict中本身的value类型

对于max与min
    在list中正常使用 
    在dict中
        判断标准可以由key=来决定
        假设  key = lambda x：x[1]则是value [0]则是key
    