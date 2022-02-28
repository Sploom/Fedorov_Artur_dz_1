import datetime


def main():
    global duration
    try:
        duration = int(input('Введите кол-во секунд для конвертации'))
    except:
        print('Возможно вы ввели не числовое значение, попробуйте снова')
    res = datetime.timedelta(seconds=duration)
    print(res)


if __name__ == '__main__':
    main()
