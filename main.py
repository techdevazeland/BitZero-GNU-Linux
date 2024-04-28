import time
from telethon import events, utils, Button
import asyncio
from telethon.sync import TelegramClient
from telethon.tl import types
import time
from FastTelethon import download_file, upload_file
import random
import requests
from bs4 import BeautifulSoup
import os
import base64
import shutil
import re
import threading
import aiohttp
bitzero = 1
proxy = ""
process = 0

#DATOS-ADMIN
host = "https://revinfcientifica.sld.cu/index.php/ric/"
username = "techdev"
password = "@A1a2a3mo"
repository = "4647"
devname = "TechDev"
devusername = "l_tech_dev_l"
user_id_admin = 5692000351
api_id = 9024532
api_hash = "131b576240be107210aace99a5f5c5b0"
token = "6850777466:AAG1ATsgL-Ev1w7mzblW3DI5ndD801IPbeg"


users = [user_id_admin]
key = base64.b64encode(host.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(username.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(password.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(str(repository).encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")
if not os.path.exists("users"):
    os.mkdir("users")
for u in users:
    if not os.path.exists("users/"+str(u)):
        os.mkdir("users/"+str(u))
        open("users/"+str(u)+"/plan","w").write("1073741824000")
        open("users/"+str(u)+"/used","w").write("0")
    else:
        open("users/"+str(u)+"/used","w").write("0")
cola_download = []
cola_global = []
users_urls = []
for u in users:
    cola_download.append({"user":u,"cola":[], "vip":0})
    users_urls.append({"user":u,"urls":[]})
session = requests.Session()
logindata = {"username":username,"password":password}
login = session.post(host+"/login/signIn",data=logindata,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
print("SESIÓN INICIADA")
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)
def unlink(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
def upload_div(ruta_archivo,tamano_parte_mb):
    tamano_parte_bytes = tamano_parte_mb * 1024 * 1024
    lista_archivos_divididos = []
    tamano_archivo = os.path.getsize(ruta_archivo)
    if tamano_archivo < tamano_parte_bytes:
        lista_archivos_divididos.append(ruta_archivo)
    else:
        with open(ruta_archivo, 'rb') as archivo_original:
            numero_parte = 1
            while True:
                contenido_parte = archivo_original.read(tamano_parte_bytes)
                if not contenido_parte:
                    break
                nombre_parte = f"{ruta_archivo}_parte_{numero_parte}"
                with open(nombre_parte, 'wb') as archivo_parte:
                    archivo_parte.write(contenido_parte)
                lista_archivos_divididos.append(nombre_parte)
                numero_parte += 1
    return lista_archivos_divididos
def upload(host, username, password, repo,session, path, proxy=""):
            global bitzero
            patho = path
            if not os.path.exists("temp"):
                os.mkdir("temp")
            if bitzero == 1:
                spypng = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178U\x00\x00\x00\x00IEND\xaeB`\x82'
                open("temp/"+path+f"_@bitzero.png","wb").write(spypng+open(path,"rb").read())
                path = "temp/"+path+f"_@bitzero.png"
            elif bitzero == 2:
                spypng = '<!DOCTYPE html>\n<html lang="es">\n<bytes>'
                spypng2 = '</bytes></html>'
                with open(path, 'rb') as file:
                    bytes_data = file.read()
                    base64_data = base64.b64encode(bytes_data).decode('utf-8')
                open("temp/"+path+f"_@bitzero.html","w").write(spypng+base64_data+spypng2)
                path = "temp/"+path+f"_@bitzero.html"
            elif bitzero == 3:
                spypng = open("blank.docx","rb").read()
                open("temp/"+path+f"_@bitzero.docx","wb").write(spypng+open(path,"rb").read())
                path = "temp/"+path+f"_@bitzero.docx"
            else:
                None
            data = {"articleId":repo,"from":"","title[es_ES]":random.randint(100000,999999),"creator[es_ES]":"TechDev","subject[es_ES]":"","type":"Herramienta de investigación","typeOther[es_ES]":"","description[es_ES]":"Subido por TechDev","publisher[es_ES]":"","sponsor[es_ES]":"TechDev","dateCreated":"","source[es_ES]":"","language":"es"}
            filek = {"uploadSuppFile": open(path,"rb")}
            upFile = session.post(host+"/author/saveSuppFile?path=",data=data,files=filek,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
            getLink = session.get(host+"/author/submission/"+repo,proxies=dict(http=proxy,https=proxy))
            soup = BeautifulSoup(getLink.text, "html.parser")
            entradas = soup.find_all('a',{'class':'file'})
            regex1 = str(entradas).split(",")
            regex2 = regex1[-1]
            regex3 = regex2.replace("]","")
            regex4 = regex3.split("-")[1]
            getid = session.get(host+"/author/submit/4?articleId="+repository)
            soup = BeautifulSoup(getid.text, 'html.parser')
            ultimo_tr = soup.find_all('tr', {'valign': 'top'})[-1]
            primer_td = ultimo_tr.find('td')
            unlink(path)
            textid = primer_td.text
            ides = textid+"-"+regex4
            return ides
async def download_link(url, msg):
    size=0
    timed = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                file_size = response.headers.get('Content-Length')  # Tamaño del archivo
                try:
                    file_name = response.headers.get('Content-Disposition').split('"')[1]  # Nombre original del archivo
                except:
                    file_name = url.split('/')[-1]
                with open(file_name, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        size+=1024
                        if time.time() - timed > 1.0:
                            timed = time.time()
                            porcentaje = (size/int(file_size))*100
                            if os.path.exists(str(ide)):
                                await msg.edit(f"<b>⬇️ DESCARGANDO</b> {round(porcentaje,2)}%\n\n<code>{file_name}</code>", parse_mode="HTML", buttons=[Button.inline("× CANCELAR ×", data=b'cancel|'+str(ide).encode('utf-8'))])
                            else:
                                os.unlink(file_name)
                                return "close"
                                break
                        if not chunk:
                            break
                        f.write(chunk)
                    os.unlink(str(ide))
                    return file_name
async def upload_path(path, msg, session, idek):
    await msg.edit("📚", parse_mode="HTML")
    archivos = upload_div(path, 10)
    code = []
    await msg.edit(f"<b>⬆️SUBIENDO</b> <i>0%</i>\n\n<code>{path.split('/')[-1]}</code>", buttons=[Button.inline("× CANCELAR ×", data=b'cancel|'+idek.encode("utf-8"))], parse_mode="HTML")
    current = 1
    for f in archivos:
        if not os.path.exists(idek):
            return "close"
            print(x)
        cola_global[0]["info"] = "upload/"+str(current-1)+"/"+str(len(archivos))
        await msg.edit(f"<b>⬆️SUBIENDO</b> <i>{round(((current-1)/len(archivos))*100,2)}%</i>\n\n<code>{path.split('/')[-1]}</code>",buttons=[Button.inline("× CANCELAR ×", data=b'cancel|'+idek.encode("utf-8"))], parse_mode="HTML")
        ide = upload(host,username,password,repository, session, f)
        code.append(ide)
        current += 1
    kcode = str(bitzero)+"/"+'_'.join(code)+"/"+str(base64.b64encode(path.split("/")[-1].encode('utf-8')).decode('utf-8'))+"/"+str(os.path.getsize(path))+"/"+key
    if len(archivos) > 1:
        os.unlink(path)
    return kcode

client = TelegramClient("bF", api_id, api_hash)

client.start(bot_token=token)

class Timer:
    def __init__(self, time_between=2):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False
@client.on(events.NewMessage())
async def download_or_upload(event):
    global users
    global host
    global username
    global password
    global repository
    global process
    global devname
    global devusername
    global cola_global
    global cola_download
    text = event.raw_text
    user_id = event.message.chat.id
    msg_id = event.message.id
    username = event.message.chat.username
    cd = "./"
    if not os.path.exists(cd):
        os.mkdir(cd)
    type_of = ""
    msg = None
    user_cola = 0
    for c in cola_download:
        if user_id == c["user"]:
            break
        else:
            user_cola += 1
    timer = Timer()
    if "/start" in text and user_id in users:
        plan = int(open("users/"+str(user_id)+"/plan","r").read())
        used = int(open("users/"+str(user_id)+"/used","r").read())
        await client.send_file(user_id, file="start.png",caption=f"<b>BITFAST • TechDev</b>\n\n<code>🥇 El mejor sistema de descargas alquiladas administrado por {devname}.</code>\n\n<i>En este bot contamos con la cantidad de {len(users)} usuario/s</i>\n\n<b>👤 - @{username} - {user_id}:</b>\n<i>Usado:</i> <code>{sizeof_fmt(used)}/{sizeof_fmt(plan)}</code>",buttons=[[Button.url("📞 Administrador", url=f"https://t.me/{devusername}")],[Button.inline("🎫 Eventos", data=b'eventos|'),Button.inline("🎓 Tutorial", data=b'tutorial|')]], parse_mode="HTML")
    elif "/start" in text and not user_id in users:
        await client.send_file(user_id, file="start.png",caption=f"<b>BITFAST • TechDev</b>\n\n<code>🥇 El mejor sistema de descargas alquiladas administrado por {devname}</code>\n\n<b>👤 - @{username} - {user_id}:</b>\n<i>Aprovecha y compra un plan ahora.</i>", buttons=[Button.url("🛒 ¡¡Comprar Plan!!", url=f"https://t.me/{devusername}")], parse_mode="HTML")
    elif "/cpanel" in text and user_id==users[0]:
        await event.reply("<b>PANEL DE CONTROL</b>\n\n<code>Escoga una de las siguientes opciones para administrar el sistema.</code>", buttons=[[Button.inline("👥️ MIS USUARIOS",data=b'users|')],[Button.inline("🗑️ LIMPIAR NUBE",data=b'clean|')]], parse_mode="HTML")
    elif "/promo " in text and user_id==users[0]:
        for u in users:
            await client.send_message(u, text.replace("/promo ",""), parse_mode="HTML")
    elif "/clean" in text and user_id==users[0]:
        msg = await event.reply("<b>SISTEMA DE LIMPIEZA</b>\n\n<code>Limpiando página, espere...</code>", parse_mode="HTML")
        ver = session.get(host)
        if "Salir" in ver.text or "Log Out" in ver.text:
            None
        else:
            logindata = {"username":username,"password":password}
            login = session.post(host+"/login/signIn",data=logindata,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
        web = session.get(host+"/author/submit/4?articleId="+repository)
        soup = BeautifulSoup(web.text, 'html.parser')
        urls = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.match('^https?://', href):
                urls.append(href)
        for u in urls:
            if "delete" in u:
                session.get(u,headers={"x-http-method-override": "DELETE","x-requested-with":"XMLHttpRequest"})
        await client.delete_messages(user_id, msg.id)
        for u in users:
            await client.send_message(u, "<b>☁️ Se ha limpiado la nube</b>", parse_mode="HTML")
    elif "/users" in text and user_id == users[0]:
        us = ""
        for a in users:
            used = int(open("users/"+str(a)+"/used","r").read())
            us += f"<code>{a} - {sizeof_fmt(used)}</code>\n"
        await event.reply(f"<b>USUARIOS DEL BOT:</b>\n\n"+us, parse_mode="HTML")
    elif "/deluser " in text and user_id == users[0]:
        user = int(text.replace("/deluser ",""))
        users.remove(user)
        unlink("users/"+str(user))
        await event.reply("<b>Borrado</b>", parse_mode="HTML")
    elif "/setuser " in text and user_id == users[0]:
        bits = text.replace("/setuser ","").split(" ")
        user_id = int(bits[0])
        gb = int(bits[1])*1024*1024*1024
        users.append(int(bits[0]))
        if "vip" in text:
            vip = 1
        else:
            vip = 0
        cola_download.append({"user":user_id,"cola":[],"vip":vip})
        users_urls.append({"user":u,"urls":[]})
        if not os.path.exists("users/"+str(user_id)):
            os.mkdir("users/"+str(user_id))
            open("users/"+str(user_id)+"/plan","w").write(str(gb))
            open("users/"+str(user_id)+"/used","w").write("0")
        else:
         open("users/"+str(user_id)+"/plan","w").write(str(gb))
        await client.send_message(user_id, f"<b>Su plan ahora es de </b><code>{sizeof_fmt(gb)}</code>", parse_mode="HTML")
        await event.reply(f"<code>Se modificó y avisó al usuario de la compra de un plan de {sizeof_fmt(gb)}</code>", parse_mode="HTML")
    elif ("http://" in text or "https://" in text) and not (" https://" in text or " http://" in text) and user_id in users:
	    url = text
	    msg = await event.reply("✨")
	    ide = str(random.randint(10000,99999))
	    cola_global.append({"ide":ide, "info":"none"})
	    open(ide, "w").write("1")
	    timek = time.time()
	    espera = True
	    while True:
	                   if not cola_global[0]["ide"] == ide:
	                       if cola_global[0]["info"] == "none":
	                           times = str(round(time.time()-timek,2)).split(".")[0]
	                           await msg.edit(f"<b>✨ COLA GLOBAL [{ide}]</b>\n\n<code>Calculando procesos...</code>\n\n⌛Tiempo: {times}s", buttons=[Button.url("⚡OPTIMIZAR A VIP",url=f"https://t.me/{devusername}")], parse_mode="HTML")
	                           await asyncio.sleep(3)
	                       else:
	                           info = cola_global[0]["info"]
	                           type = ""
	                           if info.split("/")[0] == "download":
	                               type = "⬇️ DESCARGANDO... "
	                           elif info.split("/")[0] == "upload":
	                               type = "⬆️ SUBIENDO... "
	                           porcentaje = round((int(info.split("/")[1])/int(info.split("/")[2]))*100,2)
	                           process = 0
	                           times = str(round(time.time()-timek,2)).split(".")[0]
	                           for p in cola_global:
	                               if p["ide"] == ide:
	                                   break
	                               else:
	                                   process += 1
	                           await msg.edit(f"<b>✨ COLA GLOBAL [{ide}]</b>\n\n<code>Esperando por ({process}) procesos...</code>\n\n<i>{type}{porcentaje}%</i>\n\n⌛Tiempo: {times}s", buttons=[Button.url("⚡OPTIMIZAR A VIP",url=f"https://t.me/{devusername}")], parse_mode="HTML")
	                           await asyncio.sleep(3)
	                   else:
	                       break
	    try:
	                name = await download_link(url, msg)
	                await msg.edit(f"⌛", parse_mode="HTML")
	                await asyncio.sleep(3)
	                if name == "close":
	                    await msg.edit(f"❌", parse_mode="HTML")
	                    cola_global.pop(0)
	                    return
	                await msg.edit(f"✨", parse_mode="HTML")
	                filesize = os.path.getsize(name)
	                code = await upload_path(name, msg, session,ide)
	                if code == "close":
	                    await msg.edit("<b>Se detuvo la subida</b>", parse_mode="HTML")
	                    cola_global.pop(0)
	                    return
	                dcode = random.randint(100000,999999)
	                open(str(dcode), "w").write(code.split("/")[1])
	                bytes_code = str(dcode).encode("utf-8")
	                await msg.edit(f"<b>🟢 Se completó el proceso</b>\n\n<i><b>📛Nombre: </b></i><code>{name}</code>\n<i><b>⚖️Tamaño: </b></i><code>{sizeof_fmt(filesize)}</code>\n\n<b>📋Pulse para copiar:</b>\n\n<code>bitfast {code}</code>", buttons=[Button.inline("🗑️ ELIMINAR", data=b'delete|'+bytes_code)], parse_mode="HTML")
	                for u in users_urls:
	                    if u["user"] == user_id:
	                        u["urls"].append(code)
	                plan = int(open("users/"+str(user_id)+"/plan","r").read())
	                used = int(open("users/"+str(user_id)+"/used","r").read())
	                open("users/"+str(user_id)+"/used","w").write(str(used+filesize))
	                cola_global.pop(0)
	                try:
	                    unlink(name)
	                except:
	                    None
	                if (used+filesize) >= plan:
	                    users.remove(user_id)
	                    await client.send_message(user_id, "<b>Usted ya sobrepasó su plan, para seguir usando el bot compre otro plan.</b>", parse_mode="HTML")
	    except:
	                await msg.edit(f"<b>❌ ERROR DESCONOCIDO</b>", parse_mode="HTML")
    elif event.document and user_id in users:
        msg = await event.reply("✨", parse_mode="HTML")
        ide = str(random.randint(10000,99999))
        cola_global.append({"ide":ide, "info":"none"})
        open(ide, "w").write("1")
        timek = time.time()
        espera = True
        while True:
            if not cola_global[0]["ide"] == ide:
                    if cola_global[0]["info"] == "none":
                        times = str(round(time.time()-timek,2)).split(".")[0]
                        await msg.edit(f"<b>✨ COLA GLOBAL [{ide}]</b>\n\n<code>Calculando procesos...</code>\n\n⌛Tiempo: {times}s", buttons=[Button.url("⚡OPTIMIZAR A VIP",url=f"https://t.me/{devusername}")], parse_mode="HTML")
                        await asyncio.sleep(3)
                    else:
                        info = cola_global[0]["info"]
                        type = ""
                        if info.split("/")[0] == "download":
                            type = "⬇️ DESCARGANDO... "
                        elif info.split("/")[0] == "upload":
                            type = "⬆️ SUBIENDO... "
                        porcentaje = round((int(info.split("/")[1])/int(info.split("/")[2]))*100,2)
                        process = 0
                        times = str(round(time.time()-timek,2)).split(".")[0]
                        for p in cola_global:
                            if p["ide"] == ide:
                                break
                            else:
                                process += 1
                        await msg.edit(f"<b>✨ COLA GLOBAL [{ide}]</b>\n\n<code>Esperando por ({process}) procesos...</code>\n\n<i>{type}{porcentaje}%</i>\n\n⌛Tiempo: {times}s", buttons=[Button.url("⚡OPTIMIZAR A VIP",url=f"https://t.me/{devusername}")], parse_mode="HTML")
                        await asyncio.sleep(3)
            else:
                break
        ver = session.get(host)
        if "Salir" in ver.text or "Log Out" in ver.text:
            None
        else:
            logindata = {"username":username,"password":password}
            login = session.post(host+"/login/signIn",data=logindata,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
        caption = event.message.message
        mime_type = str(event.media.document.mime_type)
        extension = mime_type.split("/")[1]
        if event.file.name:
            name = event.file.name
        else:
            if caption:
                name = str(caption).split("\n")[0]+"."+extension
            else:
                name = "document_"+str(time.strftime("%d_%H_%M_%S"))+"."+extension
        async def progress_bar(current, total):
            global process
            if os.path.exists(ide):
                if timer.can_send():
                    cola_global[0]["info"] = "download/"+str(current)+"/"+str(total)
                    await client.edit_message(user_id, msg.id, f"<b>⬇️ DESCARGANDO</b> {round(current * 100 / total,2)}%\n\n<code>{name}</code>", parse_mode="HTML", buttons=[Button.inline("× CANCELAR ×", data=b'cancel|'+ide.encode('utf-8'))])
                    timed = time.time()
            else:
                await client.edit_message(user_id, msg.id, f"<b>× CANCELADO ×</b>\n\n<code>{name}</code>", parse_mode="HTML")
                cola_global.pop(0)
                os.unlink(name)
                return
        with open(name, "wb") as out:
            await download_file(event.client, event.document, out, progress_callback=progress_bar)
        filesize = os.path.getsize(name)
        await msg.edit("✨️")
        await asyncio.sleep(3)
        code = await upload_path(name, msg, session, ide)
        if code == "close":
            await msg.edit("<b>Se detuvo la subida</b>", parse_mode="HTML")
            os.unlink(ide)
            cola_global.pop(0)
            return
        dcode = random.randint(100000,999999)
        open(str(dcode), "w").write(code.split("/")[1])
        bytes_code = str(dcode).encode("utf-8")
        if user_id == users[0]:
            await msg.edit(f"<b>🟢 Se completó el proceso</b>\n\n<i><b>📛Nombre: </b></i><code>{name}</code>\n<i><b>⚖️Tamaño: </b></i><code>{sizeof_fmt(filesize)}</code>\n\n<b>📋Pulse para copiar:</b>\n\n<code>bitfast {code}</code>", buttons=[[Button.url("⬇️ Descargar (BitNav)", url=f"http://127.0.0.1:8181/newurl?code={code.replace(' ','+')}")],[Button.inline("🗑️ ELIMINAR", data=b'delete|'+bytes_code)]], parse_mode="HTML")
        else:
            await msg.edit(f"<b>🟢 Se completó el proceso</b>\n\n<i><b>📛Nombre: </b></i><code>{name}</code>\n<i><b>⚖️Tamaño: </b></i><code>{sizeof_fmt(filesize)}</code>\n\n<b>📋Pulse para copiar:</b>\n\n<code>bitfast {code}</code>", buttons=[[Button.inline("🗑️ ELIMINAR", data=b'delete|'+bytes_code)]], parse_mode="HTML")
        plan = int(open("users/"+str(user_id)+"/plan","r").read())
        used = int(open("users/"+str(user_id)+"/used","r").read())
        open("users/"+str(user_id)+"/used","w").write(str(used+filesize))
        os.unlink(ide)
        cola_global.pop(0)
        try:
            unlink(name)
        except:
            None
        if (used+filesize) >= plan:
            users.remove(user_id)
            await client.send_message(user_id, "<b>Usted ya sobrepasó su plan, para seguir usando el bot compre otro plan.</b>", parse_mode="HTML")
    elif not user_id in users:
        await client.send_message(users[0], "<b>El usuario @"+username+" (<code>"+str(user_id)+"</code>) presionó el botón de inicio, desea darle prueba?</b>", buttons=[[Button.inline("🎁 REGALAR 500MiB", data=b'regalo|'+str(user_id).encode("utf-8")+b'|500M')],[Button.inline("🎁 REGALAR 1GiB", data=b'regalo|'+str(user_id).encode("utf-8")+b'|1G')],[Button.inline("🎁 REGALAR 5GiB", data=b'regalo|'+str(user_id).encode("utf-8")+b'|5G')]],parse_mode="HTML")
        await client.send_file(user_id, file="start.png",caption=f"<b>BITFAST • TechDev</b>\n\n<code>🥇 El mejor sistema de descargas alquiladas administrado por {devname}</code>\n\n<b>👤 - @{username} - {user_id}:</b>\n<i>Aprovecha y compra un plan ahora.</i>", buttons=[Button.url("🛒 ¡¡Comprar Plan!!", url=f"https://t.me/{devusername}")], parse_mode="HTML")
@client.on(events.CallbackQuery)
async def callback_query(event):
    user_id = event.query.user_id
    msg_id = event.query.msg_id
    data = event.query.data.decode("utf-8")
    orden = str(data).split("|")[0]
    if orden == "clean":
        msg = await client.send_message(user_id,"<b>SISTEMA DE LIMPIEZA</b>\n\n<code>Limpiando página, espere...</code>", parse_mode="HTML")
        ver = session.get(host)
        if "Salir" in ver.text or "Log Out" in ver.text:
            None
        else:
            logindata = {"username":username,"password":password}
            login = session.post(host+"/login/signIn",data=logindata,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
        web = session.get(host+"/author/submit/4?articleId="+repository)
        soup = BeautifulSoup(web.text, 'html.parser')
        urls = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.match('^https?://', href):
                urls.append(href)
        for u in urls:
            if "delete" in u:
                session.get(u,headers={"x-http-method-override": "DELETE","x-requested-with":"XMLHttpRequest"})
        await client.delete_messages(user_id, msg.id)
        for u in users:
            await client.send_message(u, "<b>☁️ Se ha limpiado la nube</b>", parse_mode="HTML")
    if orden == "eventos":
        await client.edit_message(user_id, msg_id, "<i>No hay eventos disponibles actualmente...</i>", parse_mode="HTML")
    if orden == "tutorial":
        await client.edit_message(user_id, msg_id, "<i>Proximamente...</i>", parse_mode="HTML")
    if orden == "delete":
        code = str(data).split("|")[1]
        surl = open(code, "r").read()
        os.unlink(code)
        await client.edit_message(user_id, msg_id, "❌")
        if "_" in surl:
            urls = surl.split("_")
        else:
            urls = [surl]
        for url in urls:
            session.get(host+"/author/deleteSubmitSuppFile/"+url.split("-")[0]+"?articleId="+repository,headers={"x-http-method-override": "DELETE","x-requested-with":"XMLHttpRequest"})
    if orden == "cancel":
        await client.edit_message(user_id, msg_id, "❌")
        os.unlink(str(data).split("|")[1])
print("CONECTADO")
client.run_until_disconnected()