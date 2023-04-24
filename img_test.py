import json
import requests
headers = {
    "Authorization":"Bearer ya29.a0Ael9sCOd-eNjqbUqOf4_OOv4ZdPYcEMiMATjC30HMdSWizCA3bz06zwwFVfmkLdiERzKl-oA8WzrXWBTM-5Udh0_gxwa_KUaknksL3mSoM6lYmS55HNlQEV40tF-QvVs9pOhyic_Aor7KOvp1FATO_IRs-wDaCgYKAR8SARASFQF4udJh1zXBNabExech2zvmgOo--g0163"
}

para = {
    "name":"img.jpg",
    "parents":["1i4uf7IAag480KyVdYEx_NATwlDDoO3qg"]
}

files = {
    'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),
    'file':open('./img.jpg','rb')
}

r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)