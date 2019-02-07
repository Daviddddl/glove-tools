from pyltp import Segmentor

ltp_model_path = '/home/david/PycharmProjects/PERQA/ltp_data_v3.4.0/cws.model'
segmentor = Segmentor()
segmentor.load(ltp_model_path)
words = segmentor.segment('啊啊啊，你好啊，请问你是谁啊？')
# print("|".join(words))        # 啊|啊|啊|，|你好|啊|，|请问|你|是|谁|啊|？
segmentor.release()
