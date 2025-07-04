## 项目简介  About the Project

这是一个辅助空洞骑士BP赛制下挑选护符和上锁的小工具

An assistant tool for picking charms and bindings based on BP rules for a Hollow Knight Competition

BP赛赛制参考文件: https://docs.qq.com/doc/DQXdXdkpEcWp5Tmxm

BP rules (Chinese only): https://docs.qq.com/doc/DQXdXdkpEcWp5Tmxm


$${\color{red} 想直接使用工具，可以单独下载压缩包 2025\_BP\_Tool\_v1.1.zip }$$


## 开发工具  Built with

* python 3.13
 
* Qt Designer 5.11.1
 

## 使用指南 Usage

* 使用过程请参考视频 Demo.mp4

* 下方"当前操作"窗口里的也是使用步骤

* 先手队伍选择：第一局的先手队伍必须手动选择。 开始第二局BP时，先手队伍会自动变成对面，可手动更改。 第三局的先手队伍也必须手动选择。

* 每点选一个护符，都会有相应的护符槽数被点亮，控制单轮护符槽上限时，需要操作者自行计算

+ 当一方护符槽满了，推荐的做法是让对面一口气选完剩下的所有护符，点击"确认选择"后，即可开始下一局 （不然需要手动轮空一些步骤，增加了不必要的动作）


自定义队伍名和队员名:

* 修改Text文件夹下Team_1.json，Team_2.json，Team_3.json，Team_4.json的内容
 
* 目前只预留了四个队伍的位置，当队伍数量大于四，需要手动替换以上文件内容
 

自定义护符槽(强化Mod玩家可用):

* 修改Text文件夹下的CharmData.json
 
* 护符槽是每行notch_X对应的内容
 
* 请不要改变charm_X对应的内容
 

## Trouble-shooting

* 每一次操作后都需要点击"确认选择"按钮，进入下一个步骤

* 每一轮是选择一个还是多个护符，全凭操作者自行控制

* 每一队护符只能显示最多11个，超出的会被自动忽略

* 不可连续点击"确认操作"按钮，每次点击应当在音效播放结束后进行

* 窗口最大为1920x1080，如出现窗口显示不完全的问题，请检查显示器分辨率和应用缩放比例
