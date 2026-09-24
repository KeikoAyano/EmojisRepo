import os
from urllib import error, parse, request

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

class TiebaEmotion:
    def regularEmotion(self, spath):
        '''
        默认表情
        '''
        second_dir = os.path.join(spath, 'regular')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/editor/images/client/image_emoticon{}.png'.format(i)
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))

    def regulargif(self, spath):
        '''默认表情（补充)'''
        second_dir = os.path.join(spath, 'regular')

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 100):
            # url = 'https://tb2.bdstatic.com/tb/editor/images/face/i_f{}.png'.format(i)
            url = 'https://tb2.bdstatic.com/tb/editor/images/face/i_f{}.gif'.format(i)
            fname = os.path.join(second_dir, url.split('/')[-1])

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))

    def bearchildren(self, spath):
        '''熊孩子表情系列'''
        second_dir = os.path.join(spath, 'bearchildren')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 100):
            url = 'https://tb2.bdstatic.com/tb/editor/images/bearchildren/bearchildren_{:0>2d}.gif'.format(i)
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def tiexing(self, spath):
        '''痒小贱表情系列'''
        second_dir = os.path.join(spath, 'tiexing')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 80):
            url = 'https://tb2.bdstatic.com/tb/editor/images/tiexing/tiexing_{:0>2d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def ali(self, spath):
        '''阿狸表情系列'''
        second_dir = os.path.join(spath, 'ali')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/ali/ali_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def luoluobu(self, spath):
        '''罗罗布表情系列'''
        second_dir = os.path.join(spath, 'luoluobu')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/luoluobu/llb_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def qpx(self, spath):
        '''气泡🐻表情系列'''
        second_dir = os.path.join(spath, 'qpx_n')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 100):
            url = 'https://tb2.bdstatic.com/tb/editor/images/qpx_n/b{:0>2d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def xyj(self, spath):
        '''小幺🐓表情系列'''
        second_dir = os.path.join(spath, 'xyj')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/xyj/xyj_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def lt(self, spath):
        '''冷🐇表情系列'''
        second_dir = os.path.join(spath, 'lt')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/lt/ltn_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def bfmn(self, spath):
        '''白发魔女表情系列'''
        second_dir = os.path.join(spath, 'bfmn')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/bfmn/bfmn_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def pczxh(self, spath):
        '''张小盒表情系列'''
        second_dir = os.path.join(spath, 'pczxh')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 200):
            url = 'https://tb2.bdstatic.com/tb/editor/images/pczxh/zxh_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def tsj(self, spath):
        '''🐇斯基表情系列'''
        second_dir = os.path.join(spath, 'tsj')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/tsj/t_{:0>4d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def wdj(self, spath):
        '''豌豆荚表情系列'''
        second_dir = os.path.join(spath, 'wdj')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/wdj/wdj_{:0>2d}.png'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def lxs(self, spath):
        '''冷先森表情系列'''
        second_dir = os.path.join(spath, 'lxs')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/lxs/lxs_{:0>3d}.gif'.format(i)

            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def baodong(self, spath):
        '''暴漫静态表情系列'''
        second_dir = os.path.join(spath, 'baodong')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/baodong/b_{:0>4d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def baodong_d(self, spath):
        '''暴漫动态表情系列'''
        second_dir = os.path.join(spath, 'baodong_d')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 50):
            url = 'https://tb2.bdstatic.com/tb/editor/images/baodong_d/bd_{:0>4d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def bobo(self, spath):
        '''波波表情系列'''
        second_dir = os.path.join(spath, 'bobo')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 100):
            url = 'https://tb2.bdstatic.com/tb/editor/images/bobo/B_{:0>4d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def shadow(self, spath):
        '''影子表情系列'''
        second_dir = os.path.join(spath, 'shadow')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/shadow/yz_{:0>3d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def ldw(self, spath):
        '''绿🐸表情系列'''
        second_dir = os.path.join(spath, 'ldw')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 60):
            url = 'https://tb2.bdstatic.com/tb/editor/images/ldw/w_{:0>4d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))
    
    def tenth(self, spath):
        '''十周年表情系列'''
        second_dir = os.path.join(spath, '10th')  # 二级保存目录

        if not os.path.exists(second_dir):
            os.mkdir(second_dir)

        for i in range(1, 20):
            url = 'https://tb2.bdstatic.com/tb/editor/images/10th/10th_{:0>3d}.gif'.format(i)
            
            # 获取保存的图片名称
            fname = os.path.join(second_dir, url.split('/')[-1])
            if os.path.exists(fname):
                continue

            try:
                response = request.Request(url=url, headers=HEADERS)
                r = request.urlopen(response)

                with open(fname, 'wb') as fp:
                    fp.write(r.read())
                    print('正在保存{}'.format(fname))
            except error.URLError:
                print("第{}条保存失败".format(i))