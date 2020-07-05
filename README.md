# app更新提醒
## IOS
1. 根据官网提供的查询接口, 传入APP对应的ID, 获取到APP的详细信息
2. 和本地版本号进行比较, 然后显示更新内容
3. 使用轻量级的非关系型数据库[tinydb](https://github.com/msiemens/tinydb)将上一版的apps信息保存

顺便吹一下tinydb的厉害之处:

1.仅有1800行代码, 其中40%还是注释文档;
 
2.实现了100%的测试覆盖率;

## 使用

在`data\ios_apps_observed.yml`文件内, 添加你需要关注的ios app的id信息
(支持动态添加, 添加后, 不需要重新启动服务)

在`config.py`文件内添加你接收的邮箱信息

目前是每小时执行一次更新检查, 如果需要更换, 需要修改`run.py`内的`do_task`方法

## 意义
很多人可能认为这么做没有任何意义, 下面是一张分析的图片, 表明了我们可以获取到更有效的信息

### TODO: 爬豆瓣
https://www.douban.com/app/


参考文献: [Apple官方文档](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1)