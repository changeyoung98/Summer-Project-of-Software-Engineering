# Summer-Project-of-Software-Engineering
# Group 8
## 开发记录
### Week One
2018-7-2
- 建立github repo并各自建立分支，尝试pull request等功能。
- 建立README
- 创建初始的maven项目，连接本地摄像头
- 初步了解tensorflow

2018-7-3
- 完成前端的基本框架及登陆注册功能
- 完成objectDetection 的初步识别
- 画出楼层图
- 继续学习tensorflow
- 学习视频传输协议相关知识，尝试通过服务器连接摄像头

2018-7-4
- 配置red5环境，实现从一台电脑连接另一台电脑的摄像头
- 实现objectDetection从实时画面中识别物品、人
- 尝试将red5与web项目整合在一起。

2018-7-5
- 完善前端相关功能，添加上传图片等功能。
- 实现从视频中截取图片获得目标与视频画面的分离
- 为已经完成的前端功能添加后端

2018-7-6
- 实现连接另一台电脑摄像头的工作量简单化，即在html中写定好访问数据，直接输入固定网址即可得到另一台电脑的摄像头画面
- 将此html修改为react的语法，实现从我们的前端项目中获得监控画面
- 完善前端功能，实现登陆注册输入的自动检验

### Week Two
2018-7-9
- 继续完善后端功能
- 尝试实现前端的截屏等图片视频小功能
- 学习cropper，了解运用其中的图片裁剪功能
- 撰写需求变更和迭代报告初稿

2018-7-10
- 后端功能基本实现
- reID可以跑自己的测试用例并成功识别
- 实现自动分时段截屏和保存

2018-7-11
- 实现cropper与react的结合，完成上传图片并根据用户需求裁剪的功能
- 学习ffmpeg相关知识，尝试在后端对flash进行截图
- 开始撰写第一次迭代的测试文档

2018-7-12
- 继续完善测试文档的编写
- 前端实现在楼层平面图上面点击摄像头区域即可获得直播视频
- 统一并美化前端界面风格
- ffmpeg实现后端截图，并进行整体项目整合
- 服务器通过client脚本发送图片给计算系统（另一台计算机），并接受返回的信息（图片及提示信息等）

2018-7-13
- 前后端整合完成，对登陆注册播放截屏等工作进行测试
- 后台可以通过视频或图片截取出里面的行人作为搜索目标集，并通过给出的目标行人图片进行行人再识别，在搜索目标集中找到目标人物
- 进行迭代评审
- 完善迭代报告和测试用例，完成测试报告

### Week Three
2018-7-16
- 增加选择框，为设想的不提供图片而是根据描述特征进行识别搜寻做前端的准备
- 美化前端界面排版
- 解决迭代一遗留的视频播放问题
- 运用Dijkstra算法进行预测算法的设计

2018-7-17
- 了解前端单元测试框架karma,mocha以及react自带的Jest测试框架，开始写单元测试
- 解决直播视频和本地视频的tomcat播放问题
- 整合准备工作：用Java调用写好的Python脚本进行不同电脑之间的信息传输
- 初步完成web项目与信息发送的整合

2018-7-18
- 调整视频播放的格式
- 经过学习比较确定使用Jest+enzyme作为前端测试框架，进行环境配置、版本调整和初步的单元测试编写
- 扩展功能的尝试
