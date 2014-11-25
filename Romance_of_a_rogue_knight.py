
# -*- coding: utf-8 -*-
from sys import exit
star_split = '\n' * 10 + "* " * 20
fight_skill = [['平砍', 0, 2]]
enemies = [['土狼',10,5],
]
def skill_gain(skill):
    
    global fight_skill
	
    if skill not in fight_skill:
        print '>>>习得 %s<<<' % skill[0]
        fight_skill.append(skill) 
def fight(enemy):
	health = 50
	mana = 50
	enemy_health = enemy[1]
	while enemy_health > 0:
		print star_split
		print '选择你要用的招式\n\n'
		for num in range(len(fight_skill)):
			print '%d %s    ' % (num + 1,fight_skill[num][0]),
		
		print '\n'
		attack = raw_input('>>>') 

		if int(attack)  not in range(1,len(fight_skill)+1):
			print "请选择有效招式。"
		elif mana < fight_skill[int(attack)-1][1]:
			print "体力不足！请重新选择！"
		else:
			enemy_damage = enemy[2]
			your_damage = fight_skill[int(attack)-1][2]
			print '生命值：%d， 法力值：%d' % (health, mana)
			print "%s 对你造成了 %d 点伤害！" % (enemy[0], enemy_damage)
			print "你对 %s 造成了 %d 点伤害！" % (enemy[0], your_damage)
			mana -= fight_skill[int(attack)-1][1]
			health -= enemy_damage
			enemy_health -= your_damage
			print '生命值：%d， 法力值：%d' % (health, mana)
			if health <= 0:
				print '你输掉了战斗！'
				print '按下q退出游戏，按下其他键再战一次。'
				next = raw_input('>>>')
				if next == 'q':
					exit(0)
				else:
					fight(enemy)
	print star_split
	print '恭喜你战胜了%s！' % enemy[0]

def start():
	print "	欢迎来到剑仙情缘2文字版！"
	print "	这是一个奇妙的世界。"
	print "	祝你玩得开心。"
	print "\t\t——————刘晗"
	print star_split
	print "您可以随时按下q键退出游戏。\n按其余任意键开始游戏~"
	next = raw_input(">>>")

	if next == "q":
		exit(0)
	else:
		home()
def home():
	global star_split
	print star_split
	print """
我叫南宫飞云。
16岁。
我爸是大侠客张如梦，我妈是大美女南宫彩虹。
家里还有黑煞和白煞两个帮手。
可今天的气氛好像有点不对劲.....

	"""


	
	mo_and_fa = False
	black_ghost = False
	white_ghost = False

	while True:
		print '''
你打算找谁聊聊？
1. 父母
2. 黑煞
3. 白煞
4. 四处转一转
5. 不聊，我要出门
'''
		next = raw_input(">>>")
		if next == "1":
			print star_split
			print '''
南宫彩虹： "飞云，你年纪不小了，该出去闯荡闯荡了。"
张如梦  ： "是啊，去发现更大的世界吧。走之前别忘了找
你的黑白双煞俩叔叔道个别。"
南宫彩虹： "对了，飞云，把这个天王令带上，日后自有用处。"

>>>获得 天王令 <<<
好吧。既然赶我走，那我就恭敬不如从命了！

'''

			mo_and_fa = True

		elif next == "2":
			print star_split
			print '''
黑煞： "来来来，飞云，我教你一招\'寒霜掌\'。
此招威力巨大，能极大减缓敌人行动。
看好喽！"
//一道白光从黑煞手中喷射而出，所碰之物皆披白霜。
好厉害的招式!//

呜呜呜，黑煞叔叔最疼我。



			'''
			skill_gain(['寒霜掌',1,3])
			
			black_ghost = True

		elif next == '3':
			print star_split
			print '''
白煞： “飞云，身为一个长者，我有必要向你介绍一些...人生的
经验... ”
我呸。
白煞： “现在，我便将毕生所学传授给你...
看好了！杀意心法！嗬！”
//一片沉寂//
白煞： “这便是杀意心法的全部奥义...飞云啊，
江湖险恶，你要多加提防，时刻注意blablabla...”

我于是就逃走。


			'''

			skill_gain(['杀意心法',0, 0])
			white_ghost = True
		elif next == '4':
			print star_split
			print '''
哦，不错哦，这里有几个箱子。。。
里面果然是钱！蛤蛤~

'''

		elif next == '5':
			if mo_and_fa and black_ghost and white_ghost:
				shazhoucun()
			else:
				print star_split
				print '''
不要急嘛，再兜兜转转~
'''

		elif next == 'q':
			exit(0)
		else:
			print star_split
			print "输入有误。请重新输入。"



killwolves = False
def shazhoucun():
	global killwolves
	print star_split
	print '''
这里便是离家最近的村庄沙洲村了。
一个荒凉的地方，只有寥寥数户和
一间“有间客栈”。
'''
	while True:
		print star_split
		print '''
接下来去干什么？
1. 进客栈看看！
2. 去东边看看吧。
3. 南下去中原。
'''
		next = raw_input('>>>')
		if next == '1' and not killwolves:
			print star_split
			print '''
//黄沙弥漫的客栈里，老板正在柜台前翻看账簿//

老板： “火狼啊火狼。。。托你们的福，又损失了二十两白银。。。”
我暗忖，莫非村子糟了灾？这为民除害的好事，此时不做，更待何时？

我  ： “敢问让掌柜的为之头疼的禽兽可是叫做火狼？”
老板： “正是此兽！毁了我不少财物不说，人命已经被它夺去数条了！”
我  ： “蛤蛤~掌柜的你运气不错，本少侠今天专程为除害而来！”
老板： “少侠此话可当真？火狼就在村东一带，若少侠真能除掉它们，
老夫必有重谢！”
我  ： “老板，你就等我的好消息吧！”

仰天大笑出门去，我辈岂是蓬蒿人。

按下任意键继续。
'''
			
			raw_input('>>>')
		elif next == '1' and killwolves:
			print '''
我  ：“老板！火狼已经被我杀掉了！”
老板: "少侠好身手！这是上好的竹叶
青！尝一尝！"

好酒。。。好酒。。。
'''

		elif next == '2':
			talkwithmaster = True
			kill_fire_wolves()
		elif next == '3' and not killwolves:
			print '''
慌什么~继续逛逛，时间还早~
'''			
			print '* ' * 20

		elif next == '3' and killwolves:
			kuangshazhen()
		elif next == 'q':
			exit(0)
		else:
			print '请正确输入。'
			print '* ' * 20

def kill_fire_wolves():
	global killwolves
	print star_split
	print '''
离开村子一路向东，突然冒出两匹狼！

开战！

按下任意键继续
'''
	fight(enemies[0])
	killwolves = True

	



start()





