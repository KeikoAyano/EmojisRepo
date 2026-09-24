import json
import urllib
import urllib.request
import os
from collections import defaultdict


HEADERS = {
    'User-Agent':
    'Image AutoDownload'
}
payload = {
    "business": "reply",
    "web_location": "333.788"
}
MODULE_NAME = 'BILIBILI'
SAVE_DIR = './emotion/BILIBILI'
URL_DIR = './url/BILIBILI'


def downloadImage(url, save_file_name):
    try:
        req = urllib.request.Request(
        url,
        headers=HEADERS
        )
        rep = urllib.request.urlopen(req)

        with open(save_file_name, 'wb') as img_writer:
            img_writer.write(rep.read())
        return True
    except ValueError as e:
        print(e)
        return False
    except urllib.error.URLError as e:
        print(e)
        return False


def parse_response(data):
    packages = data['data']['packages']
    # save emoji info
    emoji_spec = defaultdict(list)

    for p in packages:
        p_id = p['id']
        p_text = p['text']
        p_url = p['url']
        _, ext = os.path.splitext(p_url)
        # add to emoji info dict
        emoji_spec[p_id].append([p_text, p_url])
        # print package info
        # print(f'{p_id} {p_text} {p_url}')
        
        package_dir = os.path.join(SAVE_DIR, p_text)  # the save dir
        # create sub dir for each group
        os.makedirs(package_dir, exist_ok = True)
        
        # 保存封面表情包
        success = downloadImage(
            p_url,
            os.path.join(package_dir, f'{p_text}{ext}')
        )

        package = p['emote']
        
        for emoji in package:
            e_id = emoji['id']
            e_text = emoji['text']
            e_url = emoji['url']
            _, e_ext = os.path.splitext(p_url)
            e_alias = emoji.get('meta', {}).get('alias', '')
            # save emoji info
            emoji_spec[p_id].append([e_id, e_text, e_url, e_alias])

            # print(f'ID: {e_id}, TEXT: {e_text},URL: { e_url}, ALIAS: {e_alias}')

            # 保存package中的各個表情包
            success = downloadImage(
                e_url,
                os.path.join(package_dir, f'{e_text}{e_ext}')
            )
            
        
        #print(package_list)
        #break

    with open(os.path.join(URL_DIR, "EMOJI_SPEC.json"), mode = 'w', encoding='UTF-8') as writer:
        json.dump(dict(emoji_spec), writer)

        
if __name__ == '__main__':
    os.makedirs(SAVE_DIR, exist_ok= True)

    '''
    https://api.bilibili.com/x/emote/user/panel/web?business=reply&web_location=333.788
    query string
    business: reply
    web_location: 333.788
    '''


    with open(os.path.join(URL_DIR, "emoji.json"), mode = 'r', encoding = 'UTF-8') as fp:
        data = json.load(fp)
    parse_response(data)

