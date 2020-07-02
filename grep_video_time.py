import csv
import matplotlib.pyplot as plt

mysql_result = '/Users/shiyuchen/Downloads/video_psm/MySQL_result.csv'

def get_duration(csv_file):
    duration_list = []
    with open(mysql_result) as row_f:
        csv_f = csv.reader(row_f)
        header = next(csv_f)
        for row in csv_f:
            # print(row[1])
            duration = float(row[1].split(',')[5].split(':')[1])
            # print(duration)
            duration_list.append(duration)
        row_f.close()
    return duration_list


def draw_scatter(duration_list):
    x = []
    for i in range(len(duration_list)):
        x.append(i)
    print(len(duration_list), len(x))

    plt.scatter(x, duration_list, c='r')
    plt.xlabel('serial number')
    plt.ylabel('video time')
    plt.title('the video time of online users')
    plt.show()

def count_time(duration_list):
    time_0, time_3, time_10, time_30, time_60, time_180 = 0,0,0,0,0,0
    for duration in duration_list:
        if duration == 0:
            time_0 = time_0 + 1
        elif duration <=3:
            time_3 = time_3 + 1
        elif duration <= 10:
            time_10 = time_10 + 1
        elif duration <= 30:
            time_30 = time_30 + 1
        elif duration <= 60:
            time_60 = time_60 + 1
        else:
            time_180 = time_180 + 1
    print("time_0, time_3, time_10, time_30, time_60, time_180: {}, {}, {}, {}, {}, {}".format(time_0, time_3, time_10, time_30, time_60, time_180))


if __name__ == '__main__':
    duration_list = get_duration(mysql_result)
    print(duration_list)
    # draw_scatter(duration_list)
    count_time(duration_list)
