import telebot,os
from time import sleep

dev = [1160471152]

bot = telebot.TeleBot("5550501271:AAGkxuY8-zfx0Xsq1KpJGOEdtYRRuWMAxFw")

def add(message):
	if message.text:
		if str(message.from_user.id) in str(dev):
			add_band = open("banned.txt","a")
			add_band.write(f"{message.text}"+"\n")
			bot.reply_to(message,"تم حظره تدلل سيدي")
			ide = message.text
			name = bot.get_chat(ide).first_name
			for ban in open("members.txt","r").readlines():
				if str(message.from_user.id) in str(ban):
					pass
				else:
					try:
						bot.send_message(ban,f"تم حظر {name}\nبسبب سوء سلوكه او كلامه\nلن يتمكن من ازعاجكم مرة اخرى")
						sleep(3)
					except:
						pass
		else:
			pass

@bot.message_handler(commands=["start"])
def start(message):
	ms = message.text
	id = message.from_user.id
	if message.chat.type == "supergroup":
		pass
	else:
		band = open("banned.txt","r").read()
		
		if str(id) in str(band):
			bot.reply_to(message,"أنت محظور ولن تصل رسالتك لأي شخص\nيالدودة")
		else:
			bot.reply_to(message,"""
مرحبا بك في بوت التواصل الاجتماعي
عند إرسال أي شيء سيصل لكل من هو في البوت
فتأكد بأن الله يراك (;
""")
			members = open("members.txt","r").read()
			if str(message.from_user.id) not in str(members):
				add = open("members.txt","a")
				add.write(str(message.from_user.id)+"\n")

@bot.message_handler(commands=["ban"])
def band(message):
	if str(message.from_user.id) in str(dev):
		done = bot.reply_to(message,"حسنا سيدي ارسل الايدي")
		sleep(1)
		bot.register_next_step_handler(done,add)
	
@bot.message_handler(content_types=['text','photo',"voice","sticker","video","animation","document"])
def content(message):
	ms = message.text
	id = message.from_user.id
	band = open("banned.txt","r").read()
	if message.chat.type == "supergroup":
		pass
		
	else:
		
		if str(id) in str(band):
			bot.reply_to(message,"أنت محظور ولن تصل رسالتك لأي شخص\nيالدودة")
		else:
			if message.text:
				for A in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(A):
						pass
					else:
						try:
							bot.send_message(A,message.text)
							sleep(3)
						except:
							pass
				bot.send_message(1160471152,f"الرسالة: {ms}\nالمرسل: {id}")
		
		
				
			elif message.photo:
				fileID = message.photo[-1].file_id
				for B in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(B):
						pass
					else:
						try:
							bot.send_photo(B,fileID)
							sleep(3)
						except Exception as error:
							pass
				bot.send_photo(1160471152,fileID,caption=f"المرسل: {id}")
				
			elif message.video:
				fileID = message.video.file_id
				for C in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(C):
						pass
					else:
						try:
							bot.send_video(C,fileID)
							sleep(3)
						except:
							pass
				bot.send_video(1160471152,fileID,caption=f"المرسل: {id}")
				
			elif message.sticker:
				fileID = message.sticker.file_id
				for D in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(D):
						pass
					else:
						try:
							bot.send_sticker(D,fileID)
							sleep(3)
						except Exception as error:
							pass
				bot.send_sticker(1160471152,fileID)
				bot.send_message(1160471152,f"المرسل: {id}")
			
			elif message.voice:
				fileID = message.voice.file_id
				for E in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(E):
						pass
					else:
						try:
							bot.send_voice(E,fileID)
							sleep(3)
						except Exception as error:
							pass
				bot.send_voice(1160471152,fileID,caption=f"المرسل: {id}")
			
			elif message.animation:
				fileID = message.animation.file_id
				for F in open("members.txt","r").readlines():
					if str(message.from_user.id) in str(F):
						pass
					else:
						try:
							bot.send_animation(F,fileID)
							sleep(3)
						except:
							pass
				bot.send_animation(1160471152,fileID,caption=f"المرسل: {id}")
			
			else:
				pass
bot.infinity_polling()