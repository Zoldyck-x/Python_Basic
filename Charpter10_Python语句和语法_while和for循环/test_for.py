#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

List1 = ['aaa', 111, (4, 5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4, 5)]
for x in List1:
    for y in List2:
        if x == y:
            print(str(x), 'in List1 and List2')
            break
    else:
        print(str(x), 'only in List1')
