一个辅助空洞骑士BP赛制下挑选护符和上锁的小工具
An assistant tool for picking charms and bindings based on BP tournament rules for Hollow Knight Competition

BP赛赛制参考文件: https://docs.qq.com/doc/DQXdXdkpEcWp5Tmxm
BP tournament rules (Chinese only): https://docs.qq.com/doc/DQXdXdkpEcWp5Tmxm

想直接使用工具，可以单独下载压缩包 2025_BP_v1.0,zip
开发工具及版本号:
	python 3.13
	Qt Designer 5.11.1

自定义文件名:
	修改Text文件夹下Team_1.json，Team_2.json，Team_3.json，Team_4.json的内容
	目前只预留了四个队伍的位置，当队伍数量大于四，需要手动替换以上文件内容

自定义护符槽:
	修改Text文件夹下的CharmData.json
	护符槽是每行notch_X对应的内容
	请不要改变charm_X对应的内容

Trouble-shooting
1. 每一次操作后都需要点击"确认选择"按钮，进入下一个步骤
2. 每一轮是选择一个还是多个护符，全凭操作者自行控制
3. 每一队护符只能显示最多11个，超出的会被自动忽略
4. 不可连续点击"确认操作"按钮，每次点击应当在音效播放结束后进行
4. 窗口大小固定1920x1080，如出现窗口显示不完全的问题，请检查显示器分辨率和应用缩放比例

使用步骤请参考视频 Demo.mp4