import base64
import csv
import requests
from time import sleep

row_file_word = "/Users/shiyuchen/Downloads/mdd_rhino_words_160ms.csv"
row_file_sen = "/Users/shiyuchen/Downloads/mdd_rhnoi_sen_160_eh.csv"
new_file_word = '/Users/shiyuchen/Downloads/class-online/words.csv'



path = '/Users/shiyuchen/Downloads/class-online/test.wav'
csv_path = '/Users/shiyuchen/Downloads/class-online/test.csv'

f= open(path,'rb+')

chunksize = 2*1024



def radio_to_csv():
    with open(path, 'rb') as f:
        with open(csv_path, 'w') as csvfile:
            while True:
                chunk = f.read(chunksize)
                if not chunk:
                    break
                encodestr = base64.b64encode(chunk)
                # print(str(encodestr, 'utf-8'))
                writer = csv.writer(csvfile)
                writer.writerow([str(encodestr, 'utf-8')])

                encodestr = base64.b64encode(chunk.encode('utf-8'))
                print(encodestr)
    f.close()

def download_file(url, wav_file):
    r = requests.get(url)
    with open(wav_file, "wb") as f:
        f.write(r.content)
        f.close()

def words_to_csv():
    with open(row_file_word) as row_f:
        f_csv = csv.reader(row_f)
        header = next(f_csv)

        with open(new_file_word, 'w') as new_f:
            newf_csv = csv.writer(new_f)
            newf_csv.writerow(header)

            for row in f_csv:
                new_row = [row[0], row[1], row[2]]
                print(row[0], row[1])

                wav_file = "/Users/shiyuchen/Downloads/class-online/wav/{}.wav".format(row[1])
                download_file(row[0], wav_file)

                with open(wav_file, 'rb') as f_wav:
                    i = 3
                    while True:
                        chunk = f_wav.read(chunksize)
                        if not chunk:
                            break
                        encodestr = base64.b64encode(chunk)
                        print(str(encodestr, 'utf-8'))
                        new_row.append(str(encodestr, 'utf-8'))
                    f_wav.close()

                newf_csv.writerow(new_row)

        new_f.close()
    row_f.close()



def sen_to_csv():
    pass

if __name__ == '__main__':
    sleep(1)
    words_to_csv()
    # radio_to_csv()
    # with open('/Users/shiyuchen/Downloads/class-online/wav/apple.wav', 'rb') as f_wav:
    #     # a = f_wav.read()
    #     # encodestr = base64.b64encode(a)
    #     # print(str(encodestr, 'utf-8'))
    #     while True:
    #         chunk = f_wav.read(chunksize)
    #         if not chunk:
    #             break
    #         encodestr = base64.b64encode(chunk)
    #         print(str(encodestr, 'utf-8'))
    # f_wav.close()