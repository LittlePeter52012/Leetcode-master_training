# 计算及网络体系架构
![](2022-05-18-11-06-05.png)

1. **五层协议**

- **应用层：**为特定应用程序提供数据传输服务，例如`HTTP`、`DNS`等协议。数据单位为报文。
- **传输层：**为进程提供通用数据传输服务。由于应用层协议很多，定义通用的传输协议就可以支持不断增多的应用层协议。运输层包括两种协议：
  1. 传输控制协议`TCP`，提供面向链接、可靠的数据传输服务，数据单位为报文段；
  2. 用户数据报协议UDP，提供无连接，尽最大努力的数据传输服务，数据单位为用户数据报。
  - TCP主要提供完整性服务，UDP主要提供及时性服务。
- **网络层：**为主机提供数据传输服务。而**传输层协议**是为主机中的**进程**提供数据传输服务。网络层把传输层传递下来的报文段或者用户数据报封装给分组。
- **数据链路层：**网络层针对的还是主机之间的数据传输服务，而主机之间可以有很多链路，链路层协议就是为同一链路的主机提供数据传输服务。**数据链路层把网络层传下来的分组封装成帧。**
- **物理层：**考虑的是怎样在传输媒体上传输数据比特流，而不是指具体的传输媒体。物理层的作用是尽可能屏蔽传输媒体和通信手段的差异，使数据链路层感觉不到这些差异。

2. **OSI**

其中表示层和会话层用途如下：
- `表示层：`数据压缩，加密以及数据描述，这使得应用程序不必关心在各台主机中数据内部格式不同的问题。
- `会话层：`建立及管理会话。

> 五层协议没有表示层和会话层，而是将这些功能留给应用程序开发者处理。

3. **TCP/ IP**
只有四层，相当于五层协议中数据链路层和物理层合并为**网络接口层**。
TCP/ IP体系结构不严格遵循`OSI`分层概念，应用层可能会直接使用IP层或者网络接口层。
![](2022-05-20-00-07-05.png)

4. **数据在各层之间的传递过程**
在向下的过程中，需要添加下层协议所需要的首部或尾部，而向上的过程中，不断拆开首部和尾部。
  - 路由器只有下面三层协议，因为路由器位于网络核心中，不需要为进程或者应用程序提供服务，因此也就不需要传输层和应用层。