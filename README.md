# app更新提醒
## IOS
1. 根据官网提供的查询接口, 传入APP对应的ID, 获取到APP的详细信息
2. 和本地版本号进行比较, 然后显示更新内容
3. 目前是将上一版的apps信息存成了txt文件, 日后会使用轻量级的非关系型数据库[tinydb](https://github.com/msiemens/tinydb)

顺便吹一下tinydb的厉害之处:

1.仅有1800行代码, 其中40%还是注释文档;
 
2.实现了100%的测试覆盖率;

## 文件说明
### notify.py 
配置通知方式, 如邮件

### ios/notify.py
对比ios apps的版本号, 发送邮件通知

### exe_task.py 
配置定时任务

参考文献: [Apple官方文档](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1)